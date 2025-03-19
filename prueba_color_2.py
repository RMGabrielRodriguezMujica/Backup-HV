import cv2
import mediapipe as mp

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Iniciar la cámara
cap = cv2.VideoCapture(0)

# Configurar ventana a pantalla completa



# Definir los landmarks y sus colores
amarillo_landmarks = {4, 7, 8, 11, 12, 15, 16, 19, 20}
azul_landmarks = {2, 3, 5, 6, 9, 10, 13, 14, 17, 18}
rojo_landmarks = {0, 1}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar la imagen para detectar manos
    results = hands.process(image_rgb)

    # Si se detectan manos
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar los landmarks con colores personalizados
            for idx, landmark in enumerate(hand_landmarks.landmark):
                # Obtener las coordenadas del landmark
                h, w, _ = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                # Asignar colores según el índice del landmark
                if idx in amarillo_landmarks:  # Landmarks amarillos
                    color = (0, 255, 255)  # Amarillo en BGR
                elif idx in azul_landmarks:  # Landmarks azules
                    color = (255, 0, 0)  # Azul en BGR
                elif idx in rojo_landmarks:  # Landmarks rojos
                    color = (0, 0, 255)  # Rojo en BGR
                else:  # Resto de landmarks (sin color)
                    continue

                # Dibujar un círculo en el landmark con el color correspondiente
                cv2.circle(frame, (cx, cy), 5, color, -1)

    # Mostrar la imagen
    cv2.imshow("Hand Landmarks", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()