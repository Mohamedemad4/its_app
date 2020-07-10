import sys
import kivy
from kivy.app import App
from kivy_garden.mapview import MapSource, MapView

from screens import onboarding
from api import api

api_ins=api()

class itsd_App(App):
    def build(self):
        return onboarding.onboarding(api_ins=api_ins)
    def on_pause(self):
        return True
    def on_resume(self):
        pass

if __name__ == '__main__':
    itsd_App().run()