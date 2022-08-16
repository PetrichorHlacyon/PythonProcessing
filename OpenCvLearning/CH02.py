#-*- coding:UTF-8 -*-
from turtle import Turtle
import numpy as np
import cv2

#从摄像头读取图像，将他转化为黑白然后保存
#video object
cap = cv2.VideoCapture(0)
#out object
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('CH02.avi',fourcc,20.0,(640,480))

while (cap.isOpened()):
    ret , frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        img_flip = cv2.flip(gray,1)
        out.write(img_flip)
        cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows() 
