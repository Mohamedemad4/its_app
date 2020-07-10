from kivy.clock import Clock
from kivy.uix.button import Button
from kivy_garden.mapview import MapMarker, MapView

from screens.template_screen import template_screen

class map_screen(template_screen):
    def gotoopts(self,*args):self.manager.current="options_screen"
    def gotoHelp(self,*args):self.manager.current="help"

    def on_pre_enter(self,*args):
        self.map_update_event=Clock.schedule_interval(self.update_map_location,.5)
        
        lat,lon=self.api.get_current_car_cords()
        lat,lon=round(lat,4),round(lon,4) # round the viewport to nearest n-decimals

        self.map_view=MapView(zoom=3, lat=lat, lon=lon)
        self.add_widget(self.map_view)
    
        help_btn=Button(text="help",size_hint=(0.1,0.07),pos_hint={'top':1,"right":1})
        
        help_btn.bind(on_release=self.gotoHelp)
        self.add_widget(help_btn)

        options_btn=Button(text="options",size_hint=(0.1,0.07),pos_hint={'top':1,"left":1})
        
        options_btn.bind(on_release=self.gotoopts)
        self.add_widget(options_btn)
    

    def update_map_location(self,dt):
        lat,lon=self.api.get_current_car_cords()
        marker = MapMarker(lat=lat,lon=lon)
        self.map_view.add_marker(marker)
        return
    
    
