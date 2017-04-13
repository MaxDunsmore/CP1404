

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class WidgetLoop(App):
    list = ["one", "two", "three", "asd"]

    def build(self):
        self.title = "loop widgets"
        self.root = Builder.load_file("widget_loop.kv")
        for i in self.list:
            button = Button(text=i)
            self.root.ids.this.add_widget(button)

WidgetLoop().run()

