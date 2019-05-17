import unittest2 as unittest

from classes.truck import Truck


class TestTruck(unittest.TestCase):

    def setUp(self):
        self.truck = Truck(
                license_plate='111112', is_muddy=False, bed_down=False)

    def tearDown(self):
        pass

    def test_can_wash_true(self):
        can_wash, msg = self.truck.can_wash()
        self.assertTrue(can_wash)

    def test_can_wash_false(self):
        self.truck.bed_down = True
        can_wash, msg = self.truck.can_wash()
        self.assertEqual(msg, 'Truck: 111112 has bed down, was not washed.')
        self.truck.bed_down = False

    def test_calculate_price_first_time(self):
        price = self.truck.calculate_price(False)
        self.assertEqual(price, 10.00)

    def test_calculate_price_second_time(self):
        price = self.truck.calculate_price(True)
        self.assertEqual(price, 5.00)
