# motion "didattico" modifiche da fare qui e se funzionanti da implementare nel a

# importo le librerie che mi servono
import cv2  # importo opencv che è una libreria che mi serve per analizzare ogni video o immagine , prendere immagini dalla videocamera
import mediapipe as mp  # ho importato la libreria che mi serve per catturare il movimento
# e quindi da unire alla libreria mediapipe per controllare le immagini che catturo


mp_drawing = mp.solutions.drawing_utils  # drawn utility
mp_holistic = mp.solutions.holistic  # modello holistic

# importo il materiale per far funzionare la fotocamera del computer
# cap = cv2.VideoCapture(0)  # array di videocamere presenti nel computer
# while cap.isOpened():  # quando cap è aperto allora leggerà tutto quello che c'è da leggere e attiverà la videocamera ecc
# praticamente legge quello che gli da dalla videocamera con cap.read
#    ret, frame = cap.read()
#    cv2.imshow('Raw Webcam Feed', frame)

# può non funzionare se lo starto da qui quindi copiare nella console python
#    if cv2.waitKey(10) & 0xFF == ord('q'):
#        break

# quando chiudo la finestra di python potrebbe continuare a prendere informazioni allora con il cap.release interrompo la cattura da parte di cv2 e con cv2 destroy all windows chiudo tutte le finestre aperte e i processi correlati ad esse
# cap.release()
# mp.destroyAllWindows()
# cv2.destroyAllWindows()

# cap.release()
# cv2.destroyAllWindows()

# in queste righe ho collegato la videocamera al codice e ho deciso quale dispositivo di cattura video usare

cap = cv2.VideoCapture(0)

# inizializzo holistic
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        # cambio colore a quello che mi torna dal video
        # ricolorazione con il colore
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # faccio la rilevazione
        results = holistic.process(image)
        # cercare il modo di salvare questi file direttamente in un foglio di testo in modo tale da cercare di mettere in ascolto il pacchetto per rilevare il movimento
        print(results.face_landmarks)

        #face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
        # mi trasmette in tempo reale la posizione di una determinata cosa : la mano destra o sinistra, la testa  e il corpo

        # Draw face landmarks
        mp_drawing.draw_landmarks(
            image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)

        # Right hand
        # mp_drawing.draw_landmarks(
        # image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Left Hand
        # mp_drawing.draw_landmarks(
        # image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Pose Detections
       # mp_drawing.draw_landmarks(
        # image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        cv2.imshow("Motion Capture", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

mp_holistic.POSE_CONNECTIONS

mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
mp_drawing.draw_landmarks
cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        print(results.face_landmarks)

        # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks

        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 1. Draw face landmarks
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(80, 110, 10), thickness=1, circle_radius=1),
                                  mp_drawing.DrawingSpec(
                                      color=(80, 256, 121), thickness=1, circle_radius=1)
                                  )

        # 2. Right hand
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(80, 22, 10), thickness=2, circle_radius=4),
                                  mp_drawing.DrawingSpec(
                                      color=(80, 44, 121), thickness=2, circle_radius=2)
                                  )

        # 3. Left Hand
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(121, 22, 76), thickness=2, circle_radius=4),
                                  mp_drawing.DrawingSpec(
                                      color=(121, 44, 250), thickness=2, circle_radius=2)
                                  )

        # 4. Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(245, 117, 66), thickness=2, circle_radius=4),
                                  mp_drawing.DrawingSpec(
                                      color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
