
#define TINY_GSM_MODEM_SIM868
#define SerialMon Serial
#define TINY_GSM_DEBUG SerialMon
#include <SoftwareSerial.h>
SoftwareSerial SerialAT(9, 8); // RX, TX

//#define DUMP_AT_COMMANDS
//#define LOGGING  // <- Logging is for the HTTP library

#include <TinyGsmClient.h>
#include <ArduinoHttpClient.h>

#define MACHINE_TOKEN "test-token"
#define SERVER_DUMP_URI "/data_dump/%s/0/0/0/%s/%s/%s/%s/" //data_dump/<token>/<x>/<y>/<z>/<lat>/<lon>/<speed>/<accuracy>

#if !defined(TINY_GSM_RX_BUFFER)
  #define TINY_GSM_RX_BUFFER 1024
#endif

#define HTTP_TIMEOUT 3000 //in ms
#define SERVER_HOSTNAME "52.255.192.159"
#define SERVER_PORT 7060
#define GOOD_GET_REQUEST_BDLENGTH 22

#define dump_buff_size 85
char dump_buff[dump_buff_size]; 

const char apn[]  = "";
const char gprsUser[] = "";
const char gprsPass[] = "";

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
    DBG("fail");
    delay(10000);
    return;
  }
  DBG("success");

  if (modem.isNetworkConnected()) {
    DBG("connected to network");
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
  SerialMon.begin(9600);
  SerialAT.begin(9600);
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
  if(!getGPSData(&lat,&lon,&speed,&acc)){
    //snprintf AVR implementation doesn't support %f so we have todo this shit instead
    //also I am bad at cpp (sorry)
    String lat_str=String(lat,6);
    char *lat_chr = lat_str.c_str();
    String lon_str=String(lon,6);
    char *lon_chr = lon_str.c_str();
    String spd_str=String(speed,1);
    char *speed_chr = spd_str.c_str();
    String acc_str=String(acc,2);
    char *acc_chr = acc_str.c_str();
    memset(dump_buff,0,dump_buff_size);
    snprintf(dump_buff,dump_buff_size,SERVER_DUMP_URI,MACHINE_TOKEN,lat_chr,lon_chr,speed_chr,acc_chr);
    if(make_dump_req()){
      DBG("Failed to log data");
    }
    delay(1000);
  }else
  {
    DBG("!getGPSData()");
  }
}

bool getGPSData(float* lat,float* lon,float* speed,float * acc){
  float alt;
  int vsat,usat,year,month,day,hour,min,sec;
  DBG("Requesting current GPS/GNSS/GLONASS location");
  if (modem.getGPS(lat, lon, speed, &alt, &vsat, &usat, acc,
                  &year, &month, &day, &hour, &min, &sec)) {
    return 0;
  }
  DBG("Couldn't get GPS/GNSS/GLONASS location");
  return 1;
}

bool make_dump_req(){
  HttpClient http(client, SERVER_HOSTNAME, SERVER_PORT);
  DBG("Requesting ",dump_buff);
  int err = http.get(dump_buff);
  if (err != 0) {
    DBG("Failed to connect to",SERVER_HOSTNAME,SERVER_PORT);
    delay(HTTP_TIMEOUT);
    return 1;
  }
  int status = http.responseStatusCode();
  DBG("Status Code:",String(status));
  if (!status) {
    delay(HTTP_TIMEOUT);
    return 1;
  }
  String body = http.responseBody();
  http.stop();
  if (body.length()==GOOD_GET_REQUEST_BDLENGTH){return 0;}
  return 1;
}
