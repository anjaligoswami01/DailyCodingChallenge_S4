import nltk
from nltk.tokenize import sent_tokenize
import tiktoken

# Download tokenizer
nltk.download('punkt')

# -----------------------------------
# Load Text File
# -----------------------------------

with open("company_policy.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("\nORIGINAL DOCUMENT:\n")
print(text)

# -----------------------------------
# Sentence-Based Chunking
# -----------------------------------

print("\n" + "=" * 60)
print("SENTENCE-BASED CHUNKING")
print("=" * 60)

sentences = sent_tokenize(text)

chunks = []
current_chunk = ""

MAX_CHARS = 120

for sentence in sentences:
    if len(current_chunk) + len(sentence) < MAX_CHARS:
        current_chunk += " " + sentence
    else:
        chunks.append(current_chunk.strip())
        current_chunk = sentence

if current_chunk:
    chunks.append(current_chunk.strip())

for idx, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {idx}:")
    print(chunk)

# -----------------------------------
# Token Counting (AI Engineering)
# -----------------------------------

print("\n" + "=" * 60)
print("TOKEN ANALYSIS")
print("=" * 60)

encoding = tiktoken.get_encoding("cl100k_base")

for idx, chunk in enumerate(chunks, start=1):
    tokens = encoding.encode(chunk)

    print(f"\nChunk {idx}")
    print(f"Characters : {len(chunk)}")
    print(f"Tokens      : {len(tokens)}")

# -----------------------------------
# Metadata Creation
# -----------------------------------

print("\n" + "=" * 60)
print("CHUNK METADATA")
print("=" * 60)

chunk_data = []

for idx, chunk in enumerate(chunks, start=1):
    chunk_info = {
        "chunk_id": idx,
        "content": chunk,
        "length": len(chunk)
    }

    chunk_data.append(chunk_info)

for item in chunk_data:
    print(item)

# -----------------------------------
# Engineering Insights
# -----------------------------------

print("\n" + "=" * 60)
print("ENGINEERING INSIGHTS")
print("=" * 60)

print("""
1. Sentence-aware chunking keeps information meaningful.

2. Token counting is important because LLMs process tokens, not characters.

3. Smaller chunks improve retrieval speed.

4. Metadata helps AI systems track chunk sources.

5. Good chunking improves RAG performance and search accuracy.
""")