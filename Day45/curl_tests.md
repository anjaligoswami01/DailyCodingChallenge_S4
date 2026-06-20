# Day 45 Curl Verification

## Create Session

curl -X POST http://127.0.0.1:8000/session/create 
-H "x-api-key: day45-secret-key"

Expected:

{
"session_id": "uuid"
}

---

## Ask Question

curl -X POST http://127.0.0.1:8000/ask 
-H "Content-Type: application/json" 
-H "x-api-key: day45-secret-key" 
-d '{
"session_id":"uuid",
"query":"Explain Apache Airflow"
}'

Expected:

{
"response":"...",
"latency_ms":1,
"retrieval_score":0.90
}

---

## Conversation History

curl -X GET http://127.0.0.1:8000/history/{session_id} 
-H "x-api-key: day45-secret-key"

Expected:

{
"messages":[]
}

---

## Feedback

curl -X POST http://127.0.0.1:8000/feedback 
-H "Content-Type: application/json" 
-H "x-api-key: day45-secret-key" 
-d '{
"session_id":"uuid",
"query":"Explain Apache Airflow",
"rating":5,
"helpful":true,
"comments":"Excellent explanation"
}'

Expected:

{
"status":"saved"
}

---

## Rate Limiting

Expected after 20 requests:

HTTP 429

{
"detail":"You have reached the limit of 20 requests per hour."
}
