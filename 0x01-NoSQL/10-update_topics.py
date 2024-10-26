#!/usr/bin/env python3
"""A python functing using pymongo"""


def update_topics(mongo_collection, name, topics):
    """A function that changes document in a collection"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
