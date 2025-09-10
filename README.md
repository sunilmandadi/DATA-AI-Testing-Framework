# 🧪 DATA AI Data Testing Framework (OSS)
> Autonomous, Layer-Wise Data Validation for Datalake → EDW → Datamart → QlikSense — Powered by Open-Source LLMs, RAG & Multi-Agent MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Built with Ollama + Llama3](https://img.shields.io/badge/LLM-Llama3%20%7C%20Mistral%20%7C%20Phi--3-ff69b4)](https://ollama.com)
[![RAG + MCP](https://img.shields.io/badge/Architecture-RAG%20%2B%20Multi--Agent%20MCP-00bfff)](https://microsoft.github.io/autogen)

---

## ✅ What is This?

A **100% open-source, AI-driven data testing framework** designed for the **DATA platform** (or any modern data stack) that:

- 🤖 **Autonomously generates test scripts** per layer (Datalake, EDW, Datamart, Reporting) using **local LLMs** (Llama 3, Mistral, Phi-3 via Ollama).
- 📚 **Interprets mapping docs & interface specs** via **RAG** (LlamaIndex + ChromaDB).
- 🤝 **Coordinates validation across layers** using **Multi-Agent Collaborative Planning (MCP)** with Microsoft AutoGen.
- 🧩 **Self-healing & adaptive** — learns from test history, adjusts tolerances, detects drift.
- 🔌 **Plug-and-play** with Hadoop, Hive, Teradata, QlikSense, Spark, and more.

---

## 📁 Project Structure

- `agents/` — Layer-specific AI agents (Datalake, EDW, Datamart, Reporting)
- `rag/` — Powered by vector embeddings and RAG (built with LlamaIndex + ChromaDB)
- `autogen/` — Multi-agent MCP orchestration (AutoGen)
- `specs/` — Sample mapping documents
- `ui/` — Streamlit dashboard
- `workflows/` — Prefect/Airflow pipelines
- `configs/` — Configuration files
- `docs/` — Documentation

---
## **UI:**
<img width="1341" height="583" alt="image" src="https://github.com/user-attachments/assets/9dc0638b-71b7-46aa-9e47-baf70dec7b6c" />


## ⚙️ Quick Start

```bash
git clone https://github.com/YOUR-USERNAME/edag-ai-testing-oss.git
cd edag-ai-testing-oss

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Pull local LLM
ollama pull llama3:8b-instruct-q4_K_M

# Ingest sample spec
python rag/ingest.py --input specs/datalake/ --collection datalake_specs

# Run agent
python agents/datalake_agent.py

# Launch dashboard
streamlit run ui/dashboard.py
