#This thing is really Motherfucking ugly.
#ig I wrote myself into a corner by writing the use case first and not the API huh?
import time
import json
import requests as req
from kivy.storage.jsonstore import JsonStore


"""
#storage.json

{
   "tokens":{
      "tokens":{
         "test-token":44.0,
         "car2":33.0,
         "car3":44.0
      }
   },
   "token_current":{
      "token_current":"test-token"
   },
   "email":{
      "email":"ss@gmi.com"
   }
}
"""

class api:
    def __init__(self,server_uri="http://localhost:7060"):
        self.server_uri=server_uri
        self.storage = JsonStore('storage.json')
        self.tokens={}
        if self.is_registered():
            self.email=self.storage["email"]["email"]
            self.get_all_vars()

    def api_call(self,endpoint,*args):
        try:
            resp=req.get(self.server_uri+"/"+endpoint+"/"+"/".join(str(i) for i in args))
            if resp.status_code==200:
                return json.loads(resp.content),resp.status_code
            else:
                return False,resp.status_code
        except Exception as e:
            print(e)
            return False,000

    def get_all_vars(self):
        """
        gets every piece of data from the server
        """
            
        metadata,_=self.api_call("get_metadata_by_email",self.email)
        if not metadata:
            return False

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
        self.storage.put("token_current",token_current=token)
        return True
    
    def get_email_by_token(self,token):
        metadata,_=self.api_call("get_metadata_by_token",token)
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
        data,_=self.api_call("get_data_recent",self.current_token)
        if not data:
            return False,False,False
        return data["lat"],data["lot"],data["speed"]
    
    def change_email(self,new_email):
        stat,_=self.api_call("change_car_metadata",self.current_token,new_email,self.tokens[self.current_token])
        if not stat:
            return False
        self.email=new_email
        self.get_all_vars() #refresh the object storage
        return True
    
    def change_spd(self,new_spd):
        stat,_=self.api_call("change_car_metadata",self.current_token,self.email,new_spd)
        if not stat:
            return False
        self.get_all_vars() #refresh the object storage
        return True
    
    def get_other_car_tokens(self):
        return [i for i in self.tokens.keys()]
    
    def switch_cur_car(self,token):
        self.storage.put("token_current",token_current=token)
        self.current_token=token
        return True