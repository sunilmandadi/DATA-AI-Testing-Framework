from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
import argparse
import os

def ingest_docs(input_dir: str, collection_name: str):
    print(f"[RAG] Ingesting docs from {input_dir} into collection '{collection_name}'")

    if not os.path.exists(input_dir):
        print(f"❌ Input directory {input_dir} not found.")
        return

    # Load documents
    documents = SimpleDirectoryReader(input_dir).load_data()
    print(f"📄 Loaded {len(documents)} document(s)")

    # Setup Chroma
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Build index
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    print("[RAG] ✅ Ingestion complete. Ready for queries.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest documents into RAG system")
    parser.add_argument("--input", type=str, required=True, help="Input directory path")
    parser.add_argument("--collection", type=str, required=True, help="ChromaDB collection name")
    args = parser.parse_args()
    
    ingest_docs(args.input, args.collection)