import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# -----------------------------------
# Load FREE Local Embedding Model
# -----------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# -----------------------------------
# Load Document
# -----------------------------------
with open(r"C:\Users\DELL\Documents\DailyCodingChallenge_S4\Day16\ai_notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

# -----------------------------------
# Chunking Function
# -----------------------------------
def chunk_text(text, chunk_size=250, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

# Create chunks
chunks = chunk_text(text)

# -----------------------------------
# Create Embeddings
# -----------------------------------
def get_embedding(text):

    embedding = model.encode(text)

    return embedding

# Generate embeddings for all chunks
embeddings = [get_embedding(chunk) for chunk in chunks]

# Convert to numpy float32
embedding_matrix = np.array(embeddings).astype("float32")

# -----------------------------------
# Create FAISS Index
# -----------------------------------
dimension = embedding_matrix.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embedding_matrix)

# -----------------------------------
# Retrieve Similar Chunks
# -----------------------------------
def retrieve(query, top_k=3):

    query_embedding = np.array(
        [get_embedding(query)]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    retrieved_chunks = []

    for rank, idx in enumerate(indices[0]):

        # Similarity threshold
        if distances[0][rank] < 2.0:

            chunk_data = {
                "chunk_id": int(idx),
                "score": float(distances[0][rank]),
                "content": chunks[idx]
            }

            retrieved_chunks.append(chunk_data)

    return retrieved_chunks

# -----------------------------------
# Generate Answer
# -----------------------------------
def generate_answer(query, retrieved_chunks):

    if len(retrieved_chunks) == 0:
        return "No relevant information found."

    context = "\n\n".join(
        [chunk["content"] for chunk in retrieved_chunks]
    )

    answer = f"""
Generated answer based on retrieved context:

{context[:400]}
"""

    return answer

# -----------------------------------
# Failure Classification
# -----------------------------------
def classify_failure(query, answer, retrieved_chunks):

    if len(retrieved_chunks) == 0:
        return "Retrieval Failure"

    combined_context = " ".join(
        [chunk["content"] for chunk in retrieved_chunks]
    ).lower()

    # Context overflow simulation
    if len(combined_context) > 1200:
        return "Context Window Overflow"

    # Vague retrieval
    vague_queries = [
        "what is it",
        "how does this work",
        "why is this important"
    ]

    for vague in vague_queries:
        if vague in query.lower():
            return "Vague Context Retrieved"

    # Correct chunk but weak answer
    if "Generated answer" in answer:
        return "Correct Chunk Retrieved but Weak Generation"

    return "Successful Retrieval"

# -----------------------------------
# Test Queries (15)
# -----------------------------------
test_queries = [

    # Retrieval Failure
    "What is quantum computing?",
    "Explain blockchain technology",
    "What is cloud gaming?",

    # Context Overflow
    "Summarize all AI topics in detail",
    "Explain every concept mentioned",
    "Give complete detailed notes",

    # Answer-Context Mismatch
    "What is machine learning?",
    "Define neural networks",
    "Explain embeddings",

    # Vague Retrieval
    "What is it used for?",
    "How does this system work?",
    "Why is this important?",

    # Correct Retrieval
    "What is semantic search?",
    "What does FAISS do?",
    "What are vector embeddings?"
]

# -----------------------------------
# Run Diagnostics
# -----------------------------------
results = []

retrieval_scores = []
answer_scores = []

print("\n========== RAG DIAGNOSTICS ==========\n")

for query in test_queries:

    print("\n----------------------------------")
    print("QUERY:", query)

    # Retrieve chunks
    retrieved = retrieve(query)

    # Generate answer
    answer = generate_answer(query, retrieved)

    # Classify result
    failure_type = classify_failure(
        query,
        answer,
        retrieved
    )

    # Simple scoring
    retrieval_quality = min(len(retrieved) + 2, 5)
    answer_quality = 3 if len(retrieved) > 0 else 1

    retrieval_scores.append(retrieval_quality)
    answer_scores.append(answer_quality)

    # Store result
    result = {
        "query": query,
        "retrieved_chunks": retrieved,
        "generated_answer": answer,
        "failure_type": failure_type,
        "retrieval_quality": retrieval_quality,
        "answer_quality": answer_quality
    }

    results.append(result)

    # Print output
    print("\nRetrieved Chunks:")

    for chunk in retrieved:

        print(f"\nChunk ID: {chunk['chunk_id']}")
        print(f"Score: {chunk['score']:.4f}")
        print(f"Content: {chunk['content'][:150]}")

    print("\nFailure Type:", failure_type)

    print("\nGenerated Answer:")
    print(answer)

# -----------------------------------
# Save Results to JSON
# -----------------------------------
with open("results.json", "w", encoding="utf-8") as f:

    json.dump(
        results,
        f,
        indent=4,
        ensure_ascii=False
    )

# -----------------------------------
# Final Scorecard
# -----------------------------------
avg_retrieval = sum(retrieval_scores) / len(retrieval_scores)

avg_answer = sum(answer_scores) / len(answer_scores)

print("\n===================================")
print("FINAL SCORECARD")
print("===================================")

print(f"Average Retrieval Quality: {avg_retrieval:.2f}/5")

print(f"Average Answer Quality: {avg_answer:.2f}/5")

print("\nResults saved to results.json")