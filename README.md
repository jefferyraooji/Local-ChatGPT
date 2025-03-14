# 🤖 Local-ChatGPT: Run LLaMA Model Locally

This project runs a **local ChatGPT-like chatbot** using **LLaMA models** with `llama-cpp-python`. No API key required!

## 🚀 Features
- Runs **offline** (no OpenAI API required)
- Uses **LLaMA models** for text generation
- Lightweight and fast

## 📂 Project Structure
- **Local-ChatGPT/**
  - 📂 `models`
    - `llama-2-7b.Q4_K_M.gguf`- Store downloaded Llama model here
  - 📄 `chatbot.py` - Chatbot script
  - 📄 `README.md` - Project documentation
  - 📄 `requirements.txt` - Dependencies

## 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/jefferyraooji/First-AI-Project.git
cd Local-ChatGPT

# Install dependencies
pip install -r requirements.txt
```
## 🏗️ Download a Model
Place a Llama model inside the models/ folder.
You can download .gguf models from:

🔗 TheBloke HuggingFace Repo
🔗 Meta's LLaMA-2 Models

mkdir models
wget -P models/ https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf

## 🏃 Run the Chatbot
```bash
python chatbot.py
```
## 🌟 Example interaction:
```bash
You: Hello!
🤖 Chatbot: Hi! How can I assist you today?
```