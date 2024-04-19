#!/usr/bin/python3
"""Este módulo define una clase base para todos los modelos en nuestro clon de hbnb"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models.engine.db_storage import DBStorage


Base = declarative_base()
storage = DBStorage()  # Crea una instancia de DBStorage


class BaseModel:
    """Una clase base para todos los modelos de hbnb"""

    # Verifica el tipo de almacenamiento para determinar las definiciones de columnas
    if storage.get_storage_type() == 'SQLAlchemy':
        # Define columnas para almacenamiento en SQLAlchemy
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    else:
        def __init__(self, *args, **kwargs):
            """Instancia un nuevo modelo"""
            # Verifica si se pasan argumentos
            if not kwargs:
                # Si no hay argumentos, asigna valores predeterminados
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()
            else:
                # Si se pasan argumentos, verifica si se proporcionan valores específicos para id, created_at y updated_at,
                # y si no, asigna valores predeterminados
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.utcnow()
                if 'updated_at' not in kwargs:
                    self.updated_at = datetime.utcnow()
                # Elimina '__class__' del diccionario kwargs
                kwargs.pop('__class__', None)
                # Actualiza los atributos de la instancia con los kwargs proporcionados
                self.__dict__.update(kwargs)

        def save(self):
            """Actualiza updated_at con la hora actual cuando se cambia la instancia y guarda según el tipo de almacenamiento"""
            self.updated_at = datetime.utcnow()
            storage.new(self)
            storage.save()  # Guarda en el almacenamiento

        def __str__(self):
            """Devuelve una representación en cadena de la instancia"""
            cls = type(self).__name__
            return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

        def to_dict(self):
            """Convierte la instancia en formato de diccionario"""
            dictionary = {}
            dictionary.update(self.__dict__)
            dictionary['__class__'] = type(self).__name__
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
            # Elimina la clave '_sa_instance_state' si existe
            dictionary.pop('_sa_instance_state', None)
            return dictionary

        def delete(self):
            """Elimina la instancia actual del almacenamiento."""
            storage.delete(self)
