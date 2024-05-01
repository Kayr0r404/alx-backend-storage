#!/usr/bin/env python3
"""task 12"""

from pymongo import MongoClient


def log_stats():
    """log status of nginx"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(db.nginx.count_documents({})))
    print("Methods:")
    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, db.nginx.count_documents({"method": method})
            )
        )
    print("{} status check".format(db.nginx.count_documents({"path": "/status"})))

    print("IPs:")
    request_logs = client.logs.nginx.aggregate(
        [
            {"$group": {"_id": "$ip", "totalRequests": {"$sum": 1}}},
            {"$sort": {"totalRequests": -1}},
            {"$limit": 10},
        ]
    )
    for request_log in request_logs:
        ip = request_log["_id"]
        ip_requests_count = request_log["totalRequests"]
        print("\t{}: {}".format(ip, ip_requests_count))


if __name__ == "__main__":
    log_stats()
