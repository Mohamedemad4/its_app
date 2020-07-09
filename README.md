# its_app

### Packages

 #### dashboard app
     - using https://github.com/kivy-garden/mapview 1.0.5
 #### prototype app
     - using https://github.com/kivy/plyer/ v1.4.3

### Config Vars

#### data_server/tests/test_api.py
- email is the email to register the token with
- ```CAR_DATA_KEYS``` is the JSON keys expected as the output of the API for for the getData
```
    server_uri="http://localhost:7060"
    email="mohamed.emad4bubble@gmail.com"
    CAR_DATA_KEYS=["car_token","lat","lot","speed","accuracy","Unixtimestamp"]
```
#### data_server/utils.py
email to use to send the warning to registered users
```
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
```