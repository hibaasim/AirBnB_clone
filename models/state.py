#!/usr/bin/python3
'''Module for states'''
from models.base_model import BaseModel

class State(BaseModel):
    '''Defines a state
    
    Attributes:
        name: name of the state
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Instance initialisation'''
        super().__init__(*args, **kwargs)
