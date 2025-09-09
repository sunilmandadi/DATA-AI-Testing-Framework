# DATA-AI-Testing-Framework
Autonomous Data Testing Framework for EDAG — OSS LLMs (Llama3) + RAG + Multi-Agent MCP

# 🧪 **EDAG AI Data Testing Framework (OSS)**  
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
