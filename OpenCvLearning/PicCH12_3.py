"""
author : Zelin Yao
date : 2022-8-23
"""
#Goal
"""
将图片上的点绘制成不同颜色，颜色根据点到轮廓的距离计算
【重点】理解opencv图片的储存方式，shape的第一个是行，第二个是列，第三个是维度
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

image = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH10\\Fig1015(a)[noiseless].tif")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(image.shape)
cv2.namedWindow('image')
cv2.createTrackbar('threshold','image',150,255,nothing)
while True:
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
    threshold = cv2.getTrackbarPos('threshold','image')
    ret , img_binary = cv2.threshold(gray,threshold,255,cv2.THRESH_BINARY)
    contours , hierarchy = cv2.findContours(img_binary , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            dist = cv2.pointPolygonTest(cnt,(j,i),True)
            if dist < 0:
                image[i,j] = (-dist % 255,100,100)
            elif dist > 0:
                image[i,j] = (100,dist % 255,100)
    cv2.imshow('image',image)
    cv2.waitKey(100)
