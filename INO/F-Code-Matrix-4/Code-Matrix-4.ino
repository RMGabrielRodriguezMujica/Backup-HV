#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>

// Definiciones de hardware
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 4
#define CLK_PIN   52
#define DATA_PIN  51
#define CS_PIN    53

// Usar SPI por hardware o software
MD_Parola P = MD_Parola(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);

// Configuración del desplazamiento
uint8_t scrollSpeed = 80;    // velocidad por defecto
textEffect_t scrollEffect = PA_SCROLL_LEFT;
textPosition_t scrollAlign = PA_LEFT;
uint16_t scrollPause = 75;   // pausa en milisegundos

// Buffers para mensajes
#define BUF_SIZE 75
char curMessage[BUF_SIZE] = { "" };
char newMessage[BUF_SIZE] = { "" };
bool newMessageAvailable = false;

void setup()
{
  Serial.begin(9600);  // Mayor velocidad para mejor comunicación
  Serial.println("Arduino listo para recibir mensajes...");
  
  P.begin();
  P.displayText(curMessage, scrollAlign, scrollSpeed, scrollPause, scrollEffect, scrollEffect);
}

void loop()
{
  // Leer mensajes del puerto serial
  if (Serial.available() > 0) {
    String received = Serial.readStringUntil('\n'); // Leer hasta salto de línea
    received.trim(); // Eliminar espacios o retornos de carro adicionales
    
    // Copiar el mensaje recibido al buffer
    received.toCharArray(newMessage, BUF_SIZE);
    newMessageAvailable = true;
    
    Serial.print("Mensaje recibido: ");
    Serial.println(newMessage);
  }

  // Animación del display
  if (P.displayAnimate()) {
    if (newMessageAvailable) {
      strcpy(curMessage, newMessage);
      newMessageAvailable = false;
      P.displayReset();
    }
  }
}