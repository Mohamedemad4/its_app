from kivy.uix.label import Label
from screens.template_screen import template_screen

class options_screen(template_screen):
    def on_enter(self):
            self.main_label=Label(text="an amaizng list of ground breaking options")   
            self.add_widget(self.main_label)