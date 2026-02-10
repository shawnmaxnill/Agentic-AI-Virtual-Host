# Uses load_csv and indexer.py
# Main script to create vectorstore

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from load_csv import load_products
from indexer import row_to_document

def build_index(csv_path, out_dir):

    print("Loading paths...")
    rows = load_products(csv_path)

    print("Converting to documents...")
    docs = [row_to_document(r) for r in rows if r]

    print("Loading in Transformers...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating vector stores")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(out_dir)

    print("Vector store created")

if __name__ == "__main__":
    build_index("../data/product.xlsx", "../data/vectorstore")
