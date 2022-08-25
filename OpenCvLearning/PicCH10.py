"""
author : Zelin Yao
date : 2022-8-20
"""
#Goal
"""
Canny
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
    pass

img = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH06\\Fig0612(a).tif",0)

cv2.namedWindow('image')
cv2.createTrackbar('minVal','image',100,255,nothing)
cv2.createTrackbar('maxVal','image',200,255,nothing)
while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
    min_val = cv2.getTrackbarPos('minVal','image')
    max_val = cv2.getTrackbarPos('maxVal','image')
    img_edge = cv2.Canny(img,min_val,max_val)
    # plt.subplot(122)
    # plt.imshow(img_edge,cmap = 'gray')
    cv2.imshow('image',img_edge)
    cv2.waitKey(100)
cv2.destroyAllWindows()