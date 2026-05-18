# 🚀 Day 17 — Improve RAG Precision with Metadata Filtering

## 📌 Project Overview

This project upgrades a basic Retrieval-Augmented Generation (RAG) pipeline by adding **metadata-aware retrieval** using LangChain and FAISS.

Traditional vector similarity search retrieves documents only based on semantic similarity, which can lead to irrelevant or outdated results. Metadata filtering improves retrieval precision by applying structured constraints such as:

- Category
- Source
- Date
- Document Type

This project demonstrates how modern AI systems combine semantic search with metadata filtering to build smarter and more accurate retrieval pipelines.

---

# 🧠 Features

✅ Semantic vector search using FAISS  
✅ Metadata-aware retrieval  
✅ Category filtering  
✅ Date filtering  
✅ Document type filtering  
✅ Precision comparison (with vs without filters)  
✅ Free local embeddings using HuggingFace  
✅ Beginner-friendly implementation

---

# 🛠️ Tech Stack

- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Sentence Transformers

---

# 📂 Project Structure

```bash
Day17/
│── app.py
│── documents.json
│── README.md