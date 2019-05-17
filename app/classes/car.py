""" Car Class """


from classes.automobile import Automobile


class Car(Automobile):

    def __init__(self, **kwargs):
        """ Set base price for car wash """
        super(Car, self).__init__(**kwargs)
        self.base_price = 5.00

    def calculate_price(self, returning):
        """ Calculates the price the automobile should pay for a car wash """
        if returning:
            return self.base_price / 2

        return self.base_price
