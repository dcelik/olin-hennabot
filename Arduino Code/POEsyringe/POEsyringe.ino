// set pin numbers:
const int motorPinDown = 9;     // the number of the pushbutton pin
const int motorPinUp = 10;
const int sensorPin= A0;
const int motorSpeed = 50;
int sensorValue = 0;

void setup() {  
  pinMode(motorPinDown, OUTPUT);
  pinMode(motorPinUp, OUTPUT);
  Serial.begin(9600); 
}

void loop(){
  // read the state of the IR sensor:
  digitalWrite(motorPinDown, HIGH);
  digitalWrite(motorPinUp, LOW);
  sensorValue = analogRead(sensorPin);
  Serial.print("The Sensor reads ");
  Serial.println(sensorValue);
  
  if(sensorValue<950){
   digitalWrite(motorPinDown, LOW);
   digitalWrite(motorPinUp, LOW);
   delay(50); 
  }
  if(sensorValue<800){
    digitalWrite(motorPinUp, HIGH);
    digitalWrite(motorPinDown, LOW);
    delay(50);
  }
  //digitalWrite(motorPin, LOW);
  
  delay(10);
}

