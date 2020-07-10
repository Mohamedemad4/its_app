import re
import time
class utils:
    def __init__(self):
        self.email_pat=re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        self.screen_stack=[]
        return

    def validate_email(email):
        if self.email_pat.search(email):
            return True
        else:
            return False
    def current_screen(self,sname):
        self.screen_stack.append(sname)

    def prev_screen(self):
        print(self.screen_stack)
        return self.screen_stack[len(self.screen_stack)-2]
