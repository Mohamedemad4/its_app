import React,{useState} from 'react';
import { Redirect, Route } from 'react-router-dom';
import {
  IonApp,
  IonIcon,
  IonLabel,
  IonRouterOutlet,
  IonTabBar,
  IonTabButton,
  IonTabs
} from '@ionic/react';
import { IonReactRouter } from '@ionic/react-router';
import {helpCircleOutline,mapSharp,settingsOutline} from 'ionicons/icons';
import HelpScreen from './pages/HelpScreen';
import MapScreen from './pages/Map';
import SetMaxSpd from './pages/SetMaxSpd';

import Settings from './pages/Settings';
import ViewOtherCars from './pages/ViewOtherCars';
import TokenRegistrar from './pages/TokenRegistrar';
import NoConn from './pages/NoConnPage';

/* Core CSS required for Ionic components to work properly */
import '@ionic/react/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/react/css/normalize.css';
import '@ionic/react/css/structure.css';
import '@ionic/react/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/react/css/padding.css';
import '@ionic/react/css/float-elements.css';
import '@ionic/react/css/text-alignment.css';
import '@ionic/react/css/text-transformation.css';
import '@ionic/react/css/flex-utils.css';
import '@ionic/react/css/display.css';
import './theme/variables.css';

/**On Storage
 * client_token string 
 *    is the client_token (duh!) set by TokenRegistrar on first use
 * curr_car_token string
 *    Current token to be monitored set TokenRegistrar 
 */

import AsyncStorage from '@react-native-community/async-storage';

function App(){
  const [clientToken, setClientToken] = useState("not_set");
  
  const [bottomTab,setbottomTab] = useState(
    <div>
      <IonTabButton tab="settings" href="/settings">
        <IonIcon icon={settingsOutline} />
        <IonLabel>Settings</IonLabel>
      </IonTabButton>
      <IonTabButton tab="map" href="/map">
        <IonIcon icon={mapSharp} />
        <IonLabel>Map</IonLabel>
      </IonTabButton>
      <IonTabButton tab="help" href="/help">
        <IonIcon icon={helpCircleOutline} />
        <IonLabel>Help</IonLabel>
      </IonTabButton>
    </div>
  )

  AsyncStorage.getItem("client_token").then((v)=>{
    if (v!=null){
      setClientToken(v)
    }
  })

  return (
      <IonApp>
        <IonReactRouter>
          <IonTabs>

            <IonRouterOutlet>
              <Route path="/help" component={HelpScreen} exact={true}/>
              <Route path="/settings" component={Settings} exact={true}/>
              <Route path="/settings/alert_speed" component={SetMaxSpd} exact={true}/>
              <Route path="/settings/view_other_cars" component={ViewOtherCars} exact={true}/>
              <Route path="/reg_token" component={TokenRegistrar} exact={true}/>
              <Route path="/map" component={MapScreen} exact={true}/>
              <Route path="/no_conn" component={NoConn} exact={true}/>
              <Route path="/" render={() =>
              {
                if (clientToken==="not_set") {
                  setbottomTab(<span></span>)
                  return (<Redirect to="/reg_token" />)
                }else{
                  return (<Redirect to="/map" />)
                }
              }} exact={true} />
                
            </IonRouterOutlet>
            <IonTabBar slot="bottom">
              {bottomTab}
           </IonTabBar>
          </IonTabs>
        </IonReactRouter>
      </IonApp>
    );
}

export default App;
