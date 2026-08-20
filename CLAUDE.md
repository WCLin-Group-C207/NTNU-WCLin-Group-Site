# CLAUDE.md

本檔案提供給 Claude Code 在此 repository 工作時的規則與現況說明。

## 專案概覽

NTNU WCLin Group（NanoMaterials & Spintronics Laboratory）實驗室網站。純 HTML + CSS + 少量 JavaScript，**沒有** React/Vue、沒有建置系統、沒有後端。每個頁面是獨立的`.html` 檔案，CSS 寫在各頁自己的 `<style>` 區塊內(尚未抽成共用 CSS)。

完整編輯教學見 [README.md](README.md)(英文)與 [README_Chinese.md](README_Chinese.md)(中文)。

主要頁面：
```
index.html            首頁
group-leader.html     指導教授 / PI
members.html          成員與 Alumni
research.html         研究方向
publications.html     論文列表(含搜尋/篩選 JS)
facilities.html       實驗設備
exchange-awards.html  交流與獲獎
gallery.html          相簿
```

## 硬性命名規則（務必遵守）

- 圖片檔名只能用**英文字母、數字、連字號 `-`**，禁止空白、中文字、`(1)` 這類重複標記。
- 圖片副檔名限定 `.jpg` / `.jpeg` / `.png`，不要用其他副檔名(即使檔案內容其實是圖片)。
- GitHub Pages 對檔名**大小寫敏感**——`Po-Wei.jpg`、`po-wei.jpg`、`Po-Wei.JPG` 是三個不同檔案，改圖或加圖時要特別注意大小寫一致。
- 所有圖片統一放在 `assets/images/`(或其子資料夾)，HTML/CSS 一律用相對路徑引用。
- 若要重新命名任何 HTML 或圖片檔案，必須同步更新所有引用它的地方(nav、footer、`<img src>`、CSS `url(...)`)。

## Gallery 照片命名規則（`assets/images/gallery/` 底下務必遵守）

檔名統一格式：`AAAABBB-CCCC-DDD-EE.jpg`

| 欄位 | 意義 | 範例 |
|---|---|---|
| `AAAA` | 西元年，4 碼 | `2022` |
| `BBB`  | 月份縮寫，3 碼(Jan/Feb/Mar/…/Dec) | `Jul` |
| `CCCC` | 會議 / 計畫 / 活動名稱，會議優先用縮寫，沒有縮寫才打全名 | `TPS`、`TAMT`、`MMM` |
| `DDD`  | 國家縮寫 | `TW`、`JP`、`KR`、`US` |
| `EE`   | 兩位數流水號，同一場活動有多張照片時遞增 | `01`、`02` |

範例：`2022Jul-TAMT-TW-01.jpg`

**未知的欄位一律用 `XXX` 代替**，不要留空、不要用問號、不要用猜測值頂替。例如月份不確定：`2016XXX-MMM-US-01.jpg`。

### 三大分類定義（conference / program / event）

- **conference**：國內外學術會議。目前已知：`MMM`、`ICMFs`、`TAMT`(通常七月，台灣)、`TPS`(通常一月，台灣)。
- **program**：出國計畫、國外參訪、移地實驗，含修課附帶的短期出國參訪、國內移地實驗。目前已知：學海築夢、千里馬。
- **event**：除了 conference、program 以外的任何活動，例如實驗室聚餐、出遊等。

## 設計風格禁止事項

目標是 Nature / MIT 類型的學術期刊感，**不要**加入：

- 高飽和紫色 / AI 風格漸層
- 正式區塊裡的 emoji 圖示
- 大量圓角、SaaS/startup 風格卡片
- 很重的陰影
- 太多不一致的顏色或字體

## 全站共用區塊（改動時要注意）

因為沒有共用 CSS/模板，以下三種改動**必須同步更新到每一個 HTML 檔案**：

- 導覽列(nav)內容或順序
- Footer 資訊(地址、電話、教授 email、著作年份等)
- 全站顏色 / 字體變數(`--color-ink`、`--color-accent` 等 CSS 變數)

導覽列每頁只有當前頁面的連結該有 `class="active"`，其餘頁面不要有。
