import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            classes = [BaseModel, User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        objs = {}
        for c in classes:
            query = self.__session.query(c)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

class DBStorage(BaseModel):
    """This method retrive one oblect and returns objects based
       on the class and its id, or None if not found.
    """

    def get(self, cls, id):
        """Retrieve one object by class and ID"""
        
        all_objs = self.all(cls)
        for obj_id , obj in all_objs.items():
            if obj_id == id:
                return obj
            return None

    def count(self, cls=None):
        """Count the number of objects in storage matching the given class"""

        all_objs = self.all(cls)
        return len(all_objs)
