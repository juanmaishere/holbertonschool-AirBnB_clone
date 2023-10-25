#!/usr/bin/python3
""" summary """
import json


class FileStorage():
    """
    Class filestorage
    made for storing the dicts
    in json
    """
    
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, obj):
        return self.__objects
    
    def save(self):
        with open(self.__file_path, 'w') as f:
            c = json.dumps(self.__objects)
            f.write(c)
