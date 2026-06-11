# LangChain LLM Application Development Framework

Welcome to the **LangChain Course** repository! This project is a practical, code-first guide to building advanced applications powered by Large Language Models (LLMs) using the LangChain framework. 

From simple prompt engineering to complex autonomous agents with memory, this repository contains clean Jupyter notebooks and scripts designed to teach you end-to-end LLM orchestration.

---

## 🧠 LangChain Workflow Architecture
Below is the workflow structure of how LangChain connects LLMs with external data sources, memory, and tools:

![LangChain Architecture](https://github.com/YOUR_USERNAME/langchain-llm-apps/blob/main/images/langchain_architecture.png?raw=true)

---

## 🚀 Key Features & Concepts Covered
* **Models & Prompts:** Managing LLMs (OpenAI, Hugging Face, Ollama) and creating dynamic Prompt Templates.
* **Chains (LCEL):** Building sequential workflows using LangChain Expression Language (LCEL).
* **Memory Management:** Adding conversational memory (Buffer, Summary) to keep track of chat history.
* **Data Connection (RAG Basics):** Loading documents, splitting text, and connecting with Vector Stores.
* **Agents & Tools:** Creating smart agents that can decide which tool to use (e.g., Web Search, Calculator, Database).

---

## 🛠️ Tech Stack Used
* **Orchestration Framework:** LangChain (Core, Community, OpenAI)
* **Language:** Python
* **LLM Providers:** OpenAI (GPT-4), Anthropic (Claude), Ollama (Local Models)
* **Vector Store (Optional):** ChromaDB / FAISS

---

## 📂 Repository Structure
```text
├── 01_Prompt_Templates_and_Models/ # Basics of prompting and LLM interaction
├── 02_Chains_and_LCEL/             # Creating custom application pipelines
├── 03_Memory_in_LLMs/              # Adding context and history to chatbots
├── 04_Agents_and_Tools/            # Autonomous agents using Google search/math tools
├── images/                         # Contains architecture diagrams and pictures
│   └── langchain_architecture.png  # LangChain workflow diagram
├── requirements.txt                # Project dependencies
└── .env.example                    # Environment variables template
