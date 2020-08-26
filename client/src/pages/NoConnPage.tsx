import React,{useState} from 'react';
import {Redirect} from 'react-router-dom'
import "../styles/genericStyles.css"
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import {conf,strings} from "../Globals"
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
          <IonTitle>{strings.no_conn_title}</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
          {redirect}
          <div className="center_up">
              <h1>{strings.no_conn_text1}</h1>
              <h2>{strings.no_conn_text2}</h2>
          </div>
      </IonContent>
    </IonPage>
  );
};

export default NoConn;
