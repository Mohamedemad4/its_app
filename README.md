# its_app

### Schematics and PCB notes
 - 
### Notes on the SIM868 Module
 - it *needs* it's 2A peak current recommend connecting power to a battery
 - APN doens't really matter what you call it (at least Etisalat egypt)

### Notes about data_server
 - there is a 30char **hard** limit on token names
 - Expected Hz is .5Hz 
    - i.e 30 logs is a minute of data
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
- ```NOTF_KEYS``` is the JSON keys expected output of the API for get_notfs
- ```real_hz``` how often (in hertz) do we send the data to the server?
- ```min_of_speeding_to_alert``` how many minutes should pass before warning the user to a speed_exceeding event?
    - see #17
```
    server_uri="http://localhost:7060"
    email="mohamed.emad4bubble@gmail.com"
    CAR_DATA_KEYS=["car_token","lat","lot","speed","accuracy","Unixtimestamp"]
    TOKEN_METADATA_KEYS=["car_token","email","max_spd"]
    NOTF_KEYS=["new_notf","title","msg"]
    real_hz=.5
```
#### data_server/notf_man.py
How many logs should pass before sending a warning notf?
```
    self.MAX_THROT_ENTRIES=15 # 30 logs means a min of speeding
```
