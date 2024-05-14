#!/usr/bin/env python3


"""function that returns the list of school having a specific topic"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic
    """
    result = mongo_collection.find({}, {"topic": topic})
    return [doc for doc in result]
