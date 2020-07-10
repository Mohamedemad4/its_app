from screens.template_screen import template_screen

class onboarding(template_screen):
    emailtb=False
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
            self.ids.main_onboarding_label.text="hmmm. We can't find that token. Please try again"
            return False
        else:
            if not self.api.get_email_by_token(token):
                self.ids.main_onboarding_label.text="Welcome!\nPlease Register with your email Below"
                self.emailtb=True
            else:
                self.ids.main_onboarding_label.text="Welcome Back!"

    def _register_email(self,email):   
        if not validate_email(email):
            self.ids.main_onboarding_label.text="hmm, The email address appears to be invalid"
            return False
        else:
            if self.api.register_email(email):
                self.ids.main_onboarding_label.text="Success! your email address has been registered." 
                time.sleep(1)    
                self.manager.current="template_screen"  
            else:
                self.ids.main_onboarding_label.text="Couldn't Register your email address it appears to be registered to another user"
        