import time
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from ..template_screen import template_screen

class options_view_other_cars(template_screen):
    def on_enter(self):
        self.main_label=Label(text="",pos_hint={'center_y':.85})
        self.main_label.text="other cars registered to your email"
        self.add_widget(self.main_label)

        self.btn_layout=GridLayout(cols=1, spacing=20, size_hint_y=None)
        self.btn_layout.bind(minimum_height=self.btn_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height*.70))
        for token in self.api.get_other_car_tokens():
            car_btn=Button(text=token,size_hint_y=None,height=Window.height*.08)
            car_btn.bind(on_release=self.switch_cur_car)
            self.btn_layout.add_widget(car_btn)

        self.scroll_view.add_widget(self.btn_layout)
        self.add_widget(self.scroll_view)

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
