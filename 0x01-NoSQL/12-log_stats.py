#!/usr/bin/env python3
"""task 12"""

from pymongo import MongoClient


def log_stats():
    """log status of nginx"""
    client = MongoClient()
    db = client.logs
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(db.nginx.count_documents({})))
    print("methods:")
    for method in methods:
        print(
            "\t method {}: {}".format(
                method, db.nginx.count_documents({"method": method})
            )
        )
    print("{} status check".format(db.nginx.count_documents({"path": "/status"})))


if __name__ == "__main__":
    log_stats()
