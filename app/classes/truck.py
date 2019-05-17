""" Truck Class """


from classes.automobile import Automobile


class Truck(Automobile):

    def __init__(self, **kwargs):
        """ Set base price and other attributes for car wash """
        super(Truck, self).__init__(**kwargs)
        self.base_price = 10.00
        self.muddy_truck_add_on = 2.00
        self.is_muddy = kwargs.get("is_muddy")
        self.bed_down = kwargs.get("bed_down")

    def calculate_price(self, returning):
        """ Calculates the price the automobile should pay for a car wash """
        price = self.base_price

        if self.is_muddy:
            price += self.muddy_truck_add_on

        if returning:
            return price / 2

        return price

    def can_wash(self):
        """ Check to see if we can wash this automobile """
        if self._is_stolen():
            return False, "Stolen vehicle: {} was not washed.".format(
                    self.license_plate)

        if self.bed_down:
            return False, "Truck: {} has bed down, was not washed.".format(
                    self.license_plate)

        return True, "Success"