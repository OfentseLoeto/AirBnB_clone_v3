#!/usr/bin/python3
"""Unit tests for DBStorage class"""
import unittest
from models.engine.db_storage import DBStorage

class TestBDStorage(unittest.TestCase):

    def setUp(self):
        self.storage = DBStorage()

    def test_dbstorage_get(self):
        storage = DBStorage()
        test_obj = TestClass(name="test_object")
        storage.new(test_obj)
        storage.save()

        retrieved_obj = self.storage.get(TestClass, test_obj.id)
        assert retrieved_obj == test_obj

    def test_dbstorage_count(self):
        storage = DBStorage()
        test_obj1 = TestClass(name="obj1")
        test_obj2 = TestClass(name="obj2")
        storage.new(test_obj1)
        storage.new(test_obj2)
        storage.save()

        count_all = sellf.storage.count()
        count_class = self.storage.count(TestClass)
        self.assertEqual(count_all, 2)
        self.assertEqual(count_class, 2)

if __name__ == '__main__':
    unittest.main()
