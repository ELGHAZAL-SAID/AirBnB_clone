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

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        dict = {}
        for key, obj in FileStorage.__objects.items():
            serialized_data = obj.to_dict()
            dict[key] = serialized_data

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dict, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        dct = {'BaseModel': BaseModel, 'User': User, 'State': State, "City": City, "Amenity":Amenity, 'Amenity': Place, 'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for value in json.load(f).values():
                    self.new(dct[value['__class__']](**value))
