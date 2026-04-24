# NTNU WCLin Group 網站 · 使用說明

共 8 個 HTML 檔案，每個都是**獨立自足**的單檔，可以分別貼進 Google Sites。

---

## 檔案清單

| 檔名 | 對應頁面 | 內容 |
|---|---|---|
| `index.html` | 首頁 | News、4 大研究方向、CTA |
| `group-leader.html` | Group Leader | Prof. Lin 個人頁 |
| `members.html` | Members | 現役成員 + Alumni 表格 |
| `research.html` | Research | 5 大研究主題詳述 |
| `publications.html` | **Publications** | 全部 127 篇論文，可搜尋/篩選/排序 |
| `facilities.html` | Facilities | 6 台儀器總覽 |
| `exchange-awards.html` | Awards | 獎項時間軸 + 國際交流（切換標籤） |
| `photos.html` | Gallery | 相簿模板（自己放圖） |

---

## 如何放到 Google Sites

1. 到 Google Sites 編輯器
2. 右側選單 **插入 → 內嵌 → 嵌入代碼**
3. 用文字編輯器（記事本／VS Code）打開任一 `.html` 檔，**全選複製**
4. 貼進 Google Sites 的嵌入代碼視窗
5. 按「下一步 → 插入」

每一頁都要重複這個動作一次。建議在 Google Sites 左側建立對應的 8 個分頁。

---

## 如何修改內容

所有可編輯的地方都有 HTML 註解標示，像這樣：

```html
<!-- ▼▼▼ 新增成員請複製整個 .member-card 區塊 ▼▼▼ -->
<div class="member-card">
  ...
</div>
<!-- ▲▲▲ -->
```

打開 `.html` 檔，用 Ctrl+F 搜尋 `▼` 就能快速找到所有可編輯區塊。

### 常見修改

**換文字** → 直接改 HTML 裡的內容
**新增一則 News** → 複製一段 `.news-item`，改裡面的字
**新增一篇論文** → 在 `publications.html` 的 JavaScript 陣列裡新增一筆物件：

```javascript
{
  year: 2026,
  title: "論文標題",
  authors: "作者列表 (用逗號分隔)",
  journal: "期刊名稱",
  volume: "卷期頁碼",
  url: "論文連結",
  role: "corresp",  // 或 "cocorresp" 或 ""
  thumbnail: ""     // 留空自動用年份當縮圖；或填圖片網址
}
```

**改整站主色** → 打開任一 `.html`，找到檔案開頭的 `:root {` 區塊，改 `--color-accent` 等變數值

---

## 關於圖片

Google Sites 嵌入的 HTML **無法直接上傳本地檔案**。圖片要先上傳到：
- Google Drive（設為公開）
- Google Photos
- Imgur 等圖床

取得公開連結後，把網址貼到 `<img src="這裡">`。

若使用 GitHub Pages，建議在 repository 建立 `assets/images/` 資料夾，將圖片放入後用相對路徑，例如 `<img src="assets/images/group-photo.jpg" alt="Group photo">`。

`photos.html` 的每張照片有清楚註解標示哪裡放圖。

---

## 設計系統

- **字型**：Fraunces（襯線標題）+ Arial（英文字體／內文與連結）+ Noto Sans TC（中文備援）
- **主色**：深藍墨 `#1a2238`、深紅 `#a82740`、米白 `#faf7f0`
- **8 個檔案每個都是自給自足的單檔**，沒有共用 CSS / JS 檔案

如果要改整站配色，每個檔案的 `:root { ... }` 區塊都要改（因為 Google Sites 限制無法共用 CSS）。

---

© 2026 · Built for Prof. Wen-Chin Lin's NanoMaterials & Spintronics Lab


---

## 本次細部優化紀錄

- 內文與導覽／頁面連結字型改為 Arial，標題字型保留 Fraunces。
- Footer 設計署名改為 `Designed by 陳可凡 & 陳柏維 · Rebuilt 2026`。
- 首頁 `NanoMaterials & Spintronics Laboratory` 標籤略放大。
- 首頁主標題 `Magnetic thin films, 2D materials, and the spins between.` 略縮小並調整行距。
- 首頁 PI、Institution、Founded 資訊列略放大，提高可讀性。
