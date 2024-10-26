#!/usr/bin/env python3
""" A python function using pymongo module"""


def insert_school(mongo_collection, **kwargs):
    """A function that inserts a new document in a collection"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
