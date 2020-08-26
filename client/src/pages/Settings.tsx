import React,{useState} from 'react';
import '../styles/genericStyles.css'
import { IonContent, IonButton,IonIcon,IonHeader,IonItemDivider,IonPage, IonTitle, IonToolbar, IonList } from '@ionic/react';
import {alertCircleOutline,eyeOutline} from 'ionicons/icons';
import { Redirect } from 'react-router-dom';
import {strings} from '../Globals'

const Settings: React.FC = () => {
  const [redirect,setRedirect]=useState(<span></span>)
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>{strings.settings_title}</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        {redirect}
        <IonList className="center_up">
          <IonItemDivider>
            {strings.settings_ch_spd_btn_txt}
          </IonItemDivider>
          <IonButton size="large" className="main_btn" onClick={()=>{
                 setRedirect(<Redirect to="/settings/alert_speed"/>)
               }} color="primary">
              <IonIcon icon={alertCircleOutline}/>
          </IonButton>

          <IonItemDivider>
            {strings.settings_view_other_cars_txt}
          </IonItemDivider>
          <IonButton size="large" className="main_btn" onClick={()=>{
                 setRedirect(<Redirect to="/settings/view_other_cars"/>)
               }} color="primary">
              <IonIcon icon={eyeOutline}/>
          </IonButton>

      </IonList>
      </IonContent>
    </IonPage>
  );
};

export default Settings;
