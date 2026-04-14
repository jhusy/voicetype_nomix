# Changelog

All notable changes to VoiceType will be documented in this file.

## [Unreleased] - 2026-04-14

### ✨ New Features

#### 中文繁簡轉換 (OpenCC) 強制模式
- **整合 OpenCC 轉換引擎** - 在文字注入前強制套用轉換，確保輸出字體一致性。
- **支援多種變體**：
  - 繁體中文 (台灣用語優化 `s2twp`)：具備慣用語轉換（如「軟件」->「軟體」）。
  - 繁體中文 (標準 `s2t`)。
  - 繁體中文 (香港標準 `s2hk`)。
  - 簡體中文 (標準 `t2s`)。
  - 日本語漢字 (新字體 `t2jp`)。
- **無縫 UI 整合** - 一般設定中可即時切換變體。

#### OpenRouter 支援與自訂模型功能
- **新增 OpenRouter 引擎** - 整合 OpenRouter 聚合服務，可串接 Gemini、Claude、Llama 等多款頂尖模型。
- **自訂模型輸入框** - 在 OpenAI 與 OpenRouter 選項下新增輸入框，允許用戶手動輸入任何支援的模型 ID（如 `gpt-4.5-preview` 或 `google/gemini-2.0-flash-001`）。
- **擴展模型清單** - 更新預設推薦模型，包含最新的 o3-mini 與 Gemini 2.0 系列。
- **靈活配置** - 設定檔可獨立儲存 OpenRouter API Key，並支援自訂模型字串的永久化。

### ⚙️ Engineering Improvements
- **單元測試自動化** - 新增 `tests/test_converter.py` 進行 100% 邏輯驗證。
- **GitHub Actions CI** - 建立 `.github/workflows/ci.yml` 執行自動化測試與 Lint。
- **Git 工作流優化** - 完善 `.gitignore` 並保持 Commit History 潔淨。

### 📝 Changed Files
- `core/converter.py` - [NEW] OpenCC 轉換封裝。
- `tests/test_converter.py` - [NEW] 轉換邏輯單元測試。
- `.github/workflows/ci.yml` - [NEW] CI 自動化流程。
- `main.py` - 整合轉換管線進入主流程。
- `core/llm.py` - 實作 OpenRouter 支援與模型自訂邏輯。
- `config/settings.py` - 新增 `google/openrouter` 支援欄位。
- `ui/settings.html` - 更新 UI，新增金鑰輸入與模型自訂框。
- `README.md` - 更新功能說明與引擎清單。

---

## [0.1.0] - 2026-03-03

### 🎯 Major Improvements

#### LLM 模型升級到 GPT-4.1
- **從 GPT-4o 升級到 GPT-4.1** - 更強的指令遵循能力
- **解決了 LLM 回答問題的問題** - 現在能完美遵守「只清理文字，不回答問題」的指令
- **性能提升** - GPT-4.1 比 GPT-4o 便宜 20%（$2.00/$8.00 vs $2.50/$10.00 per 1M tokens）
- **上下文容量提升** - 128K tokens 上下文（vs Groq LLM 的 8K-32K）

### ✨ New Features

#### 托盤選單模型選擇器
- **即時切換模型** - 右鍵托盤圖標 → 「模型選擇」
- **支援模型**：
  - GPT-4.1（推薦）
  - GPT-4.1-mini
  - GPT-4o
  - GPT-4o-mini
- **即時生效** - 無需重啟應用程式
- **狀態顯示** - 托盤圖標顯示當前使用的模型

#### 字典擴充
- **從 129 個詞擴充到 160 個詞**
- **新增分類**：
  - AI 模型：GPT-4.1, GPT-4o, GPT-5.2, GPT-5.3, Groq, Ollama
  - AI/ML 概念：LLM, STT, API, prompt, temperature, tokens, context
  - 通訊軟體：Discord, Messenger, WhatsApp, Slack, Teams
  - 郵件客戶端：Outlook, Gmail, Thunderbird
  - 文件編輯：Word, Docs, Notion, Obsidian
  - 開發工具：VSCode, PyCharm
  - 資料庫：PostgreSQL, MongoDB, Redis, FastAPI
  - DevOps：Kubernetes

### 🔧 Optimizations

#### System Prompt 強化
- **更明確的「不回答問題」指令**
- **添加正反範例** - 清楚展示正確和錯誤的輸出
- **強化格式規則** - 更詳細的清理和格式化指導

#### Temperature 優化
- **從預設值調整到 0.1** - 極低溫度確保嚴格遵守指令
- **應用於所有 LLM provider** - OpenAI, Anthropic, Groq, Ollama

### 🐛 Bug Fixes

#### 上下文限制問題
- **問題**：使用 Groq LLM 時，上下文太短（8K-32K tokens）無法處理大量字典詞彙
- **解決**：切換到 OpenAI GPT-4.1（128K tokens）完全解決
- **效果**：現在可以使用數千個字典詞彙而不會超出上下文

#### 托盤選單 Lambda 函數簽名錯誤
- **修正**：MenuItem 回呼函數需要接受 `(icon, item)` 兩個參數
- **影響**：修正後托盤選單的模型選擇功能正常運作

### 📝 Changed Files

- `main.py` - 添加模型選擇器和切換功能
- `core/llm.py` - 調整 temperature 到 0.1
- `config/settings.py` - 更新預設 system prompt
- `config.json` - 升級到 GPT-4.1，擴充字典到 160 個詞

### 💡 Recommendations

- **推薦模型**：GPT-4.1（指令遵循能力最強，性價比高）
- **不推薦**：GPT-4o-mini、GPT-3.5-turbo（無法遵守「不回答問題」的指令）
- **字典擴充**：GPT-4.1 的 128K 上下文可以輕鬆處理數千個詞彙，可以繼續擴充

---

## Previous Versions

### Phase 1 & 2: Focus Loss and Process Hanging Fixes
- Fixed focus loss issue after voice input
- Fixed process hanging on Windows
- Improved focus restoration mechanism
- Added thread safety with locks
- Added timeout protection for AttachThreadInput
- Reordered execution sequence (focus → escape → unhook → inject → rehook)
