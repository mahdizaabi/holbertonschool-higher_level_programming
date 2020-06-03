#!/usr/bin/python3
"""
JSON to text
"""
import json

def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file"""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
