#!/usr/bin/python3
'''BaseModel module'''
import models
import uuid
from datetime import datetime


class BaseModel:
    '''Defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''Defines the instances
        '''
        time = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, time))
                else:
                    setattr(self, key, value)
        
        models.storage.new(self)


    def __str__(self):
        '''Prints string representation'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''Updates updated_at with the current datetime'''
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        '''Creates a dictionary

        Returns:
            __dict__: dictionary of instance
        '''
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

