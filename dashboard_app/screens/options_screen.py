import time
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from screens.template_screen import template_screen

class options_screen(template_screen):
    def on_enter(self):
        self.main_label=Label(text="",pos_hint={'center_y':.75})
        self.add_widget(self.main_label)

        self.change_email_btn=Button(text="change email",pos_hint={'center_y':.25,'center_x':.5},size_hint=(.7,0.07))
        self.change_email_btn.bind(on_release=self.change_email_action)

        self.change_alert_btn=Button(text="change Alert Speed",pos_hint={'center_y':.40,'center_x':.5},size_hint=(.7,0.07))
        self.change_alert_btn.bind(on_release=self.change_alert_action)

        self.add_another_btn=Button(text="Add Another Unit",pos_hint={'center_y':.75,'center_x':.5},size_hint=(.7,0.07))
        self.add_another_btn.bind(on_release=self.add_new_unit_action)

        self.other_cars=Button(text="look at other cars",pos_hint={'center_y':.9,'center_x':.5},size_hint=(.7,0.07))
        self.other_cars.bind(on_release=self.new_cars_action)
        
        self.add_all_btns()

    def rm_all_bts(self):
        self.remove_widget(self.change_email_btn)
        self.remove_widget(self.change_alert_btn)
        self.remove_widget(self.add_another_btn)
        self.remove_widget(self.other_cars)
    
    def add_all_btns(self):
        self.add_widget(self.add_another_btn)
        self.add_widget(self.other_cars)
        self.add_widget(self.change_alert_btn)
        self.add_widget(self.change_email_btn)
        
    def change_email_action(self,ins):
        self.rm_all_bts()
        self.main_label.text="Type in your New email address"
        self.email_textbox=TextInput(multiline=False,size_hint=(1,0.05),pos_hint={'center_y':.5})
        self.add_widget(self.email_textbox)
        self.email_textbox.bind(on_text_validate=self.change_email_func)
        return
    
    def change_email_exit_routine(self,*args):
        self.remove_widget(self.email_textbox)
        self.main_label.text=""
        self.add_all_btns()
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
    
    def change_alert_action(self,ins):
        self.rm_all_bts()
        return
    
    def add_new_unit_action(self,ins):
        self.rm_all_bts()
        return

    def new_cars_action(self,ins):
        self.rm_all_bts()
        return