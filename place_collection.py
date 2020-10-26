"""Travel Tracker 2.0
Place collection class
which inherits from place class
and is superclass of TravelTracker
name: Charles Anderson
date started: 17/09/2020
Github URL: https://github.com/CharlesA750/Assignment_2_CharlesA
"""

from place import Place

"""Places Collection class"""
FILENAME = "places.csv"  # creating a universal variable of the file name to be called later


class PlaceCollection(Place):
    """Create place collection class """
    def __init__(self):
        """Create initial method with blank list"""
        self.places = []  # blank list to append to later

    def add_place(self, new_place):
        """Append a new place to the blank list"""
        new_place = Place()
        self.places.append(new_place)  # add new place to the list using place class

    def load_places(self):
        """Append the loaded file to the blank list to view it"""
        places_list = open(FILENAME, "r")  # open the file in read mode
        for line in places_list:
            parts = line.strip().split()  # split the csv file into parts
            self.places.append(
                Place(parts[0], parts[1], int(parts[2]), (parts[3])))  # append the split parts to the list in __init__
            if parts[3] == "n":
                parts[3] = False
            else:
                parts[3] = True
        places_list.close()  # close the list

    def save_places(self):
        """Append the loaded file to the blank list to modify it"""
        places_list = open(FILENAME, "w")  # open the file in write mode
        for line in places_list:
            parts = line.strip().split()  # split the csv file into parts
            self.places.append(
                Place(parts[0], parts[1], int(parts[2]), (parts[3])))  # append the split parts to the list in __init__
            if parts[3] == "n":
                parts[3] = False
            else:
                parts[3] = True
        places_list.close()  # close the list

    def get_num_unvisited(self):
        """Count the number of visited places in the list"""
        num_visited = 0
        for i in range(len(self.places)):  # for each place show count which are visited
            num_visited += 1
        return num_visited


PlaceCollection()
