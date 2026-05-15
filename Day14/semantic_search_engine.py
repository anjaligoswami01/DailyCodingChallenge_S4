from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 2: Sample dataset (you can expand this later)
documents = [
    "I love learning artificial intelligence",
    "Python is great for data science",
    "Machine learning is a subset of AI",
    "I enjoy watching movies",
    "Deep learning models use neural networks",
    "Data analysis is an important skill"
]

# Step 3: Convert documents into embeddings
doc_embeddings = model.encode(documents)

# Step 4: Semantic Search Function
def semantic_search(query, top_k=3):
    query_embedding = model.encode([query])
    
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
    
    # Get top results
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = [(documents[i], similarities[i]) for i in top_indices]
    return results

# Step 5: Run search
query = input("Enter your search query: ")

results = semantic_search(query)

print("\nTop Results:\n")
for text, score in results:
    print(f"{text} (Score: {score:.4f})")