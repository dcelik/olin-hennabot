const int ledPin =  13;
const int xStep = 6;
const int xDir = 7;
const int yStep = 8;
const int yDir = 9;

int incbyte = 0;
void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  pinMode(xStep, OUTPUT);
  pinMode(xDir, OUTPUT);
  pinMode(yStep, OUTPUT);
  pinMode(yDir, OUTPUT);
  
}


void loop()
{
  incbyte = Serial.read();
//  if(incbyte==87) //w
  if(incbyte==49)
  {
    Serial.println('w');
    
    digitalWrite(yDir, LOW);
    digitalWrite(yStep, HIGH);
    delay(25);
    digitalWrite(yStep, LOW);
//    delay(25);
  }
  
//  if(incbyte==65) //a
    if(incbyte==50)
  {
    
    
    
    Serial.println('a');
    digitalWrite(xDir, HIGH);
    digitalWrite(xStep, HIGH);
    delay(25);
    
    digitalWrite(xStep, LOW);
//    delay(25);     
  }
//  if(incbyte==83) //s
    if(incbyte==51)
  {
    Serial.println('s');
    digitalWrite(yDir, HIGH);
    digitalWrite(yStep, HIGH);
    delay(25);
    digitalWrite(yStep, LOW);
//    delay(25);
  }
//  if(incbyte==68) //d
    if(incbyte==52)
  {
    Serial.println('d');
    digitalWrite(xDir, LOW);
    digitalWrite(xStep, HIGH);
    delay(25);
    digitalWrite(xStep, LOW);
//    delay(25);
  }
  delay(3);
}




