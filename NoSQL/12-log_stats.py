#!/usr/bin/env python3
"""Log stats from the collection"""

from pymongo import MongoClient

METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


def log_stats(mongo_collection):
    """Script which provides stats about Nginx logs stored in MongoDB"""
    # Count the total number of documents in the collection
    total_logs = mongo_collection.count_documents({})

    print(f"{total_logs} logs")

    print("Methods:")
    # Count the number of documents for each HTTP method and print the results
    for method in METHODS:
        count = mongo_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # Count the number of documents with method=GET and path=/status
    status_check = mongo_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check} status check")


if __name__ == "__main__":
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Specify the database and collection
    db = client.logs
    nginx_collection = db.nginx

    # Call the log_stats function to generate the statistics
    log_stats(nginx_collection)
