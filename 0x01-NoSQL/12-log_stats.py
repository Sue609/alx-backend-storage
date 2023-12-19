#!/usr/bin/env python3
'''
python module for log stats.
'''
from pymongo import MongoClient


if __name__ == "__main__":
    """
    function that returns the list of school having a specific topic
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    PRINT('Methods:')

    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx.collection.count_documents(
            {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')

