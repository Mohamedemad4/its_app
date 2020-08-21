import os
import time
import sqlite3
from datetime import datetime
from db_mod import dict_factory

class notf_manager:
    def __init__(self):
        self.MAX_THROT_ENTRIES=15 # 30 logs means a min of speeding
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = dict_factory
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE car_spd_warn_throt
                 (car_token VARCHAR(255),Unixtimestamp BIGINT)''')
                 
        ##implements a notf queqe to handle nots piling up on the user
        self.c.execute('''CREATE TABLE notfs_q
                 (email VARCHAR(255),msg VARCHAR(255),title VARCHAR(255))''')
        self.conn.commit()

    def get_cur_date(self):
        return datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def warn_via_email(self,email,token,title,wmsg):
        self.c.execute("INSERT INTO car_spd_warn_throt VALUES (?,?)",(token,time.time()))
        self.c.execute("SELECT * from car_spd_warn_throt WHERE car_token=?",(token,))
        if len(self.c.fetchall())>=self.MAX_THROT_ENTRIES:
            self.c.execute("DELETE FROM car_spd_warn_throt WHERE car_token=?",(token,))
        else:
            return False
        self.c.execute("INSERT INTO notfs_q VALUES (?,?,?) ",(email,wmsg,title))       
        return True
    
    def get_notfs(self,email):
        self.c.execute("SELECT * from notfs_q WHERE email=?",(email,))
        fa=self.c.fetchall()
        if fa==[]:
            return False
        else:
            self.c.execute("DELETE FROM notfs_q WHERE email=?",(email,))
            return fa