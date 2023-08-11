#!/usr/bin/python3

"""_summary_

"""

import json
import os.path




class FileStorage():
    __file_path = ""
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        dict = {}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dict, file)