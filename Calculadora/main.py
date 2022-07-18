# autor: Luis Carlos Pacheco Lanzziano
from tkinter import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculadoraScreen(Widget):
    Window.size = (250, 400)
    def calculate(self, calculadora):
        if calculadora:
            try:
                self.mi_display.text = str(eval(calculadora))
            except Exception:
                self.mi_display.text = "Error"
   
class CalculadoraApp(App):
    def build(self):
        self.icon = 'myicon.png'
        return CalculadoraScreen()


if __name__ == "__main__":
    CalculadoraApp().run()
