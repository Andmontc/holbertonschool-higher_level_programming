#!/usr/bin/python3
""" script to add arguments to a list """
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    try:
        itemslist = load_from_json_file("add_item.json")
    except:
        itemslist = []
    itemslist.extend(sys.argv[1:])
    save_to_json_file(itemslist, "add_item.json")
