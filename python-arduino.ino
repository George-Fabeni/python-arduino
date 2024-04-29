#include <cvzone.h>
#include <Servo.h>

Servo Servo1;
Servo Servo2;
Servo Servo3;
SerialData serialData(3, 3);

int servoPin1 = 9;
int servoPin2 = 10;
int servoPin3 = 11;
int angle[3];

void setup() {

  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
  Servo3.attach(servoPin3);
  serialData.begin(9600);
  
}

void loop() {

  serialData.Get(angle);
  Servo1.write(angle[0]);
  Servo2.write(angle[1]);
  Servo3.write(angle[2]);

}
