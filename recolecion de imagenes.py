import os
import cv2

# Definir el directorio donde se almacenarán los datos
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)  # Crear la carpeta si no existe

# Definir el número de clases y la cantidad de imágenes por clase
number_of_classes = 3  # Número total de clases a capturar
dataset_size = 100  # Cantidad de imágenes por clase

# Inicializar la captura de video desde la cámara web
cap = cv2.VideoCapture(0)

# Crear carpetas para cada clase dentro del directorio de datos
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)  # Crear la carpeta si no existe

    print('Collecting data for class {}'.format(j))

    # Esperar a que el usuario presione 'q' para comenzar la captura
    while True:
        ret, frame = cap.read()  # Capturar un fotograma desde la cámara
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)  # Mostrar mensaje en pantalla
        cv2.imshow('frame', frame)  # Mostrar el fotograma en una ventana
        if cv2.waitKey(25) == ord('q'):  # Esperar a que el usuario presione 'q'
            break

    # Capturar y almacenar imágenes en la carpeta de la clase actual
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()  # Capturar un fotograma desde la cámara
        cv2.imshow('frame', frame)  # Mostrar el fotograma en la ventana
        cv2.waitKey(25)  # Pequeña pausa para evitar sobrecargar el sistema

        # Guardar la imagen en la carpeta correspondiente con un nombre único
        image_path = os.path.join(class_dir, '{}.jpg'.format(counter))
        cv2.imwrite(image_path, frame)

        counter += 1  # Incrementar el contador de imágenes capturadas

# Liberar la cámara y cerrar todas las ventanas al finalizar
cap.release()
cv2.destroyAllWindows()
