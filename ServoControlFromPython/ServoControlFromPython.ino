#include <Servo.h>

Servo myservo;  // create servo object to control a servo
int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
int timeout = 0; // timeout value received from Python

void setup() {
  Serial.begin(9600); // Initialize serial communication
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  if (Serial.available() > 0) { // If data is available on serial port
    timeout = Serial.parseInt(); // Read the timeout value from Python
    digitalWrite(13, HIGH); // turn on LED
  }
  delay(timeout); // waits for the specified timeout
    for (val = 0; val <= 360; val++) { // move from left to right
    myservo.write(val);
    delay(5);
  }
}
