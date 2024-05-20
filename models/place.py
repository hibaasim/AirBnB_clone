#!/usr/bin/python3
'''Module for places'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''Defines the place

    Attributes:
        city_id: the City.id
        user_id: the User.id
        name: the place name
        description: the place description
        number_rooms: number of rooms
        number_bathrooms: number of bathrooms
        max_guest: maximum number of guests
        price_by_night: price per night
        latitude: the latitude
        longitude: the longitude
        amenity_ids: the list of Amenity.id
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
