import os
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class db_mod():
    def __init__(self):
        init_db=False
        if os.path.exists("its_app.db")==False:
            init_db=True

        self.conn = sqlite3.connect('its_app.db')
        self.conn.row_factory = dict_factory
        self.c = self.conn.cursor()
        
        if init_db:
            self.c.execute('''CREATE TABLE car_spd
                         (car_token VARCHAR(255),lat REAL,lot REAL,speed REAL,accuracy REAL,Unixtimestamp BIGINT)''')

            self.c.execute('''CREATE TABLE car_metadata
                         (car_token VARCHAR(255),client_token VARCHAR(255),max_spd REAL)''')
            
            self.c.execute('''CREATE TABLE registered_cars
                        (car_token VARCHAR(255))''')
            for i in ["test-token-88","1111-1111-1111","2222-2222-2222","3333-3333-3333"]:
                self.c.execute("INSERT INTO registered_cars VALUES (?)",(i,))

            self.conn.commit()
    
    def is_car_token_registered(self,token):
        self.c.execute("SELECT * FROM registered_cars WHERE car_token=? ",(token,))
        if self.c.fetchall()==[]:
            return False
        else:
            return True

    def log_car_data(self,token,lat,lon,speed,accuracy,tstamp):
        self.c.execute("INSERT INTO car_spd VALUES (?,?,?,?,?,?)",(token,lat,lon,speed,accuracy,tstamp))
        self.conn.commit() 
    
    def get_car_data(self,token,from_stamp=0,to_stamp=10e+10): # should work for a decade LOL
        self.c.execute("SELECT * FROM car_spd where car_token=? AND Unixtimestamp>=? AND Unixtimestamp<=? ORDER BY Unixtimestamp",
            (token,from_stamp,to_stamp))
        fa=self.c.fetchall()
        if fa==[]:
            return False
        else:
            return fa

    def make_car_metadata(self,token,client_token,max_spd,ov=False):
        self.c.execute("DELETE FROM car_metadata where car_token = ?",(token,))
        self.c.execute("INSERT INTO car_metadata VALUES (?,?,?)",(token,client_token,max_spd))
        self.conn.commit() 
        return True
        
    def get_car_metadata_by_token(self,token):
        self.c.execute("SELECT * FROM car_metadata where car_token=?",(token,))
        fs=self.c.fetchall()
        if fs==None:
            return False
        return fs
    
    def get_metadata_by_client_token(self,client_token):
        self.c.execute("SELECT * FROM car_metadata WHERE client_token=?",(client_token,))
        fa=self.c.fetchall()
        if fa==None:
            return False
        return fa
