#!/usr/bin/env python3
"""task 8"""


def list_all(mongo_collection):
    """list all documents"""
    return mongo_collection.find()
