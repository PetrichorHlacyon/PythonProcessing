"""
author : Zelin Yao
date : 2022-8-26
"""
#Goal
"""
SIFT(暂时没有找到有关函数，所以这部分不太完整)
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt

pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH04\\Fig0407(a).tif')
sift = cv2.SIFT()

kp = sift.detect(pic,None)
cv2.drawKeypoints(pic,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('image',pic)
cv2.waitKey(0)