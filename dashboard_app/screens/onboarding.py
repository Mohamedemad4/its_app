from screens.template_screen import template_screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class onboarding(template_screen):
    emailtb=False

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
        else:
            self._check_token(text) 

    def _check_token(self,token):
        if not self.api.check_token(token):
            self.main_onboarding_label.text="hmmm. We can't find that token. Please try again"
            return False
        else:
            if not self.api.get_email_by_token(token):
                self.main_onboarding_label.text="Welcome!\nPlease Register with your email Below"
                self.emailtb=True
            else:
                self.main_onboarding_label.text="Welcome Back!"

    def _register_email(self,email):   
        if not validate_email(email):
            self.main_onboarding_label.text="hmm, The email address appears to be invalid"
            return False
        else:
            if self.api.register_email(email):
                self.main_onboarding_label.text="Success! your email address has been registered." 
                time.sleep(1)    
                self.manager.current="template_screen"  
            else:
                self.main_onboarding_label.text="Couldn't Register your email address it appears to be registered to another user"
        