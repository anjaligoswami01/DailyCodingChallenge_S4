# Peer Feedback

Peer:
ABTalks Community Member

Feedback:

The initial architecture lacked a caching mechanism, which could increase latency and API costs for repeated questions.

Improvement Made:

Added Redis Cache between the FastAPI Backend and Retrieval Layer.

Impact:

Reduced response time and lowered repeated LLM usage costs.