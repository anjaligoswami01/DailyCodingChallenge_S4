from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load movie data
movies = []

with open("movies.txt", "r", encoding="utf-8") as file:
    for line in file:
        title, description = line.strip().split("|")
        movies.append({
            "title": title.strip(),
            "description": description.strip()
        })

# Create embeddings
movie_descriptions = [movie["description"] for movie in movies]
movie_embeddings = model.encode(movie_descriptions)

print("\n🎬 AI Movie Retrieval System Ready!")

while True:
    query = input("\nEnter movie idea (or type 'exit'): ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    # Convert query to embedding
    query_embedding = model.encode([query])

    # Similarity search
    similarities = cosine_similarity(
        query_embedding,
        movie_embeddings
    )[0]

    # Get top 3 matches
    top_indices = similarities.argsort()[-3:][::-1]

    print("\n🔍 Top Matching Movies:\n")

    for index in top_indices:
        print(f"🎥 {movies[index]['title']}")
        print(f"📖 {movies[index]['description']}")
        print(f"⭐ Similarity Score: {similarities[index]:.4f}\n")