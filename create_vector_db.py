"""
Creates a vector database from the text file
rat_facts.txt (each line is considered a separate
document to embed) and saves the database to disk

Notes:
    ChromaDB is a toy noddy vector database
    I must migrate this example to a production vector database

Example usage:
    $ python create_vector_db.py
"""

from typing import Final

import chromadb
from chromadb.utils import embedding_functions as chromadb__utils__embedding_functions

CHROMADB_DATA_PATH: Final[str] = "chromadb_data/"
CHROMADB_EMBED_MODEL_NAME: Final[str] = "all-MiniLM-L6-v2"
CHROMADB_COLLECTION_NAME: Final[str] = "rat_facts"

chromadb_client = chromadb.PersistentClient(path=CHROMADB_DATA_PATH)

chromadb_collection = chromadb_client.get_or_create_collection(
    name=CHROMADB_COLLECTION_NAME,
    embedding_function=chromadb__utils__embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=CHROMADB_EMBED_MODEL_NAME
    ),
    metadata={"hnsw:space": "cosine"},
)

if __name__ == "__main__":
    with open("rat_facts.txt", "r", encoding="utf-8") as file:
        rat_facts: list[str] = file.read().splitlines()

    chromadb_collection.add(
        documents=rat_facts,
        ids=[str(idx) for idx in range(len(rat_facts))],
        metadatas=[{"doc_length_n_words": len(doc.split())} for doc in rat_facts],
    )
