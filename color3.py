import cv2
import mediapipe as mp

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Iniciar la cámara
cap = cv2.VideoCapture(0)

# Configurar ventana a pantalla completa
cv2.namedWindow("Tiempo Real", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Tiempo Real", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Definir los landmarks y sus colores
amarillo_landmarks = {4, 7, 8, 11, 12, 15, 16, 19, 20}
azul_landmarks = {2, 3, 5, 6, 9, 10, 13, 14, 17, 18}
rojo_landmarks = {0, 1}

# Conexiones entre los landmarks (según MediaPipe Hands)
hand_connections = mp_hands.HAND_CONNECTIONS

# Función para obtener el color de un landmark
def get_landmark_color(idx):
    if idx in amarillo_landmarks:
        return (0, 255, 255)  # Amarillo en BGR
    elif idx in azul_landmarks:
        return (255, 0, 0)  # Azul en BGR
    elif idx in rojo_landmarks:
        return (0, 0, 255)  # Rojo en BGR
    else:
        return None  # Sin color

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

                # Obtener el color del landmark
                color = get_landmark_color(idx)
                if color is not None:
                    # Dibujar un círculo en el landmark con el color correspondiente
                    cv2.circle(frame, (cx, cy), 5, color, -1)

            # Dibujar las líneas entre los landmarks con el color del primer punto
            for connection in hand_connections:
                # Obtener los índices de los landmarks conectados
                start_idx, end_idx = connection

                # Obtener las coordenadas de los landmarks
                start_point = (int(hand_landmarks.landmark[start_idx].x * w),
                               int(hand_landmarks.landmark[start_idx].y * h))
                end_point = (int(hand_landmarks.landmark[end_idx].x * w),
                             int(hand_landmarks.landmark[end_idx].y * h))

                # Obtener el color del primer landmark de la conexión
                line_color = get_landmark_color(start_idx)
                if line_color is not None:
                    # Dibujar la línea con el color del primer landmark
                    cv2.line(frame, start_point, end_point, line_color, 2)

    # Mostrar la imagen
    cv2.imshow("Tiempo Real", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()