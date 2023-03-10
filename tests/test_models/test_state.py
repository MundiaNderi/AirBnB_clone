#!/usr/bin/python3
""" Unittest for state.py"""
import unittest
from models.state import State
from models.base_model import BaseModel
import os


class TestPlace(unittest.TestCase):
    """ Class to test state.py """

    def setUp(self):
        """ Sets up the testing environment """

        self.s1 = State()
        self.s2 = State()
        self.s2.name = "Nairobi"

    def test_non_existant_instance(self):
        """ Checks for a non-existent instance """

        self.s3 = State()
        self.assertIsInstance(self.s3, State)

    def test_inheritance(self):
        """Checks to make sure review inherits from BaseModel"""

        self.assertTrue(issubclass(State, BaseModel))

    def test_check_attributes(self):
        """Checks for class specific attributes """

        self.assertTrue(hasattr(State(), "name"))

    def test_new_instances(self):
        """Checks that new instances were created """

        self.assertTrue(self.s1)
        self.assertTrue(self.s2)

    def test_new_instances_attribute_creation(self):
        """ Checks that new instances have designated attributes"""

        self.assertIn("name", self.s2.__dict__)
        self.assertEqual(self.s2.name, "Nairobi")

    def test_ids(self):
        """Checks for different IDs """

        self.assertNotEqual(self.s1.id, self.s2.id)

    def test_name(self):
        """ Checks the names of instances """

        self.assertEqual(self.s2.name, "Nairobi")
        self.s1.name = "Mombasa"
        self.assertEqual(self.s1.name, "Mombasa")

    def tearDown(self):
        """ Tears down the testing enviroment """

        del self.s1
        del self.s2
        if os.path.exists("file.json"):
            os.remove("file.json")
