void setup() {
  Serial.begin(9600);
  Serial.println("NANO");

  pinMode(2, INPUT_PULLUP);

  for (int i=3; i<6; i++) {
    pinMode(i, OUTPUT);  
  }
}

void turn_on_led(String message) {
  int led = message.toInt();

  for (int i=3; i<6; i++) {
    digitalWrite(i, LOW);
  }

  digitalWrite(5 - led, HIGH);
}

void loop() {
  if (!digitalRead(2)) {
    Serial.println("1");
  } else {
    Serial.println("0");
  }
  

  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    data.trim();

    turn_on_led(data);

//    Serial.print("NANO Received: ");
//    Serial.println(data);
  }

  delay(10);
}
