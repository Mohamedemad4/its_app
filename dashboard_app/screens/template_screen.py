from kivy.uix.screenmanager import Screen

class template_screen(Screen):
    def __init__(self,name,api_ins):
        super().__init__()
        self.cols = 1
        self.rows = 2
        self.name=name
        self.api=api_ins
