#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Devuelve un diccionario de objetos almacenados.

        Args:
            cls (type): Tipo de clase de los objetos a buscar. Si es None, devuelve todos los objetos.

        Returns:
            dict: Diccionario de objetos del tipo de clase especificado.
        """
        if cls is not None:
            objects_of_class = {obj.id: obj for obj in self.__objects.values() if isinstance(obj, cls)}
            return objects_of_class
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """
        Elimina un objeto del diccionario __objects si está presente.

        Args:
            obj (BaseModel): El objeto a eliminar. Si es None, no se realiza ninguna acción.
        """
        # Verifica si el objeto no es None
        if obj is not None:
            # Construye la clave para el objeto en el diccionario __objects
            key = obj.__class__.__name__ + '.' + obj.id
            # Verifica si la clave existe en el diccionario
            if key in self.__objects:
                # Elimina el objeto del diccionario
                del self.__objects[key]
                # Guarda los cambios en el archivo JSON
                self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                file_contents = f.read()
                if file_contents.strip():  # Verificar si el archivo no está vacío
                    temp = json.loads(file_contents)
                    for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
