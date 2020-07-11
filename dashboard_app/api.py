#Dummy API class 
#will write the real thing later
class api:
    def __init__(self):
        self.token="e"
        self.current_token="e" # the token that the user is interacting with rn
        self.email="e@b.com"
        self.token_user_new="aa"
        self.internet=True

    def get_cars(self):
        "returns car tokens"
        return
    
    def check_token(self,token):
        if token==self.token or token==self.token_user_new:
            return True
        return False

    def register_token(self,token):
        return True

    def get_email_by_token(self,token):
        if token==self.token:
            return self.email
        return False
        
    def register_email(self,email):
        if email!=self.email:
             return True
    
    def check_for_internet(self):
        if self.internet:
            return True
        return False

    def is_registered(self):
        return True
    
    def get_current_car_drivedata(self):
        return 31.2086,30.0094,30
    
    def change_email(self,new_email):
        return True
    
    def change_spd(self,new_spd):
        return True
    
    def get_other_car_tokens(self):
        return [str(i) for i in range(1,6)]#self.token,self.token_user_new]
    
    def switch_cur_car(self,token):
        return True