#!/usr/bin/python3
'''Module for City'''
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    '''Defines the cities

    Attributes:
        state_id: the state id
        name: the city's name
    '''
    state_id = ""
    name  = ""
