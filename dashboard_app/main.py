import sys
import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

from screens.onboarding import onboarding
from screens.template_screen import template_screen

from api import api

api_ins=api()

sm = ScreenManager()
Builder.load_file('screens/onboarding.kv')
sm.add_widget(onboarding(name="onboarding",api_ins=api_ins))

Builder.load_file('screens/template_screen.kv')
sm.add_widget(template_screen(name="template_screen",api_ins=api_ins))

class itsd_App(App):
    def build(self):
        return sm
    def on_pause(self):
        return True
    def on_resume(self):
        pass

if __name__ == '__main__':
    itsd_App().run()