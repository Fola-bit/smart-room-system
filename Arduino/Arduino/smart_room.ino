int pirPin = 2;
int ledPin = 9;
int ldrPin = A0;
int buttonPin = 3;

int threshold = 900;

unsigned long lightOnTime = 10000;
unsigned long lastMotionTime = 0;

int mode = 0;  // 0 = AUTO, 1 = MANUAL ON, 2 = MANUAL OFF
int lastButtonState = HIGH;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int motion = digitalRead(pirPin);
  int buttonState = digitalRead(buttonPin);

  int total = 0;
  for (int i = 0; i < 10; i++) {
    total += analogRead(ldrPin);
    delay(5);
  }
  int lightLevel = total / 10;

  if (buttonState == LOW && lastButtonState == HIGH) {
    mode = mode + 1;
    if (mode > 2) {
      mode = 0;
    }
    delay(200);
  }

  lastButtonState = buttonState;

  if (mode == 0) {
    if (motion == HIGH && lightLevel < threshold) {
      lastMotionTime = millis();
    }

    if (lightLevel < threshold &&
        (motion == HIGH || millis() - lastMotionTime < lightOnTime)) {
      digitalWrite(ledPin, HIGH);
    } else {
      digitalWrite(ledPin, LOW);
    }
  }
  else if (mode == 1) {
    digitalWrite(ledPin, HIGH);
  }
  else if (mode == 2) {
    digitalWrite(ledPin, LOW);
  }

  int ledState = digitalRead(ledPin);

  Serial.print(millis());
  Serial.print(",");
  Serial.print(lightLevel);
  Serial.print(",");
  Serial.print(motion);
  Serial.print(",");
  Serial.print(ledState);
  Serial.print(",");
  Serial.println(mode);

  delay(200);
}
