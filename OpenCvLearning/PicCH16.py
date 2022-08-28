"""
author : Zelin Yao
date : 2022-8-26
"""
#Goal
"""
1. Hough line
2.probabilistic Hough line
3.Hough circle
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt

'''1. Hough line'''
# pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH15\\variant_goal\\source.jpg')
# gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
# edge = cv2.Canny(gray,50,150)
# lines = cv2.HoughLines(edge,1,np.pi/180,150)
# print(lines[:,0,:])
# #lines转换为二维数组才能够像下面这样操作
# #python基础不牢
# for rho,theta in lines[:,0,:]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv2.line(pic,(x1,y1),(x2,y2),(0,0,255),2)
# cv2.imshow('pic',pic)
# cv2.waitKey(0)

'''2.probabilistic Hough line'''
# def nothing(x):
#     pass
# pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH15\\variant_goal\\source.jpg')
# gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.createTrackbar('min val','image',100,255,nothing)
# cv2.createTrackbar('max val','image',150,255,nothing)
# while True:
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     min_val = cv2.getTrackbarPos('min val','image')
#     max_val = cv2.getTrackbarPos('max val','image')
#     edge = cv2.Canny(gray,min_val,max_val)
#     lines = cv2.HoughLinesP(edge,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
#     for x1,y1,x2,y2 in lines[:,0,:]:
#         cv2.line(pic,(x1,y1),(x2,y2),(0,0,255),3)
#     cv2.imshow('image',pic)

'''3.Hough circle'''
pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH09\\Fig0925(a).tif')
gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,150,30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
print(circles)
for x,y,radius in circles[0,:,:]:
    cv2.circle(pic,(x,y),radius,(0,0,255),3)
    cv2.circle(pic,(x,y),2,(0,255,0),3)
cv2.imshow('pic',pic)
cv2.waitKey(0)