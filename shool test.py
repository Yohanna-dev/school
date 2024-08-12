from kivy.app import App
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        return Label(text='سلام')

if name == '__main__':
    SimpleApp().run()
