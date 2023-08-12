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
        """ Deserializes __objects from the JSON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for value in json.load(f).values():
                    self.new(dct[value['__class__']](**value))
