//Библиотеки для работы с рфид-ридером
#include<SPI.h>
#include<MFRC522.h>

//Обозначение пинов
#define SS_PIN 10
#define RST_PIN 9

//Создание переменных
MFRC522 rf(SS_PIN, RST_PIN);

MFRC522::MIFARE_Key key;

void setup() {
  Serial.begin(9600); //Запуск сериал порта
  SPI.begin();  //Запуск рфид считывателя
  rf.PCD_Init(); 

}

void loop() {
  if ( rf.PICC_IsNewCardPresent() && rf.PICC_ReadCardSerial()) { //Если предтавлена новая карта
  printHEX(rf.uid.uidByte, rf.uid.size); //Отправка юид и его размеров на вывод
  Serial.println();
  rf.PICC_HaltA();
  rf.PCD_StopCrypto1();
  }
  else { return; }
}


void printHEX(byte *buffer, byte sizeb) {
  for (byte i = 0; i < sizeb; i++) {
    if ( buffer[i] < 0x10 ) { Serial.print("0"); }
    Serial.print(buffer[i], HEX); //Вывод байтов в формате HEX
  }
}
