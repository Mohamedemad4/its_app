import React from 'react';
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';

const OnBoarding: React.FC = () => {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Onboarding</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
       <h1>Some thing</h1>
      </IonContent>
    </IonPage>
  );
};

export default OnBoarding;
