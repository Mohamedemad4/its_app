import os
import logging
import functools
from gevent.pywsgi import WSGIServer
from flask import Flask,Request,Response,render_template,request,abort

app = Flask(__name__)
app.debug = True

def log_requests_and_origin(f):
    #https://stackoverflow.com/questions/26736419/
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print("got a {1} request from {0}".format(request.remote_addr,request.full_path))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/data_dump/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>',methods=["GET"])
@log_requests_and_origin
def get_data_dump(x,y,z,lat,lon,speed,accuracy):
    gps_dump=(lat,lon)
    print(gps_dump)
    return "200ok!"

if __name__=="__main__":
    server = WSGIServer(("0.0.0.0",7060), app) 
    server.serve_forever()
    #app.run(host="0.0.0.0",port=7060)