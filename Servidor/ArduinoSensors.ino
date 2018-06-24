// Programa : Sensor de temperatura DS18B20 + Sensor de nível

#include <OneWire.h>
#include <DallasTemperature.h>
// Porta do pino de sinal do DS18B20
#define sensorTemp 2
// Define uma instancia do oneWire para comunicacao com o sensor
OneWire oneWire(sensorTemp);
//Envia a leitura da temperatura para o DallasTemperature
DallasTemperature sensors(&oneWire);
DeviceAddress end_sensorTemp;
//Porta analógica utilizada pelo sensor de nível
int sensorNivel = 13;

// Definição dos pinos dos atuadores
const int bomba = 8;
const int aquecedor = 12;
const int resfriador = 11;
 
// Definição das temperaturas mínima e máxima
float tempMin = 25;
float tempMax = 27;

char dados;
float tempAtual = 0.0;
  
void setup(void) {
  Serial.begin(9600);
  sensors.begin();
  pinMode(sensorNivel, INPUT);

}
void loop()
{
   // Le a informacao do sensor de nivel
  int nivelAqua = digitalRead(sensorNivel);
  // Le a informacao do sensor de temperatura
  sensors.requestTemperatures();

  //atualiza temperatura atual
  tempAtual = sensors.getTempC(end_sensorTemp);

  //Verifica estado do aquario e caso nescessario toma as devidas providencias
  actions(nivelAqua, tempAtual);

  //Se houve algum sinal sendo passado pela serial
  //tais dados sao alocados na variavel - dados -
//  if (Serial.available() > 0){      
//    dados = Serial.read();          
//    ler(dados,tempAtual,nivelAqua);
//  }
}
void actions(int nivelAqua,float tempAtual){
    
    //Controle de nivel
    if(nivelAqua == 0){
      digitalWrite(bomba, HIGH);
    }else{
      digitalWrite(bomba, LOW);
    }

    //Controle de temperatura
    if (tempAtual < tempMin) {
      digitalWrite(aquecedor, HIGH);
    }
     if (tempAtual = tempMax) {
      digitalWrite(aquecedor, LOW);
    }
     if (tempAtual > tempMax) {
      digitalWrite(resfriador, HIGH);
    }
     if (tempAtual = tempMin) {
      digitalWrite(resfriador, LOW);
    }
    
    
    
}
//void ler(char dados, float tempAtual, int nivelAqua){
//    if (dados == '1'){      
//      Serial.println(tempAtual); //Envia leitura para a porta serial e consequentemente para o servidor
//    }else{
//      Serial.println(nivelAqua); //Envia leitura para a porta serial e consequentemente para o servidor
//     
//    }
//}

