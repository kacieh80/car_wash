""" car_wash.py """


import sys

from classes.input_file import InputFile
from classes.car_wash import CarWash


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide a filename from the input_file folder.')
        sys.exit(-1)

    automobiles = InputFile().load_file(sys.argv[1])
    car_wash = CarWash(automobiles)
    washed_cars = car_wash.wash_cars()

    for washed_car in washed_cars:
        print(washed_car)
    sys.exit(-1)
