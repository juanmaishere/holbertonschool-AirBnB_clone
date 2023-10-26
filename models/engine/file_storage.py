#!/usr/bin/python3
""" summary """
import json


class FileStorage:
    """
    Filestorage for the classes
    Serializes and deserializes
    """
    def __init__(self):
        """
        create or open json file to
        serialize each obj dict
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ Returns the dict of attr"""
        return self.__objects

    def save(self):
        """ Serialize objects to JSON and save to file """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def new(self, obj):
        """ Create new keyvalue in dict"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def reload(self):
        """deserialize the json to dict"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except Exception:
            pass
