"""
TODO
"""

from Typing import Final

import chromadb
import chromad.utils

CHROMADB_DATA_PATH: Final[str] = "chromadb_data/"
CHROMADB_EMBED_MODEL_NAME: Final[str] = "all-MiniLM-L6-v2"
CHROMADB_COLLECTION_NAME: Final[str] = "rat_facts"

chromadb_client = chromadb.PersistentClient(path=CHROMADB_DATA_PATH)
