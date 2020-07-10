import sys
import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

from screens.no_conn import no_conn
from screens.onboarding import onboarding
from screens.help_screen import help_screen

from api import api
from utils import utils

api_ins=api()
utils_ins=utils()

sm = ScreenManager()
Builder.load_file('screens/onboarding.kv')
sm.add_widget(onboarding(name="onboarding",api_ins=api_ins,utils_ins=utils_ins))

Builder.load_file('screens/help_screen.kv')
sm.add_widget(help_screen(name="help",api_ins=api_ins,utils_ins=utils_ins))

Builder.load_file('screens/no_conn.kv')
sm.add_widget(no_conn(name="no_conn",api_ins=api_ins,utils_ins=utils_ins))

class itsd_App(App):
    def build(self):
        return sm
    def on_pause(self):
        return True
    def on_resume(self):
        pass

if __name__ == '__main__':
    itsd_App().run()