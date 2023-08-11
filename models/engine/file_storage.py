#!/usr/bin/python3

"""files storage file

"""

import json
import os.path


class FileStorage():
    """_summary_

    Returns:
        _type_: _description_
    """

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
        for key, obj in FileStorage.__objects.items():
            serialized_data = obj.to_dict()
            dict[key] = serialized_data

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dict, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    obj = cls(**obj_data)
                    FileStorage.__objects[key] = obj
