#!/usr/bin/python3
"""Unit test for file_storage get and count methods
"""
import unittest

class TestFileStorage():

    def test_filestorage_get():
        storage = FileStorage()
        test_obj = TestClass(name="test_object")
        storage.new(test_obj)
        storage.save()

        retrieved_obj = storage.get(TestClass, test_obj.id)
        assert retrieved_obj == test_obj

    def test_filestorage_count():
        storage = FileStorage()
        test_obj1 = TestClass(name="obj1")
        test_obj2 = TestClass(name="obj2")
        storage.new(test_obj1)
        storage.new(test_obj2)
        storage.save()

        count_all = storage.count()
        count_class = storage.count(TestClass)
        assert count_all == 2
        assert count_class == 2

        pass

if __name__ == '__main__':
    unittest.main()
