#!/usr/bin/env python3
"""task 12"""

from pymongo import MongoClient


def log_stats():
    """log status of nginx"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, collection.count_documents({"method": method})
            )
        )
    print("{} status check".format(collection.count_documents({"path": "/status"})))

    print("IPs:")

    cursor = collection.aggregate(
        [
            {"$group": {"_id": "$ip", "same ip": {"$sum": 1}}},
            {"$sort": {"same ip": -1}},
            {"$limit": 10},
        ]
    )
    print(type(collection))

    for i in cursor:
        print((i))


if __name__ == "__main__":
    log_stats()
