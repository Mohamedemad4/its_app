import time
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from ..template_screen import template_screen

class change_alert_spd(template_screen):
    def on_enter(self):
        self.main_label=Label(text="",pos_hint={'center_y':.75})
        self.main_label.text="Type in The new speed Which you want to be alerted too for {0}".format(self.api.current_token)
        self.add_widget(self.main_label)
        
        self.other_label=Label(text="",pos_hint={'center_y':.70},size_hint=(1,.02))
        self.other_label.text="Want to change the speed for another car?\nPick it first from options->look at other cars".format(self.api.current_token)
        self.add_widget(self.other_label)

        self.spd_textbox=TextInput(input_filter='float',multiline=False,size_hint=(1,0.05),pos_hint={'center_y':.5})
        self.add_widget(self.spd_textbox)
        self.spd_textbox.bind(on_text_validate=self.change_spd_func)

    def change_spd_exit_routine(self,*args):
        self.manager.current="options_screen"
        Clock.unschedule(self.change_se_event)

    def change_spd_func(self,ins):
        text=float(self.spd_textbox.text)
        if self.api.check_for_internet():
            if self.api.change_spd(text):
                self.main_label.text="Success!"
                self.change_se_event=Clock.schedule_interval(self.change_spd_exit_routine,1.5)
            else:
                self.main_label.text="Couldn't Change Alert Speed please try again_later"
        else:
            self.manager.current="no_conn"
        return
