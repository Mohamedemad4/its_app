import time
import json
import random
import pprint
import requests as req


hz=.1 # real time is 2hz test time is 10hz
server_uri="http://localhost:7060"
token="test-token"
fake_token="I-am-not-real"
email="mohamed.emad4bubble@gmail.com"
max_spd=30
max_spd_beta=50
lon,lat,accuracy=1.3,1.3,1.3
CAR_DATA_KEYS=["car_token","lat","lot","speed","accuracy","Unixtimestamp"]
TOKEN_METADATA_KEYS=["car_token","email","max_spd"]
time_window=(0,0) 
dump_req=50

def _log_data(token,speed):
    res=req.get(server_uri+"/data_dump/{token}/0/0/0/{lat}/{lon}/{speed}/{acc}".format(
        token=token,lat=lat,lon=lon,acc=accuracy,speed=speed
    ))
    return res.status_code

def test_ping():
    res=req.get(server_uri+"/ping")
    assert res.status_code==200

def test_registration():
    "Test Registration Of a new Token"
    res=req.get(server_uri+"/register_token/{token}/{email}/{max_spd}".format(
        token=token,email=email,max_spd=max_spd
    ))
    assert res.status_code==200

def test_Double_registration():
    res=req.get(server_uri+"/register_token/{token}/{email}/{max_spd}".format(
        token=token,email=email,max_spd=max_spd
    ))
    assert res.status_code==400

def test_register_unregistered_token():
    res=req.get(server_uri+"/register_token/{token}/{email}/{max_spd}".format(
        token=fake_token,email=email,max_spd=max_spd
    ))
    assert res.status_code==400

def test_get_metadata_by_token():
    res=req.get(server_uri+"/get_metadata_by_token/{token}".format(
        token=token
    ))
    assert res.status_code==200
    json_res=json.loads(res.content)
    assert set([i for i in json_res.keys()])==set(TOKEN_METADATA_KEYS)

def test_get_metadata_by_email():
    res=req.get(server_uri+"/get_metadata_by_email/{email}".format(
        email=email
    ))
    assert res.status_code==200
    json_res=json.loads(res.content)
    assert set([i for i in json_res[0].keys()])==set(TOKEN_METADATA_KEYS)

def test_get_metadata_by_token_non_existant():
    res=req.get(server_uri+"/get_metadata_by_token/{token}".format(
        token=fake_token
    ))
    assert res.status_code==400
    
def test_get_metadata_by_email_non_existant():
    res=req.get(server_uri+"/get_metadata_by_email/{email}".format(
        email=fake_token
    ))
    assert res.status_code==400

def test_dump_speed_compliant_data():
    "Test Dump Good drive data"
    responses=[]
    for i in range(dump_req):
       responses.append(_log_data(token,random.randint(0,max_spd-2)))
       time.sleep(hz)
    assert sum(responses)==dump_req*200 # make sure they all are 200

def test_dump_bad_token():
    "Test Dump data with a nonexistant token"
    responses=[]
    for i in range(10):
       responses.append(_log_data(fake_token,random.randint(0,max_spd-2)))
       time.sleep(hz)
    assert sum(responses)==10*400

def test_dump_speed_exceeding_data_test():
    "Test ump data that's over the speed limit"
    responses=[]
    for i in range(dump_req):
       responses.append(_log_data(token,random.randint(max_spd,max_spd*2)))
       time.sleep(hz)
    assert sum(responses)==dump_req*200

def test_fetch_all_data_test_and_keys_match_test():
    "Test Fetching and check if the JSON keys match"
    global time_window
    res=req.get(server_uri+"/get_data/{token}/{from_t}/{to_t}".format(
        token=token,
        from_t=0,
        to_t=10e+10
    ))
    json_resp=json.loads(res.content)
    pprint.pprint(json_resp[:2])
    
    #sets the begining and end time of the "drive"
    t_list=[i["Unixtimestamp"] for i in json_resp]
    time_window=(min(t_list),max(t_list))

    # set() makes the lists order agnostic
    assert set([i for i in json_resp[0].keys()])==set(CAR_DATA_KEYS)
    assert res.status_code==200

def test_fetch_data_within_time_range_test():
    "Test time range logic"
    
    res=req.get(server_uri+"/get_data/{token}/{from_t}/{to_t}".format(
        token=token,
        from_t=time_window[0],
        to_t=time_window[1]-2 # take 2 seconds from the end of the drive
    ))
    assert res.status_code==200
    json_resp_drive_minus_2=json.loads(res.content)
    
    res=req.get(server_uri+"/get_data/{token}/{from_t}/{to_t}".format(
        token=token,
        from_t=time_window[0]+2,
        to_t=time_window[1] # take 2 seconds from the end of the drive
    ))
    assert res.status_code==200
    json_resp_drive_plus_2=json.loads(res.content)

    time_minus_2=[i["Unixtimestamp"] for i in json_resp_drive_minus_2]
    time_plus_2=[i["Unixtimestamp"] for i in json_resp_drive_plus_2]

    #make sure the upper and lower time bounds are not in their respective excluding ranges
    assert time_window[0] not in time_plus_2
    assert time_window[1] not in time_minus_2

def test_change_car_metadata_test():
    "Test Changing Metadata"
    res=req.get(server_uri+"/change_car_metadata/{token}/{email}/{max_speed_beta}".format(
        token=token,
        email=email,
        max_speed_beta=max_spd_beta
    ))
    assert res.status_code==200
    res=req.get(server_uri+"/get_metadata_by_token/{token}".format(
        token=token
    ))
    assert res.status_code==200
    assert int(json.loads(res.content)["max_spd"])==max_spd_beta

def test_change_car_metadata_nonexistant_test():
    "Test Changing Metadata of nonexistant token"
    res=req.get(server_uri+"/change_car_metadata/{token}/{email}/{max_speed_beta}".format(
        token=fake_token,
        email=email,
        max_speed_beta=max_spd_beta
    ))
    assert res.status_code==400