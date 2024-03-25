"""
Example usage:

    python query_vector_db.py \
            --query "What are rats good at?" \
            --top_k 3
"""


import argparse

from create_vector_db import chroma_collection


