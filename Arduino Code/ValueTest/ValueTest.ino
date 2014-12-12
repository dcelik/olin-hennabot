const int xStep = 6;
const int xDir = 7;
const int yStep = 8;
const int yDir = 9;
const int xEn = 10;
const int yEn = 11;

int inChar = 0;
String inString = "";
int inInt = 0;

void setup() {
  Serial.begin(9600);
  pinMode(xStep, OUTPUT);
  pinMode(xDir, OUTPUT);
  pinMode(yStep, OUTPUT);
  pinMode(yDir, OUTPUT);
}

void decode(String str){
  String prt = str.substring(0,1);
  return;
}

void ysteps(int i){
  return;
}

void xsteps(int i){
  return;
}

void dir(int i){
  return;
}

void startPrint(boolean b){
  return;
}  


void loop()
{
  inChar = Serial.read();
  if(inChar==80){//Starts printing if you pass it P
    startPrint(true);
  }
  if (isDigit(inChar)){
      inString += (char)inChar;
      //Serial.print(inString);
  }
  if(inString.length()==14){
    Serial.print(inString);
    //DO SHIT
    Serial.print("?");
    char blanks[15];
    Serial.readBytes(blanks,15);
    inString = "";
  }
  delay(15);
}




