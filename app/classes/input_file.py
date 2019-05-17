""" Input File Class. Handles parsing the file and creating objects """


import sys

from classes.car import Car
from classes.truck import Truck


class InputFile(object):

    def load_file(self, file_name):
        """ Given an input file, parse, store, and return it """
        try:
            data = open("input_files/{}".format(file_name), 'r')
        except:
            print( 'Could not find your file.')
            sys.exit(-1)
        try:
            automobiles = self._parse_file_data(data)
        except:
            print ('Something went wrong while parsing your file, \
                    please check your file, and try again.')
            data.close()
            sys.exit(-1)
        data.close()

        return automobiles

    def _parse_file_data(self, data):
        """ Parse the meat of the file and return automobiles """
        automobiles = []

        for line in data:
            line_list = line.split(' ')

            type = line_list[0]
            license_plate = line_list[1]

            if type == "Truck":
                bed_down = True if line_list[2] == 'bed_down' else False
                is_muddy = True if line_list[3].strip() == 'muddy' else False
                automobile = Truck(
                        license_plate=license_plate.strip(),
                        bed_down=bed_down,
                        is_muddy=is_muddy)
            elif type == "Car":
                automobile = Car(license_plate=license_plate.strip())
            else:
                automobile = None

            automobiles.append(automobile)

        return automobiles
