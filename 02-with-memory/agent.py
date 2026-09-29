"""A2：會記得對話的 AI Agent。

跟 A1 的差別只有一個 list：每一輪都把整串對話重送一次。

    ollama serve        # 另一個終端機
    python3 agent.py
"""

import json
import urllib.error
import urllib.request

API = "http://localhost:11434/api/chat"
MODEL = "ministral-3:8b"


def ask(messages):
    """把整串對話送給模型，回傳整包 response。"""
    body = {"model": MODEL, "stream": False, "messages": messages}
    request = urllib.request.Request(API, json.dumps(body).encode(),
                                     {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.load(response)


messages = []  # 這個 list 就是「記憶」，模型那端什麼都不會留

print(f"跟 {MODEL} 聊天。輸入 /bye 或直接按 Enter 離開。")
while True:
    try:
        question = input("\n你 > ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if question in ("", "/bye"):
        break
    messages.append({"role": "user", "content": question})
    try:
        reply = ask(messages)
    except urllib.error.URLError:
        print("連不上 Ollama。請先在另一個終端機執行 ollama serve")
        messages.pop()
        continue
    answer = reply["message"]["content"]
    messages.append({"role": "assistant", "content": answer})
    print("\n模型 >", answer)
    print(f"[送出 {reply['prompt_eval_count']} tokens，回答 {reply['eval_count']} tokens，"
          f"對話已有 {len(messages)} 則訊息]")

print("\n掰掰")
