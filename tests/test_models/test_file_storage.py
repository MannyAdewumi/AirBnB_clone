#!/usr/bin/python3

"""
This module contains all the test cases for
the FileStorage class methods.
"""
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "_FileStorage__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "_FileStorage__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(storage), FileStorage)


class TestStorageMethods(unittest.TestCase):
    """Contains test cases against the methods present in FileStorage"""

    @classmethod
    def setUp(cls):
        """Code to execute before testing occurs"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """Code to execute after tests are executed"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Tests all() method of the FileStorage class"""
        self.assertTrue(isinstance(storage.all(), dict))
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_method(self):
        """Tests the new() method of the FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        self.assertIn(f"BaseModel.{dummy_bm.id}", storage.all().keys())
        self.assertIn(dummy_bm, storage.all().values())
        self.assertIn(f"User.{dummy_user.id}", storage.all().keys())
        self.assertIn(dummy_user, storage.all().values())
        self.assertIn(f"State.{dummy_state.id}", storage.all().keys())
        self.assertIn(dummy_state, storage.all().values())
        self.assertIn(f"Place.{dummy_place.id}", storage.all().keys())
        self.assertIn(dummy_place, storage.all().values())
        self.assertIn(f"City.{dummy_city.id}", storage.all().keys())
        self.assertIn(dummy_city, storage.all().values())
        self.assertIn(f"Amenity.{dummy_amenity.id}", storage.all().keys())
        self.assertIn(dummy_amenity, storage.all().values())
        self.assertIn(f"Review.{dummy_review.id}", storage.all().keys())
        self.assertIn(dummy_review, storage.all().values())

        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save_method(self):
        """Tests the save() method of the FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn(f"BaseModel.{dummy_bm.id}", save_text)
            self.assertIn(f"User.{dummy_user.id}", save_text)
            self.assertIn(f"State.{dummy_state.id}", save_text)
            self.assertIn(f"Place.{dummy_place.id}", save_text)
            self.assertIn(f"City.{dummy_city.id}", save_text)
            self.assertIn(f"Amenity.{dummy_amenity.id}", save_text)
            self.assertIn(f"Review.{dummy_review.id}", save_text)

        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method(self):
        """Tests the reload() method"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        storage.save()
        storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn(f"BaseModel.{dummy_bm.id}", objects)
        self.assertIn(f"User.{dummy_user.id}", objects)
        self.assertIn(f"State.{dummy_state.id}", objects)
        self.assertIn(f"Place.{dummy_place.id}", objects)
        self.assertIn(f"City.{dummy_city.id}", objects)
        self.assertIn(f"Amenity.{dummy_amenity.id}", objects)
        self.assertIn(f"Review.{dummy_review.id}", objects)

        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
