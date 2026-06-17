import os
import re
import time
import pandas as pd

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

start_time = time.time()

# -------------------
# PREPROCESSING
# -------------------

def preprocess(text):
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text

# -------------------
# LOAD DOCUMENTS
# -------------------

documents = []

for filename in os.listdir("data"):

    if filename.endswith(".txt"):

        path = os.path.join("data", filename)

        loader = TextLoader(path, encoding="utf-8")

        docs = loader.load()

        for doc in docs:
            doc.page_content = preprocess(
                doc.page_content
            )

        documents.extend(docs)

print(f"\nLoaded Documents: {len(documents)}")

# -------------------
# CHUNKING
# -------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

# -------------------
# EMBEDDINGS
# -------------------

print("\nLoading Embedding Model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------
# FAISS INDEX
# -------------------

print("Creating FAISS Index...")

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

vector_store.save_local("faiss_index")

# -------------------
# METRICS
# -------------------

avg_chunk_size = sum(
    len(chunk.page_content)
    for chunk in chunks
) / len(chunks)

ingestion_time = (
    time.time() - start_time
)

metrics = pd.DataFrame([{
    "documents": len(documents),
    "chunks": len(chunks),
    "avg_chunk_size": round(avg_chunk_size, 2),
    "ingestion_time_seconds": round(ingestion_time, 2),
    "embedding_model": "all-MiniLM-L6-v2"
}])

metrics.to_csv(
    "metrics_log.csv",
    index=False
)

print("\n===== METRICS =====")
print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")
print(f"Average Chunk Size: {avg_chunk_size:.2f}")
print(f"Ingestion Time: {ingestion_time:.2f} seconds")

print("\nFAISS index saved successfully!")
print("metrics_log.csv generated successfully!")

