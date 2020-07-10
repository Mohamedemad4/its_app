from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
class template_screen(Screen):

    def gotoopts(self,*args):self.manager.current="options_screen"
    def gotoHelp(self,*args):self.manager.current="help"
    def __init__(self,name,api_ins,utils_ins):
        super().__init__()
        self.cols = 1
        self.rows = 2
        self.name=name
        self.api=api_ins
        self.utils=utils_ins
        Window.bind(on_keyboard=self.Android_back_click)
        help_btn=Button(text="help",size_hint=(0.1,0.07),pos_hint={'top':1,"right":1})
        
        help_btn.bind(on_release=self.gotoHelp)
        self.add_widget(help_btn,index=2)

        options_btn=Button(text="options",size_hint=(0.1,0.07),pos_hint={'top':1,"left":1})
        
        options_btn.bind(on_release=self.gotoopts)
        self.add_widget(options_btn,index=2)

    def on_enter(self,*args):
        self.utils.current_screen(self.name)

    def Android_back_click(self,window,key,*args):
        if key == 27:
            self.manager.current = self.utils.prev_screen()
            return True