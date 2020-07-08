import sqlite3

class db_mod():
    def __init__(self):
        init_db=False
        if not os.path.exists("it_app.db"):
            init_db=True

        self.conn = sqlite3.connect('its_app.db')
        self.c = self.conn.cursor()

        if init_db:
            self.c.execute('''CREATE TABLE car_spd
                         (car_token VARCHAR(50),lat REAL,lot REAL,speed REAL,accuracy REAL,Unixtimestamp BIGINT)'''

            self.c.execute('''CREATE TABLE car_metadata
                         (car_token VARCHAR(50),email VARCHAR(255),max_spd REAL)'''

            self.conn.commit()

    def log_car_data(self,token,lat,lon,speed,accuracy,tstamp):
        self.c.execute("INSERT INTO car_spd VALUES (?,?,?,?,?,?)",token,lat,lon,speed,accuracy,Unixtimestamp)
        self.conn.commit() 
    
    def get_car_data(self,token,from_stamp=0,to_stamp=10e+10): # should work for a decade LOL
        self.c.execute("SELECT * where car_token=? FROM car_spd AND Unixtimestamp>=? AND Unixtimestamp<=? ORDER BY Unixtimestamp",
            token,from_stamp,to_stamp)
        return self.c.fetchall()

    def make_car_metadata(self,token,email,max_spd,ov=False):
       
        if ov=True:
            self.c.execute("DELETE car_metadata where car_token = ?",token)
        if ov=False:
            self.c.execute("SELECT email from car_metadata WHERE car_token=?",token)
            if self.c.fetchone()!=None
                return False

        self.c.execute("INSERT INTO car_metadata VALUES (?,?,?)",token,email,max_spd)
        self.conn.commit() 

    def get_car_metadata(self,token,ov=False):
        self.c.execute("SELECT * FROM car_metadata where car_token=?",token)
        return self.c.fetchone()
