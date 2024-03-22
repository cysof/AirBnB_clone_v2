#!/usr/bin/python3

""" This module defines a class to manage file storage for hbnb clone
"""
import json


class FileStorage:

    """ This class manages storage of hbnb models in JSON format.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        """
        # if no class is provided, return all stored objects
        if cls is None:
            return FileStorage.__objects
        else:
            # create empty dictionary to hold filtered objects
            filtered_objects = {}
            # iterate through all objects in the __objects dictionary
            for key, obj in FileStorage.__objects.items():
                # we check if the object is an instance of the provided class
                if isinstance(obj, cls):
                    # if object is an instance of the provided class,
                    # we add it to the filtered_objects dictionary
                    filtered_objects[key] = obj
            # Return the dictionary containing objects of the specified class
            return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary.
        """
        key = obj.to_dict()['__class__'] + '.' + obj.id
        self.all()[key] = obj

    def save(self):
        """Saves storage dictionary to file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists.
        """
        # check if an object is provided
        if obj is not None:
            # generate unique key for the object based on its class and ID
            key = obj.to_dict()['__class__'] + '.' + obj.id
            # Remove the object from __objects dictionary if it exists
            # using the generated key; if key doesn't exist, do nothing
            FileStorage.__objects.pop(key, None)

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects.
        """
        self.reload()
