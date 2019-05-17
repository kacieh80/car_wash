import unittest2 as unittest

from classes.car import Car
from classes.truck import Truck
from classes.input_file import InputFile


class TestInputFile(unittest.TestCase):

    def setUp(self):
        self.input_file = InputFile()

    def tearDown(self):
        pass

    def test_load_file(self):
        f = "automobiles.txt"
        automobiles = self.input_file.load_file(f)
        self.assertEqual(type(automobiles[0]), Car)
        self.assertEqual(type(automobiles[2]), Truck)
        self.assertEqual(automobiles[11], None)
