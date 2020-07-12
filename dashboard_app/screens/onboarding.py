from screens.template_screen import template_screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class onboarding(template_screen):
    emailtb=False
    max_spdtb=False

    def on_pre_enter(self):
        self.main_onboarding_label=Label(text="Hello! Please Enter the Name of your Unit",pos_hint={'top':1.2})
        self.main_onboarding_input=TextInput(multiline=False,size_hint=(1,0.05),pos_hint={'top':.5})
        self.main_onboarding_input.bind(on_text_validate=self.check_onboardbox)
        self.add_widget(self.main_onboarding_input)
        self.add_widget(self.main_onboarding_label)

    def check_onboardbox(self,ins):
        if not self.api.check_for_internet():
            self.manager.current="no_conn"

        text=ins._lines[0] #idk man,idk
        if self.emailtb:
            self._register_email(text)
        elif self.max_spdtb:
            self._maxspd(text)
        else:
            self._check_token(text) 

    def _check_token(self,token):
        if not self.api.check_token(token):
            self.main_onboarding_label.text="hmmm. We can't find that token. Please try again"
            return False
        else:
            self.token=token
            self.api.save_token(token)
            if not self.api.get_email_by_token(token):
                self.main_onboarding_label.text="Welcome!\nPlease Register with your email Below"
                self.emailtb=True
            else:# 2 options,new car same user,old car old user (used from the options screen remmember?)
                self.api.get_all_vars()
                if token in [i for i in self.api.tokens.keys()]:
                    self.main_onboarding_label.text="Welcome Back!"
                    self.manager.current="map_screen"
                else:
                    self.main_onboarding_label.text="What Would you Like your Alert speed to be?\nif your car reaches this speed we will send you and alert email" 
                    self.main_onboarding_input.text=""
                    self.main_onboarding_input.input_filter="float"
                    self.max_spdtb=True
                    self.emailtb=False
                    self.email=self.api.email

    def _register_email(self,email):   
        if not self.utils.validate_email(email):
            self.main_onboarding_label.text="hmm, The email address appears to be invalid"
            return False
        else:
            self.main_onboarding_label.text="What Would you Like your Alert speed to be?\nif your car reaches this speed we will send you and alert email" 
            self.main_onboarding_input.text=""
            self.main_onboarding_input.input_filter="float"
            self.max_spdtb=True
            self.emailtb=False
            self.email=email
    
    def _maxspd(self,ms):
        if self.api.register_user(self.token,self.email,ms):
            self.main_onboarding_label.text="you Have been registered!"
            Clock.schedule_once(self.switch_to_mapscreen,1)
        else:
            self.main_onboarding_label.text="Couldn't register you please try again later"

    def switch_to_mapscreen(self,*args):
        self.manager.current="map_screen"