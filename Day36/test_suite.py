import requests
import json

URL = "https://your-app.up.railway.app/query"

queries = [
    f"Test query {i}"
    for i in range(1, 16)
]

results = []

for q in queries:
    r = requests.post(
        URL,
        json={"question": q}
    )

    results.append(r.json())

with open(
    "reports/railway_results.json",
    "w"
) as f:
    json.dump(results, f, indent=2)

print("15 tests completed")