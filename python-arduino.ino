#include <cvzone.h>
#include <Servo.h>

Servo Servo1;
SerialData serialData(1, 3);

int servoPin = 9;
int angle[1];

void setup() {

  Servo1.attach(servoPin);
  serialData.begin(9600);
  
}

void loop() {

  serialData.Get(angle);
  Servo1.write(angle[0]);

}
