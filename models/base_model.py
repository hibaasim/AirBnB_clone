#!/usr/bin/pyhton3
'''Module for the base model'''
from datetime import datetime
import uuid
import models

class BaseModel():
    '''Defines the basemodel'''

    def __init__(self):
        '''Defines the instances

        Args:
            self
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''string that defines the object

        Returns:
            str : string representation
        '''

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''Updates the date
        '''
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        '''Creates a dictionary

        Returns:
            dict: dictionary instance of __dict__
        '''
        dictionary = self.__dict__.copy
        dictionary['__class__'] = self.__class__.name
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

