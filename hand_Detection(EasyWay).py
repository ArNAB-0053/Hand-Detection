import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pre_time = 0
current_time = 0

while(True):
    succes, frame = cap.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frameRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x*w) , int(lm.y*h)
                print(id, cx, cy)

                if id == 4: # We can use (0 -20) and each of index has specific hand part
                    cv2.circle(frame, (cx, cy), 10, (159, 19, 75), cv2.FILLED)

            mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)

    current_time = time.time()
    fps = 1/ (current_time-pre_time)
    pre_time = current_time

     # Black Box
    start_point = (0, 0)
    end_point = (102, 32)
    color = (0 ,0, 0)
    thickness = -1

    black_box = cv2.rectangle(frame, start_point, end_point, color, thickness) 

    # Text on Black Box
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

    cv2.putText(
        black_box,
        str(int(fps)),
        (31, 26),
        font, 1,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Camera", frame)

    if cv2.waitKey(10) == ord('0'):
        break