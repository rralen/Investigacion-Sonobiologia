import serial
import numpy as np
import matplotlib.pyplot as plt

# Configura el puerto serial (ajusta 'COM3' al puerto que estés usando)
port = 'COM3'  # Cambia esto según tu configuración
baudrate = 115200
num_electrodes = 5

def read_serial_data(ser):
    line = ser.readline().decode('utf-8').strip()
    return line

def main():
    # Abre el puerto serial
    with serial.Serial(port, baudrate, timeout=1) as ser:
        plt.ion()  # Modo interactivo
        
        while True:
            try:
                # Lee datos del puerto serial
                data = read_serial_data(ser)
                print(f"Datos recibidos: {data}")

                # Procesa los datos
                if data.startswith("Impedancias:"):
                    # Extraer los valores de impedancia
                    values = data.replace("Impedancias: ", "").split(", ")
                    impedances = [float(v) for v in values]

                    # Crear un gráfico circular
                    plt.clf()  # Limpiar la figura anterior
                    angles = np.linspace(0, 2 * np.pi, num_electrodes, endpoint=False).tolist()
                    impedances += impedances[:1]  # Para cerrar el círculo
                    angles += angles[:1]  # Para cerrar el círculo

                    ax = plt.subplot(111, polar=True)
                    ax.fill(angles, impedances, color='red', alpha=0.25)
                    ax.plot(angles, impedances, color='red', linewidth=2)

                    ax.set_xticks(angles[:-1])  # No incluir el último para evitar duplicados
                    ax.set_xticklabels([f"Electrodo {i+1}" for i in range(num_electrodes)])
                    ax.set_title('Gráfica Circular de Impedancias')

                    plt.pause(0.1)  # Pausa para actualizar el gráfico

            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == '__main__':
    main()
