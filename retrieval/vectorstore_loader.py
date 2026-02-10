# Loading in vectorstore for LLM

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def load_vectorstore(path: str):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") # maintain same model

    # return vectorstore object
    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )

