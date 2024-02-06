#!/usr/bin/python3
"""define load_from_json_file"""


import json


def load_from_json_file(filename):
    """create to json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
