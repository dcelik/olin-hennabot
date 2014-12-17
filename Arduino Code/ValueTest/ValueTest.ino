#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

#define xStep 6
#define xDir 7
#define yStep 8
#define yDir 9
#define xEn 10
#define yEn 11
#define zOut 12
#define sensorPin A0

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotor = AFMS.getMotor(3);
Adafruit_DCMotor *hennaMotor = AFMS.getMotor(4);

String inString = "";
int inChar = 0;
int xstepcompleted = 0;
int ystepcompleted = 0;
long xcounter = 0;
long ycounter = 0;
int irSensor = 0;

void setup() {
  Serial.begin(9600);
  AFMS.begin();
  Serial.setTimeout(10000);
  pinMode(xStep, OUTPUT);
  pinMode(xDir, OUTPUT);
  pinMode(yStep, OUTPUT);
  pinMode(yDir, OUTPUT);
  pinMode(xEn, OUTPUT);
  pinMode(yEn, OUTPUT);
  pinMode(zOut,INPUT);
  myMotor->setSpeed(255);
  hennaMotor->setSpeed(255);
  hennaMotor->run(RELEASE);
  myMotor->run(RELEASE);
}


void decode(String str){
  int prt = str.substring(0,1).toInt();
  if(prt ==0){
   hennaMotor->run(RELEASE); 
  }
  int dir = str.substring(1,2).toInt();
  selectDir(dir);
  int xDist = str.substring(2,6).toInt();
  int yDist = str.substring(6,10).toInt();
  int xDelay = str.substring(10,14).toInt();
  int yDelay = str.substring(14,18).toInt();
  if(prt==0){
    stepMotors(xDist, yDist, xDelay, yDelay);
  }
  else if(prt==1 && dir==0){
    startZFind();
  }
  else if(prt==1){
    long timetaken = lowerZ();
    hennaMotor->run(BACKWARD);
    stepMotors(xDist, yDist, xDelay, yDelay);
  }
}

void stepxone(int del){
  if(millis()-xcounter>del){
    xcounter = millis();
    digitalWrite(xStep,HIGH);
    delay(10);
    digitalWrite(xStep,LOW);
    xstepcompleted++;
  }
}

void stepyone(int del){
  if(millis()-ycounter>del){
    ycounter = millis();
    digitalWrite(yStep,HIGH);
    delay(10);
    digitalWrite(yStep,LOW);
    ystepcompleted++;
  }
}

void stepMotors(int xsteps, int ysteps, int xdel, int ydel){
 while(ystepcompleted<ysteps || xstepcompleted<xsteps){
   if(ystepcompleted<ysteps){
     stepyone(ydel);
   }
   if(xstepcompleted<xsteps){
     stepxone(xdel);
   } 
  }
  ystepcompleted = 0;
  xstepcompleted = 0; 
}

void selectDir(int i){
  if(i==0){
    digitalWrite(xEn,HIGH);
    digitalWrite(yEn,HIGH);
  }else if(i==1){
    digitalWrite(xEn,HIGH);
    digitalWrite(yEn,LOW);
    digitalWrite(yDir,LOW);
  }else if(i==2){
    digitalWrite(xEn,LOW);
    digitalWrite(yEn,LOW);
    digitalWrite(yDir,LOW);
    digitalWrite(xDir,LOW);
  }else if(i==3){
    digitalWrite(xEn,LOW);
    digitalWrite(yEn,HIGH);
    digitalWrite(xDir,LOW);
  }else if(i==4){
    digitalWrite(xEn,LOW);
    digitalWrite(yEn,LOW);
    digitalWrite(yDir,HIGH);
    digitalWrite(xDir,LOW);  
  }else if(i==5){
    digitalWrite(xEn,HIGH);
    digitalWrite(yEn,LOW);
    digitalWrite(yDir,HIGH);
  }else if(i==6){
    digitalWrite(xEn,LOW);
    digitalWrite(yEn,LOW);
    digitalWrite(yDir,HIGH);
    digitalWrite(xDir,HIGH);
  }else if(i==7){
    digitalWrite(xEn,LOW);
    digitalWrite(yEn,HIGH);
    digitalWrite(xDir,HIGH);
  }else if(i==8){
    digitalWrite(xEn,LOW);
    digitalWrite(yEn,LOW);
    digitalWrite(yDir,LOW);
    digitalWrite(xDir,HIGH);
  }
}

void startZFind(){
  irSensor = analogRead(sensorPin);
  Serial.print(irSensor);
  long zcounter = millis();
  while(irSensor>950 || irSensor<800){
    if(irSensor>950){
      myMotor->run(BACKWARD);
    }
    else if(irSensor<800){
      myMotor->run(FORWARD); 
    } 
    irSensor = analogRead(sensorPin);
  }
  myMotor->run(RELEASE);
  long timedif = millis()-zcounter;
  henna();
  long donetime = millis();
  while(millis()-donetime>timedif){
    myMotor->run(FORWARD);
  }
  myMotor->run(RELEASE);
}

long lowerZ(){
  irSensor = analogRead(sensorPin);
  Serial.print(irSensor);
  long zcounter = millis();
  while(irSensor>950 || irSensor<800){
    if(irSensor>950){
      myMotor->run(BACKWARD);
    }
    else if(irSensor<800){
      myMotor->run(FORWARD); 
    } 
    irSensor = analogRead(sensorPin);
  }
  myMotor->run(RELEASE);
  long timedif = millis()-zcounter;
  return timedif;
}



void henna(){
  hennaMotor->run(FORWARD);
  Serial.print("PRINTING");
  delay(100000);
  hennaMotor->run(RELEASE);
}

void loop()
{
  inChar = Serial.read();
  if (isDigit(inChar)){
      inString += (char)inChar;
      Serial.print((char)inChar);
  }
  if(inString.length()==18){
    //Serial.print(inString);
    decode(inString);
    Serial.println("!");
    inString = "";
  }
  selectDir(0);
}

