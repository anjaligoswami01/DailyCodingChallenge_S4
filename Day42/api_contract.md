# API Contract

## POST /mentor

Purpose:
Answer Data Engineering questions.

Request

{
  "question": "Explain Spark partitioning"
}

Response

{
  "answer": "...",
  "sources": ["Spark Documentation"]
}

Errors

400 Bad Request
429 Rate Limit
500 Internal Server Error

---

## POST /generate-roadmap

Request

{
  "target_role": "Data Engineer",
  "experience_level": "Beginner",
  "skills": ["SQL"]
}

Response

{
  "roadmap": [
    "Advanced SQL",
    "Python",
    "Airflow",
    "Spark"
  ]
}

---

## POST /review-code

Request

{
  "language": "sql",
  "code": "SELECT * FROM employees"
}

Response

{
  "feedback": "Avoid SELECT * in production systems."
}

---

## GET /progress/{user_id}

Response

{
  "completed_topics": 12,
  "progress_percentage": 45
}

---

## GET /health

Response

{
  "status": "healthy"
}