# DATA-AI-Testing-Framework
Autonomous Data Testing Framework for EDAG — OSS LLMs (Llama3) + RAG + Multi-Agent MCP

# 🧪 **DATA AI Data Testing Framework (OSS)**  
> *Autonomous, Layer-Wise Data Validation for Datalake → EDW → Datamart → QlikSense — Powered by Open-Source LLMs, RAG & Multi-Agent MCP*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Built with Ollama + Llama3](https://img.shields.io/badge/LLM-Llama3%20%7C%20Mistral%20%7C%20Phi--3-ff69b4)](https://ollama.com)
[![RAG + MCP](https://img.shields.io/badge/Architecture-RAG%20%2B%20Multi--Agent%20MCP-00bfff)](https://microsoft.github.io/autogen)

---

## ✅ What is This?

A **100% open-source, AI-driven data testing framework** designed for the **DATA platform** (or any modern data stack) that:

- 🤖 **Autonomously generates test scripts** per layer (Datalake, DWH, Datamart, Reporting) using **local LLMs** (Llama 3, Mistral, Phi-3 via Ollama).
- 📚 **Interprets mapping docs & interface specs** via **RAG** (LlamaIndex + ChromaDB).
- 🤝 **Coordinates validation across layers** using **Multi-Agent Collaborative Planning (MCP)** with Microsoft AutoGen.
- 🧩 **Self-healing & adaptive** — learns from test history, adjusts tolerances, detects drift.
- 🔌 **Plug-and-play** with Hadoop, Hive, Teradata, QlikSense, Spark, and more.

---

## 🚀 Key Features

| Feature                  | Tech Used                          |
|--------------------------|------------------------------------|
| **LLM-Powered Script Gen** | Llama 3 / Mistral / Phi-3 (Ollama) |
| **Dynamic Spec Reading**   | RAG (LlamaIndex + Chroma + SentenceTransformers) |
| **Cross-Layer Coordination** | AutoGen Multi-Agent MCP            |
| **Test Execution**         | PySpark, SQL, Python, Qlik API     |
| **UI Dashboard**           | Streamlit                          |
| **Workflow Orchestration** | Prefect / Airflow                  |
| **OCR for Dashboards**     | PaddleOCR + OpenCV (Optional)      |
| **Zero Cloud Dependency**  | 100% On-Prem / Local Execution     |

---

## 📁 Project Structure
edag-ai-testing-oss/
├── agents/ # Layer-specific AI agents
├── rag/ # RAG ingestion & querying
├── autogen/ # Multi-agent MCP orchestration
├── specs/ # Sample mapping docs (YAML, PDF, TXT)
├── tests/generated/ # Auto-generated test scripts
├── ui/ # Streamlit dashboard
└── workflows/ # Prefect/Airflow pipelines

🌐 Use Cases
✅ Automate data validation script creation for large EDW migrations
✅ Reduce testing cycle time by 70% with AI-generated scripts
✅ Ensure consistency from raw ingestion → business dashboards
✅ Enable non-technical teams to “ask” the system to validate rules in plain English
✅ Self-healing tests adapt to schema changes — no manual updates needed

🤝 Contributing
We ❤️ contributions!

Add connectors: Snowflake, BigQuery, Power BI, etc.
Improve RAG accuracy with fine-tuned embeddings
Build Grafana dashboards or CI/CD integrations
Add Kubernetes deployment templates
👉 See CONTRIBUTING.md

📜 License
MIT — Use freely in commercial and open-source projects.

🧑‍💻 Built For
Data Engineers
Data Quality Analysts
Platform Architects
AI/ML Engineers
DevOps / MLOps Teams
📬 Contact / Support
Created with ❤️ for intelligent, open, and autonomous data platforms.
