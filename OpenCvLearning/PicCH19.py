"""
author : Zelin Yao
date : 2022-8-26
"""
#Goal
"""
亚像素级精度角点检查

"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt

pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH04\\Fig0407(a).tif')
gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,0,0.01,10)
corners = np.int0(corners)
for x,y in corners[:,0,:]:
    cv2.circle(pic,(x,y),3,(0,255,0),3)
cv2.imshow('pic',pic)
cv2.waitKey(0)