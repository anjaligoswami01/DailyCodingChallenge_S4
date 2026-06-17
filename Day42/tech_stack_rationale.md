# Tech Stack Rationale

| Layer            | Technology            | Reason                                                                     |
| ---------------- | --------------------- | -------------------------------------------------------------------------- |
| Frontend         | Next.js               | Server-side rendering improves dashboard loading performance               |
| Backend          | FastAPI               | Async request handling reduces latency during retrieval and LLM processing |
| Database         | PostgreSQL            | Structured storage for user profiles, progress, and learning roadmaps      |
| Vector Database  | FAISS                 | Fast local semantic search with zero infrastructure cost                   |
| Embeddings       | Sentence Transformers | Local embeddings eliminate recurring API costs                             |
| Cache            | Redis                 | Reduces repeated retrieval and LLM requests                                |
| LLM              | Claude/OpenAI         | Strong reasoning for mentorship and roadmap generation                     |
| Deployment       | Railway               | Simplifies deployment without extensive DevOps work                        |
| Frontend Hosting | Vercel                | Optimized hosting for Next.js applications                                 |
| Monitoring       | LangSmith             | Tracks and debugs RAG pipeline behavior                                    |

## Selection Criteria

* Low operating cost
* Fast response time
* Easy deployment
* Scalable for future growth
* Supports Retrieval-Augmented Generation
