import React, { Component } from 'react'
import QrReader from 'react-qr-reader'
import {
    IonContent,IonHeader,IonPage,IonTitle,IonToolbar, IonLabel
} from '@ionic/react';
import { Redirect } from 'react-router-dom';
/**
 * Reads and registered tokens to Backend
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
      if (result==="helloworld"){ 
        this.setState({ result:"Got it!",redirect:<Redirect to="/settings/alert_speed"/> })
        //do some check to verify it's a QR code by us without having to send to API
        // add a client_token registerer if it doesn't exist in AsyncStorage
        // add token_current=result
        //alert(result) //echoes a string
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