import os
import time
import logging
import functools
from flask import jsonify
from gevent.pywsgi import WSGIServer
from flask_cors import CORS
from flask import Flask,Request,Response,render_template,request,abort
from db_mod import db_mod
from notf_man import notf_manager

app = Flask(__name__)
app.debug = True
CORS(app) # avoid cross origin problems
db_ins=db_mod()
notf=notf_manager()

def log_requests_and_origin(f):
    #https://stackoverflow.com/questions/26736419/
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print("got a {1} request from {0}".format(request.remote_addr,request.full_path))
        return f(*args, **kwargs)
    return decorated_function

def check_for_car_token(f):
    @functools.wraps(f)
    def wrapper(car_token, *args, **kwargs):
        if db_ins.is_car_token_registered(car_token):
            return f(car_token,*args, **kwargs)
        return jsonify({"status":"Car Token Doesn't Exist!"}),400  
    return wrapper

@app.route("/ping")
@app.route("/ping/")
@log_requests_and_origin
def ping():
    return jsonify({"status":"ok!"})

@app.route('/data_dump/<car_token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>')
@app.route('/data_dump/<car_token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>/')
@log_requests_and_origin
def log_data_dump(car_token,x,y,z,lat,lon,speed,accuracy):
    if not db_ins.is_car_token_registered(car_token):
        return jsonify({"status":"Token isn't registered"}),400

    metadata=db_ins.get_car_metadata_by_token(car_token)
    if metadata:
        for i in metadata:
            client_token,max_spd=i["client_token"],i["max_spd"]
            if float(speed)>float(max_spd):
                notf.push(client_token,car_token,"Speed Alert!","car {0} exceeded Max speed limit {1} and is running at {2}".format(car_token,max_spd,speed))
    db_ins.log_car_data(car_token,lat,lon,speed,accuracy,time.time())
    return jsonify({"status":"ok!"})

@app.route("/get_notfs/<client_token>")
@app.route("/get_notfs/<client_token>/")
@log_requests_and_origin
def get_notfs(client_token):
    metadata=db_ins.get_metadata_by_client_token(client_token)
    if not metadata:
        return jsonify({"status":"client_token isn't registered!"}),400
    notfs=notf.get_notfs(client_token)
    if notfs:
        return jsonify(notfs)
    return jsonify({"new_notfs":False})
        

@app.route("/get_data_recent/<car_token>")
@app.route("/get_data_recent/<car_token>/")
@log_requests_and_origin
@check_for_car_token
def get_data_recent(car_token):
    raw_data=db_ins.get_car_data(car_token)
    if raw_data:
        return jsonify(raw_data[-1])
    else:
        return jsonify({"status":"can't retreive speed data at this time"}),400

@app.route("/get_data/<car_token>/<from_stamp>/<to_stamp>")
@app.route("/get_data/<car_token>/<from_stamp>/<to_stamp>/")
@log_requests_and_origin
@check_for_car_token
def get_data_dump(car_token,from_stamp,to_stamp):
    raw_data=db_ins.get_car_data(car_token,from_stamp,to_stamp)
    return jsonify(raw_data)


@app.route("/is_car_token_registered/<car_token>")
@app.route("/is_car_token_registered/<car_token>/")
def is_token_registered(car_token):
    if db_ins.is_car_token_registered(car_token):
        return jsonify({"status":"ok!"})
    else:
        return jsonify({"status":"Token isn't registered"}),400

@app.route("/register_token/<car_token>/<client_token>/<max_spd>")
@app.route("/register_token/<car_token>/<client_token>/<max_spd>/")
@log_requests_and_origin
def register_token(car_token,client_token,max_spd):
    if not db_ins.is_car_token_registered(car_token):
        return jsonify({"status":"Token isn't registered"}),400
    db_ins.make_car_metadata(car_token,client_token,max_spd)
    return jsonify({"status":"ok!"})


@app.route("/change_car_metadata/<car_token>/<client_token>/<max_spd>")
@app.route("/change_car_metadata/<car_token>/<client_token>/<max_spd>/")
@log_requests_and_origin
@check_for_car_token
def change_car_metadata(car_token,client_token,max_spd):
    db_ins.make_car_metadata(car_token,client_token,max_spd)
    return jsonify({"status":"ok!"})

@app.route("/get_metadata_by_client_token/<client_token>")
@app.route("/get_metadata_by_client_token/<client_token>/")
def get_metadata_by_client_token(client_token):
    metadata=db_ins.get_metadata_by_client_token(client_token)
    if not metadata:
        return jsonify({"status":"client_token isn't registered!"}),400
    return jsonify(metadata)

@app.route("/get_metadata_by_token/<car_token>")
@app.route("/get_metadata_by_token/<car_token>/")
@check_for_car_token
def get_metadata_by_token(car_token):
    metadata=db_ins.get_car_metadata_by_token(car_token)
    return jsonify(metadata)
    
if __name__=="__main__":
    server = WSGIServer(("0.0.0.0",7060), app) 
    server.serve_forever()