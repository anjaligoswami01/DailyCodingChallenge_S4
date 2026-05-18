import json
from datetime import datetime
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# Load environment variables
load_dotenv()

# -----------------------------
# Load Documents
# -----------------------------
with open(r"C:\Users\DELL\Documents\DailyCodingChallenge_S4\Day17\document.json", "r") as file:
    raw_docs = json.load(file)

documents = []

for item in raw_docs:
    doc = Document(
        page_content=item["text"],
        metadata=item["metadata"]
    )
    documents.append(doc)

# -----------------------------
# Create Embeddings + Vector DB
# -----------------------------

# Free local embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    documents,
    embeddings
)

print("✅ Vector database created successfully!")

# -----------------------------
# Filtered Retrieval Function
# -----------------------------
def filtered_retrieve(query, filters=None, top_k=3):

    # Step 1: Similarity Search
    results = vectorstore.similarity_search(query, k=top_k)

    # Step 2: Apply Metadata Filters
    if filters:
        filtered_results = []

        for doc in results:

            metadata = doc.metadata

            # Category Filter
            if "category" in filters:
                if metadata.get("category") != filters["category"]:
                    continue

            # Document Type Filter
            if "document_type" in filters:
                if metadata.get("document_type") != filters["document_type"]:
                    continue

            # Date Filter
            if "date_after" in filters:

                doc_date = datetime.strptime(
                    metadata.get("date"),
                    "%Y-%m-%d"
                )

                cutoff_date = datetime.strptime(
                    filters["date_after"],
                    "%Y-%m-%d"
                )

                if doc_date < cutoff_date:
                    continue

            filtered_results.append(doc)

        return filtered_results

    return results

# -----------------------------
# Test Queries
# -----------------------------
queries = [
    "What is LangChain?",
    "How does FAISS work?",
    "What improves retrieval precision?",
    "AI adoption trends",
    "AI chatbots for marketing"
]

print("\n==============================")
print("WITHOUT FILTERS")
print("==============================")

for query in queries:

    print(f"\nQuery: {query}")

    results = filtered_retrieve(query)

    for idx, doc in enumerate(results, start=1):
        print(f"\nResult {idx}")
        print("Text:", doc.page_content)
        print("Metadata:", doc.metadata)

print("\n==============================")
print("WITH FILTERS")
print("==============================")

filter_examples = [
    {"category": "AI"},
    {"category": "Vector Database"},
    {"document_type": "research"},
    {"date_after": "2023-01-01"},
    {"category": "Marketing"}
]

for query, filters in zip(queries, filter_examples):

    print(f"\nQuery: {query}")
    print("Filters:", filters)

    results = filtered_retrieve(query, filters)

    if not results:
        print("No matching documents found.")

    for idx, doc in enumerate(results, start=1):
        print(f"\nResult {idx}")
        print("Text:", doc.page_content)
        print("Metadata:", doc.metadata)