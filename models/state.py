#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """

    # Para DBStorage:
    if storage.get_storage_type() == 'SQLAlchemy':
        __tablename__ = 'states'  # Nombre de la tabla en la base de datos
        name = Column(String(128), nullable=False)  # Columna para el nombre del estado
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
        # cities es un atributo de clase que representa una relación con la clase City.
        # Si se elimina un objeto State, todas las instancias de City relacionadas se eliminarán automáticamente.

    # Para FileStorage:
    else:
        """
        @property es un decorador en Python que convierte el método en una propiedad.
        Esto significa que podemos acceder al método cities como si fuera un atributo
        de instancia, sin necesidad de llamarlo como una función.
        """
        @property
        def cities(self):
            """Getter method for cities related to this state"""
            from models import storage
            from models.city import City
            cities_list = []
            # Iteramos sobre todas las instancias de City en el almacenamiento
            for city in storage.all(City).values():
                # Verificamos si el state_id de la ciudad coincide con el id del estado actual
                if city.state_id == self.id:
                    # Si hay coincidencia, agregamos la ciudad a la lista de ciudades
                    cities_list.append(city)
            # Devolvemos la lista de ciudades relacionadas con el estado actual
            return cities_list

