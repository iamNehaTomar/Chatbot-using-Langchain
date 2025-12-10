Chatbot using LangChain & Llama 2

A simple and customizable AI chatbot built using LangChain, Llama 2 open-source model, and supporting prompt templates for controlled responses.

🚀 Features

Uses Llama 2 (via local inference or API)

Built with LangChain for prompt management and chaining

Custom prompt templates for structured chatbot behavior

Clean modular code

Easy to run and extend

Fully open-source setup

🏗️ Tech Stack

Python 3.x

LangChain

Llama 2 (local or via Ollama/HuggingFace)

Streamlit (if you used UI)


📂 Project Structure (example)
📦 chatbot-using-langchain
├── app.py                # Main chatbot script / UI / API
├── prompts/              # Your custom prompts
│   └── system_prompt.txt
│
├── models/               # Llama model or config
│   └── llama2.yaml
│
├── requirements.txt      # Dependencies
└── README.md             # Documentation

📝 How It Works

Load the Llama 2 model (locally or from Ollama/HuggingFace).

Use LangChain LLM wrappers to connect the model.

Apply a prompt template to control chatbot behavior.

Accept user input and generate responses.

Optionally wrap it with a Streamlit UI or an API.



⚙️ Installation
1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2. Install dependencies
pip install -r requirements.txt

3. Pull the Llama 2 model
ollama pull llama2


▶️ Run the Chatbot
streamlit run app.py
