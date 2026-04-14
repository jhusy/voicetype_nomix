# VoiceType

> 按住說話，放開即輸出 — Windows 語音輸入工具

VoiceType 是一個系統級的語音輸入工具。按住快捷鍵說話，放開後自動透過 AI 去除贅字、修正語句、加入標點，然後將文字注入到任何應用程式的游標位置。

---

## 🎉 最新更新 (2026-04-14)

### ✨ 重大功能
- **🌐 OpenRouter 支援** - 串接 OpenRouter 聚合服務，可自由選用 Google Gemini, Anthropic Claude, Meta Llama 3 等多款最新模型。
- **⌨️ 自訂模型名稱** - 在 OpenAI 與 OpenRouter 選項中新增自訂輸入框，支持手動輸入任何 Model ID (如 `gpt-4.5-preview`, `o3-mini`)。
- **🇹🇼 中文變體強制轉換 (OpenCC)** - 整合 OpenCC 轉換引擎，在 LLM 修飾後強制套用繁簡轉換、台灣用語優化或日文漢字轉換，確保輸出的統一性。

### 💰 效能與架構提升
- **解耦式 Provider 架構** - 重新設計 LLM 處理模組，支援快速插件化接入新引擎。
- **Temperature 全域優化** - 預設調整至 0.1，確保嚴格遵守指令避免 AI 產生發散內容。

查看完整更新內容：[CHANGELOG.md](CHANGELOG.md)

---

## 功能

- **Push-to-Talk** — 按住 Right Alt 說話，放開自動輸出
- **AI 智能修飾** — 自動去除贅字、修正語句、加入標點，支援多種 LLM 引擎
- **多引擎支援** — STT (Groq, OpenAI, 本地) 與 LLM (OpenAI, Anthropic, OpenRouter, Ollama)
- **自訂 LLM 模型** — 支援手動輸入模型 ID，突破預設清單限制
- **自訂字典** — 支援批次匯入專有名詞，同時用於語音辨識與 LLM 修飾效果
- **中文變體轉換 (OpenCC)** — 整合 OpenCC，強制定向轉換為繁體 (台灣/香港)、簡體或日音漢字
- **全應用程式支援** — Chrome, VS Code, Notion, LINE, 任何有文字輸入的地方均可使用
- **Web 設定介面** — 本地 HTTP Server 提供直覺的設定頁面
- **系統托盤常駐** — 背景安靜運行，支援右鍵快速切換模型與開啟設定
- **隨 Windows 啟動** — 可在設定中一鍵開啟/關閉開機自啟動

## 快速開始

### 使用 EXE（推薦）

1. 從 [Releases](../../releases) 下載 `VoiceType.exe`
2. 雙擊執行
3. 首次啟動會自動開啟設定頁面 → 填入 API Key → 完成

### 從原始碼執行

```bash
pip install -r requirements.txt
python main.py
```

### 取得 API Key

| 服務 | 用途 | 連結 |
|------|------|------|
| **Groq** | 語音辨識（STT） | https://console.groq.com/keys |
| **OpenAI** | 文字修飾（LLM） | https://platform.openai.com/api-keys |
| **OpenRouter** | 聚合多款 LLM | https://openrouter.ai/keys |

> Groq 提供免費額度，OpenAI GPT-4.1 指令遵循能力最強，兩者搭配為推薦組合。

## 使用方式

1. VoiceType 啟動後常駐在系統托盤（右下角）
2. 在任何 App 中，將游標放在要輸入文字的地方
3. **按住 Right Alt** 開始說話（會聽到提示音）
4. **放開 Right Alt** 等待 1-2 秒
5. 修飾後的文字自動出現在游標位置

```
按住 Right Alt → 錄音開始
放開 Right Alt → 錄音結束並傳輸
         ↓
  STT 語音辨識 (Groq/OpenAI/Local)
  "那個呃我想說明天的會議改到呃禮拜三下午兩點"
         ↓
  LLM 智能修飾 (OpenAI/OpenRouter/Claude...)
  "明天的會議改到禮拜三下午兩點。"
         ↓
  OpenCC 文字轉換 (繁簡轉換/用語優化)
  "明天的會議改到禮拜三下午兩點。"
         ↓
  系統注入 (剪貼簿 + Ctrl+V)
```

## 設定

設定方式（擇一）：
- 系統托盤右鍵 →「開啟設定」（Web 介面）
- 手動編輯 `%APPDATA%\voicetype\config.json`

### STT 引擎

| 引擎 | 速度 | 費用 | 說明 |
|------|------|------|------|
| **Groq Whisper** | 極快 | 幾乎免費 | 推薦 |
| OpenAI Whisper | 中等 | ~$0.006/min | 品質穩定 |
| 本地 Whisper | 依硬體 | 免費 | 需安裝 faster-whisper |

### LLM 引擎比較

| 引擎 | 費用 | 說明 |
|------|------|------|
| **OpenAI GPT-4.1 / o3** | 依使用量 | 指令遵循能力極強，文字處理穩定 |
| **OpenRouter** | 依模型 | **推薦**，單一 API 即可調用 Gemini 2.0, Claude 3.5, Llama 3.3 等 |
| **Anthropic Claude** | 依使用量 | 高品質文字審稿與格式處理 |
| **Groq (Llama/Gemma)** | 免費額度 | 推理極快（~300 tokens/s），適合簡短修正 |
| **Ollama** | 免費 | 完全本地運行，隱私保護最佳 |
| **自訂模型** | - | 支援手動輸入任何支援的 Model ID String |

## 🛠 技術架構

本專案採用解耦的 **Provider-Engine 架構**，將具體的 API 調用（Provider）與核心處理流（Engine）分離，這使得 VoiceType 具備極高的擴充性：
- **統一介面**: 無論是 OpenAI, Groq 還是 OpenRouter，均透過一致的 `LLMProcessor` 介面進行通訊。
- **強健的文字管線**: 文字經過 `STT -> LLM -> OpenCC -> Injector` 的層層處理，確保最終輸出符合用戶的語言偏好與格式需求。
- **授權合規**: 專案嚴格區分主體代碼 (MIT) 與第三方組件 (Apache 2.0)，確保開源遵循的合規性。

### 文字轉換 (OpenCC)

VoiceType 整合了 OpenCC，在 LLM 修飾後強制執行轉換，確保文字字體的一致性。支援模式：

- **繁體中文 (台灣用語優化) `s2twp`** - 自動轉換大陸用語為台灣習慣稱呼（如：軟件 → 軟體）
- **繁體中文 (標準) `s2t`** - 標準簡轉繁
- **繁體中文 (香港標準) `s2hk`**
- **簡體中文 (標準) `t2s`**
- **日本語漢字 (新字體) `t2jp`** - 將繁體漢字轉為日文習慣字體

### 快捷鍵

預設 `Right Alt`，可在設定中更改為 Right Ctrl、F9、CapsLock 或 ScrollLock。

## 專案結構

```
voicetype/
├── main.py                  # 主程式入口
├── core/
│   ├── recorder.py          # 音訊錄製
│   ├── stt.py               # 語音轉文字
│   ├── llm.py               # LLM 智能修飾
│   ├── converter.py         # 中文繁簡轉換 (OpenCC)
│   ├── injector.py          # 文字注入（剪貼簿 + Ctrl+V）
│   ├── hotkey.py            # 全域快捷鍵
│   ├── sounds.py            # 音效提示
│   └── tray_icons.py        # 系統托盤圖示
├── config/
│   ├── settings.py          # 設定管理
│   └── settings_server.py   # Web 設定伺服器
├── ui/
│   └── settings.html        # 設定頁面
├── assets/
│   └── VoiceType.exe.manifest
├── build.py                 # 打包腳本
├── requirements.txt         # Python 依賴
└── start.bat                # 一鍵啟動
```

## 自行打包

```bash
pip install pyinstaller
python build.py
```

產出 `dist/VoiceType.exe`。

## 系統需求

- Windows 10 / 11
- 麥克風
- 網路連線（使用雲端 STT/LLM 時）

## License

本專案採用 **MIT License** 授權。

### 第三方組件聲明 (Third-party Licenses)

本專案使用了以下開源組件，其授權條款如下：

- **OpenCC (Open Chinese Convert)**: 採用 [Apache License 2.0](https://github.com/BYVoid/OpenCC/blob/master/LICENSE) 授權。
- **opencc-python-reimplemented**: 採用 [Apache License 2.0](https://github.com/yichen0831/opencc-python/blob/master/LICENSE) 授權。
- **其他相依套件** (如 OpenAI SDK, pystray 等): 分別採用其各自的 MIT 或 BSD 授權。
