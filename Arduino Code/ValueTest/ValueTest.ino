//#include <Wire.h>
//#include <Adafruit_MotorShield.h>
//#include "utility/Adafruit_PWMServoDriver.h"

#define xStep 6
#define xDir 7
#define yStep 8
#define yDir 9
#define xEn 10
#define yEn 11
#define zOut 12

//Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
//Adafruit_DCMotor *myMotor = AFMS.getMotor(1);

String inString = "";
int inChar = 0;
int xstepcompleted = 0;
int ystepcompleted = 0;
long xcounter = 0;
long ycounter = 0;

void setup() {
  Serial.begin(9600);
 // AFMS.begin();
  Serial.setTimeout(10000);
  pinMode(xStep, OUTPUT);
  pinMode(xDir, OUTPUT);
  pinMode(yStep, OUTPUT);
  pinMode(yDir, OUTPUT);
  pinMode(xEn, OUTPUT);
  pinMode(yEn, OUTPUT);
  pinMode(zOut,INPUT);
  //myMotor->setSpeed(50);
//myMotor->run(RELEASE);
}


void decode(String str){
  int prt = str.substring(0,1).toInt();
  int dir = str.substring(1,2).toInt();
  selectDir(dir);
  int xDist = str.substring(2,6).toInt();
  int yDist = str.substring(6,10).toInt();
  int xDelay = str.substring(10,14).toInt();
  int yDelay = str.substring(14,18).toInt();
  stepMotors(xDist, yDist, xDelay, yDelay);
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

void startPrint(boolean b){
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

