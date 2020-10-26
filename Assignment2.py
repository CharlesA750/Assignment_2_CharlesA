"""Travel Tracker 2.0
Kivy app using classes to track locations
name: Charles Anderson
date started: 17/09/2020
Github URL: https://github.com/CharlesA750/Assignment_2_CharlesA
"""

# Import necessary packages
from kivy.app import App
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from place_collection import PlaceCollection

SORTING_DICT = {"Priority": "priority", "Visited": "visit_status", "Country": "country", "City": "city"}
FILENAME = "places.csv"
# universal variables to simplify code


class TravelTracker(App):
    """Create the Travel Tracker class"""
    current_sort = StringProperty()
    sorting_code = ListProperty()

    def build(self):
        """Build the Travel Tracker App"""
        self.title = "Travel Tracker"
        self.root = Builder.load_file("travel_app.kv")
        self.sorting_code = SORTING_DICT.keys()
        self.root.ids.sorting_type.text = self.sorting_code[1]
        print(self.root.ids.sorting_type.text)
        return self.root

    def change_sorting(self, sorting_code):
        """Change the sorting type in the spinner"""
        self.root.ids.missing_id_name.text = SORTING_DICT[self.root.ids.sorting_type.text]

    def clear_place(self, instance):
        """Clear the text inputs in the GUI"""
        self.root.ids.name_entry.text = ""  # these three reset the squares to blank
        self.root.ids.country_entry.text = ""
        self.root.ids.priority_entry .text = ""

    def create_widget(self):
        """Create a new dynamic widget for place"""
        self.place_collect = PlaceCollection()
        self.place_collect.load_places(FILENAME)
        for place in self.place_collect.places:
            temp_button = Button(text=place, id=place)
            temp_button.bind(on_release=self.create_widget())  # create a button for each data entry
            self.root.ids.entries_box.add_widget(temp_button)

    def change_status(self):
        """Change the text to what the sorting status is"""
        self.root.ids.status_text.text = SORTING_DICT[self.sorting_code]
        self.place_collection.sort(SORTING_DICT[self.sorting_code])

    def save_list(self):
        """Save the list"""
        self.save_list(FILENAME)


TravelTracker().run()
