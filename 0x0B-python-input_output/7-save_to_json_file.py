#!/usr/bin/python3
""" write an obj to a file"""
import json


def save_to_json_file(my_obj, filename):
    """ function that write an ibj into a file"""
    text = json.dumps(my_obj)
    with open(filename, 'w') as f:
        return f.write(text)
