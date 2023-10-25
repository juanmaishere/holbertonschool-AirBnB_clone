#!/usr/bin/python3
""" summary """
import json


class FileStorage:
    
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def save(self):
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                json.dump({key: value}, f)

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except Exception:
            pass
