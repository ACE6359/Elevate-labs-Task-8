# ChatBuddy 🤖 - Rule-Based & AI-Powered Chatbot

## Overview
**ChatBuddy** is a Python-based chatbot that can respond to user input dynamically. It started as a simple rule-based chatbot using `if-elif-else` statements and has been enhanced to integrate with **Ollama**, a local large language model (LLM). With Ollama, ChatBuddy can answer any question, hold a conversation, and provide intelligent responses in real-time.

---

## Features
- **Rule-Based Mode:** Responds to greetings, basic questions, and common expressions.
- **AI-Powered Mode:** Uses Ollama (`gemma3:27b`) to dynamically answer any user query.
- **Interactive:** Supports conversation history for context-aware responses.
- **User-Friendly:** Friendly messages with emojis and varied phrases.
- **Cross-Platform:** Tested with Python on Windows (PowerShell).

---

## Tools & Technologies
- **Python 3.x**
- **Requests** library (`pip install requests`)
- **Ollama** LLM (`gemma3:27b` recommended)

---

## Installation & Setup

1. **Clone the repository**
```powershell
git clone <your-repo-url>
cd Task-8-Chatbot
````

2. **Install Python dependencies**

```powershell
pip install requests
```

3. **Install Ollama**
   Download and install from [Ollama Website](https://ollama.com/).
   Verify installation:

```powershell
ollama --help
```

4. **Run Ollama model**
   Open PowerShell and start the model:

```powershell
ollama run gemma3:27b
```

### Optional: Run Ollama in the background and chatbot in one command

You can start Ollama in a new PowerShell process and then run your chatbot in the same window:

```powershell
Start-Process powershell -ArgumentList "ollama run gemma3:27b"
python chatbot.py
```

5. **Run ChatBuddy**
   If you started Ollama separately, open a second terminal and run:

```powershell
python chatbot.py
```

Type anything to chat. Type `quit` to exit.

---

## How It Works

1. User input is captured in Python using `input()`.
2. Input is sent to the Ollama API at `http://localhost:11434/v1/ask`.
3. Ollama generates a response and sends it back.
4. ChatBuddy displays the response dynamically.

---

## Example Conversation

```
You: hi
ChatBuddy: Hello! How are you today? 😄
You: what's your name?
ChatBuddy: I am ChatBuddy, your friendly chatbot! 🤖
You: tell me a joke
ChatBuddy: Why did the computer go to the doctor? Because it caught a virus! 😂
You: quit
ChatBuddy: Goodbye! Have a great day! 👋
```

---

## Key Concepts

* **Control Flow:** `if-elif-else` for rule-based logic.
* **Loops:** `while` loop keeps the chatbot running until exit.
* **Input Handling:** Uses `input()` and `strip().lower()` for normalization.
* **HTTP Requests:** Communicates with Ollama API for dynamic responses.

---

## License

This project is open-source and free to use. No warranty implied.

Do you want me to do that?
```
