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
int OUT4 =8;
int OUT3 =9;
int OUT2 =10;
int OUT1 =11;

void setup()
{
  Serial.begin(9600);

  pinMode(OUT4, INPUT); 
  pinMode(OUT3, INPUT); 
  pinMode(OUT2, INPUT); 
  pinMode(OUT1, INPUT);
}
void loop()
{
  Serial.print(digitalRead(OUT4));
  Serial.print(" ");
  Serial.print(digitalRead(OUT3));
  Serial.print(" ");
  Serial.print(digitalRead(OUT2));
  Serial.print(" ");
  Serial.println(digitalRead(OUT1));
  delay(500);
}