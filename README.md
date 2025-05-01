# LangChain + Ollama Demo

This is a minimal example illustrating how to use [LangChain](https://www.langchain.com/) with [Ollama](https://ollama.com/) for local language model inference. It demonstrates invoking a local model using the `langchain_ollama` integration.

---

## 🧠 What Is Ollama?

[Ollama](https://ollama.com/) is a tool that lets you run open-source large language models (LLMs) locally on your machine. It provides an easy interface for downloading, running, and interacting with models such as **LLaMA**, **Mistral**, **Gemma**, and others.

You can search for available models and view their sizes here: [ollama.com/search](https://ollama.com/search)

---

## 🔗 What Is LangChain?

[LangChain](https://www.langchain.com/) is a powerful framework for building applications powered by language models. It provides components to integrate with LLMs, manage prompts, chain operations, and more. In this example, we're using `langchain_ollama` to interface with a local Ollama-hosted model through LangChain’s unified chat API.

---

## 💡 What This Demo Does

This script:

- Connects to a locally running Ollama instance.
- Loads the `gemma3:1b` model (or any compatible model you specify).
- Sends a message to the LLM using LangChain's `ChatOllama` interface.
- Prints the AI-generated response.

---

## ⚠️ System Requirements

Running language models locally can be **resource-intensive**, especially on CPU-only machines. Expect high usage of memory and processing power.

> ✅ For lighter performance needs, consider using **smaller models** like `gemma:2b`, `mistral:7b-instruct`, or `llama2:7b`.  
> 🔎 You can explore and compare models at [ollama.com/search](https://ollama.com/search), including their sizes and capabilities.

---

## 🔧 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- A supported model pulled via Ollama (e.g., `ollama pull gemma3:1b`)
- `langchain`, `langchain-community`, and `langchain-ollama` packages

---

## 📦 Installation

1. **Clone the project** and move into the directory:

```
git clone <your-repo-url>
cd <your-project-dir>
```

2. **(Optional but recommended) Create a virtual environment:**

```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies:**

```
pip install -r requirements.txt
```

4. **Install and run Ollama:**

- Download from [ollama.com](https://ollama.com/) and install for your OS.
- Start Ollama in a terminal:

```

ollama run gemma3:1b

```

If you haven't pulled the model yet:

```

ollama pull gemma3:1b

```

## 🚀 Usage

You can use this project in two ways:

---

### 1. Basic One-Off Translation (`main.py`)

Runs a fixed prompt and prints the result.

```
python main.py
```

**Output:**

```
J'aime la programmation.
```

### 2. Interactive Chat Mode (chat.py)

Use the CLI to translate custom text with a selected model and target language.

**Example: Translate a single sentence**

```
python chat.py --text "I love programming." --language French
```

**Example: Start a chat loop**

```
python chat.py
```

**Example: Use a different model or language**

```
python chat.py --model mistral:7b-instruct --language Spanish
```

Type exit or quit to leave chat mode.

## 🧠 References

- [LangChain Ollama Docs](https://python.langchain.com/docs/integrations/chat/ollama/)
- [Ollama Website](https://ollama.com/)
- [LangChain Documentation](https://docs.langchain.com/)

```

```
