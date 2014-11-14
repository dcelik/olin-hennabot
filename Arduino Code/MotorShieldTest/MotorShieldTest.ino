  /* 
This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2 
---->	http://www.adafruit.com/products/1438
*/

#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS(0x60); // Default address, no jumpers

Adafruit_StepperMotor *myStepper = AFMS.getStepper(200, 1);
Adafruit_StepperMotor *myStepper2 = AFMS.getStepper(200,2);

void setup() {
  AFMS.begin(); // Start the bottom shield
  myStepper->setSpeed(1);
  myStepper->setSpeed(2);
}

int i,on;
void loop() {
 on = Serial.read();
 if(on==1){
   for (i=0; i<300; i++) {
      myStepper->onestep(BACKWARD, DOUBLE);
      delay(3);
   }
   
   for (i=0; i<300;i++){
     myStepper->onestep(FORWARD,DOUBLE);
     delay(3);
   }
   
   for (i=0; i<300; i++) {
      myStepper2->onestep(BACKWARD, DOUBLE);
      delay(3);
   }
   
   for (i=0; i<300; i++) {
      myStepper2->onestep(FORWARD, DOUBLE);
      delay(3);
   }
 }
 delay(3);
}
