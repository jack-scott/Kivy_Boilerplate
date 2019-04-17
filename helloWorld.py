import kivy
import subprocess
kivy.require('1.0.6')

from kivy.app import App        #this is important, it is the base class from which we build
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Next to button'))
        self.button = Button(text='Hello world', font_size=14)
        self.button.bind(on_press=self.launch)
        self.add_widget(self.button)

    def launch(self, instance):
        print("we launching")




class MyApp(App):
    def build(self):        #have to have a build method which return a widget instance
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()           #call the run method, this initialises the app