const int ledPin =  13; 
int incbyte = 0;
void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  incbyte = Serial.read();
  
  if(incbyte==49)
  {
    Serial.print(incbyte);
    digitalWrite(ledPin, HIGH);
    delay(50);
  }
  if(incbyte==48)
  {
    digitalWrite(ledPin, LOW);
    Serial.print(incbyte);
    delay(50);
  }
  delay(3);
}

