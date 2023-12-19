#!/usr/bin/env python3
'''
This module introduces a mongodb python script
'''


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection.
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents

