import time
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from screens.template_screen import template_screen

class options_screen(template_screen):
    def on_enter(self):
        if not self.api.is_registered():
            self.current.manager="onboarding"

        self.change_email_btn=Button(text="change email",pos_hint={'center_y':.25,'center_x':.5},size_hint=(.7,0.07))
        self.change_email_btn.bind(on_release=self.change_email_action)

        self.change_alert_btn=Button(text="change Alert Speed",pos_hint={'center_y':.40,'center_x':.5},size_hint=(.7,0.07))
        self.change_alert_btn.bind(on_release=self.change_alert_action)

        self.add_another_btn=Button(text="Add Another Unit",pos_hint={'center_y':.75,'center_x':.5},size_hint=(.7,0.07))
        self.add_another_btn.bind(on_release=self.add_new_unit_action)

        self.other_cars=Button(text="look at other cars",pos_hint={'center_y':.9,'center_x':.5},size_hint=(.7,0.07))
        self.other_cars.bind(on_release=self.other_cars_action)
        
        self.add_widget(self.add_another_btn)
        self.add_widget(self.other_cars)
        self.add_widget(self.change_alert_btn)
        self.add_widget(self.change_email_btn)
        
    def change_email_action(self,ins):
        self.manager.current="options_change_email"
        return
    def change_alert_action(self,ins):
        self.manager.current="options_alert_spd"
        return
    
    def add_new_unit_action(self,ins):
        self.manager.current="onboarding"
        return

    def other_cars_action(self,ins):
        self.manager.current="options_view_other_cars"
        return