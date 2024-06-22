/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-temperature-humidity-sensor
 */

#include "DHT.h"
#define DHTPIN A2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
const int IN_A0 = A0;
const int IN_D0 = 8;
void setup() {
  Serial.begin(9600);
  dht.begin(); // initialize the sensor
  pinMode (IN_A0, INPUT);
  pinMode (IN_D0, INPUT);
}
int value_A0;
bool value_D0;
void loop() {
  // wait a few seconds between measurements.
  delay(100);
  value_A0 = analogRead(IN_A0); // reads the analog input from the IR distance sensor
  value_D0 = digitalRead(IN_D0);// reads the digital input from the IR distance sensor
  // read humidity
  float humi  = dht.readHumidity();
  // read temperature as Celsius
  float tempC = dht.readTemperature(true);
  // read temperature as Fahrenheit
  float tempF = dht.readTemperature(true);

  // check if any reads failed
  if (isnan(humi) || isnan(tempC) || isnan(tempF)) {
    Serial.println("Failed to read from DHT sensor!");
  } else {
    
    Serial.print(humi);
    Serial.print("%");
    Serial.print(" ");
    Serial.print(tempC);
    Serial.print(" ");
    Serial.print((tempF*9/5)+32);
    Serial.print(" ");
    Serial.println(value_A0);
    //if(value_A0>490){
    //  Serial.println("Dark");
    //}
    //else if(value_A0<490){
    //  Serial.println("Bright");
    //}
    

    
  }
}