"""
author : Zelin Yao
date : 2022-8-23
"""
#Goal
"""
匹配模板图片
【注意】通过drawContours画图时，如果要使得轮廓线条显示为彩色，那么他的第一个参数也应该是个BGR格式，而不是gray
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH12_4\\OriginPic.jpg',0)
image2 = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH12_4\\template.jpg',0)
image = cv2.cvtColor(image1,cv2.COLOR_GRAY2BGR)
ret,origin = cv2.threshold(image1,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
ret,template = cv2.threshold(image2,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

contours1, hirearchs = cv2.findContours(origin,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

contours2, hirearchs = cv2.findContours(template,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]
min_val = 0.5
for i in range(len(contours1)):
    cnt1 = contours1[i]
    match_val = cv2.matchShapes(cnt1,cnt2,1,0.0)
    if match_val < min_val:
        idx = i
        min_val = match_val
print(idx)
cv2.drawContours(image,contours1,idx,(0,255,0),3)
cv2.imshow('image',image)
cv2.waitKey(0)