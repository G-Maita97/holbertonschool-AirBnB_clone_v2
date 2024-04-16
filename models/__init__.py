#!/usr/bin/python3
"""Este script inicializa el tipo de almacenamiento para la aplicación HBNB."""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Verificar si la variable de entorno HBNB_TYPE_STORAGE está configurada como 'db'
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    # Si HBNB_TYPE_STORAGE es 'db', crear una instancia de DBStorage y almacenarla en la variable storage
    storage = DBStorage()
else:
    # Si HBNB_TYPE_STORAGE no es 'db', crear una instancia de FileStorage y almacenarla en la variable storage
    storage = FileStorage()

# Llamar al método reload() para cargar los datos del almacenamiento correspondiente
storage.reload()

