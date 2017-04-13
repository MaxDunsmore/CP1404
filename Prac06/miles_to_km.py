"""
Horrible compared to the demo, but it still works :^)
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKmApp(App):
    def build(self):
        Window.size = (525, 222)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file("miles_to_km.kv")
        return self.root

    def change_input(self, value, up_or_down):
        valid_input = 0
        while valid_input == 0:
            try:
                value = int(value)
                if up_or_down == 1:
                    value += 1
                if up_or_down == 0:
                    value -= 1
                valid_input = 1
            except:
                value = 0
        self.root.ids.input.text = str(value)

    def calculate_miles(self, value):
        valid_input = 0
        while valid_input == 0:
            try:
                value = float(value)
                value *= 1.60934
                valid_input = 1
            except:
                value = 0
        self.root.ids.calculation.text = "{:.3f}".format(value)
        return value

MilesToKmApp().run()
