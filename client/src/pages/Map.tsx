import React from 'react';
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import {strings} from '../Globals'
const MapScreen: React.FC = () => {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>{strings.map_title}</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
          <h1>Some thing</h1>
      </IonContent>
    </IonPage>
  );
};

export default MapScreen;