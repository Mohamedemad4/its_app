import React,{useState} from 'react';
import {
  IonIcon,IonButton,IonInput,IonListHeader,IonLabel,IonItem,
  IonContent,IonHeader,IonPage,IonTitle,IonToolbar
} from '@ionic/react';
import {arrowForward} from 'ionicons/icons';
import '../styles/genericStyles.css'
import { Redirect } from 'react-router-dom';
import {strings,conf} from '../Globals';
import AsyncStorage from '@react-native-community/async-storage';

function SetMaxSpd(){
  const [textValue,setTextValue] = useState("")
  const [redirect,SetRedirect] = useState(<span></span>)
  function handleSetMaxSpd(){
    AsyncStorage.getItem("client_token").then((client_token)=>{
      if (client_token!=null){
        AsyncStorage.getItem("curr_car_token").then((car_token)=>{
          fetch(`${conf.ServerURI}/register_token/${car_token}/${client_token}/${textValue}/`).then((response)=>{
            if(response.status===200){
              SetRedirect(<Redirect to="/map"/>)
            }else{
              console.log(`Server returned ${response.status}`)
            }
          }).catch(error => {
            console.log(Error(`Failed to get /register_token/${car_token}/${client_token}/${textValue} with error`))
            console.log(error)
            SetRedirect(<Redirect to="/no_conn"/>)
          })
        })
      }
    })
  }
  return (
      <IonPage>
        <IonHeader>
          <IonToolbar>
            <IonTitle>{strings.set_spd_title}</IonTitle>
          </IonToolbar>
        </IonHeader>
        <IonContent fullscreen>
          <div className="center_up">
            {redirect}
          <IonListHeader lines="full">
            <IonLabel>
              {strings.spd_title_text1}
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
