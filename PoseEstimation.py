# con il pose estimation possiamo tracciare una determinata posizione che ci può servire.
# appena rilevo una posizione che decido io posso triggherare una determinata variabile/ funzione per fare una determinata cosa


# importo le librerie
import cv2
import mediapipe as mp
# numpy è una libreria che importa il "potere" computazionale di c e fortran a pythhon
import numpy as np
# ci serve per calcolare i diversi angoli

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# funzione che mi serve per calcolare l'angolo


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    # cordinata y di c meno la cordinata y di b e fa la cordinata x di c meno la cordinata x di b
    # arctan2 mi trasforma i calcoli che ho fatto sulle cordinate x e y dei valori a b c in angoli
    # quindi l'angolo della sottrazione tra y di c e y di b e x di c e x di b - l'angolo della sottrazione tra y di a e y di b meno x di a e x di b
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
        np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0:  # appena l'angolo supera i 180 diventa 360 meno l'angolo perchè lui ragiona a 2 angoli di 180 da 0 a 180 e poi da 360 meno angolo
        angle = 360-angle

    return angle


cap = cv2.VideoCapture(0)
# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates
            # mi prendo le cordinate del punto n 11
            # del punto numero 13 e del punto n 15 in modo tale che posso lavorare sull'angolo che c'è tra il 13 e 11 e il 13 e il 15
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Mi faccio il calcolo dell'angolo
            angle = calculate_angle(shoulder, elbow, wrist)

            # Visualize angle
            # gli passo quello che mi torna dal video, l'angolo che mi sono calcolato prima castato in stringa e poi
            cv2.putText(image, str(angle),
                        # con questa cosa mi prendo la posizione della variabile elbow nello schermo perchè moltiplico le cordinate per le dimensioni che la fotocamera mi restituisce ovvero una risoluzione di 640x480 che andrò a trasformare in un intero e a castare in una tupla perchè opencv accetta solo una tupla per questo dato
                        tuple(np.multiply(elbow, [640, 480]).astype(int)),
                        # lo style di come verranno stampati i dati
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,
                                                        255, 255), 2, cv2.LINE_AA
                        )
            
            #logica giocino stupido 
            if angle < 130: #se langolo tra 11(left_shoulder) e 13(left_elbow) / 13(left_elbow) e 15(left_wrist) è minore di 130 allora sono comunista
              stage = "comunista"
            if angle > 140 and stage == 'comunista': #se langolo tra 11(left_shoulder) e 13(left_elbow) / 13(left_elbow) e 15(left_wrist) è maggiore di 140 e sono ancora comunista divento fascista
              stage = "fascista"
              
            print(stage)

        except:
            pass

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(
                                      color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
