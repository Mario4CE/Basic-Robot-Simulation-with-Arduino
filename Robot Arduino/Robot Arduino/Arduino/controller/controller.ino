

// las constantes no cambiarán. Se utilizan aquí para establecer números pin:
const int buttonB1 = 2;     // el pin donde se icieron las conecciones em la proto
const int buttonB2 = 3;
const int buttonB3 = 4;
const int buttonB4 = 5;
const int buttonB5 = 6;
const int ledPin =  8;      // el pin donde se establecio la coneccion en la proto



// variables cambian a un valor:
int btnB1State = 0;         // variables que corresponden a los botones
int btnB2State = 0;
int btnB3State = 0;
int btnB4State = 0;
int btnB5State = 0;

void setup() {
  // Inicicia el Led como un output:
  pinMode(ledPin, OUTPUT);
  //Inician los botones como un input:
  pinMode(buttonB1, INPUT);
  pinMode(buttonB2, INPUT);
  pinMode(buttonB3, INPUT);
  pinMode(buttonB4, INPUT);
  pinMode(buttonB5, INPUT);
  Serial.begin(9600);
  Serial.println("Inicio");
}

void loop() {
  readBtn();
  readSerial();
}

void readBtn() {
  // leer el estado del valor del pulsador:
  btnB1State = digitalRead(buttonB1);
  btnB2State = digitalRead(buttonB2);
  btnB3State = digitalRead(buttonB3);
  btnB4State = digitalRead(buttonB4);
  btnB5State = digitalRead(buttonB5);


  // comprobar si el pulsador está pulsado. Si es así, el estado del botón es  HIGH:
  if (btnB1State == HIGH) {
    Serial.println("B1");

  } else if (btnB2State == HIGH) {
    // turn LED on:
    Serial.println("B2");

  }
  else if (btnB3State == HIGH) {
    // turn LED on:
    Serial.println("B3");

  } else if (btnB4State == HIGH) {
    // turn LED on:
    Serial.println("B4");
  }
  else if (btnB5State == HIGH) {
    // turn LED on:
    Serial.println("B5");
  }
  delay(500);

}

void readSerial() {
  if (Serial.available() > 0) {
    // lee lo puesto en el string:
    String incomingString = Serial.readString();

    // printea que ha resivido el mandato
    Serial.print("I received: ");
    Serial.println(incomingString);
    compareIncoming(incomingString);
    return incomingString;
  }
}


void compareIncoming(String message) {
  if (message == "hola") {
    digitalWrite(ledPin, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(ledPin, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
  }
}
