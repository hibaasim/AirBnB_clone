#!/usr/bin/python3
'''Module for JSON conversion'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    '''Defines the file storage units

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects

        Returns:
            dict: the __objects dictionary
        '''
        return self.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: the value
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file'''
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as objfile:
            json.dump(obj_dict, objfile)

    def reload(self):
        '''Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as objfile:
                obj_dict = json.load(objfile)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    objct = eval(class_name)
                    instance = objct(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
