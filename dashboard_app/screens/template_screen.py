from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

class template_screen(Screen):
    def __init__(self,name,api_ins,utils_ins):
        super().__init__()
        self.cols = 1
        self.rows = 2
        self.name=name
        self.api=api_ins
        self.utils=utils_ins
        Window.bind(on_keyboard=self.Android_back_click)
        
    def on_enter(self,*args):
        self.utils.current_screen(self.name)

    def Android_back_click(self,window,key,*args):
        if key == 27:
            self.manager.current = self.utils.prev_screen()
            return True