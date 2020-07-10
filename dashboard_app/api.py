#Dummy API class 
#will write the real thing later
class api:
    def __init__(self):
        self.token="e"
        self.email="e@b.com"
        self.token_user_new="aa"

    def get_cars(self):
        "returns car tokens"
        return
    
    def check_token(self,token):
        if token==self.token or token==self.token_user_new:
            return True
        return False

    def get_email_by_token(self,token):
        if token==self.token:
            return self.email
        return False
        
    def register_email(self,email):
        if email!=self.email:
             return True