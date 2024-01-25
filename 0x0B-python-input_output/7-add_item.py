#!/usr/bin/python3
'''function that creates an Object from a “JSON file'''
import json
import sys


def load_from_json_file(filename):
    '''function that creates an Object from a “JSON file'''
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file,
    using a JSON representation'''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


if len(sys.argv) > 1:
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    new_items = sys.argv[1:]
    updated_data = existing_data + new_items
    save_to_json_file(updated_data, "add_item.json")
