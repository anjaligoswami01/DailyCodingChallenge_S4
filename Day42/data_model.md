# Data Model

## Product Overview

AI Data Engineering Mentor provides personalized learning guidance, roadmap generation, code reviews, and technical question answering for aspiring Data Engineers.

---

## Data Requirements

### User Profile

Stores learner information.

Fields:

* user_id
* name
* experience_level
* target_role
* current_skills
* target_skills

Storage:
PostgreSQL

---

### Learning Roadmap

Stores generated learning plans.

Fields:

* roadmap_id
* user_id
* milestone
* status

Storage:
PostgreSQL

---

### Progress Tracking

Stores completed topics and progress percentage.

Fields:

* user_id
* completed_topics
* progress_percentage

Storage:
PostgreSQL

---

### Knowledge Chunks

Stores processed technical content.

Fields:

* chunk_id
* source
* topic
* content
* embedding

Storage:
FAISS

---

## Data Sources

Knowledge comes from:

* PostgreSQL Documentation
* Python Documentation
* Apache Spark Documentation
* Apache Airflow Documentation
* Snowflake Documentation
* Data Engineering Interview Questions
* Project Templates

---

## Data Processing Flow

Documents
→ Chunking
→ Embedding Generation
→ FAISS Indexing
→ Retrieval

---

## Knowledge Base Updates

New content follows:

Document Upload
→ Chunking
→ Embedding Generation
→ FAISS Update
→ Available for Retrieval
