"""Travel Tracker 2.0
Place class which is super class
of all other classes
name: Charles Anderson
date started: 17/09/2020
Github URL:
"""

IMPORTANCE_DECIDE = 2


class Place:
    """Create a class for places"""
    def __init__(self, name="", country="", priority="", visit_status=False):
        """ Create Initial Method"""
        self.name = name
        self.country = country
        self.priority = priority
        self.visit_status = visit_status

    def __str__(self):
        """Create printing method"""
        return "{} in {} with priority {} status {}".format(self.name, self.country, self.priority, self.visit_status)
        # string that the user sees in each button

    def change_visited(self):
        """Change the place to visited"""
        self.visit_status = True
        # reassigning the value of the last list element to true from false

    def change_unvisited(self):
        """Change the place to not visited"""
        self.visit_status = False
        # reassigning the value of the last list element to false from true

    def define_important_status(self):
        """Define whether the place is important"""
        if int(self.priority) <= IMPORTANCE_DECIDE:
            self.important_status = True
        else:
            self.important_status = False
        # deciding whether the place is important by comparing the priority to the given threshold

