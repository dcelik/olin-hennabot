const int ledPin =  13;
const int xStep = 6;
const int xDir = 7;
const int yStep = 8;
const int yDir = 9;

int incbyte = 0;
void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  pinMode(xStep, OUT)
  pinMode(xDir, OUT)
  pinMode(yStep, OUT)
  pinMode(yDir, OUT)
  
}


void loop()
{
  incbyte = Serial.read();
  if(incbyte==87) //w
  {
    digitalWrite(6, HIGH);
    delay(75);
    digitalWrite(6, LOW);
    delay(75);
  }
  if(incbyte==65) //a
  {
    
  }
  if(incbyte==83) //s
  {}
  if(incbyte==68) //d
  {}
  delay(3);
}

