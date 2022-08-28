"""
author : Zelin Yao
date : 2022-8-26
"""
#Goal
"""
1.Harris 角点检测
2.subPix 修正

"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt

'''1.Harris 角点检测'''
pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH10\\Fig1006(a).tif')
gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.05)
#设置阈值
pic[dst > 0.1*dst.max()] = (0,0,255)
cv2.imshow('pic',pic)
cv2.waitKey(0)

'''2.subPix 修正'''
pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH04\\Fig0407(a).tif')
gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.05)
#阈值处理
ret,dst = cv2.threshold(dst,0.1*dst.max(),255,cv2.THRESH_BINARY)
dst = np.uint8(dst)
ret,labels,stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
corners = np.uint0(corners)
centroids = np.uint0(centroids)
pic[corners[:,0],corners[:,1]] = [0,255,0]
pic[centroids[:,0],centroids[:,1]] = [0,0,255]
plt.imshow(pic)
plt.show()