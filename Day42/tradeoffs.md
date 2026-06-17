# Architectural Trade-Offs

## Trade-Off 1

Chosen:
FAISS Vector Database

Gave Up:
Cloud-scale distributed vector search

Why Acceptable:
The knowledge base is small enough to fit efficiently on a single machine.

---

## Trade-Off 2

Chosen:
Local Sentence Transformer Embeddings

Gave Up:
Potentially higher-quality commercial embedding APIs

Why Acceptable:
Development cost remains close to zero while maintaining sufficient retrieval quality.

---

## Trade-Off 3

Chosen:
Single FastAPI Application

Gave Up:
Independent scaling of mentor, roadmap, and review services

Why Acceptable:
Simpler architecture accelerates development and debugging during the MVP stage.
