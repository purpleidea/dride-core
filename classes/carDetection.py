# import the necessary packages
import numpy as np
import cv2
import math
import os

from matplotlib import pyplot as plt





cap = cv2.VideoCapture("/Users/saoron/Desktop/driveRaw4/encoded/1459726505.h264.mp4")
cascade_src = '/Users/saoron/cardiganCam/assets/haar/cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    if cap.grab():
        flag, frame = cap.retrieve()
        frame = frame[200:350, 100:300]

        frame = cv2.flip(frame, -1)
        frame = cv2.flip(frame, 1)


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(frame, 1.1, 1)

        for (x, y, w, h) in cars:
            avgX = int(x + w/2)
            avgY = int(y + h/2)

            dy = avgX - 0
            dx = avgY - 0
            angle = int(math.atan2(dy, dx) * 180.0 / math.pi);

            cv2.rectangle(frame, (x, y), (x + w, y + h), (51, 51, 51), 2)
            cv2.putText(frame, str(angle), (avgX, avgY), font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.circle(frame, (avgX, avgY), 5, (0,0,0), -1)

    cv2.imshow('video1', frame)

    if cv2.waitKey(10) == 27:
        break