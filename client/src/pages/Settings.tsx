import React,{useState} from 'react';
import '../styles/genericStyles.css'
import { IonContent, IonButton,IonIcon,IonHeader,IonItemDivider,IonPage, IonTitle, IonToolbar, IonList } from '@ionic/react';
import {alertCircleOutline,eyeOutline} from 'ionicons/icons';
import { Redirect } from 'react-router-dom';

const Settings: React.FC = () => {
  const [redirect,setRedirect]=useState(<span></span>)
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Settings</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        {redirect}
        <IonList className="center_up">
          <IonItemDivider>
            Change Alert Speed
          </IonItemDivider>
          <IonButton size="large" className="main_btn" onClick={()=>{
                 setRedirect(<Redirect to="/settings/alert_speed"/>)
               }} color="primary">
              <IonIcon icon={alertCircleOutline}/>
          </IonButton>

          <IonItemDivider>
            View other Cars
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
