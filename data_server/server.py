import os
import time
import logging
import functools
from flask import jsonify
from gevent.pywsgi import WSGIServer
from flask import Flask,Request,Response,render_template,request,abort
from db_mod import db_mod
from utils import warn_via_email

app = Flask(__name__)
app.debug = True
db_ins=db_mod()

def log_requests_and_origin(f):
    #https://stackoverflow.com/questions/26736419/
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print("got a {1} request from {0}".format(request.remote_addr,request.full_path))
        return f(*args, **kwargs)
    return decorated_function

def check_for_token(f):
    @functools.wraps(f)
    def wrapper(token, *args, **kwargs):
        if db_ins.get_car_metadata_by_token(token):
            return f(token,*args, **kwargs)
        return jsonify({"status":"Token Doesn't Exist!"}),400  
    return wrapper

@app.route("/ping")
@app.route("/ping/")
@log_requests_and_origin
def ping():
    return jsonify({"status":"ok!"})

@app.route("/gsm_dump_loc",methods=["POST"])
@app.route("/gsm_dump_loc/",methods=["POST"])
def gsD():
   new_vpn_conf=str(request.data)+" "+str(time.time())+"\n"
   with open("clib_data.txt","a+") as f:
        f.write(str(new_vpn_conf))
   return "oki"

@app.route('/data_dump/<token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>')
@app.route('/data_dump/<token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>/')
@log_requests_and_origin
def log_data_dump(token,x,y,z,lat,lon,speed,accuracy):
    if not db_ins.is_token_registered(token):
        return jsonify({"status":"Token isn't registered"}),400

    metadata=db_ins.get_car_metadata_by_token(token)
    if metadata:
        email,max_spd=metadata["email"],metadata["max_spd"]
        if float(speed)>float(max_spd):
            warn_via_email(email,token,"car {0} exceeded Max speed limit {1} and is running at {2}".format(token,max_spd,speed))
            
    db_ins.log_car_data(token,lat,lon,speed,accuracy,time.time())
    return jsonify({"status":"ok!"})

@app.route("/get_data_recent/<token>")
@app.route("/get_data_recent/<token>/")
@log_requests_and_origin
@check_for_token
def get_data_recent(token):
    raw_data=db_ins.get_car_data(token)
    if raw_data:
        return jsonify(raw_data[-1])
    else:
        return jsonify({"status":"can't retreive speed data at this time"}),400

@app.route("/get_data/<token>/<from_stamp>/<to_stamp>")
@app.route("/get_data/<token>/<from_stamp>/<to_stamp>/")
@log_requests_and_origin
@check_for_token
def get_data_dump(token,from_stamp,to_stamp):
    raw_data=db_ins.get_car_data(token,from_stamp,to_stamp)
    return jsonify(raw_data)


@app.route("/is_token_registered/<token>")
@app.route("/is_token_registered/<token>/")
def is_token_registered(token):
    if db_ins.is_token_registered(token):
        return jsonify({"status":"ok!"})
    else:
        return jsonify({"status":"Token isn't registered"}),400

@app.route("/register_token/<new_token>/<email>/<max_spd>")
@app.route("/register_token/<new_token>/<email>/<max_spd>/")
@log_requests_and_origin
def register_token(new_token,email,max_spd):
    if db_ins.get_car_metadata_by_token(new_token):
        return jsonify({"status":"token already in use"}),400
    if not db_ins.is_token_registered(new_token):
        return jsonify({"status":"Token isn't registered"}),400
    db_ins.make_car_metadata(new_token,email,max_spd)
    return jsonify({"status":"ok!"})


@app.route("/change_car_metadata/<token>/<email>/<max_spd>")
@app.route("/change_car_metadata/<token>/<email>/<max_spd>/")
@log_requests_and_origin
@check_for_token
def change_car_metadata(token,email,max_spd):
    db_ins.make_car_metadata(token,email,max_spd)
    return jsonify({"status":"ok!"})

@app.route("/get_metadata_by_email/<email>")
@app.route("/get_metadata_by_email/<email>/")
def get_metadata_by_email(email):
    metadata=db_ins.get_metadata_by_email(email)
    if not metadata:
        return jsonify({"status":"email isn't registered!"}),400
    return jsonify(metadata)

@app.route("/get_metadata_by_token/<token>")
@app.route("/get_metadata_by_token/<token>/")
@check_for_token
def get_metadata_by_token(token):
    metadata=db_ins.get_car_metadata_by_token(token)
    return jsonify(metadata)
    
if __name__=="__main__":
    server = WSGIServer(("0.0.0.0",7060), app) 
    server.serve_forever()