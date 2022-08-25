"""
author : Zelin Yao
date : 2022-8-24
"""
#Goal
"""
1.统计直方图
2.绘制直方图
3. learn to use mask
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''1.统计直方图'''
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
hist = cv2.calcHist([pic_color],[0],None,[256],[0,256])


'''2.绘制直方图'''
#matplotlib函数
plt.hist(pic_color.ravel(),256,[0,256])
plt.show()
#opencv
color = ['b','g','r']
for i , col in enumerate(color):
    hist = cv2.calcHist([pic_color],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()

'''3. learn to use mask'''
pic = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",0)
mask  = np.zeros(pic.shape[0:2],np.uint8)
mask[100:300,100:400] = 255
masked_pic = cv2.bitwise_and(pic,pic,mask=mask)

hist1 = cv2.calcHist([pic],[0],None,[256],[0,256])
hist2 = cv2.calcHist([pic],[0],mask,[256],[0,256])
plt.subplot(1,3,1)
plt.imshow(pic,'gray')
plt.subplot(1,3,2)
plt.imshow(masked_pic,'gray')
plt.subplot(1,3,3)
plt.plot(hist1,color='b')
plt.plot(hist2,color='g')
plt.xlim([0,256])
plt.show()