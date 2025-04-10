import pickle
import cv2
import mediapipe as mp
import numpy as np

import serial
import time
from dibujador_landmark import draw_hand_landmarks  # Importa el módulo de dibujo
#------------------------------------------------
#ser = serial.Serial('COM10', 9600, timeout = 1)
#ser = serial.Serial('COM10', 9600, timeout = 1)
#time.sleep(2)
#__ ---_______________________________________________

model_dict = pickle.load(open('./model.p', 'rb'))
# model_dict = pickle.load(open('./modelABLEIOU1000.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands # cpu

hands = mp_hands.Hands(
    static_image_mode=True,
    min_detection_confidence=0.3,
    model_complexity=1  # Usa el modelo más pesado (mejor precisión en GPU)
)

mp_drawing = mp.solutions.drawing_utils
#
#mp_drawing_styles = mp.solutions.drawing_styles
#mp_drawing_styles = draw_hand_landmarksmp_hands = mp.solutions.hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

#labels_dict = {0: 'A', 1: 'B', 2: 'L'}
labels_dict = {0: 'A', 1: 'B', 2: 'L', 3: 'E', 4:'I' , 5:'O', 6:'U'}

ta = None  # Almacena el último carácter enviado

# Crear una ventana con nombre antes de establecerla en pantalla completa
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


while True:

    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()

    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ##############################


    results = hands.process(frame_rgb)

    frame = draw_hand_landmarks(frame, results)


    if results.multi_hand_landmarks:
        ##-----------------------
        first_hand = results.multi_hand_landmarks[0]  # Solo la primera mano detectada

        mp_drawing.draw_landmarks(
            frame, first_hand,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        )
        #-------------------------

        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))



        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10

        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10



        prediction = model.predict([np.asarray(data_aux)])

        predicted_character = labels_dict[int(prediction[0])] # Obtén el carácter predicho


        T = predicted_character  # Carácter actual

        if T != ta:  # Solo envía si es diferente al anterior
           # ser.write(labels_dict[int(prediction[0])].encode('utf-8'))  # Enviar carácter por Serial
            ta = T  # Actualizar el último carácter enviado
            print(T)  # Mostrar el carácter enviado


        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()