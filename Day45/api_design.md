# AI Data Engineering Mentor API Surface

| Method | Endpoint              | Purpose                         |
| ------ | --------------------- | ------------------------------- |
| POST   | /session/create       | Create a new user session       |
| POST   | /ask                  | Ask a Data Engineering question |
| GET    | /history/{session_id} | Retrieve conversation history   |
| POST   | /feedback             | Submit response feedback        |
| GET    | /health               | Health check                    |

## Definition of Good Response

A good response should:

* Answer the user's Data Engineering question correctly
* Be clear and easy to understand
* Provide practical guidance
* Suggest next learning steps
* Be relevant to the query
