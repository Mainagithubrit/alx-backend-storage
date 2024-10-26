#!/usr/bin/env python3
"""A pyhton function using pymongo"""
from pymongo import MongoClient


def nginx_request_logs_print(nginx_collection):
    """Prints nginx request logs"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))

def execute():
    """Provides stats on nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)

if __name__ == '__main__':
    execute()
