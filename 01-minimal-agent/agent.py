"""A1：最小的 AI Agent。

跟本機的模型一問一答。沒有記憶、沒有角色設定，只有骨架。

    ollama serve        # 另一個終端機
    python3 agent.py
"""

import json
import urllib.error
import urllib.request

API = "http://localhost:11434/api/chat"
MODEL = "ministral-3:8b"


def ask(question):
    """把一個問題送給模型，回傳整包 response。"""
    body = {"model": MODEL, "stream": False,
            "messages": [{"role": "user", "content": question}]}
    request = urllib.request.Request(API, json.dumps(body).encode(),
                                     {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.load(response)


print(f"跟 {MODEL} 聊天。輸入 /bye 或直接按 Enter 離開。")
while True:
    try:
        question = input("\n你 > ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if question in ("", "/bye"):
        break
    try:
        reply = ask(question)
    except urllib.error.URLError:
        print("連不上 Ollama。請先在另一個終端機執行 ollama serve")
        continue
    print("\n模型 >", reply["message"]["content"])
    print(f"[送出 {reply['prompt_eval_count']} tokens，回答 {reply['eval_count']} tokens]")

print("\n掰掰")
