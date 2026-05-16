# =========================================================
# DAY 15 - FREE LOCAL RAG PIPELINE
# FAISS + HUGGING FACE + FLAN-T5
# =========================================================

# -----------------------------
# IMPORT LIBRARIES
# -----------------------------

from langchain_text_splitters import CharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from transformers import pipeline

# =========================================================
# STEP 1 - LOAD KNOWLEDGE BASE
# =========================================================

with open("knowledge_base.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("\nKnowledge Base Loaded Successfully!\n")

# =========================================================
# STEP 2 - SPLIT TEXT INTO CHUNKS
# =========================================================

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print("=" * 70)
print("TEXT CHUNKS")
print("=" * 70)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)
    print("-" * 70)

# =========================================================
# STEP 3 - CREATE EMBEDDINGS
# =========================================================

print("\nCreating Embeddings...\n")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embeddings Created Successfully!")

# =========================================================
# STEP 4 - CREATE FAISS VECTOR STORE
# =========================================================

print("\nCreating FAISS Vector Store...\n")

vectorstore = FAISS.from_texts(
    chunks,
    embeddings
)

print("FAISS Vector Store Ready!")

# =========================================================
# STEP 5 - LOAD LOCAL LLM
# =========================================================

print("\nLoading Local AI Model...\n")
print("First run may take some time...\n")

llm = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_length=256
)


print("Local LLM Loaded Successfully!")

# =========================================================
# STEP 6 - GENERATE WITH RAG
# =========================================================

def generate_with_rag(query):

    # Retrieve Top 3 Similar Chunks
    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    # Combine Retrieved Chunks
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Prompt Template
    prompt = f"""
You are an intelligent AI assistant.

Use only the information provided in the context to answer the question.

If the required information is not available in the context,
respond with:
"I don't know based on the given context."

Do not make up or assume any information.

Context:
{context}

Question:
{query}

Answer:
"""

    # Generate Response
    response = llm(prompt)

    return response[0]["generated_text"]

# =========================================================
# STEP 7 - GENERATE WITHOUT RAG
# =========================================================

def generate_without_rag(query):

    response = llm(query)

    return response[0]["generated_text"]

# =========================================================
# STEP 8 - TEST QUESTIONS
# =========================================================

queries = [

    "Who is founder of OpenAI?",

    "Explain RAG in simple Terms.",

    "Which team has won the most IPL trophies?",

    "Which famous investor is known as the “Big Bull of India”?",

    "What is GraphQL primarily used for?"

]

# =========================================================
# STEP 9 - COMPARE OUTPUTS
# =========================================================

for i, query in enumerate(queries):

    print("\n" + "=" * 80)
    print(f"TEST QUERY {i+1}")
    print("=" * 80)

    print(f"\nQUESTION:\n{query}")

    # ------------------------------------------------
    # WITHOUT RAG
    # ------------------------------------------------

    without_rag = generate_without_rag(query)

    print("\nWITHOUT RAG:\n")
    print(without_rag)

    # ------------------------------------------------
    # WITH RAG
    # ------------------------------------------------

    with_rag = generate_with_rag(query)

    print("\nWITH RAG:\n")
    print(with_rag)

# =========================================================
# STEP 10 - FAILURE ANALYSIS
# =========================================================

print("\n" + "=" * 80)
print("FAILURE ANALYSIS")
print("=" * 80)

print("""
1. Some answers were inaccurate because the retrieved chunks
did not contain enough detailed information.

2. In a few cases, retrieval returned partially related chunks,
which caused incorrect or incomplete responses.
""")

print("\nRAG Pipeline Execution Completed Successfully!")