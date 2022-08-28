"""
author : Zelin Yao
date : 2022-8-22
"""
#Goal
"""
1.轮廓查找和绘制
(默认white为foreground,black为background)
2.轮廓特征
3.轮廓性质

"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

'''1.轮廓查找和绘制'''
def nothing(x):
    pass
image = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH10\\Fig1015(a)[noiseless].tif")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gray = image
# cv2.namedWindow('image')
# cv2.createTrackbar('threshold','image',150,255,nothing)
# while True:
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#     threshold = cv2.getTrackbarPos('threshold','image')
#     ret , img_binary = cv2.threshold(gray,threshold,255,cv2.THRESH_BINARY)
#     contours , hierarchy = cv2.findContours(img_binary , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
#     cv2.drawContours(image,contours,-1,(0,255,0),3)
#     cv2.imshow('image',image)
#     cv2.waitKey(100)

'''2.轮廓特征'''
#2.1moments(cal 重心并绘制)
image = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH10\\Fig1015(a)[noiseless].tif")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image')
cv2.createTrackbar('threshold','image',150,255,nothing)
threshold = cv2.getTrackbarPos('threshold','image')
ret , img_binary = cv2.threshold(gray,threshold,255,cv2.THRESH_BINARY)
contours , hierarchy = cv2.findContours(img_binary , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
M = cv2.moments(contours[0])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
# cv2.drawContours(image,contours,-1,(0,255,0),3)
# cv2.circle(image,(cx,cy),2,(0,0,255),2)
# cv2.imshow('image',image)

#2.2轮廓面积
S1 = cv2.contourArea(contours[0])
S2 = M['m00']
print('S1=',S1)
print('S2=',S2)

#2.3Length
C1 = cv2.arcLength(contours[0],True)
print('C1=',C1)

#2.4 contour approximate
approx = cv2.approxPolyDP(contours[0],0.01*C1,True)
temp = approx.reshape((-1,1,2))
# cv2.polylines(image,[approx],True,(0,0,255),2)
# cv2.imshow('image',image)
# cv2.waitKey(0)

#2.5 convexHull
hull = cv2.convexHull(contours[0],clockwise=True,returnPoints=True)
# print(hull)
# cv2.polylines(image,[hull],True,(0,0,255),2)
# cv2.imshow('image',image)
# cv2.waitKey(0)

#2.6 detection of convexity
k = cv2.isContourConvex(contours[0])
print(k)

#2.7 boundingRect
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int64(box)
# cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
# cv2.drawContours(image,[box],-1,(0,0,255),2)
# cv2.imshow('image',image)
# cv2.waitKey(0)

#2.8 and 2.9
(x,y),radius = cv2.minEnclosingCircle(cnt)
cv2.circle(image,(np.int0(x),np.int0(y)),np.int0(radius),(255,0,0),2)
ellipse = cv2.fitEllipse(cnt)
# print(ellipse)
# cv2.ellipse(image,ellipse,(0,0,255),2)
# cv2.imshow('image',image)
# cv2.waitKey(0)

'''3.轮廓性质'''
#pole 
left_most = cnt[cnt[:,:,0].argmin()][0]
right_most = cnt[cnt[:,:,0].argmax()][0]
up_most = cnt[cnt[:,:,1].argmin()][0]
dowm_most = cnt[cnt[:,:,1].argmax()][0]
cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.circle(image,left_most,2,(0,0,255),2)
cv2.circle(image,right_most,2,(0,0,255),2)
cv2.circle(image,up_most,2,(0,0,255),2)
cv2.circle(image,dowm_most,2,(0,0,255),2)
cv2.imshow('image',image)
cv2.waitKey(0)