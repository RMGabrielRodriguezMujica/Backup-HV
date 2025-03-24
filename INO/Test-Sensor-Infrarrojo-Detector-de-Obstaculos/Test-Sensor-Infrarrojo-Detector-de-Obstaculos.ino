int led = 13;
int s = 7; // Sensor Infrarojo d
const int estado = 0;

void setup() {
  // put your setup code here, to run once:

  pinMode(led, OUTPUT);
  pinMode(s, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  estado = digitalRead(s);
  Serial.println(estado);

  if (estado == 0){
    digitalWrite(led, 1);
    
  }else{
    digitalWrite(led, 0);
  }
}
