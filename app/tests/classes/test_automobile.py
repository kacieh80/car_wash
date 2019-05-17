import unittest2 as unittest

from classes.automobile import Automobile


class TestAutomobile(unittest.TestCase):

    def setUp(self):
        self.automobile = Automobile()

    def tearDown(self):
        pass

    def test_can_wash_true(self):
        self.automobile.license_plate = '111112'
        can_wash, msg = self.automobile.can_wash()
        self.assertTrue(can_wash)

    def test_can_wash_false(self):
        self.automobile.license_plate = '111111'
        can_wash, msg = self.automobile.can_wash()
        self.assertFalse(can_wash)

    def test_calculate_price(self):
        self.assertRaises(NotImplementedError,
                self.automobile.calculate_price, True)
