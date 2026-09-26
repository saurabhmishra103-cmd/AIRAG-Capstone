"""
Vector Database Interface.
This script manages the connection and interactions with the underlying vector database
(such as ChromaDB, FAISS, Qdrant, or Pinecone).
It provides standard methods for initializing the database, inserting document chunks and
their corresponding embeddings, deleting old records, and persisting the index to disk.
This abstraction ensures the core RAG logic remains decoupled from specific database vendors.

Classes:
- BaseVectorStore: Abstract interface for vector databases.
- JSONVectorStore: Implementation using a simple JSON file.
- ChromaDBStore: Implementation using local ChromaDB.
- PineconeStore: Implementation using Pinecone cloud vector DB.
- QdrantStore: Implementation using Qdrant vector DB.
- VectorStoreFactory: Factory to initialize the configured vector store.

Methods:
- add_document(filename, file_type, chunks, embeddings): Inserts records.
- search(query_embedding, top_k): Searches for relevant chunks.
"""




# TODO: Implement ChromaDBStore
class ChromaDBStore(BaseVectorStore):
    def add_document(
        self, filename: str, file_type: str, chunks: list, embeddings: list
    ):
        pass

    def search(self, query_embedding: list[float], top_k: int = 5) -> list[dict]:
        pass


# TODO: Implement PineconeStore
class PineconeStore(BaseVectorStore):
    def add_document(
        self, filename: str, file_type: str, chunks: list, embeddings: list
    ):
        pass

    def search(self, query_embedding: list[float], top_k: int = 5) -> list[dict]:
        pass


# TODO: Implement QdrantStore
class QdrantStore(BaseVectorStore):
    def add_document(
        self, filename: str, file_type: str, chunks: list, embeddings: list
    ):
        pass

    def search(self, query_embedding: list[float], top_k: int = 5) -> list[dict]:
        pass


class VectorStoreFactory:
   
