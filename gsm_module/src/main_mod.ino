
#define TINY_GSM_MODEM_SIM868
#define SerialMon Serial
#define SerialAT Serial3

#include <TinyGsmClient.h>
#include <ArduinoHttpClient.h>

#define MACHINE_TOKEN "test-token"
#define SERVER_DUMP_URI "/data_dump/%s/0/0/0/%f/%f/%f/%f/" //data_dump/<token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>

#if !defined(TINY_GSM_RX_BUFFER)
  #define TINY_GSM_RX_BUFFER 1024
#endif

#define HTTP_TIMEOUT 3000 //in ms
#define SERVER_HOSTNAME "0.0.0.0"
#define SERVER_PORT 7060
#define GOOD_GET_REQUEST_BDLENGTH 100

#define dump_buff_size 130
char dump_buff[dump_buff_size]; 

const char apn[]  = "";
const char gprsUser[] = "";
const char gprsPass[] = "";

//#define DUMP_AT_COMMANDS
#define TINY_GSM_DEBUG SerialMon
//#define LOGGING  // <- Logging is for the HTTP library

#ifdef DUMP_AT_COMMANDS
  #include <StreamDebugger.h>
  StreamDebugger debugger(SerialAT, SerialMon);
  TinyGsm modem(debugger);
#else
  TinyGsm modem(SerialAT);
#endif
TinyGsmClient client(modem); //Switch from TLS/SSL to plain old TCP/IP HTTP

void GRPS_connect(){
   DBG("Waiting for network...");
   if (!modem.waitForNetwork()) {
    DBG(" fail");
    delay(10000);
    return;
  }
  DBG("success");

  if (modem.isNetworkConnected()) {
    DBG("con");
  }
  // GPRS connection parameters are usually set after network registration
    if (!modem.gprsConnect(apn, gprsUser, gprsPass)) {
      DBG("Can't connect to GRPS");
      delay(10000);
      return;
    }
    if (modem.isGprsConnected()) {
      DBG("GPRS connected!");
    }
}
void setup() {
  // Set console baud rate
  SerialMon.begin(115200);
  SerialAT.begin(115200);
  DBG("Wait...");
  delay(2000);
  modem.restart();
  String modemInfo = modem.getModemInfo();
  DBG("Modem Info: ");
  DBG(modemInfo);
  GRPS_connect();
  DBG("Enable GPS");
  modem.enableGPS();
  delay(15000L);
}

void loop() {
  float lat,lon,speed,acc;
  if(getGPSData(&lat,&lon,&speed,&acc)){
    DBG(lat);
    DBG(lon);
    DBG(speed); 
    DBG(acc);
    memset(&dump_buff,0,dump_buff_size);
    snprintf(dump_buff,dump_buff_size,SERVER_DUMP_URI ,MACHINE_TOKEN,lat,lon,speed,acc);
    make_get_req(dump_buff);
    delay(1000);
  }else
  {
    DBG("Couldn't");
  }
}

bool getGPSData(float* lat,float* lon,float* speed,float * acc){
  float alt;
  int vsat,usat,year,month,day,hour,min,sec;
  DBG("Requesting current GPS/GNSS/GLONASS location");
  if (modem.getGPS(lat, lon, speed, &alt, &vsat, &usat, acc,
                  &year, &month, &day, &hour, &min, &sec)) {
    DBG("Latitude:", String(lat, 8), "\tLongitude:", String(lon, 8));
    DBG("Accuracy:", accuracy);
    return 0;
  }
  DBG("Couldn't get GPS/GNSS/GLONASS location");
  return 1;
}

bool make_get_req(char uri){
  HttpClient http(client, SERVER_HOSTNAME, SERVER_PORT);
  int err = http.get(uri);
  if (err != 0) {
    DBG("Failed to connect to",SERVER_HOSTNAME,SERVER_PORT);
    delay(HTTP_TIMEOUT);
    return 1;
  }
  int status = http.responseStatusCode();
  DBG("Status Code:",String(status,4));
  if (!status) {
    delay(HTTP_TIMEOUT);
    return 1;
  }
  String body = http.responseBody();
  http.stop();
  if (body.length()==GOOD_GET_REQUEST_BDLENGTH){return 0;}
  return 1;
}
