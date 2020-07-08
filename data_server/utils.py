import os
import time
import sqlite3
from flask import Flask
from datetime import datetime
from flask_mail import Mail,Message

MAX_THROT_ENTRIES=2*20 # 120 logs means a min of speeding
app=Flask(__name__)

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE car_spd_warn_throt
                 (car_token VARCHAR(50),Unixtimestamp BIGINT)''')
conn.commit()

def get_cur_date():
    return datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


MAIL_USERNAME = ""
MAIL_PASSWORD = ""

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME":MAIL_USERNAME,
    "MAIL_PASSWORD":MAIL_PASSWORD
}

app.config.update(mail_settings)
mail = Mail(app)


def warn_via_email(res,token,wmsg):
    c.execute("INSERT INTO car_spd_warn_throt VALUES (?,?)",(token,time.time()))
    c.execute("SELECT * from car_spd_warn_throt WHERE car_token=?",(token,))
    if len(c.fetchall())>=MAX_THROT_ENTRIES:
        c.execute("DELETE FROM car_spd_warn_throt WHERE car_token=?",(token,))
    else:
        return False

    """Sends an Email to the default email reciver No throtteling so expect to see multipule emails on a single event"""
    with app.app_context():
        body="Current Date: "+get_cur_date()+" UTC\n "+wmsg
        msg = Message(sender=("DATA ACQUISITION SYSTEM WARNING",MAIL_USERNAME),
                  recipients=[res],
                  subject=wmsg,
                  body=body)
        try:
            mail.send(msg)
            print("Sent")
            return True
        except:
            print("exp")
            return 'the Message Was not Sent,this incident will be <a href="https://xkcd.com/838/">reported</a>'

if __name__=="__main__":
    warn_via_email("Testing Emails Ma dude Current time is {0}".format(time.time()))
    