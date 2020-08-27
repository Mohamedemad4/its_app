import LocalizedStrings from 'react-localization';
import AsyncStorage from '@react-native-community/async-storage';

let strings = new LocalizedStrings({
    "en":{
        help_title:"Help",
        map_title:"Map",
        set_spd_title:"What Would you Like your Alert speed to be?",
        no_conn_title:"No Connection",
        settings_title:"Settings",
        
        map_curr_spd_txt:"Current Speed: ",
        no_conn_text1:"Can't Connect to Server",
        no_conn_text2:"Try again later",
        
        spd_title_text1:"if your car reaches this speed we will send you and alert.",
        settings_ch_spd_btn_txt:"Change Alert Speed",
        settings_view_other_cars_txt:"View other Cars",
        
        tr_title:"Scan QR code on the device",
        tr_no_result:"No result",
        tr_err_token:"Error identifying Token. Are you Sure this is the Correct QR code?",
        tr_success:"Got it!"
    }
})

const conf={
    ServerURI: 'http://localhost:7060',
    devmode:true
}

if (conf.devmode==true){
    AsyncStorage.setItem('client_token',"client-token-69").catch(e=>console.log(e))
    AsyncStorage.setItem('curr_car_token',"test-token-88").catch(e=>console.log(e))
}

export {conf,strings} 