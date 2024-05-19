#!/usr/bin/python3
'''Module for file storage'''
from models.base_model import BaseModel
import json


class FileStorage:
    '''Defines a JSON serialization and Deserialization process

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns __objects

        Returns:
            dict: the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''Sets the key of the dictionary

        Args:
            obj: the object class name
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file'''
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
             
        with open(self.__file_path, 'w', encoding='utf-8') as obj_file:
            json.dump(obj_dict, obj_file)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as obj_file:
                obj_dict = json.load(obj_file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    objct = eval(class_name)
                    instance = objct(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

