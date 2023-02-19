//
// Power Control for Raspberry Pi
// Version f. Arduino Micro
// V 0.1
// Author Thomas Glaser 2023 


//

const int PowerLed = 3;
const int Relay = 5;
const int PowerButton = 4;
const int ShutDown = 12;
int p = 0; 
int PState = 1;

void setup() {

pinMode(PowerLed, OUTPUT);
pinMode(PowerButton, INPUT_PULLUP);
pinMode(ShutDown, OUTPUT);
pinMode(Relay, OUTPUT); 
//
digitalWrite(PowerLed, LOW);
digitalWrite(Relay, LOW);
digitalWrite(ShutDown, HIGH);
delay(500);
digitalWrite(PowerLed, HIGH);
digitalWrite(Relay, HIGH);
//

}
//
//
void shutdown(){
    // request shutdown
    digitalWrite(ShutDown, LOW);  
    // Wait for shutdown
    for(int counter = 1;counter <= 15;counter++) {
      digitalWrite(PowerLed, HIGH);
      delay(1000);
      digitalWrite(PowerLed, LOW); 
      delay(1000);
   }
  digitalWrite(Relay, LOW);
  
}
//
void poweron() {
  
  for(int counter = 1;counter <= 3;counter++) {
    digitalWrite(PowerLed, LOW);
    delay(100);
    digitalWrite(PowerLed, HIGH); 
    delay(100);
  }
  digitalWrite(ShutDown, HIGH);
  digitalWrite(Relay, HIGH);
}

//
void loop() {
  // 
  
  // 
  p = digitalRead(PowerButton);
  // push button normally closed 
  if (p == 1) {           
    p = digitalRead(PowerButton);
    if ((p == 1) && (PState == 1)) {
//      Serial.print("Shutdown");
      shutdown();
      PState = 0;
      p = 0;
    }
    if ((p == 1) && (PState == 0)) {
 //     Serial.println("Power on");
      poweron();
      PState = 1;
    }
    
  }
  delay(100);  
}
