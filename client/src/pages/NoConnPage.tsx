import React,{useState} from 'react';
import {Redirect} from 'react-router-dom'
import "../styles/genericStyles.css"
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import conf from "../Globals"
const NoConn: React.FC = () => {
  const [redirect,setRedirect]=useState(<span></span>)
  setTimeout(() => {
      fetch(`${conf.ServerURI}/ping/`).then(()=>{
          setRedirect(<Redirect to="/map"/>)
      })
  }, 500);
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>No Connection</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
          {redirect}
          <div className="center_up">
              <h1>Can't Connect to Server</h1>
              <h2>Try again later</h2>
          </div>
      </IonContent>
    </IonPage>
  );
};

export default NoConn;
