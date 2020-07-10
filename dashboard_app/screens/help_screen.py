from screens.template_screen import template_screen
from kivy.uix.label import Label
class help_screen(template_screen):
    def on_enter(self):
            self.main_label=Label(text="'Some very important instructions'")   
            self.add_widget(self.main_label)