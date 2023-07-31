#!/usr/bin/python3
"""File Storage Module"""
import json

class FileStorage:
    """File Storage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects"""
        if cls is None:
            return self.__objects
        else:
            filtered_objs = {}
            for key, value in self.__objects.items():
                if type(value).__name__ == cls.__name__:
                    filtered_objs[key] = value
            return filtered_objs

    def new(self, obj):
        """Saves an object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves the data"""
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            objs_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(objs_dict, file)

    def reload(self):
        """Reloads the data"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                objs_dict = json.load(file)
                for key, obj_dict in objs_dict.items():
                    module_name, obj_id = key.split(".")
                    obj_class = eval(module_name)
                    obj = obj_class(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()                


class FileStorage(BaseModel):
    """This method retrieve one object and returns the object
       based on the class and its ID, or None if not found
    """

    def get(self, cls, id):
        """Retrieve one object by class and Id
        """

        all_objs = self.all(cls)
        for obj_id, obj in all_objs.items():
            if obj_id == id:
                return obj
            return None

    def count(self, cls=None):
        """Count the number of objects in storage matching the given class"""

        all_objs = self.all(cls)
        return len(all_objs)
