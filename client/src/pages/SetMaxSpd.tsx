import React,{useState} from 'react';
import {
  IonIcon,IonButton,IonInput,IonListHeader,IonLabel,IonItem,
  IonContent,IonHeader,IonPage,IonTitle,IonToolbar
} from '@ionic/react';
import {arrowForward} from 'ionicons/icons';
import '../styles/genericStyles.css'
import { Redirect } from 'react-router-dom';


function SetMaxSpd(){
  const [textValue,setTextValue] = useState("")
  const [redirect,SetRedirect] = useState(<span></span>)
  function handleSetMaxSpd(){
    //call /register_token/<car_token>/<client_token>/<max_spd>
    alert(textValue)
    SetRedirect(<Redirect to="/"/>)
  }
  return (
      <IonPage>
        <IonHeader>
          <IonToolbar>
            <IonTitle>What Would you Like your Alert speed to be?</IonTitle>
          </IonToolbar>
        </IonHeader>
        <IonContent fullscreen>
          <div className="center_up">
            {redirect}
          <IonListHeader lines="full">
            <IonLabel>
            if your car reaches this speed we will send you and alert.
            </IonLabel>
          </IonListHeader>
            <IonItem>
              <IonInput value={textValue} type="number" onIonChange={e => setTextValue(e.detail.value!)}></IonInput>
            </IonItem>
          <IonButton size="large" className="main_btn" onClick={handleSetMaxSpd} color="tertiary">
            <IonIcon icon={arrowForward}/>
          </IonButton>  
          </div>
        </IonContent>
      </IonPage>
    );
}

export default SetMaxSpd;
