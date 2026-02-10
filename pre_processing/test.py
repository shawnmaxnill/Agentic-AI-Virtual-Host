# test_vectorstore.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def main():
    # Load embeddings and FAISS index
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.load_local("../data/vectorstore", embeddings, allow_dangerous_deserialization=True)

    print("Vector store loaded. You can type queries now.\n")

    # Query loop
    while True:
        query = input("Enter your product query (or 'exit' to quit): ").strip()
        if query.lower() == "exit":
            break

        # Retrieve top 3 relevant products
        results = db.similarity_search(query, k=3)

        if not results:
            print("No products found.\n")
            continue

        # Print results
        for i, doc in enumerate(results, 1):
            print(f"\nResult {i}:")
            print("-" * 40)
            print("Text:\n", doc.page_content)
            print("Metadata:", doc.metadata)
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
