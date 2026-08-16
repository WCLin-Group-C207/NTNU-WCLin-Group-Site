#!/usr/bin/env python3
"""PreToolUse hook: 在 `git commit` 前檢查 staged 內容。

只檢查「已 staged 的新增內容」(git diff --cached)，不解析 commit 指令本身的文字，
這樣才能抓到寫進檔案裡的機密資訊，而不只是 commit message。

所有命中項目一律直接擋下 commit（deny），不使用 permissionDecision: "ask" ——
因為 ask 是否真的跳出確認，依賴當下 session 的 permission mode，在自動核准模式下
會被悄悄放行而不會真的通知使用者，無法保證一定會被看到。

Email／手機號碼這類項目額外支援白名單放行（見 allowlist.txt）：符合學術網域規則、
或是本人已經明確加進白名單的項目就不會擋下；其餘一律 deny 並在錯誤訊息裡告訴使用者
「不在白名單，如果確認要保留就把它加進 allowlist.txt 後重新 commit」。
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# Windows 上透過 pipe 輸出時，sys.stdout 預設會走系統 ANSI codepage 而不是
# UTF-8，中文字會變亂碼。強制用 UTF-8 輸出，確保 hook JSON 內容不會壞掉。
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[2]
DOMAINS_FILE = Path(__file__).resolve().parent / "academic_domains.txt"
ALLOWLIST_FILE = Path(__file__).resolve().parent / "allowlist.txt"
HOOKS_DIR_PREFIX = ".claude/hooks/"

# ---------------------------------------------------------------------------
# 1. API 金鑰 / 憑證格式（命中即擋下 commit）
#    如需擴充，直接在此清單新增一筆 (label, regex) 即可。
# ---------------------------------------------------------------------------
SECRET_PATTERNS = [
    ("OpenAI / Anthropic API key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("Google OAuth client secret", re.compile(r"GOCSPX-[A-Za-z0-9_-]{20,}")),
    ("GitHub token (classic)", re.compile(r"gh[pousr]_[A-Za-z0-9]{36}")),
    ("GitHub fine-grained PAT", re.compile(r"github_pat_[A-Za-z0-9_]{22,}")),
    ("AWS Access Key ID", re.compile(r"A(?:KIA|SIA)[0-9A-Z]{16}")),
    ("Slack token", re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,}")),
    ("Slack Incoming Webhook", re.compile(r"hooks\.slack\.com/services/T[0-9A-Za-z]+/B[0-9A-Za-z]+/[0-9A-Za-z]+")),
    ("Stripe secret key", re.compile(r"(?:sk|rk)_live_[0-9A-Za-z]{24,}")),
    ("npm access token", re.compile(r"npm_[A-Za-z0-9]{36}")),
    ("Private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |)PRIVATE KEY-----")),
]

# 2. 台灣身分證字號：先用形狀抓候選字串，再套官方檢查碼公式驗證
TAIWAN_ID_CANDIDATE = re.compile(r"\b[A-Za-z][12]\d{8}\b")
LETTER_CODE = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
    'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23,
    'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30,
    'Y': 31, 'Z': 33,
}

# 3. 圖片檔名規則：只針對 assets/images/ 底下「新增或改名」的檔案
IMAGE_PATH_PREFIX = "assets/images/"
IMAGE_EXT_RE = re.compile(r"\.(jpg|jpeg|png)$", re.IGNORECASE)
IMAGE_NAME_RE = re.compile(r"^[A-Za-z0-9-]+$")

# 4-6. 警告類（不擋下）
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
TW_MOBILE_RE = re.compile(r"\b09\d{8}\b")
PASSWORD_ASSIGN_RE = re.compile(r"\b(password|pwd|passwd|secret)\s*[:=]", re.IGNORECASE)


def run_git(args):
    result = subprocess.run(
        ["git", *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.stdout


def mask(value, keep_start=3, keep_end=2):
    if len(value) <= keep_start + keep_end:
        return "*" * len(value)
    return value[:keep_start] + "*" * (len(value) - keep_start - keep_end) + value[-keep_end:]


def is_valid_taiwan_id(candidate):
    letter = candidate[0].upper()
    digits = candidate[1:]
    if letter not in LETTER_CODE or len(digits) != 9 or not digits.isdigit():
        return False
    code = LETTER_CODE[letter]
    n1, n2 = divmod(code, 10)
    values = [n1, n2, *(int(c) for c in digits)]
    weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total = sum(v * w for v, w in zip(values, weights))
    return total % 10 == 0


def parse_added_lines(diff_text):
    """回傳 (file, line_no, text) 清單：只取 staged diff 中新增的那些行。
    hook 自己的目錄底下的內容不掃（避免規則清單裡的範例字串誤觸自己）。
    """
    added = []
    current_file = None
    new_line = 0
    header_re = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")
    for line in diff_text.splitlines():
        if line.startswith("+++ "):
            m = re.match(r"^\+\+\+ b/(.*)$", line)
            current_file = m.group(1) if m else None
            continue
        if line.startswith("@@ "):
            m = header_re.match(line)
            new_line = int(m.group(1)) if m else 0
            continue
        if line.startswith("+") and not line.startswith("+++"):
            if current_file and not current_file.startswith(HOOKS_DIR_PREFIX):
                added.append((current_file, new_line, line[1:]))
            new_line += 1
            continue
    return added


def load_academic_domains():
    if not DOMAINS_FILE.exists():
        return []
    domains = []
    for raw in DOMAINS_FILE.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        domains.append(s.lower())
    return domains


def load_allowlist():
    """讀 allowlist.txt，依內容分成三類：完整 email、網域（結尾比對）、手機號碼。"""
    emails, domains, phones = set(), [], set()
    if not ALLOWLIST_FILE.exists():
        return emails, domains, phones
    for raw in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        if "@" in s:
            emails.add(s.lower())
        elif s.isdigit():
            phones.add(s)
        else:
            domains.append(s.lower())
    return emails, domains, phones


def check_image_filenames():
    findings = []
    name_status = run_git(["diff", "--cached", "--name-status", "--diff-filter=ACMR"])
    for line in name_status.splitlines():
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R"):
            rel_path = parts[2] if len(parts) > 2 else None
        else:
            rel_path = parts[1] if len(parts) > 1 else None
        if not rel_path:
            continue
        rel_path = rel_path.replace("\\", "/")
        if not rel_path.startswith(IMAGE_PATH_PREFIX):
            continue
        if not (status.startswith("A") or status.startswith("R")):
            # 只在檔案「新增/改名」當下檢查，不會因為既有違規檔案被修改內容
            # 就每次 commit 都卡住。
            continue
        filename = rel_path.rsplit("/", 1)[-1]
        dot = filename.rfind(".")
        if dot == -1:
            findings.append(f'[圖片檔名規則] {rel_path}: 缺少副檔名')
            continue
        ext = filename[dot:]
        name = filename[:dot]
        if not IMAGE_EXT_RE.search(filename):
            findings.append(f'[圖片檔名規則] {rel_path}: 副檔名 "{ext}" 不在允許清單 (.jpg/.jpeg/.png)')
        if not IMAGE_NAME_RE.match(name):
            findings.append(f'[圖片檔名規則] {rel_path}: 檔名 "{name}" 含有不允許的字元（只能英文字母、數字、連字號 -）')
    return findings


def main():
    try:
        sys.stdin.read()
    except Exception:
        pass

    diff_text = run_git(["diff", "--cached", "--diff-filter=ACMR", "-U0"])
    added_lines = parse_added_lines(diff_text)
    academic_domains = load_academic_domains()
    allow_emails, allow_domains, allow_phones = load_allowlist()

    hard_findings = []

    for file, line_no, text in added_lines:
        for label, pattern in SECRET_PATTERNS:
            m = pattern.search(text)
            if m:
                hard_findings.append(f"[API 金鑰/憑證] {label} — {file}:{line_no} → {mask(m.group(0))}")

        for m in TAIWAN_ID_CANDIDATE.finditer(text):
            candidate = m.group(0)
            if is_valid_taiwan_id(candidate):
                hard_findings.append(f"[台灣身分證字號] {file}:{line_no} → {mask(candidate)}")

        for m in EMAIL_RE.finditer(text):
            email = m.group(0)
            email_lower = email.lower()
            domain = email_lower.split("@")[-1]
            if any(domain.endswith(suffix) for suffix in academic_domains):
                continue
            if email_lower in allow_emails or any(domain.endswith(suffix) for suffix in allow_domains):
                continue
            hard_findings.append(
                f"[Email 不在白名單] {file}:{line_no} → {email}"
                f"（非學術網域，也不在 .claude/hooks/allowlist.txt；"
                f"如確認要保留，請把完整 email 或網域加入 allowlist.txt 後重新 commit）"
            )

        for m in TW_MOBILE_RE.finditer(text):
            number = m.group(0)
            if number in allow_phones:
                continue
            hard_findings.append(
                f"[手機號碼不在白名單] {file}:{line_no} → {mask(number)}"
                f"（不在 .claude/hooks/allowlist.txt；"
                f"如確認要保留，請把完整號碼加入 allowlist.txt 後重新 commit）"
            )

        if PASSWORD_ASSIGN_RE.search(text):
            snippet = text.strip()[:80]
            hard_findings.append(f"[疑似密碼賦值語法] {file}:{line_no} → {snippet}")

    hard_findings.extend(check_image_filenames())

    if hard_findings:
        reason = "\n".join(f"- {f}" for f in hard_findings)
        output = {
            "systemMessage": f"Commit 已被攔下，偵測到 {len(hard_findings)} 項風險內容：\n{reason}",
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            },
        }
        print(json.dumps(output, ensure_ascii=False))

    sys.exit(0)


if __name__ == "__main__":
    main()
