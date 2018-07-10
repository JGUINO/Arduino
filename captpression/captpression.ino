#include <SPI.h>
#include <stdio.h>
#include <Adafruit_SSD1306.h>
#include <Wire.h>
#include <stdlib.h>
#include <system.h>
                         
#include <string.h>
#include <HX711.h>

#include <Adafruit_GFX.h>
#include <Adafruit_SPITFT.h>
#include <Adafruit_SPITFT_Macros.h>
#include <gfxfont.h>



#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define NUMFLAKES 10
#define XPOS 0
#define YPOS 1
#define DELTAY 2
#define OLED_RESET 0
Adafruit_SSD1306 display(OLED_RESET);
#include "LCDtest.h"
#define LOGO16_GLCD_HEIGHT 16 
#define LOGO16_GLCD_WIDTH  16 
#define buzzer 12
using namespace std;

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif

const char ssid[] = "Livebox-f6d8";
const char pass[] = "FE496357475DAFEF5F7ED4DFC3";
const char username[] = "";
const char brokerpass[] = "";
const char*ip;
char* msg;
char s[15];
WiFiClient esp8266;
PubSubClient client;
int Al=12;
unsigned long lastMillis = 0;
HX711 scale;
float mesure;



void connect() {
  Serial.print("checking wifi...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  
//  Serial.print("\nconnecting...");
//  
//  while (!client.connect("arduino")) {
//    Serial.print(".");
//    delay(1000);
//  }
//  
//
//  Serial.println("\nconnected!");

  //client.subscribe("pressions");
  //client.unsubscribe("pressions");
}


void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("1")) {
      Serial.println("connected");
      // Once connected, publish an announcement...

    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  
}

void alarme(){
  tone(buzzer,500);
  delay(3000);
  noTone(buzzer);
}

void jauge(float mesure,int maxi) {
  
  display.drawRect(10, 25, 100, 25, WHITE);
  display.fillRect(10,25,(mesure/maxi)*100,25,WHITE);
  delay(1);
}
void setup() {
  pinMode(Al, OUTPUT);
  Wire.begin();
  Serial.begin(9600);
  ip="192.168.1.124";
  Serial.println("HX711");
  WiFi.begin(ssid, pass);
  delay(2000);
  connect();
  // Note: Local domain names (e.g. "Computer.local" on OSX) are not supported by Arduino.
  // You need to set the IP address directly.
  //client.begin("broker.shiftr.io", net);
  client.setClient(esp8266);
  client.setServer(ip,1883);
  client.setCallback(callback);
  
  reconnect();
  

  Serial.println("Initializing the scale");
  // parameter "gain" is ommited; the default value 128 is used by the library
  // HX711.DOUT  - pin #A1
  // HX711.PD_SCK - pin #A0
  scale.begin(13, 14);

  Serial.println("Before setting up the scale:");
  Serial.print("read: \t\t");
  Serial.println(scale.read());     // print a raw reading from the ADC

  Serial.print("read average: \t\t");
  Serial.println(scale.read_average(20));   // print the average of 20 readings from the ADC

  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight (not set yet)

  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);  // print the average of 5 readings from the ADC minus tare weight (not set) divided
            // by the SCALE parameter (not set yet)

  scale.set_scale(220.f);                      // this value is obtained by calibrating the scale with known weights; see the README for details
  scale.tare();               // reset the scale to 0

  Serial.println("After setting up the scale:");

  Serial.print("read: \t\t");
  Serial.println(scale.read());                 // print a raw reading from the ADC

  Serial.print("read average: \t\t");
  Serial.println(scale.read_average(20));       // print the average of 20 readings from the ADC

  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight, set with tare()

  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);        // print the average of 5 readings from the ADC minus tare weight, divided
            // by the SCALE parameter set with set_scale

  Serial.println("Readings:");
  
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3C (for the 128x64)
  // init done
    
  // Show image buffer on the display hardware.
  // Since the buffer is intialized with an Adafruit splashscreen
  // internally, this will display the splashscreen.
  display.display();
  delay(200);
  
  // Clear the buffer.
  display.clearDisplay();

  // text i2c
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println ("Recherche addresse I2C. Recherche ...");
  byte count = 0;
  
  Wire.begin();
  for (byte i = 8; i < 120; i++)
  {
    Wire.beginTransmission (i);
    if (Wire.endTransmission () == 0)
      {
      display.print ("Adresse i2c trouvee : ");
      display.print (i, DEC);
      display.print (" (0x");
      display.print (i, HEX);
      display.println (")");
      display.display();
      count++;
      delay (1);  
      } // end of good response
  } // end of for loop
  display.println ("Fait.");
  
  display.print (count, DEC);
  display.println (" appareil(s) ");
  display.print ("trouves.");
  display.display();

  // miniature bitmap display
  display.drawBitmap(30, 16,  logo16_glcd_bmp, 16, 16, 1);
  display.display();
  delay(1);

  // invert the display
  display.invertDisplay(true);
  delay(100); 
  display.invertDisplay(false);
  delay(100); 
  display.clearDisplay();

  // lancement des mesures de distance
   display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("Salut!"); 
  display.display();

  // draw a bitmap icon and 'animate' movement
  //testdrawbitmap(logo16_glcd_bmp, LOGO16_GLCD_HEIGHT, LOGO16_GLCD_WIDTH);
  
}

void loop() {
  Serial.print("one reading:\t");
  Serial.print(scale.get_units(), 1);
  Serial.print("\t| average:\t");
   mesure = scale.get_units(10);Serial.println(mesure, 1);

  scale.power_down();             // put the ADC in sleep mode
  //client.loop();
  delay(1000);  // <- fixes some issues with WiFi stability
  scale.power_up();
 
   // Nombre maximal de chiffres + 1
  sprintf(s, "%f", mesure); // Conversion de l'entier
  printf("%f => \"%s\"\n", mesure, s);
  Serial.println(s);
  
  
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  //publish a message roughly every second.
  if (millis() - lastMillis > 1000) {
  lastMillis = millis();

  
  client.publish("capteur 1",s);
  }
  
  
  
  display.clearDisplay();  
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("Lecture Poids");
  display.println(s);
  display.println();
  jauge(mesure,10000);
 
  
  display.display();
  if (mesure>5000){
    alarme();
  }  
  memset(s,0,sizeof s);
}





