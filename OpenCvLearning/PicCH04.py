"""
author : Zelin Yao
date : 2022-8-17
"""
#Goal
"""
• 检测程序的效率
• 一些能够提高程序效率的技巧
• 你要学到的函数有：cv2.getTickCount,cv2.getTickFrequency
等
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#查看所有flag，颜色转换方式
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]


#cvtcolor
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
pic_hsv = cv2.cvtColor(pic_color,cv2.COLOR_BGR2HSV)
pic_gray = cv2.cvtColor(pic_color,cv2.COLOR_BGR2GRAY)
# cv2.imshow('original pic',pic_color)
# cv2.imshow('hsv pic',pic_hsv)
# cv2.imshow('gray pic',pic_gray)


#Object Tracking based on HSV
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0617(a).tif",1)
pic_hsv = cv2.cvtColor(pic_color,cv2.COLOR_BGR2HSV)
low_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(pic_hsv,low_blue,upper_blue)
res = cv2.bitwise_and(pic_color,pic_color,mask = mask)
# cv2.imshow('hsv',pic_hsv)
# cv2.imshow('mask',mask)
# cv2.imshow('res',res)
# cv2.waitKey(0)

#again Object Tracking
#Little Skill: use RGB to get HSV, 从而得到对应的纯色RGB对应的HSV
pic_color = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\object_tracking_test.jpg",1)
pic_hsv = cv2.cvtColor(pic_color,cv2.COLOR_BGR2HSV)
blue_bgr = np.uint8([[[255,0,0]]])
blue_hsv = cv2.cvtColor(blue_bgr,cv2.COLOR_BGR2HSV)
print(blue_hsv)

low_blue = np.array([120,100,100])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(pic_hsv,low_blue,upper_blue)
res = cv2.bitwise_and(pic_color,pic_color,mask = mask)
cv2.imshow('hsv',pic_hsv)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)