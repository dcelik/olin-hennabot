#include <pt.h>   // include protothread library

#define xStep 6
#define xDir 7
#define yStep 8
#define yDir 9
#define xEn 10
#define yEn 11

int inChar = 0;
String inString = "";
int inInt = 0;
boolean done = false;

static struct pt pt1, pt2;

void setup() {
  Serial.begin(9600);
  pinMode(xStep, OUTPUT);
  pinMode(xDir, OUTPUT);
  pinMode(yStep, OUTPUT);
  pinMode(yDir, OUTPUT);
  pinMode(xEn, OUTPUT);
  pinMode(yEn, OUTPUT);
  PT_INIT(&pt1);  // initialise the two
  PT_INIT(&pt2);  // protothread variables
}


void decode(String str){
  int prt = str.substring(0,1).toInt();
  int dir = str.substring(1,1).toInt();
  selectDir(dir);
  int xDist = str.substring(2,3).toInt();
  int yDist = str.substring(5,3).toInt();
  int xDelay = str.substring(8,3).toInt();
  int yDelay = str.substring(11,3).toInt();
  if(xDelay==10){
    yDelay = (20*yDelay)-10;
  }
  if(yDelay==10){
    xDelay = (20*xDelay)-1;
  }
}

void yDelaySteps(int ysteps,int xdel,int ydel){
  for(int i=0;i<ysteps;i++){
    digitalWrite(yStep,HIGH);
    digitalWrite(xStep,HIGH);
    delay(15);
    digitalWrite(yStep,LOW);
    delay(xdel);
  }
}

void stepxone(){
    digitalWrite(xStep,HIGH);
    delay(10);
    digitalWrite(xStep,LOW);
}

void stepyone(){
    digitalWrite(yStep,HIGH);
    delay(10);
    digitalWrite(yStep,LOW);
}

/* This function toggles the LED after 'interval' ms passed */
static int protothreadx(struct pt *pt, int interval, int steps) {
  static unsigned long timestamp = 0;
  int i = steps;
  PT_BEGIN(pt);
  while(i>0) { // never stop 
    /* each time the function is called the second boolean
    *  argument "millis() - timestamp > interval" is re-evaluated
    *  and if false the function exits after that. */
    PT_WAIT_UNTIL(pt, millis() - timestamp > interval );
    timestamp = millis(); // take a new timestamp
    stepxone();
    i--;
  }
  PT_END(pt);
}

/* exactly the same as the protothread1 function */
static int protothready(struct pt *pt, int interval, int steps) {
  static unsigned long timestamp = 0;
  int i = steps;
  PT_BEGIN(pt);
  while(i>0) {
    PT_WAIT_UNTIL(pt, millis() - timestamp > interval );
    timestamp = millis();
    stepyone();
    i--;
  }
  PT_END(pt);
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
  return;
}  


void loop()
{
  selectDir(5); 
  protothreadx(&pt1,10,100);
  protothready(&pt2,10,100);
  delay(1000);
  
//  inChar = Serial.read();
//  if(inChar==80){//Starts printing if you pass it P
//    startPrint(true);
//  }
//  if (isDigit(inChar)){
//      inString += (char)inChar;
//      //Serial.print(inString);
//  }
//  if(inString.length()==14){
//    Serial.print(inString);
//    //DO SHIT
//    Serial.print("?");
//    char blanks[15];
//    Serial.readBytes(blanks,15);
//    inString = "";
//  }
//  delay(15);
}




