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


serialized_objects = {}  # Create an empty dictionary to store serialized objects

# Iterate through each key-value pair in the FileStorage.__objects dictionary
for key, obj in FileStorage.__objects.items():
    # 'key' is the combination of class name and object ID, 'obj' is the object itself
    
    # Call the 'to_dict()' method on the object to serialize its attributes into a dictionary
    serialized_data = obj.to_dict()
    
    # Use the 'key' as the dictionary key and the 'serialized_data' as the value
    serialized_objects[key] = serialized_data

# After the loop, 'serialized_objects' contains serialized representations of all objects
# where each key is the unique identifier and the corresponding value is the serialized data
