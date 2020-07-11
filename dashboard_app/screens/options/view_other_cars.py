import time
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from ..template_screen import template_screen

class options_view_other_cars(template_screen):
    def on_enter(self):
        self.main_label=Label(text="",pos_hint={'center_y':.85})
        self.main_label.text="other cars registered to your email"
        self.add_widget(self.main_label)
        center_y_car_btn=.75
        for token in self.api.get_other_car_tokens():
            print(token)
            self.car_btn=Button(text=token,pos_hint={"center_x":.5,"center_y":center_y_car_btn},size_hint=(.7,0.07))
            self.car_btn.bind(on_release=self.switch_cur_car)
            self.add_widget(self.car_btn)
            center_y_car_btn-=.15

    def view_other_cars_exit_routine(self,*args):
        self.manager.current="map_screen"
        Clock.unschedule(self.change_se_event)

    def switch_cur_car(self,ins):
        token=ins.text
        if not self.api.check_for_internet():
            self.manager.current="no_conn"
            return
        
        if self.api.switch_cur_car(token):
            self.main_label.text="Switched to {0}".format(token)
            self.change_se_event=Clock.schedule_interval(self.view_other_cars_exit_routine,1.5)
        else:
            self.main_label.text="Couldn't Switch to {0} please try again later".format(token)
