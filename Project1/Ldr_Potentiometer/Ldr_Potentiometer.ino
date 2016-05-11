int Potpin=A0;
int LDRpin=A1;
int LDRValue = 0; 
int PotValue = 0; 
int LDRNorm,PotNorm=0;
// result of reading the analog pin

void setup() {
  //pinMode(Potpin, OUTPUT);
  pinMode(LDRpin, OUTPUT);
  Serial.begin(9600); // sets serial port for communication
}

void loop() {
  LDRValue = analogRead(LDRpin);
  PotValue = analogRead(Potpin);// read the value from the LDR
  LDRNorm=int((LDRValue));
  PotNorm=int((PotValue));
  Serial.print("LDRValue"); 
  Serial.println(LDRNorm); 
  //Serial.println(LDRValue);  
  Serial.print("PotValue"); 
  Serial.println(PotNorm);
  //Serial.println(PotValue); // print the value to the serial port
  delay(100);                    // wait a little
}
