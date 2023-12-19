#!/usr/bin/env python3
"""
module for inserting a document in python.
"""


def insert_school(mongo_collection, **kwargs):
    """
    python function that inserts a new doc in a collection.
    """
    new_doc = mongo_collection.insert(kwargs)

    return new_doc

