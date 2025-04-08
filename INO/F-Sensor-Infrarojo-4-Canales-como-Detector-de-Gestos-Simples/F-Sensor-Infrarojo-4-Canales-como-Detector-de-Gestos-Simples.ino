/*
08/04/25

GERM GROBOT IngenieroEnProceso

*/

/*  Project: Ardu_Serie # 80
 *   4-Channel Line Tracker Sensor
 *   Ensures a Successful & Accurately Navigation For Your Robot
 *   
 *   INO file: _80_yl70_01.ino
 *   
 *   date: 8/24/19//
 *  
 *  code by: http://www.energiazero.org
 *  hardware by: Walfront
 * 
 *  Description: There is no easy way to tell your robot where to go! use this module.
 *  
 *  Visit: https://medium.com/jungletronics
 *  
 *  Tutorial: https://medium.com/jungletronics/4-channel-line-tracker-sensor-e6f9a0dad304
 *  
 *  License: CC-SA 3.0, feel free to use this code however you'd like.
 *  Please improve upon it! Let me know how you've made it better.
 */
int led = 13;
int s = 7; // Sensor Infrarojo d
bool estado = false;
int x;

int OUT4 = 8;
int OUT3 = 9;
int OUT2 = 10;
int OUT1 = 11;

// Variables para verificar el estado de activación hacia la derecha
bool step4_right = false;
bool step3_right = false;
bool step2_right = false;

// Variables para verificar el estado de activación hacia la izquierda
bool step1_left = false;
bool step2_left = false;
bool step3_left = false;

void setup() {
  Serial.begin(9600);

  pinMode(led, OUTPUT);

  pinMode(OUT4, INPUT);
  pinMode(OUT3, INPUT);
  pinMode(OUT2, INPUT);
  pinMode(OUT1, INPUT);
}

void loop() {
  // Verificar si todos los sensores están en 0
  if ((digitalRead(OUT4) == LOW) && 
      (digitalRead(OUT3) == LOW) && 
      (digitalRead(OUT2) == LOW) && 
      (digitalRead(OUT1) == LOW)) {

      // Si todos están en LOW
      Serial.println("PAUSE");
  }else {
    // Secuencia hacia la derecha (OUT4 → OUT3 → OUT2 → OUT1)
    if (digitalRead(OUT4) == 0 && !step4_right) {
      step4_right = true;
      Serial.println("OUT4 activado (Derecha)");
    }

    if (step4_right && digitalRead(OUT3) == 0 && !step3_right) {
      step3_right = true;
      Serial.println("OUT3 activado (Derecha)");
    }

    if (step3_right && digitalRead(OUT2) == 0 && !step2_right) {
      step2_right = true;
      Serial.println("OUT2 activado (Derecha)");
    }

    if (step2_right && digitalRead(OUT1) == 0) {
      Serial.println("OUT1 activado. ¡Dirección marcada: Derecha!");
      Serial.println("ON");
      // Reiniciar pasos para la secuencia de derecha
      step4_right = step3_right = step2_right = false;
    }

    // Secuencia hacia la izquierda (OUT1 → OUT2 → OUT3 → OUT4)
    if (digitalRead(OUT1) == 0 && !step1_left) {
      step1_left = true;
      Serial.println("OUT1 activado (Izquierda)");
    }

    if (step1_left && digitalRead(OUT2) == 0 && !step2_left) {
      step2_left = true;
      Serial.println("OUT2 activado (Izquierda)");
    }

    if (step2_left && digitalRead(OUT3) == 0 && !step3_left) {
      step3_left = true;
      Serial.println("OUT3 activado (Izquierda)");
    }

    if (step3_left && digitalRead(OUT4) == 0) {
      Serial.println("OUT4 activado. ¡Dirección marcada: Izquierda!");
      Serial.println("OFF");
      
      // Reiniciar pasos para la secuencia de izquierda
      step1_left = step2_left = step3_left = false;
    }
  }  



  

  // Mostrar los estados de los sensores en el monitor serial
  /*Serial.print(digitalRead(OUT4));
  Serial.print(" ");
  Serial.print(digitalRead(OUT3));
  Serial.print(" ");
  Serial.print(digitalRead(OUT2));
  Serial.print(" ");
  Serial.println(digitalRead(OUT1));
  */
  //delay(500); // Retardo para evitar lecturas muy rápidas
}