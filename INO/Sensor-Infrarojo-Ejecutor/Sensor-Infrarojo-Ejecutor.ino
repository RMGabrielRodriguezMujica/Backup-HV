
int led = 13;
int s = 7; // Sensor Infrarojo d
bool estado = false;
int x;
void setup() {
  // put your setup code here, to run once:

  pinMode(led, OUTPUT);
  pinMode(s, INPUT);
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  x = digitalRead(s);
  delay(100);
  //Serial.println(estado);

  if (x == 0) {
      estado = !estado;  // Cambia el estado (true/false)
      Serial.println(estado);
      digitalWrite(led, estado ? HIGH : LOW);  // Enciende o apaga el LED
      // Envía el estado actual a la PC
      if (estado) {
        Serial.println("ON");
      } else {
        Serial.println("OFF");
      }
   }
}
