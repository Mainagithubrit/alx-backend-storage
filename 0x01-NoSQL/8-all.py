#!/usr/bin/env python3
"""Python function using mongoDB"""


def list_all(mongo_collection):
    """ A function that lists all documments in collection"""
    return [doc for doc in mongo_collection.find()]
