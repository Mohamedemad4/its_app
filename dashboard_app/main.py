import sys
import kivy
from kivy.app import App
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager,Screen

from screens.no_conn import no_conn
from screens.onboarding import onboarding
from screens.help_screen import help_screen
from screens.map_screen import map_screen
from screens.options_screen import options_screen

from api import api
from utils import utils

if platform!="android" and platform!='ios':
    from kivy.core.window import Window
    Window.size = (1080//2,1920//2)

api_ins=api()
utils_ins=utils()

sm = ScreenManager()
sm.add_widget(onboarding(name="onboarding",api_ins=api_ins,utils_ins=utils_ins))
sm.add_widget(help_screen(name="help",api_ins=api_ins,utils_ins=utils_ins))
sm.add_widget(no_conn(name="no_conn",api_ins=api_ins,utils_ins=utils_ins))
sm.add_widget(map_screen(name="map_screen",api_ins=api_ins,utils_ins=utils_ins))
sm.add_widget(options_screen(name="options_screen",api_ins=api_ins,utils_ins=utils_ins))

class itsd_App(App):
    def build(self):
        #if api_ins.is_registered():
        #    sm.current= "map_screen"
        #else:
        #    sm.current="onboarding"
        sm.current="options_screen"
        return sm
    def on_pause(self):
        return True
    def on_resume(self):
        pass

if __name__ == '__main__':
    itsd_App().run()