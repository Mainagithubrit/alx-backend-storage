#!/usr/bin/env python3
"""A python function using pymongo"""


def schools_by_topic(mongo_collection, topic):
    """A function that returns the list of school with a specific
    topic"""
    res = mongo_collection.find({"topics": topic})
    return list(res)
