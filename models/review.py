#!/usr/bin/python3
'''Module for reviews'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Defines the reviews

    Attributes:
        place_id: the Place.id
        user_id: the User.id
        text: the review
    '''
    place_id = ""
    user_id = ""
    text = ""
