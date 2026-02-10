from retrieval.paper_retriever import PaperRetriever
from retrieval.vectorstore_loader import load_vectorstore
from llama_cpp import Llama
from dotenv import load_dotenv
load_dotenv()
import os

# Load vectorstore and model once
print("Loading vecstore")
vectorstore = load_vectorstore(os.path.join(os.path.dirname(__file__), "../data/vectorstore"))
retriever = PaperRetriever(vectorstore)

print("Starting model")
model_path = os.path.join(os.path.dirname(__file__), "../models/Llama-2-7b-chat-hf.Q4_K_M.gguf")
model = Llama(model_path=model_path, n_gpu_layers=-1, verbose=True)


def answer_query(query: str, max_tokens=200):
    """Returns the model's response to the query"""
    # Retrieve docs
    docs = vectorstore.similarity_search(query, k=1)

    # Combine docs into context
    context = "\n\n".join(doc.page_content for doc in docs)

    # Build prompt
    prompt = f"""
You are a product manager, your job is to recommend items for customers. Keep the answer short yet informative.
Use the context below to answer the question. Don't use information other than the retrieved context.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{query}
"""

    # Generate answer
    output = model(
        prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=0.95,
        stop=["[INST]", "</s>"]
    )

    response = output["choices"][0]["text"]
    return response
