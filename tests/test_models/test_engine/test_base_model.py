#!/usr/bin/python3
"""Test cases my functions"""
import unittest
from datetime import datetime
import models
import pep8 as pycodestyle
from datetime import datetime


class TestBaseModel(unittest.TestCase):
        def test_default_values(self):
            # Test if default values are set correctly
            model_instance = BaseModel()
            self.assertIsInstance(model_instance.id, str)
            self.assertIsInstance(model_instance.created_at, datetime)
            self.assertIsInstance(model_instance.updated_at, datetime)

        def test_custom_values(self):
            # Test if custom values are correctly set
            custom_id = "custom_id_value"
            custom_created_at = datetime(2023, 8, 1, 12, 0, 0)
            custom_updated_at = datetime(2023, 8, 1, 12, 30, 0)

            model_instance = BaseModel(id=custom_id, created_at=custom_created_at,
                    updated_at=custom_updated_at)
            self.assertEqual(model_instance.id, custom_id)
            self.assertEqual(model_instance.created_at, custom_created_at)
            self.assertEqual(model_instance.updated_at, custom_updated_at)

        def test_save_and_delete(self):
            # Test the 'save' and 'delete' methods.
            model_instance = BaseModel()
            initial_updated_at = model_instance.updated_at

            model_instance.save()
            self.assertNotEqual(model_instance.updated_at, initial_updated_at)

            model_instance.delete()
            self.assertIsNone(models.storage.get_by_id(BaseModel, model_instance.id))

        def test_to_dict(self):
            # Test the 'to_dict' method.
            model_instance = BaseModel()
            dictionary = model_instance.to_dict()

            self.assertIsInstance(dictionary, dict)
            self.assertIn('id', dictionary)
            self.assertIn('created_at', dictionary)
            self.assertIn('updated_at', dictionary)
            self.assertEqual(dictionary['id'], model_instance.id)
            self.assertEqual(dictionary['created_at'], model_instance.created_at.isoformat())
            self.assertEqual(dictionary['updated_at'], model_instance.updated_at.isoformat())
            self.assertNotIn('_sa_instance_state', dictionary)
