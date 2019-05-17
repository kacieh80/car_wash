""" CarWash Class """


from classes.car import Car
from classes.truck import Truck


class CarWash(object):

    def __init__(self, automobiles):
        self.automobiles = automobiles
        self.visited = []

    def wash_cars(self):
        """ Wash cars in given automobiles """
        washed_cars = []
        for vehicle in self.automobiles:
            if vehicle:
                can_wash, can_wash_text = vehicle.can_wash()

                if can_wash:
                    if vehicle.license_plate in self.visited:
                        price = "{0:.2f}".format(round(
                                vehicle.calculate_price(True), 2))
                    else:
                        price = "{0:.2f}".format(round(
                                vehicle.calculate_price(False), 2))

                    washed = "Washed automobile: {} for ${}.".format(
                            vehicle.license_plate, price)

                    self.visited.append(vehicle.license_plate)
                else:
                    washed = can_wash_text
            else:
                washed = "Unknown automobile was not washed."

            washed_cars.append(washed)

        return washed_cars
