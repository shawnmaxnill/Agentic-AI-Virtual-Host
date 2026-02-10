from retrieval.paper_retriever import PaperRetriever
from retrieval.vectorstore_loader import load_vectorstore
from llama_cpp import Llama
from dotenv import load_dotenv
load_dotenv()

print("Loading vecstore")
vectorstore = load_vectorstore("../data/vectorstore")
retriever = PaperRetriever(vectorstore)


# Initialize model
print("Starting model")
model_path = "../models/Llama-2-7b-chat-hf.Q4_K_M.gguf"
model = Llama(
    model_path=model_path,
    n_gpu_layers=-1,
    verbose=True
)

# Retrieve docs
print("Loading query and S-Search")
query = "Im looking to make a smoothie, any recommendations?"
docs = vectorstore.similarity_search(query, k=1)

# Combine docs into context
print("Building context")
context = "\n\n".join(doc.page_content for doc in docs)
print(context)

# Building prompt
print("Model is reading prompt")
prompt = f"""
You are a product manager, your job is to recommend items for customers. Keep the answer short yet informative.
Use the context below to answer the question. Don't use information other than the retrieved context.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{query}
"""

# Generating answer
print("Generating response")

output = model(
    prompt,
    max_tokens=200,
    temperature=0.7,  # Add temperature
    top_p=0.95,       # Add top_p for better generation
    stop=["[INST]", "</s>"]  # Update stop tokens
)

# Choose response
response = output["choices"][0]["text"]

print(response)


