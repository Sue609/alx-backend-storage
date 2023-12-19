#!/usr/bin/env python3
'''
module that changes school topics
'''


def update_topics(mongo_collection, name, topics):
    """
    Python function that changes all topics of a school document.
    """
    query = {"name": name}
    values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, values)

