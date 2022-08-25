"""
author : Zelin Yao
date : 2022-8-25
"""
#Goal
"""


"""
from posixpath import split
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH13_4\\color_ball.png',1)

hsv_pic = cv2.cvtColor(pic,cv2.COLOR_BGR2HSV)
pic_target = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH13_4\\target.jpg',1)
hsv_target = cv2.cvtColor(pic_target,cv2.COLOR_BGR2HSV)

hist_target = cv2.calcHist([hsv_target],[0,1],None,[180,256],[0,180,0,256])
cv2.normalize(hist_target,hist_target,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsv_pic],[0,1],hist_target,[0,180,0,256],1)

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_dst=cv2.filter2D(dst,-1,disc)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('gray value','image',100,255,nothing)
while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    gray_value = cv2.getTrackbarPos('gray value','image')
    ret,thresh = cv2.threshold(img_dst,gray_value,255,cv2.THRESH_BINARY)
    #三通道对三通道，单通道对单通道与运算
    thresh = cv2.merge((thresh,thresh,thresh))
    img_merge = cv2.bitwise_and(pic,thresh)
    img = np.hstack((pic,img_merge))
    cv2.imshow('image',img)
    cv2.waitKey(10)
cv2.destroyAllWindows()
