'''
Simple Cam Test - BGR and Gray
    Create by pythonprogramming.net ==> See the tutorial here:
    https://pythonprogramming.net/loading-video-python-opencv-tutorial
Adapted by Marcelo Rovai - MJRoBot.org @8Feb18
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# set Width
cap.set(3,640)
# set Height
cap.set(4,480)

while(True):
    ret, frame = cap.read()
    # Flip camera vertically
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    k = cv2.waitKey(30) & 0xff
    # press 'ESC' to quit
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
