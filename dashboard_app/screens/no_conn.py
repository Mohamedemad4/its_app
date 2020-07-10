from kivy.clock import Clock
from screens.template_screen import template_screen

class no_conn(template_screen):
    def on_pre_enter(self,*args):
        self.check_event=Clock.schedule_interval(self.check_for_conn,.5)
        
    def check_for_conn(self,dt):
        if self.api.check_for_internet():
            self.manager.current = self.utils.prev_screen()
            Clock.unschedule(self.check_event)
        return
