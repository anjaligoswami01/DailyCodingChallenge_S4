import os
import re

os.makedirs("data", exist_ok=True)

with open("dataset.txt", "r", encoding="utf-8") as f:
    content = f.read()

parts = re.split(r"=== FILE: (.*?) ===", content)

for i in range(1, len(parts), 2):
    filename = parts[i].strip()
    text = parts[i + 1].strip()

    with open(
        os.path.join("data", filename),
        "w",
        encoding="utf-8"
    ) as out:
        out.write(text)

print("All files created successfully!")