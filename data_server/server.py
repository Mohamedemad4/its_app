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


@app.route('/data_dump/<token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>')
@app.route('/data_dump/<token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>/')
@log_requests_and_origin
def log_data_dump(token,x,y,z,lat,lon,speed,accuracy):
    metadata=db_ins.get_car_metadata(token)
    
    if not metadata:
        return "Token Doesn't Exist!",400

    email,max_spd=metadata["email"],metadata["max_spd"]
    
    if float(speed)>float(max_spd):
        warn_via_email(email,token,"car {0} exceeded Max speed limit {1} and is running at {2}".format(token,max_spd,speed))
    db_ins.log_car_data(token,lat,lon,speed,accuracy,time.time())
    return "200ok!"

@app.route("/get_data/<token>/<from_stamp>/<to_stamp>")
@app.route("/get_data/<token>/<from_stamp>/<to_stamp>/")
@log_requests_and_origin
def get_data_dump(token,from_stamp,to_stamp):
    if db_ins.make_car_metadata(token,"","",create=False):
        return "Token Doesn't exist",400
    raw_data=db_ins.get_car_data(token,from_stamp,to_stamp)
    return jsonify(raw_data)

@app.route("/register_token/<new_token>/<email>/<max_spd>")
@app.route("/register_token/<new_token>/<email>/<max_spd>/")
@log_requests_and_origin
def register_token(new_token,email,max_spd):
    if db_ins.make_car_metadata(new_token,email,max_spd):
        return "200ok!"
    return "token already in use",400

@app.route("/change_car_metadata/<new_token>/<email>/<max_spd>")
@app.route("/change_car_metadata/<new_token>/<email>/<max_spd>/")
@log_requests_and_origin
def change_car_metadata(new_token,email,max_spd):
    if db_ins.make_car_metadata(new_token,email,max_spd,create=False):
        return "Token Doesn't exist",400
    db_ins.make_car_metadata(new_token,email,max_spd,ov=True)
    return "200ok!"

if __name__=="__main__":
    server = WSGIServer(("0.0.0.0",7060), app) 
    server.serve_forever()