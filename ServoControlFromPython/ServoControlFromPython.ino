#include <Servo.h>

Servo myservo;  // create servo object to control a servo
int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
int pythonMsg = 0; // timeout value received from Python

void setup() {
  Serial.begin(9600); // Initialize serial communication
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(0);
  digitalWrite(13, HIGH); // turn on LED Blue
}

void loop() {
  if (Serial.available() > 0) { // If data is available on serial port
    pythonMsg = Serial.parseInt(); // Read the timeout value from Python

    if(pythonMsg == 1)
    {
      digitalWrite(13, LOW); // turn off LED Blue
      digitalWrite(12, HIGH); // turn on LED Orange
    }
    else if(pythonMsg == 2)
    {
      digitalWrite(12, LOW); // turn off LED Orange
      digitalWrite(8, HIGH); // turn on LED Green
       for (val = 0; val <= 180; val++) { // move from left to right
      myservo.write(val);
      delay(300);
    }
    }
  }
}
