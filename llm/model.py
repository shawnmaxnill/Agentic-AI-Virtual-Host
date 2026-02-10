# # Loading FAISS index

# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# db = FAISS.load_local("../data/vectorstore", embeddings)
# retriever = db.as_retriever()  # converts FAISS to a retriever for LLMs
