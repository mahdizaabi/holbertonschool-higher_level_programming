#!/usr/bin/python3
"""
Deserialization/decoding
"""
import json
""" Import Json Module """


def from_json_string(my_str):
    """
    JSON String deserialization/decoding
    """
    return json.loads(my_str)
