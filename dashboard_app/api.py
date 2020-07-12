#This thing is really Motherfucking ugly.
#ig I wrote myself into a corner by writing the use case first and not the API huh?
import time
import json
import requests as req
from kivy.storage.jsonstore import JsonStore


"""
#storage.json

{
    "appdata"{
        "token_current":"current token the user is using to (current car in focus)",
        "tokens":[{"car1","max_speed"}] 
        "email":"users_email"
    }
}
"""

class api:
    def __init__(self,server_uri="http://localhost:7060"):
        self.server_uri=server_uri
        self.storage = JsonStore('storage.json')
        self.tokens={}
        self.email="" # just to avoid crashes ig
        if self.is_registered():
            self.email=self.storage["email"]["email"]
            self.get_all_vars()

    def api_call(self,endpoint,*args):
        try:
            resp=req.get(self.server_uri+"/"+endpoint+"/"+"/".join(i for i in args))
            if resp.status_code==200:
                return json.loads(resp.content),resp.status_code
            else:
                return False,resp.status_code
        except:
            return False,000

    def get_all_vars(self):
        """
        gets every piece of data from the server
        """
            
        metadata,_=self.api_call("get_metadata_by_email",self.email)
        if not metadata:
            return False

        if not self.storage.exists("email"):
            print("saved Email")
            self.storage.put("email",email=self.email)

        if not self.storage.exists("token_current"):
            self.storage.put("token_current",token_current=metadata[0]["car_token"])
            self.current_token=metadata[0]["car_token"]
        else:
            self.current_token=self.storage["token_current"]["token_current"]

        for i in metadata:
            self.tokens.update({i["car_token"]:i["max_spd"]})
        self.storage.put("tokens",tokens=self.tokens)
        return True

    def check_token(self,token):
        stat,err=self.api_call("is_token_registered",token)
        if not stat:
            return False
        if stat["status"]=='ok!':
            return True
        return False

    def save_token(self,token):
        "only saves token localy and sets as current on if it isn't in the stored tokens save it to the server via self.register_new_user_car"
        if self.storage.exists("tokens"):
            self.storage["tokens"]["tokens"].append(token)
        else:
            self.storage.put("tokens",tokens=[token])
        self.storage.put("token_current",token_current=token)
        return True
    
    def get_email_by_token(self,token):
        metadata,_=self.api_call("get_metadata_by_token")
        if not metadata:
            return False
        self.email=metadata["email"]
        if not self.get_all_vars():
            return False
        return self.email
        
    def register_user(self,token,email,max_speed):
        if self.api_call("register_token",token,email,max_speed)[0]:
            self.email=email
            return self.get_all_vars()
        else:
            return False

    def check_for_internet(self):
        if self.api_call("ping")[0]:
            return True
        return False

    def is_registered(self): 
        return self.storage.exists("email")
    
    def get_current_car_drivedata(self):
        data,_=self.api_call("get_data",self.current_token,time.time()-1,10e+10)
        if not data:
            return False,False,False
        return data[-1]["lat"],data[-1]["lot"],data[-1]["speed"]
    
    def change_email(self,new_email):
        stat,_=self.api_call("change_car_metadata",self.current_token,new_email,self.tokens[self.current_token])
        if not stat:
            return False
        self.email=new_email
        return True
    
    def change_spd(self,new_spd):
        stat,_=self.api_call("change_car_metadata",self.current_token,self.email,new_spd)
        print(stat)
        if not stat:
            return False
        return True
    
    def get_other_car_tokens(self):
        return [i for i in self.tokens.keys()]
    
    def switch_cur_car(self,token):
        self.storage["appdata"].update({"token_current":token})
        return True