import cv2
import time
import mediapipe
import Hand_Detector_Module as hdm

cap = cv2.VideoCapture(0)
pre_time = 0
current_time = 0
detector = hdm.HandDetector()
while True:
    succes, frame = cap.read()
    frame = detector.FindHands(frame)
    lmList = detector.FindPosition(frame)
    if len(lmList) != 0:
        print(lmList[2])

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