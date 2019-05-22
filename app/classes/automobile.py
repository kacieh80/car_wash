""" Automobile Class """


class Automobile(object):

    def __init__(self, **kwargs):
        self.license_plate = kwargs.get("license_plate")

    def can_wash(self):
        """ Check to see if we can wash this automobile """
        if self.__is_stolen():
            msg = "Stolen vehicle: {} was not washed.".format(
                    self.license_plate)
            return False, msg
        return True, "Success"

    def calculate_price(self, returning):
        """ Calculates the price the automobile should pay for a car wash """
        raise NotImplementedError()

    def __is_stolen(self):
        """ Check to see if the car is stolen """

        if self.license_plate == '111111':
            return True

        return False
