#!/usr/bin/python3
"""Script para la clase DBStorage en el proyecto HBNB"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage


class DBStorage:
    """Clase para el almacenamiento de base de datos"""

    # Atributos privados de clase
    __engine = None  # Motor de la base de datos
    __session = None  # Sesión de la base de datos

    def __init__(self):
        """Inicializa una nueva instancia de DBStorage"""
        # Obtener variables de entorno para la configuración de la base de datos
        db_user = getenv('HBNB_MYSQL_USER', default='hbnb_dev')

        db_password = getenv('HBNB_MYSQL_PWD', default='hbnb_dev_pwd')
        db_host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db_database = getenv('HBNB_MYSQL_DB', default='hbnb_dev_db')
        db_env = getenv('HBNB_ENV', default='production')

        # Crear el motor de la base de datos con SQLAlchemy
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(db_user, db_password, db_host, db_database),
                                      pool_pre_ping=True)

        # Borrar todas las tablas si el entorno es de prueba
        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

        # Crear todas las tablas de la base de datos (crear si no existen)
        from models.base_model import Base  # Importa aquí para evitar importación circular
        Base.metadata.create_all(self.__engine)

        # Crear una sesión de base de datos usando sessionmaker
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

        self.storage_type = 'SQLAlchemy'

    def all(self, cls=None):
        """Devuelve todos los objetos en la base de datos"""
        if cls is None:
            clases_a_consultar = [User, State, City, Amenity, Place, Review]  # Agrega más clases según sea necesario
            result = {}
            for cls in clases_a_consultar:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    result[key] = obj
            return result
        else:
            objs = self.__session.query(cls).all()
            result = {}
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj
            return result

    def new(self, obj):
        """Añade un nuevo objeto a la sesión actual de la base de datos"""
        self.__session.add(obj)

    def save(self):
        """Confirma todos los cambios en la sesión actual de la base de datos"""
        self.__session.commit()

    def delete(self, obj=None):
        """Elimina un objeto de la sesión actual de la base de datos"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Recarga la sesión actual de la base de datos"""
        from models.base_model import Base  # Importa aquí para evitar importación circular
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get_storage_type(self):
        """Devuelve el tipo de almacenamiento"""
        return 'SQLAlchemy'
