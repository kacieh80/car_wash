import unittest2 as unittest

from classes.car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car(license_plate='111112')

    def tearDown(self):
        pass

    def test_calculate_price_first_time(self):
        price = self.car.calculate_price(False)
        self.assertEqual(price, 5.00)

    def test_calculate_price_second_time(self):
        price = self.car.calculate_price(True)
        self.assertEqual(price, 2.50)
