import React,{useState,useEffect} from 'react';
import '../styles/genericStyles.css'
import {carOutline} from 'ionicons/icons';
import { IonContent,IonButton,IonIcon,IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import { Redirect } from 'react-router-dom';
import {conf,strings} from '../Globals'
import AsyncStorage from '@react-native-community/async-storage';

const OnBoarding: React.FC = () => {
  const [cars,setCars]=useState([<span></span>])
  const [redirect,setRedirect]=useState(<span></span>)

  useEffect(()=>{
    AsyncStorage.getItem("client_token").then((client_token)=>{
      if (client_token!=null){
        fetch(`${conf.ServerURI}/get_metadata_by_client_token/${client_token}/`).then((response)=>{
          if (response.status===200){
            return response.json()
          }
        }).then((data)=>{
          
          let cars_list=[]
          
          let car:any;
          for (car in data){
            let car_token=String(car.car_token)
            cars_list.push(
              <IonButton size="large" className="main_btn" onClick={()=>{
                     AsyncStorage.setItem("curr_car_token",car_token).then(()=>{
                      setRedirect(<Redirect to="/map"/>)
                     }).catch(e=>console.log(e))
                   }} color="primary">
                  <IonIcon icon={carOutline}/>
              </IonButton>
            )
          }
          setCars(cars_list)
        }).catch(error => {
          console.log(Error(`Failed to get /get_metadata_by_client_token/${client_token} with error`))
          console.log(error)
          setRedirect(<Redirect to="/no_conn"/>)
        })    
      }
    })
  },[])

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>{strings.settings_view_other_cars_txt}</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        {redirect}
        <div className="center_up">
          {cars}
        </div>
      </IonContent>
    </IonPage>
  );
};

export default OnBoarding;
