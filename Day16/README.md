# Diagnosing RAG Failure Modes — Day 16

## 📌 Project Overview

This project focuses on diagnosing and debugging Retrieval-Augmented Generation (RAG) systems.

A RAG pipeline can fail silently by retrieving irrelevant chunks or generating incorrect answers despite correct retrieval. The goal of this project was to systematically identify common RAG failure modes and improve the reliability of the pipeline.

---

# 🚀 Features

- Semantic search using FAISS
- Local embeddings using Sentence Transformers
- Retrieval diagnostics and logging
- Similarity score tracking
- Failure mode classification
- JSON result storage
- Retrieval quality vs answer quality scorecard

---

# 🛠 Technologies Used

- Python
- FAISS
- NumPy
- Sentence Transformers
- JSON Logging

---

# 📂 Project Structure

```bash
Day16/
│
├── documents/
│   └── ai_notes.txt
│
├── rag_debug.py
├── results.json
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your_repo_link>
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python rag_debug.py
```

---

# 🧠 Failure Modes Diagnosed

| Failure Mode | Description |
|---|---|
| Retrieval Failure | Incorrect or unrelated chunks retrieved |
| Context Window Overflow | Too much context passed into generation |
| Answer-Context Mismatch | Generated answer does not match retrieved context |
| Vague Context Retrieval | Generic or unclear chunks retrieved |
| Correct Chunk but Weak Generation | Correct chunk retrieved but poor final answer |

---

# 🔍 Diagnostics Implemented

For every query, the system logs:

- Retrieved chunks
- Similarity scores
- Generated answer
- Failure type
- Retrieval quality score
- Answer quality score

All results are automatically stored in:

```bash
results.json
```

---

# ✅ Improvements Implemented

## 1️⃣ Increased Chunk Overlap

Improved context continuity by increasing chunk overlap during chunking.

---

## 2️⃣ Similarity Threshold Filtering

Added filtering to prevent unrelated chunks from being retrieved.

---

# 📊 Scorecard

The system evaluates:

- Retrieval Quality (1–5)
- Answer Quality (1–5)

Average scores are calculated at the end of execution.

---

# 💡 Key Learnings

- RAG systems require strong observability and debugging
- Chunking strategy significantly impacts retrieval quality
- Embedding quality affects semantic understanding
- Correct retrieval does not always guarantee correct generation
- Logging is critical for trustworthy AI systems

---

# 📌 Example Queries

- What is semantic search?
- What does FAISS do?
- Explain embeddings
- What is quantum computing?
- Summarize all AI topics in detail

---

# 🚀 Future Improvements

- Add real LLM answer generation
- Use vector databases like Pinecone or ChromaDB
- Improve chunk ranking methods
- Add evaluation metrics such as precision and recall
- Build a UI dashboard for diagnostics

---

# 👨‍💻 Author

Built as part of the Daily Coding Challenge — AI Systems Track.