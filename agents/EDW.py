import ollama
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

class EDWAgent:
    def __init__(self, spec_collection: str):
        self.spec_collection = spec_collection
        self._init_rag()

    def _init_rag(self):
        chroma_client = chromadb.PersistentClient(path="./chroma_db")
        chroma_collection = chroma_client.get_or_create_collection(self.spec_collection)
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        self.index = VectorStoreIndex.from_vector_store(vector_store)

    def generate_reconciliation_sql(self, source_table: str, target_table: str) -> str:
        prompt = f"""
Generate Teradata SQL to reconcile row count between {source_table} and {target_table}.
Include percentage difference and flag if > 1%.
Output ONLY SQL, no explanation.
"""
        try:
            response = ollama.generate(model='llama3', prompt=prompt)
            return response['response'].strip()
        except Exception as e:
            return f"-- ERROR: {str(e)}"

if __name__ == "__main__":
    print("EDW Agent ready. Initialize with spec collection.")