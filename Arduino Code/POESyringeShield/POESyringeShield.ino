
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotor = AFMS.getMotor(3);

int sensorPin = A0;
boolean tooFar = true;
boolean tooClose = false;
int motorSpeed = 0;
int sensorValue = 0;

void setup() {
  AFMS.begin();
  Serial.begin(9600);
  myMotor->setSpeed(255);
  myMotor->run(FORWARD);
  myMotor->run(RELEASE);
}

void loop(){
  // read the state of the IR sensor:
  sensorValue = analogRead(sensorPin);
  Serial.print("The Sensor reads ");
  Serial.println(sensorValue);
  
  if(sensorValue>950){
   myMotor->run(BACKWARD);
   delay(10); 
  }
  if(sensorValue<800){
    myMotor->run(FORWARD);
    delay(10);
  }
  if(sensorValue>800 && sensorValue<950){
    myMotor->run(RELEASE);
    delay(10);
  }
  delay(10);
}

