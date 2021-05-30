from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_CONVERSION = 1.609344


class MilesConverter(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles(self, miles):
        try:
            int(miles)
            value = True
        except ValueError:
            value = False
        if value:
            kilometres = int(miles) * MILES_CONVERSION
            self.root.ids.output_label.text = str(kilometres)
        else:
            self.root.ids.output_label.text = str(0)

    def handle_increment(self, miles, increment):
        try:
            int(miles)
            value = True
        except ValueError:
            value = False
        if value:
            new_miles = int(miles) + increment
            self.root.ids.input_miles.text = str(new_miles)
        else:
            self.root.ids.input_miles.text = str(increment)


MilesConverter().run()
