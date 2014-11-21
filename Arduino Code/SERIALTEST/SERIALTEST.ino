const int ledPin =  13; 
int incbyte = 0;
void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  incbyte = Serial.read();
  Serial.print(incbyte);
  if(incbyte==48)
  {
    digitalWrite(ledPin, HIGH);
    delay(100);
    digitalWrite(ledPin, LOW);
    delay(100);
  }
  delay(10);
}

