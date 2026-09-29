# ai_agent_from_scratch

從零手刻一支 AI Agent，搞懂它到底怎麼跟 LLM 講話。

這是部落格系列《AI Agent 是怎麼跟 LLM 講話的》的完整程式碼。每一篇對應一個資料夾，
每個資料夾都是**當下那篇的完整可跑快照** —— 可以直接 `diff` 相鄰兩個資料夾，
看下一篇到底多做了什麼（通常只差幾行）。

## 設計原則

- **零第三方相依**：只用 Python 標準函式庫（`json` + `urllib`）。
  不是為了炫技，而是因為這系列要看的就是底層那一包 JSON —— 套上框架就什麼都看不到了。
- **全部跑在自己電腦上**：本機 Ollama + `ministral-3:8b`，不花錢、不用網路、不外流對話。
- **每一步都實測**：文章裡貼的每個回應、每個 token 數字都是真的跑出來的。

## 目錄

| 資料夾 | 對應文章 | 多做了什麼 |
| --- | --- | --- |
| [`01-minimal-agent/`](01-minimal-agent/) | A1 | 一問一答的骨架。沒有記憶、沒有角色設定 |
| [`02-with-memory/`](02-with-memory/) | A2 | 多了一個 `messages` list：每輪把整串對話重送 |
| `03-with-system-prompt/`（即將推出） | A3 | 多了一則 `system` 訊息：把它變成專門做一件事的 agent |

## 環境需求

- Python 3.8+（只用標準函式庫，不必建虛擬環境）
- [Ollama](https://ollama.com/) 與 `ministral-3:8b` 模型

```bash
# 裝好 Ollama 之後
ollama pull ministral-3:8b
ollama serve
```

```bash
# 另一個終端機
cd 01-minimal-agent
python3 agent.py
```

## 授權

MIT
