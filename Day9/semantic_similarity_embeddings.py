from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample dataset
sentences = [
    "Artificial Intelligence is transforming industries.",
    "Machine learning helps computers learn from data.",
    "Deep learning is a subset of machine learning.",
    "The weather is pleasant today.",
    "I enjoy working on AI projects."
]

# Convert sentences into embeddings
embeddings = model.encode(sentences)

# Query sentence
query = "AI is changing the world"

# Generate query embedding
query_embedding = model.encode([query])

# Calculate cosine similarity
similarities = cosine_similarity(query_embedding, embeddings)[0]

# Create results dataframe
results = pd.DataFrame({
    "Sentence": sentences,
    "Similarity Score": similarities
})

# Sort results
results = results.sort_values(by="Similarity Score", ascending=False)

print("\nQuery:", query)
print("\nMost Similar Sentences:\n")
print(results)