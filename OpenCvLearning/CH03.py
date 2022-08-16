#-*- coding:UTF-8 -*-
"""
Topic: use opencv to draw pic
author: Zelin Yao
Date: 2022-8-16
"""

import cv2
import numpy as np 

img = np.zeros((256,256,3),np.uint8)
#draw line
img_line = cv2.line(img,(0,0),(255,255),(255,0,0),2,cv2.LINE_8)
cv2.namedWindow('line',cv2.WINDOW_NORMAL)
# cv2.imshow('line',img)
# cv2.waitKey(0)
#draw rectangle 
img_rect = cv2.rectangle(img,(50,50),(100,100),(0,255,0),1,cv2.LINE_AA)
cv2.namedWindow('rectangle',cv2.WINDOW_NORMAL)
# cv2.imshow('rectangle',img_rect)
# cv2.waitKey(0)
#draw circle
img_circle = cv2.circle(img,(125,125),30,(0,0,255),2,cv2.LINE_AA)
cv2.namedWindow('circle',cv2.WINDOW_NORMAL)
# cv2.imshow('circle',img_circle)
# cv2.waitKey(0)
#draw ellipse
img_ellip = cv2.ellipse(img,(180,180),(30,10),45,0,360,(200,100,100),2,cv2.LINE_AA)
cv2.namedWindow('ellipse',cv2.WINDOW_NORMAL)
# cv2.imshow('ellipse',img_ellip)
# cv2.waitKey(0)
#draw polylines
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts=pts.reshape((-1,1,2))
img_polylines = cv2.polylines(img,[pts],False,(100,200,100),2,cv2.LINE_AA)
cv2.namedWindow('polylines',cv2.WINDOW_NORMAL)
# cv2.imshow('polylines',img_polylines)
#add text
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
draw_text = cv2.putText(img,'OpenCv',(20,200),font,10,(255,0,0),1,cv2.LINE_AA)
cv2.namedWindow('putText',cv2.WINDOW_NORMAL)
# cv2.imshow('putText',draw_text)
cv2.waitKey(0)

#little Homework
#绘制字母n
img = np.zeros((256,256,3),np.uint8)
#n
cv2.line(img,(70,70),(70,120),(255,0,0),2,cv2.LINE_AA)
cv2.ellipse(img,(90,80),(20,10),0,180,360,(255,0,0),2)
cv2.line(img,(110,80),(110,120),(255,0,0),2,cv2.LINE_AA)
#o
cv2.circle(img,(90,50),20,(0,0,255),2,cv2.LINE_AA)
#口
cv2.rectangle(img,(60,60),(120,130),(100,200,100),2,cv2.LINE_AA)
cv2.namedWindow('no口',cv2.WINDOW_NORMAL)
cv2.imshow('no口',img)
cv2.waitKey(0)