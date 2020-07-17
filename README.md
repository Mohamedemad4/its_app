# its_app
### Notes on the SIM868 Module
 - it *needs* it's 2A peak current recommend connecting power to a battery
 - SIM Goes the other way around
 - APN doens't really matter what you call it (at least Etisalat egypt)

### Notes about data_server
 - there is a 30char **hard** limit on token names

### Packages

 #### dashboard app
     - using https://github.com/kivy-garden/mapview 1.0.5
 #### prototype app
     - using https://github.com/kivy/plyer/ v1.4.3

### Config Vars

#### data_server/tests/test_api.py
- email is the email to register the token with
- ```CAR_DATA_KEYS``` is the JSON keys expected as the output of the API for for the getData
- ```TOKEN_METADATA_KEYS``` is the JSON keys expected outputs of the API for get_metadata
```
    server_uri="http://localhost:7060"
    email="mohamed.emad4bubble@gmail.com"
    CAR_DATA_KEYS=["car_token","lat","lot","speed","accuracy","Unixtimestamp"]
    TOKEN_METADATA_KEYS=["car_token","email","max_spd"]
```
#### data_server/utils.py
email to use to send the warning to registered users
```
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
```