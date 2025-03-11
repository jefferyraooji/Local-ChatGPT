import os
from llama_cpp import Llama

# Set model path (Ensure you have a GGUF model downloaded)
MODEL_PATH = "models/llama-2-7b.Q4_K_M.gguf"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

print("🔄 Loading model, please wait...")
llm = Llama(model_path=MODEL_PATH)

# Chat function
def chat():
    print("🤖 Local ChatGPT: Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🤖 Chatbot: Goodbye!")
            break
        response = llm(user_input, max_tokens=200)
        print(f"🤖 Chatbot: {response['choices'][0]['text']}")

if __name__ == "__main__":
    chat()
