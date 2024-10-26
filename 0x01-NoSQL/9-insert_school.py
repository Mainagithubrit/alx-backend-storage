#!/usr/bin/ python3
""" A python function using pymongo module"""


def insert_school(mongo_collection, **kwargs):
    """A function that inserts a new document in a collection"""
    create = mongo_collection.insert_one(kwargs)
    return create.inserted_id
