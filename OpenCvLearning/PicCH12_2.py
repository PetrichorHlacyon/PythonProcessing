"""
author : Zelin Yao
date : 2022-8-23
"""
#Goal
"""
画出凸包和检测的凹陷点
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

image = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH10\\Fig1015(a)[noiseless].tif")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image')
cv2.createTrackbar('threshold','image',150,255,nothing)
while True:
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
    threshold = cv2.getTrackbarPos('threshold','image')
    ret , img_binary = cv2.threshold(gray,threshold,255,cv2.THRESH_BINARY)
    contours , hierarchy = cv2.findContours(img_binary , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    hull = cv2.convexHull(cnt,returnPoints=False)
    defects = cv2.convexityDefects(cnt,hull)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s,0])
        end = cnt[e,0]
        far = tuple(cnt[f][0])
        cv2.line(image,start,end,(0,255,0),3)
        cv2.circle(image,far,5,(0,0,255),-1)
    cv2.imshow('image',image)
    cv2.waitKey(0)
