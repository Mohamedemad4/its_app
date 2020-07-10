from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

import re
email_pat=re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
def validate_email(email):
    if email_pat.search(email):
        return True
    else:
        return False

class onboarding(GridLayout):
    def __init__(self,api_ins):
        super().__init__()
        self.cols = 1
        self.rows = 2
        self.api=api_ins
        self.emailtb=False
        self.main_label=Label(text='Hello! Please Enter the Name of your Unit')
        self.add_widget(self.main_label)
        self.onboard_textbox = TextInput(multiline=False)
        self.onboard_textbox.bind(on_text_validate=self.check_onboardbox)
        self.add_widget(self.onboard_textbox)
       
    def check_onboardbox(self,ins):
        text=ins._lines[0] #idk man,idk
        if self.emailtb:
            self._register_email(text)
        else:
            self._check_token(text) 

    def _check_token(self,token):
        if not self.api.check_token(token):
            self.main_label.text="hmmm. We can't find that token. Please try again"
            return False
        else:
            if not self.api.get_email_by_token(token):
                self.main_label.text="Welcome!\nPlease Register with your email Below"
                self.emailtb=True
            else:
                self.main_label.text="Welcome Back!"

    def _register_email(self,email):   
        if not validate_email(email):
            self.main_label.text="hmm, The email address appears to be invalid"
            return False
        else:
            if self.api.register_email(email):
                self.main_label.text="Success! your email address has been registered."       
            else:
                self.main_label.text="Couldn't Register your email address it appears to be registered to another user"
        