import ollama
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
import os

class DatalakeAgent:
    def __init__(self, spec_collection: str):
        self.spec_collection = spec_collection
        self._init_rag()

    def _init_rag(self):
        chroma_client = chromadb.PersistentClient(path="./chroma_db")
        chroma_collection = chroma_client.get_or_create_collection(self.spec_collection)
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        self.index = VectorStoreIndex.from_vector_store(vector_store)

    def query_spec(self, question: str) -> str:
        query_engine = self.index.as_query_engine()
        response = query_engine.query(question)
        return str(response)

    def generate_test_script(self, rule: str) -> str:
        prompt = f"""
You are a senior data engineer. Generate a PySpark validation script.
Rule: {rule}
DataFrame is named 'df'. Output ONLY executable Python code. No markdown.
"""
        try:
            response = ollama.generate(model='llama3', prompt=prompt)
            return response['response'].strip()
        except Exception as e:
            return f"# ERROR: Failed to generate script - {str(e)}"

if __name__ == "__main__":
    agent = DatalakeAgent("datalake_specs")
    try:
        rule = agent.query_spec("What is the null tolerance for customer_email?")
        print("📝 Rule:", rule)
        script = agent.generate_test_script(rule)
        print("\n🐍 Generated Script:\n")
        print(script)
    except Exception as e:
        print("⚠️ RAG not initialized. Run 'python rag/ingest.py' first.")