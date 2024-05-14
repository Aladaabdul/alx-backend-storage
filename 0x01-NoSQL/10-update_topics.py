#!/usr/bin/env python3


""" function that changes all topics of a school document based on the name"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document based on the name

    """
    value = {"school": name}
    updated_value = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(value, updated_value)
    return result
