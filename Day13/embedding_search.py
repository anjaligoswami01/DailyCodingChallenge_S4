from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read knowledge base
with open("sample_data.txt", "r", encoding="utf-8") as file:
    documents = file.readlines()

documents = [doc.strip() for doc in documents]

# Convert documents into embeddings
document_embeddings = model.encode(documents)

print("Documents converted into embeddings successfully!\n")

# User query
query = input("Enter your search query: ")

# Convert query into embedding
query_embedding = model.encode([query])

# Calculate similarity
similarities = cosine_similarity(query_embedding, document_embeddings)

# Get best match
best_match_index = np.argmax(similarities)

print("\nMost Relevant Result:")
print(documents[best_match_index])

print("\nSimilarity Score:")
print(similarities[0][best_match_index])