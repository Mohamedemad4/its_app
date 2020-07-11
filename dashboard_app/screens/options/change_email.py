import time
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from ..template_screen import template_screen

class options_change_email(template_screen):
    def on_enter(self):
        self.main_label=Label(text="",pos_hint={'center_y':.75})
        self.main_label.text="Type in your New email address"
        self.add_widget(self.main_label)
        self.email_textbox=TextInput(multiline=False,size_hint=(1,0.05),pos_hint={'center_y':.5})
        self.add_widget(self.email_textbox)
        self.email_textbox.bind(on_text_validate=self.change_email_func)

    def change_email_exit_routine(self,*args):
        self.manager.current="options_screen"
        Clock.unschedule(self.change_ee_event)

    def change_email_func(self,ins):
        text=self.email_textbox.text
        if self.utils.validate_email(text):
            if self.api.check_for_internet():
                if self.api.change_email(text):
                    self.main_label.text="Success!"
                    self.change_ee_event=Clock.schedule_interval(self.change_email_exit_routine,1.5)
                else:
                    self.main_label.text="Couldn't Register Email address please try again_later"
            else:
                self.manager.current="no_conn"
        else:
            self.main_label.text="email address is invalid please try again."
        return
