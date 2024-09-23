#define NUM_ELECTRODES 5
const int electrodePins[NUM_ELECTRODES] = {34, 35, 32, 33, 25}; // Pinea los electrodos
const float Rs = 10000; // Valor de la resistencia en ohmios (10kΩ)
const float Vin = 3.0;  // Voltaje de entrada

void setup() {
    Serial.begin(115200);
}

void loop() {
    float impedances[NUM_ELECTRODES];
    
    for (int i = 0; i < NUM_ELECTRODES; i++) {
        // Leer el voltaje del electrodo
        int analogValue = analogRead(electrodePins[i]);
        
        // Convertir el valor analógico a voltaje
        float Vout = (analogValue / 4095.0) * Vin; // Ajusta según tu ADC (12-bit en ESP32)
        
        // Calcular la impedancia
        impedances[i] = calculateImpedance(Vout);
    }
    
    // Enviar valores por puerto serial en formato CSV
    Serial.print("Impedancias: ");
    for (int i = 0; i < NUM_ELECTRODES; i++) {
        Serial.print(impedances[i], 2); // Muestra dos decimales
        if (i < NUM_ELECTRODES - 1) {
            Serial.print(", ");
        }
    }
    Serial.println();

    delay(1000); // Espera 1 segundo antes de la siguiente lectura
}

float calculateImpedance(float Vout) {
    return (Vout / (Vin - Vout)) * Rs; // Calcula la impedancia
}
