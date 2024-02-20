#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup
        Temporarily rename any existing file.json.
        Reset FileStorage objects dictionary.
        Create an instance of the command interpreter.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()
    
    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing teardown"""
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) ==DBStorage:
            models.storage._DBStorage__session.close()
    
    def setUp(self):
        """Reset FileStorage object dictionary."""
        FileStorage._FileStorage__objects = {}
    
    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass
