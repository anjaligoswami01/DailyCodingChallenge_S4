# Semantic Search vs Keyword Search
# Install required libraries first:
# pip install sentence-transformers scikit-learn pandas

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# -----------------------------
# STEP 1: Create Dataset
# -----------------------------

sentences = [
    "Artificial intelligence is transforming healthcare.",
    "Machine learning helps detect fraud in banking systems.",
    "Deep learning models are used in image recognition.",
    "Natural language processing powers modern chatbots.",
    "AI recommendation systems improve user experience.",
    "Cybersecurity uses AI to detect suspicious activities.",
    "Self-driving cars rely on computer vision technology.",
    "Robotics and AI are changing manufacturing industries.",
    "Voice assistants understand spoken language commands.",
    "AI tools can automate repetitive office tasks.",
    "Cloud computing supports large-scale AI applications.",
    "Big data is important for training AI systems.",
    "Predictive analytics helps businesses make decisions.",
    "Generative AI can create text, images, and music.",
    "Search engines use semantic understanding for better results.",
    "AI-powered healthcare systems assist doctors in diagnosis.",
    "Smartphones use AI for face recognition features.",
    "E-commerce websites use recommendation algorithms.",
    "Education platforms personalize learning with AI.",
    "Virtual assistants schedule meetings automatically."
]

df = pd.DataFrame(sentences, columns=["Sentence"])

# -----------------------------
# STEP 2: Load Embedding Model
# -----------------------------

model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert sentences into vectors
embeddings = model.encode(sentences)

# -----------------------------
# STEP 3: Semantic Search
# -----------------------------

def semantic_search(query, top_k=3):
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, embeddings)[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for idx in top_indices:
        results.append({
            "Sentence": sentences[idx],
            "Similarity Score": round(similarities[idx], 4)
        })

    return pd.DataFrame(results)

# -----------------------------
# STEP 4: Keyword Search
# -----------------------------

def keyword_search(query, top_k=3):
    query_words = query.lower().split()

    scores = []

    for sentence in sentences:
        sentence_words = sentence.lower().split()

        score = sum(word in sentence_words for word in query_words)

        scores.append(score)

    top_indices = sorted(range(len(scores)),
                         key=lambda i: scores[i],
                         reverse=True)[:top_k]

    results = []

    for idx in top_indices:
        results.append({
            "Sentence": sentences[idx],
            "Keyword Match Score": scores[idx]
        })

    return pd.DataFrame(results)

# -----------------------------
# STEP 5: Test Query
# -----------------------------

query = "AI in medical diagnosis"

print("\n==============================")
print("QUERY:", query)
print("==============================")

print("\nTop 3 Semantic Search Results:\n")
print(semantic_search(query))

print("\nTop 3 Keyword Search Results:\n")
print(keyword_search(query))