import React, { Component } from 'react'
import QrReader from 'react-qr-reader'
import {
    IonContent,IonHeader,IonPage,IonTitle,IonToolbar, IonLabel
} from '@ionic/react';
import { Redirect } from 'react-router-dom';
import AsyncStorage from '@react-native-community/async-storage';
import conf from '../Globals';

function genUniqueToken() {
    //https://stackoverflow.com/questions/105034/
    return 'xxxx-xxxx-xxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
}

/**
 * Reads token and checks if it's valid
 * if so sets curr_token to the token value 
 * Also generates a client_token if it's not set in Storage
 */
class TokenReader extends Component {
  constructor(props){
    super(props)
    this.state = {
      delay: 500,
      result: 'No result',
      redirect: <span></span>
      
    }

    this.handleScan = this.handleScan.bind(this)
  }
  handleScan(result){
    if(result){
      if (result.split("-").length===3){ 
        fetch(`${conf.ServerURI}/is_car_token_registered/${result}/`).then(response => {
            //WHY THE FUCK DOES THIS WORK?
              if (response.status===200){
                  AsyncStorage.getItem("client_token").then((v)=>{
                      if(v==null){  //if client token isn't already set      
                        AsyncStorage.setItem('client_token',genUniqueToken()).catch(e=>console.log(e))
                      }
                  }).catch(e=>console.log(e))
                  AsyncStorage.setItem("curr_car_token",result).then(()=>{
                    this.setState({result:"Got it!",redirect:<Redirect to="/settings/alert_speed"/> })
                    //somehow close the video reader
                  }).catch(e=>console.log(e))     
              }
              else{
                console.log(`Server replied with a ${response.status}`)
                this.setState({ result:"Error identifying Token. Are you Sure this is the Correct QR code?",redirect:<Redirect to="/reg_token"/> }) 
               }
            })
            .catch(error => {
                console.log(Error(`Failed to get /is_car_token_registered/${result} with error`))
                console.log(error)
                this.setState({redirect:<Redirect to="/no_conn"/>})
            })
      }else{
        this.setState({ result:"Error identifying Token. Are you Sure this is the Correct QR code?",redirect:<Redirect to="/reg_token"/> }) 
      }
    }
  }
  handleError(err){
    console.error(err)
  }
  render(){
    const previewStyle = {
      height: 240,
      width: 320,
    }

    return(
    <IonPage>
        <IonHeader>
          <IonToolbar>
            <IonTitle>Scan QR code on the device</IonTitle>
          </IonToolbar>
        </IonHeader>
        <IonContent fullscreen>
          <div className="center_up">
              <IonLabel>{this.state.result}</IonLabel>
              {this.state.redirect}
              <center>
               <QrReader
               delay={this.state.delay}
               style={previewStyle}
               onError={this.handleError}
               onScan={this.handleScan}/>
               </center>
          </div>
        </IonContent>
      </IonPage>
    )
  }
}
export default TokenReader