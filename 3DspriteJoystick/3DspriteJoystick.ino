const int xPin=A0;
const int yPin=A1;
const int buttonPin=2;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int xVal=analogRead(xPin);
  int yVal=analogRead(yPin);
  int buttonState=digitalRead(buttonPin);

  int xMapped=map(xPin,0,1023,-100,100);
  int yMapped=map(yVal,0,1023,-100,100);

  Serial.print(xMapped);
  Serial.print(",");
  Serial.print(yMapped);
  Serial.print(",");
  Serial.println(buttonState);
  delay(50);
}