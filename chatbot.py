import requests

def get_ollama_response(user_input):
    url = "http://localhost:11434/v1/ask"  # Ollama local API endpoint
    headers = {"Content-Type": "application/json"}
    data = {
        "messages": [{"role": "user", "content": user_input}],
        "model": "llama3.2"  # Change to your installed model
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("message", {}).get("content", "Sorry, I couldn't understand that.")
    else:
        return "Error: Unable to connect to Ollama model."

def chatbot():
    print("Hello! I am ChatBuddy 🤖. Ask me anything or type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("ChatBuddy: Goodbye! Have a great day! 👋")
            break
        response = get_ollama_response(user_input)
        print(f"ChatBuddy: {response}")

chatbot()
