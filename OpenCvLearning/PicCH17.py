"""
author : Zelin Yao
date : 2022-8-26
"""
#Goal
"""
分水岭算法
1.提取确定的foreground,background,unknown field
2.标记
3.进行分水岭算法
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
pic_color = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH17\\core.jpg',1)
gray = cv2.cvtColor(pic_color,cv2.COLOR_BGR2GRAY)
ret,binarization = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

opening = cv2.morphologyEx(binarization,cv2.MORPH_OPEN,kernel,iterations = 2)
#确定的前景foreground
#1.use 形态学处理
# sure_fg = cv2.erode(opening,kernel,iterations=2)
# sure_bg = cv2.dilate(opening,kernel,iterations=2)
# unknown = cv2.subtract(sure_bg,sure_fg)
# cv2.imshow('unknown',unknown)
# cv2.waitKey(0)
#2.use 距离变换
sure_bg = cv2.dilate(opening,kernel,iterations=2)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L1,3)
cv2.normalize(dist_transform,dist_transform,0,1,cv2.NORM_MINMAX)

# Finding sure foreground area
ret, sure_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

#marking
numb_label,labels = cv2.connectedComponents(sure_fg)
#吧已经确定的背景标记为1
labels = labels + 1
#unknown里面的变成0
labels[unknown == 255] = 0 
#int32->uint8(仅仅只是为了显示才转化的)
# labels = np.uint8(labels)

#分水岭算法（返回的markers中轮廓被标记为-1）
markers = cv2.watershed(pic_color,labels)
pic_color[markers == -1] = [0,255,0]
cv2.imshow('labels',pic_color)
cv2.waitKey(0)