import React,{useEffect,useState} from 'react';
import {Redirect} from 'react-router-dom'
import {IonContent, IonHeader, IonPage, IonTitle, IonToolbar} from '@ionic/react';
import {strings,conf} from '../Globals'
import {Map, Marker, Popup, TileLayer} from 'react-leaflet'
import '../styles/genericStyles.css'
import AsyncStorage from '@react-native-community/async-storage';

function MapScreen(){
  
  const [redirect,setRedirect]=useState(<span></span>)

  const [mapCenter,setMapCenter]=useState([30.0094,31.2086])
  const [markerLoc,setMarkerLoc]=useState([30.009423,31.208632])

  const [currSpeed,setCurrSpeed]=useState(666)
  const [currToken,setCurrToken]=useState("not_set")
  
  AsyncStorage.getItem("curr_car_token").then((v)=>{
    if (v!=null){
      setCurrToken(v)
    }
  })

  useEffect(()=>{
    setTimeout(() => {

      fetch(`${conf.ServerURI}/get_data_recent/${currToken}`).then((response)=>{
        if (response.status==200){
          return response.json()
        }
      }).then((data)=>{
        if (data["lat"]!=undefined && data["lon"]!=undefined && data["speed"]!=undefined ){
          setMapCenter([data["lat"],data["lon"]])
          setMarkerLoc([data["lat"],data["lon"]])
          setCurrSpeed(data["speed"])
        }
      }).catch(()=>setRedirect(<Redirect to="/no_conn"/>))

    }, 2000);
  },[])

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>{strings.map_title}</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        {redirect}
        <center>
          <h2>{strings.map_curr_spd_txt} {currSpeed}</h2>
          <Map center={mapCenter} zoom={13}>
             <TileLayer
               url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
               attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
             />
             <Marker position={markerLoc}>
               <Popup></Popup>
            </Marker>
          </Map>
        </center>
  	  </IonContent>
    </IonPage>
  );
};

export default MapScreen;