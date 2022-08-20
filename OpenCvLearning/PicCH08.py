"""
author : Zelin Yao
date : 2022-8-20
"""
#Goal
"""
1.erosion and dilation
2.open and close
3.gradient
4.tophat and blackhat
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''1.erosion and dilation'''
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH09\\Fig0910(a).tif")
erosion = cv2.erode(img,kernel,iterations=1)
dilation = cv2.dilate(img,kernel,iterations=1)
# plt.subplot(131)
# plt.imshow(img)
# plt.title('original')
# plt.subplot(132)
# plt.imshow(erosion)
# plt.title('erosion')
# plt.subplot(133)
# plt.imshow(dilation)
# plt.title('dilation')
# plt.show()

'''2.open and close'''
kernel = np.ones((55,55),np.uint8)
img = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH09\\Fig0910(a).tif")
opened = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closed = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# plt.subplot(131)
# plt.imshow(img)
# plt.title('original')
# plt.subplot(132)
# plt.imshow(opened)
# plt.title('opened')
# plt.subplot(133)
# plt.imshow(closed)
# plt.title('closed')
# plt.show()

'''3.gradient'''
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH09\\Fig0910(a).tif")
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# plt.subplot(121)
# plt.imshow(img)
# plt.title('original')
# plt.subplot(122)
# plt.imshow(gradient)
# plt.title('gradient')
# plt.show()

'''4.tophat and blackhat'''
kernel = np.ones((55,55),np.uint8)
img = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH09\\Fig0910(a).tif")
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
plt.subplot(131)
plt.imshow(img)
plt.title('original')
plt.subplot(132)
plt.imshow(tophat)
plt.title('tophat')
plt.subplot(133)
plt.imshow(blackhat)
plt.title('blackhat')
plt.show()