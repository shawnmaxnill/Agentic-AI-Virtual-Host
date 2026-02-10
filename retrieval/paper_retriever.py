# Retrieve documents from vectorstore

class PaperRetriever:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def retrieve(self, query: str, k: int = 5):
        return self.vectorstore.similarity_search(query, k=k)
