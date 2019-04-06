#define echoPin 8
#define trigPin 9
double distance = 0;
int state = -1;
void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  distance = ((pulseIn(echoPin, HIGH))*0.034/2)*0.393701;
  if(distance >= 8.5 && distance <= 9.5 && state != 0){
    Serial.println("object is within range");
    state = 0;
  }
  else if(distance <= 8.5 && state != 1){
    Serial.println("object is bellow range");
    state = 1;
  }
  else if( distance >= 9.5 && state != 2){
    Serial.println("object is out of range");
    state = 2;
  }
  delay(200);
}
