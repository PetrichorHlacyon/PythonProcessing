"""
author : Zelin Yao
date : 2022-8-21
"""
#Goal
"""
1.gauss pyramid
2.laplace pyramid
2.1 pic combination
"""

from random import gauss
import cv2
import numpy as np
import matplotlib.pyplot as plt


'''1.gauss pyramid'''
#高斯金字塔
image = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH06\\Fig0612(a).tif", 1)
up = cv2.pyrUp(image)
up_down = cv2.pyrDown(up)
down = cv2.pyrDown(image)
down_up = cv2.pyrUp(down)

# cv2.imshow('image', image)
# cv2.imshow('up', up)
# cv2.imshow('up_down', up_down)
# cv2.imshow('down', down)
# cv2.imshow('down_up', down_up)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''2.laplace pyramid'''
#拉普拉斯金字塔
image = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH06\\Fig0612(a).tif", 1)
down1 = cv2.pyrDown(image)
down2 = cv2.pyrDown(down1)
lap1 = image - cv2.pyrUp(down1)
lap2 = down1 - cv2.pyrUp(down2)

# plt.figure(0)
# plt.subplot(231), plt.imshow(image, 'gray'), plt.title('image'), plt.axis('off')
# plt.subplot(232), plt.imshow(down1, 'gray'), plt.title('down1'), plt.axis('off')  # 为了效果明显 我们选用第3层高斯
# plt.subplot(233), plt.imshow(down2, 'gray'), plt.title('down2'), plt.axis('off')  # 如果我们直接上采样
# plt.subplot(234), plt.imshow(image, 'gray'), plt.title('image'), plt.axis('off')
# plt.subplot(235), plt.imshow(lap1, 'gray'), plt.title('lap1'), plt.axis('off')
# plt.subplot(236), plt.imshow(lap2, 'gray'), plt.title('lap2'), plt.axis('off')

# #用拉普拉斯金字塔对图像复原
# plt.figure(1)
# rep = lap1 + cv2.pyrUp(lap2 + cv2.pyrUp(down2))
# plt.subplot(121), plt.imshow(image, 'gray'), plt.title('image'), plt.axis('off')
# plt.subplot(122), plt.imshow(rep, 'gray'), plt.title('LapToRestore'), plt.axis('off')

# plt.show()

'''2.1 pic combination'''
org = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\2.orange.jpg',1)
apple = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\1.apple.jpg',1)

#得出苹果橘子的高斯金字塔
O = org.copy()
gauss_pyr_org = [O]
A = apple.copy()
gauss_pyr_apple = [A]


for i in range(6):
    O = cv2.pyrDown(O)
    gauss_pyr_org.append(O)
#7个
for i in range(6):
    A = cv2.pyrDown(A)
    gauss_pyr_apple.append(A)
#--------------------------
#得出对应的拉普拉斯金字塔
lap_pyr_org = [gauss_pyr_org[6]]
lap_pyr_apple = [gauss_pyr_apple[6]]
# lap_pyr_org = []
# lap_pyr_apple = []
for i in range(6,0,-1): #不用计算原图
    temp = cv2.subtract(gauss_pyr_org[i-1] , cv2.pyrUp(gauss_pyr_org[i]))
    lap_pyr_org.append(temp)
for i in range(6,0,-1):
    temp = cv2.subtract(gauss_pyr_apple[i-1] , cv2.pyrUp(gauss_pyr_apple[i]))
    lap_pyr_apple.append(temp)
#---------------------------
#将拉普拉斯金字塔进行融合
laplace_comb = []
for o,a in zip(lap_pyr_org,lap_pyr_apple):
    rows,cols,channels = o.shape
    temp = np.hstack((a[:,0:cols//2],o[:,cols//2:]))
    laplace_comb.append(temp)

recovery = laplace_comb[0]
for i in range(1,7):
    recovery = cv2.pyrUp(recovery)
    #用opencv操作，不要用+，因为+越界是循环，会导致某些值不正常
    recovery = cv2.add(np.array(laplace_comb[i]) , recovery)
cv2.namedWindow('org',cv2.WINDOW_NORMAL)
cv2.imshow('org',org)
cv2.namedWindow('apple',cv2.WINDOW_NORMAL)
cv2.imshow('apple',apple)
cv2.namedWindow('combined',cv2.WINDOW_NORMAL)
cv2.imshow('combined',recovery)

cv2.waitKey(0)
