#!/usr/bin/env python3
'''
Module that introduces a function.
'''


def schools_by_topic(mongo_collection, topic):
    '''
    function that returns the list of school having a specific topic
    '''
    doc = mongo_collection.find({"topic": topic})
    return list(doc)

