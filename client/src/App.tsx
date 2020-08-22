import React from 'react';
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
import OnBoarding from './pages/OnBoarding';

import Settings from './pages/Settings';
import ChangeEmail from './pages/ChangeEmail';
import ChangeAlertSpeed from './pages/ChangeAlertSpeed';
import ViewOtherCars from './pages/ViewOtherCars';

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

/* Theme variables */
import './theme/variables.css';


function App(){
  return (
      <IonApp>
        <IonReactRouter>
          <IonTabs>

            <IonRouterOutlet>
              <Route path="/help" component={HelpScreen} exact={true}/>
              <Route path="/settings" component={Settings} exact={true}/>
              <Route path="/settings/change_email" component={ChangeEmail} exact={true}/>
              <Route path="/settings/change_alert_speed" component={ChangeAlertSpeed} exact={true}/>
              <Route path="/settings/view_other_cars" component={ViewOtherCars} exact={true}/>
              <Route path="/map" component={MapScreen} exact={true}/>
              <Route path="/onboarding" component={OnBoarding} exact={true} />
              <Route path="/" render={() =>
              {
                if (true) {
                  return (<Redirect to="/map" />)
                }else{
                  return (<Redirect to="/onboarding" />)
                }
              
              }} exact={true} />
            </IonRouterOutlet>

            <IonTabBar slot="bottom">
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
            </IonTabBar>

          </IonTabs>
        </IonReactRouter>
      </IonApp>
    );
}

export default App;
