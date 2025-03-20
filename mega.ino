int state = 0;

void setup() {
  Serial2.begin(9600);

  Serial1.begin(9600);
  change_led();
}

void change_led() {
  Serial1.println(String(state));
}

void change_state(String message) {
  int pressed = message.toInt();

  if (pressed) {
    Serial2.println("B:1#");
    
    while (read_pk().toInt()) { delay(10); }
    
    state = 2;
    change_led();
    
    Serial2.println("B:0#");
  }
}

String read_kvu() {
  String data = Serial2.readStringUntil('\n');
  data.trim();

  return data;
}

String read_pk() {
  String data = Serial1.readStringUntil('\n');
  data.trim();

  return data;
}

void loop() {
  if (Serial2.available()) {
    String kvu = read_kvu();
    state = kvu.toInt();
    change_led();
  }
  
  if (Serial1.available()) {
    String pk = read_pk();
    change_state(pk);
  }
  
//    Serial.print("From NANO Received: ");
//    Serial.println(data);

  delay(10);
}
