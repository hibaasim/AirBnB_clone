#!/usr/bin/python3
'''Module to deinr amenity'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Defines the amenity

    Attributes:
        name: the amenity name
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes the instances'''
        super().__init__(*args, **kwargs)
