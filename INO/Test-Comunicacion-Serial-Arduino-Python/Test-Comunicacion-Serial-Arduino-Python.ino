// GERM-GROBOT
// 20.03.25

#include <string.h>  // Librería para usar strchr()

int LED = 13;
volatile int state = LOW;
char getstr;

void stateChange() {
  state = !state;
  //Serial.println(state + "A");
  digitalWrite(LED, state);
}

// Configuración inicial
void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

// Loop principal
void loop() {

  
  if (Serial.available() > 0) {
    getstr = Serial.read();
    /* if (getstr == 'A') {
    stateChange();
    
    }*/

    if(strchr("abcdefghijklmnÑñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", getstr)){
      stateChange();
    }
  }
}
