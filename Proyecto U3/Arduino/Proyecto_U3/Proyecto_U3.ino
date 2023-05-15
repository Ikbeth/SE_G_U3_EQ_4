int ps[] = { A0, A1, A2, A3, A4 };
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1000);
}
int lectura;
void loop() {
  //CADENA = VMIN60
  if (Serial.available()) {
    //leemos con una variable tipo char que nos servira para elegir el tipo de eliminacion de ruido que se hara
    String cadena = Serial.readStringUntil('\n');
    String opcion = cadena.substring(0, 1);
    String num = cadena.substring(2, cadena.length());
    int tamMuestra = num.toInt();

    //Esta opcion hara una muestra de 30 y se eliminara a travez de valor minimo
    //Declarar nuestro arreglo
    int arr[] = { 0, 0, 0, 0, 0 };
    //Valor minimo
    if (opcion == "A") {
      int i, j, valMenor = 9999;
      for (j = 0; j < 5; j++) {
        for (i = 0; i < tamMuestra; i++) {
          lectura = analogRead(ps[j]);
          int v = map(lectura, 0, 1024, 1, 100);
          if (v < valMenor) {
            valMenor = v;
          }
          arr[j] = valMenor;
        }
        valMenor = 9999;
      }
      Serial.println(String(arr[0]) + "," + String(arr[1]) + "," + String(arr[2]) + "," + String(arr[3]) + "," + String(arr[4]));
    }  //Fin valor minimo
       ///////////////////////////////////////////////////////////////////////////////////////////////////////
    //Valor maximo
    if (opcion == "B") {
      int i, j, valMenor = -1;
      for (j = 0; j < 5; j++) {
        for (i = 0; i < tamMuestra; i++) {
          lectura = analogRead(ps[j]);
          int v = map(lectura, 0, 1024, 1, 100);
          if (v > valMenor) {
            valMenor = v;
          }
          arr[j] = valMenor;
        }
        valMenor = -1;
      }
      Serial.println(String(arr[0]) + "," + String(arr[1]) + "," + String(arr[2]) + "," + String(arr[3]) + "," + String(arr[4]));
    }  //Fin valor maximo
       /////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Promedio
    if (opcion == "C") {
      int i, j, sum = 0;
      for (j = 0; j < 5; j++) {
        for (i = 0; i < tamMuestra; i++) {
          lectura = analogRead(ps[j]);
          int v = map(lectura, 0, 1024, 1, 100);
          sum = sum + v;
        }
        arr[j] = sum / tamMuestra;
        sum = 0;
      }
      Serial.println(String(arr[0]) + "," + String(arr[1]) + "," + String(arr[2]) + "," + String(arr[3]) + "," + String(arr[4]));
    }  //Fin del promedio
       /////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Mediana
    if (opcion == "D") {
      int i, j;
      int m[tamMuestra];
      for (j = 0; j < 5; j++) {
        for (i = 0; i < tamMuestra; i++) {
          lectura = analogRead(ps[j]);
          int v = map(lectura, 0, 1024, 1, 100);
          m[i] = v;
        }
        for (int x = 0; x < tamMuestra; x++)
          for (int y = 0; y < tamMuestra - 1; y++)
            if (m[j] > m[j + 1]) {
              // intercambiar arr[j] y arr[j+1]
              int temp = m[j];
              m[j] = m[j + 1];
              m[j + 1] = temp;
            }
        if (tamMuestra == 1) {
          arr[j] = m[i];
        } else {
          if (tamMuestra % 2 == 0) {
            int suma = (m[tamMuestra / 2] + m[(tamMuestra / 2) - 1]) / 2;
            arr[j] = suma;
          } else {
            arr[j] = m[(tamMuestra / 2) - 1];
          }
        }
      }
      Serial.println(String(arr[0]) + "," + String(arr[1]) + "," + String(arr[2]) + "," + String(arr[3]) + "," + String(arr[4]));
    }  //Fin de la mediana
    ///////////////////////////////////////////////////////////////////////
    //Moda
    if (opcion == "E") {
      int i, j;
      int m[tamMuestra];
      for (j = 0; j < 5; j++) {
        for (i = 0; i < tamMuestra; i++) {
          lectura = analogRead(ps[j]);
          int v = map(lectura, 0, 1024, 1, 100);
          m[i] = v;
        }
        for (int x = 0; x < tamMuestra; x++)
          for (int y = 0; y < tamMuestra - 1; y++)
            if (m[j] > m[j + 1]) {
              // intercambiar arr[j] y arr[j+1]
              int temp = m[j];
              m[j] = m[j + 1];
              m[j + 1] = temp;
            }

        int rMax = 0;
        for (int x = 0; x < tamMuestra; x++) {
          int r = 0;
          for (int y = 0; y < tamMuestra; y++) {
            if (m[y] == m[x]) {
              r++;
            }
          }
          if (r > rMax) {
            rMax = r;
            arr[j] = m[x];
          }
        }
      }
      Serial.println(String(arr[0]) + "," + String(arr[1]) + "," + String(arr[2]) + "," + String(arr[3]) + "," + String(arr[4]));
    }
    ////////////////////////// tamMuestra = 1
    if (opcion == "Q") {
      int i;
      for (i = 0; i < 5; i++) {
        arr[i] = ps[i];
      }
      Serial.println(String(arr[0]) + "," + String(arr[1]) + "," + String(arr[2]) + "," + String(arr[3]) + "," + String(arr[4]));
    }
  }

  delay(1000);
}
