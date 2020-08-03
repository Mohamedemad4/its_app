import kivy
import time
from kivy.app import App
from kivy.clock import Clock
from kivy.utils import platform
from kivy.clock import mainthread
from kivy.uix.boxlayout import BoxLayout

import urllib.request
from plyer import gps
from plyer import accelerometer


uri="http://mohamedemad4.pythonanywhere.com"
token="car1"

class acc_x_gps(BoxLayout):
    def __init__(self):
        super().__init__()
        self.sensorEnabled = False
        self.gps_location=""
        self.gps_status=""
        self.gps_location_dict={"lat":"0.0","lon":"0.0","speed":"0.0","accuracy":"0.0"}

    def init_gps(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'
            self.ids.error.text = status


        if platform == "android":
            print("gps.py: Android detected. Requesting permissions")
            self.request_android_permissions_gps_perm()
    
    def stop_gps(self):
        gps.stop()

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        self.gps_location_dict={k:v for k,v in kwargs.items()}

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}-{}'.format(stype, status)
    
    def init_acc(self):
        try:
            accelerometer.enable() 
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            status = "Accelerometer is not implemented for your platform"
            self.ids.accel_status.text = status
            self.ids.error.text = status

    def stop_acc(self):
        accelerometer.disable()
                
    def do_toggle(self):
        if not self.sensorEnabled:
            self.init_gps()
            self.init_acc()
            self.sensorEnabled = True
            self.ids.toggle_button.text = "Stop GPS&Acc"
            Clock.schedule_interval(self.get_acc_x_gps,.1)
        else:
            Clock.unschedule(self.get_acc_x_gps)
            self.sensorEnabled = False
            self.ids.toggle_button.text = "Start GPS&Acc"

    def get_acc_x_gps(self, dt):
        val = accelerometer.acceleration[:3]

        if not val == (None, None, None):
            x_acc,y_acc,z_acc=str(val[0]),str(val[1]),str(val[2])
            self.ids.x_label.text = "X: " + x_acc
            self.ids.y_label.text = "Y: " + y_acc
            self.ids.z_label.text = "Z: " + z_acc
            self.ids.gps_loc_label.text = self.gps_location
            self.ids.gps_status.text = self.gps_status

            try:
                url_req=urllib.request.Request(uri+"/data_dump/{token}/{x}/{y}/{z}/{lat}/{lon}/{speed}/{accuracy}/".format(
                        token=token,
                        x=x_acc,y=y_acc,z=z_acc,
                        lat=self.gps_location_dict["lat"],lon=self.gps_location_dict["lon"],
                        speed=self.gps_location_dict["speed"],accuracy=self.gps_location_dict["accuracy"])
                    )
                urllib.request.urlopen(url_req)
                self.ids.error.text="" 
            except Exception as e:
                print(e)
                self.ids.error.text="Couldn't send request to {0}".format(uri)

    def request_android_permissions_gps_perm(self):
        """
        Since API 23, Android requires permission to be requested at runtime.
        This function requests permission and handles the response via a
        callback.

        The request will produce a popup if permissions have not already been
        been granted, otherwise it will do nothing.
        """
        from android.permissions import request_permissions, Permission

        def callback(permissions, results):
            """
            Defines the callback to be fired when runtime permission
            has been granted or denied. This is not strictly required,
            but added for the sake of completeness.
            """
            if all([res for res in results]):
                print("callback. All permissions granted.")
            else:
                print("callback. Some permissions refused.")

        request_permissions([Permission.ACCESS_COARSE_LOCATION,
                             Permission.ACCESS_FINE_LOCATION], callback)



class its_App(App):
    def build(self):
        mc=acc_x_gps()
        mc.do_toggle()
        return mc

    def on_pause(self):
        gps.stop()
        return True
    
    def on_resume(self):
        gps.start(1000, 0)
        pass


if __name__ == '__main__':
    its_App().run()
