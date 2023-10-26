#!/usr/bin/python3
""" summary """
import json


class FileStorage:
    """
    Filestorage for the aelfsses
    Serializes and deserializes
    """
    def __init__(self):
        # Private class attributes
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ Returns the dict of attr"""
        return self.__objects

    def save(self):
        """
        Serializes __objects to the JSON file specified by __file_path.
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def new(self, obj):
        """ Create a new key-value in the dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def reload(self):
        """Deserialize the JSON to the dictionary"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except Exception:
            pass