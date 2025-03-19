# import subprocess
# import serial
#
# # Configura el puerto serial (cambia 'COM3' por el puerto correcto)
# arduino = serial.Serial('COM3', 9600, timeout=1)
#
# while True:
#     # Lee datos del Arduino
#     if arduino.in_waiting > 0:
#         mensaje = arduino.readline().decode('utf-8').strip()
#         print(f"Recibido: {mensaje}")
#
#         # Si se recibe el comando "ACTIVAR_SCRIPT", ejecuta una acción
#         if mensaje == "ON":
#             print("Activando script...")
#             subprocess.run(["python", "prueabaColors.py"])
#             print("ACTIVADO")
#


import subprocess
import serial

# Configura el puerto serial (cambia 'COM3' por el puerto correcto)
arduino = serial.Serial('COM8', 9600, timeout=1)

# Variable para almacenar el proceso
proceso = None

while True:
    # Lee datos del Arduino
    if arduino.in_waiting > 0:
        mensaje = arduino.readline().decode('utf-8').strip()
        print(f"Recibido: {mensaje}")

        # Si se recibe el comando "ON", ejecuta una acción
        if mensaje == "ON":
            if proceso is None:  # Si el proceso no está activo
                print("Activando script...")
                proceso = subprocess.Popen(["python", "prueba color 2.py"])
                print("Script activado.")
            else:
                print("El script ya está en ejecución.")
        elif mensaje == "OFF":
            if proceso is not None:  # Si el proceso está activo
                print("Deteniendo script...")
                proceso.terminate()  # Detiene el proceso
                proceso = None  # Reinicia la variable
                print("Script detenido.")