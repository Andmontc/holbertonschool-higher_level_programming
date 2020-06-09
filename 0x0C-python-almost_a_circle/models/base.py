#!/usr/bin/python3
""" Module for Class Base """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method for json to string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method to save a json to a file """
        jfile = cls.__name__ + ".json"
        with open(jfile, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                nlist = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(nlist))

    @staticmethod
    def from_json_string(json_string):
        """ static method for json string representation """

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            obj = cls(6, 9)
            obj.update(**dictionary)
            return obj

        if cls.__name__ == "Square":
            obj = cls(7)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """
        jfile = cls.__name__ + ".json"
        try:
            with open(jfile, 'r') as f:
                cont = f.read()
            nlist = []
            for obj in cls.from_json_string(cont):
                new.append(cls.create(**obj))
            return nlist
        except FileNotFoundError:
            return []
