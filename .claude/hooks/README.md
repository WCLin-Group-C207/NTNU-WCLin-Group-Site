# Commit 安全檢查 Hook（選用）

`check_commit.py` 是給 Claude Code 用的 PreToolUse hook，會在執行 `git commit` 前掃描
**已 staged 的新增內容**，攔下疑似 API 金鑰、台灣身分證字號、非學術網域 email、台灣手機
號碼、疑似密碼賦值語法，以及不符合命名規則的 `assets/images/` 圖片檔名。

這個 hook 的邏輯（本資料夾內容）是團隊共用、會被 commit 進 repo 的，但**觸發它需要你自己
選擇加入**——預設不會對任何人自動生效，也不會影響不使用 Claude Code 的協作者。

## 如何啟用（opt-in）

1. 複製範例設定檔:
   ```
   cp .claude/settings.local.json.example .claude/settings.local.json
   ```
2. 重新啟動 Claude Code / 開新的 session。之後每次透過 Claude Code 執行 `git commit`，
   都會先跑這個檢查；有命中風險項目就會直接擋下 commit（不是用 ask 確認，因為 ask 在某些
   permission mode 下不保證會跳出提示）。
3. `.claude/settings.local.json` 是個人設定，已經被 `.gitignore` 排除，不會被 commit，
   也不會影響其他協作者的設定。

## 白名單

- `academic_domains.txt`：學術網域白名單（結尾比對），命中就不會被當成風險 email。
- `allowlist.txt`：低風險 email／網域／手機號碼的個人白名單，格式與用法見檔案內註解。

兩個檔案都是共用、會被 commit 進 repo 的清單本體；一般只有在合作對象的 email/網域不在
`academic_domains.txt` 時，才需要編輯 `allowlist.txt` 補上例外。

## 只在本機檔案系統操作

Hook 只讀取 `git diff --cached`，不會呼叫任何外部服務，也不會修改 commit 內容——只會
回傳允許或攔下的判斷。
