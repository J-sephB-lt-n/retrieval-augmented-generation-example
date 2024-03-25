"""
Interactive querying of the vector database from the command line

Example usage:
    $ python query_vector_db.py --help
    $ python query_vector_db.py --top_k 3

Example queries:
    "Do rats carry disease?"
    "Can a rat smile?"
"""

import argparse
import json

from create_vector_db import chromadb_collection

parser = argparse.ArgumentParser()
parser.add_argument(
    "-k",
    "--top_k",
    help="Number of matches to return from the database for each query",
    type=int,
    required=True,
)
args = parser.parse_args()

while True:
    print("Please enter a query: ")
    print('(enter "exit" or use <ctrl+C> to terminate this program)')
    user_query = input()
    if user_query == "exit":
        break
    query_results = chromadb_collection.query(
        query_texts=[user_query], n_results=args.top_k
    )
    print(json.dumps(query_results, indent=4))
    _ = input("Press enter to continue")
    if _ == "exit":
        break
