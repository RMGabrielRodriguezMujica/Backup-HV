import cv2
import mediapipe as mp

# Inicializar MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Definir los landmarks y sus colores
amarillo_landmarks = {4, 7, 8, 11, 12, 15, 16, 19, 20}
azul_landmarks = {2, 3, 5, 6, 9, 10, 13, 14, 17, 18}
rojo_landmarks = {0, 1}

def draw_hand_landmarks(frame, results):
    """ Dibuja los landmarks de la mano con colores personalizados. """
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for idx, landmark in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                # Asignar colores según el índice del landmark
                if idx in amarillo_landmarks:
                    color = (0, 255, 255)  # Amarillo
                elif idx in azul_landmarks:
                    color = (255, 0, 0)  # Azul
                elif idx in rojo_landmarks:
                    color = (0, 0, 255)  # Rojo
                else:
                    color = (255, 255, 255)  # Blanco por defecto

                # Dibujar un círculo en el landmark con el color correspondiente
                cv2.circle(frame, (cx, cy), 5, color, -1)

            # Dibujar conexiones de la mano
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS
            )

    return frame
