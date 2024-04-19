#!/usr/bin/python3
"""
    Init file for models
"""
from 
from os import getenv
from models.engine.db_storage import DBStorage

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
    storage.reload()
else:

