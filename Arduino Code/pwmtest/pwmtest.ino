void setup()
{
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop()
{
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  delay(75);
  digitalWrite(6, LOW);
  delay(75);
} 
