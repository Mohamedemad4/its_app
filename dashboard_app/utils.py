import re
import time
class utils:
    def __init__(self):
        self.email_pat=re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        self.screen_stack=[]
        # Screenmanager loads the first screen registered to it so we are just going to go ahead and skip that tehe (since it fucks up the Back btn logic)
        self.first_call=True
        return

    def validate_email(self,email):
        if self.email_pat.search(email):
            return True
        else:
            return False

    def current_screen(self,sname):
        if self.first_call:
            self.first_call=False
            return
        self.screen_stack.append(sname)

    def prev_screen(self):
        r_idx=len(self.screen_stack)-2
        if r_idx<0:
            return "map_screen"
        prev_name=self.screen_stack[r_idx]
        del self.screen_stack[r_idx]
        if prev_name!="no_conn":
            return prev_name
        else:
            return "map_screen" #dw map_screen has an if statement to take us to onboarding if we aren't registered