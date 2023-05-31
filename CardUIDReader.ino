//Card only HEX UID Reader

#include<SPI.h>
#include<MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 rf(SS_PIN, RST_PIN);

MFRC522::MIFARE_Key key;

void setup() {
  Serial.begin(9600);
  SPI.begin(); 
  rf.PCD_Init(); 

}

void loop() {
  if ( rf.PICC_IsNewCardPresent() && rf.PICC_ReadCardSerial()) {
  printHEX(rf.uid.uidByte, rf.uid.size);
  Serial.println();
  rf.PICC_HaltA();
  rf.PCD_StopCrypto1();
  }
  else { return; }
}


void printHEX(byte *buffer, byte sizeb) {
  for (byte i = 0; i < sizeb; i++) {
    if ( buffer[i] < 0x10 ) { Serial.print("0"); }
    Serial.print(buffer[i], HEX);
  }
}
