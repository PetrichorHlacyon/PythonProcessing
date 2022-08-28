"""
author : Zelin Yao
date : 2022-8-20
"""
#Goal
"""
1.filter2D
【*】这里kernel取float32或者float64类型
2.1 blur and boxFilter
2.2 guassian
2.3 median blur
2.4 bilatera
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''1.filter2D'''
kernel = np.ones((5,5),np.float32)/25

pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
pic_filter = cv2.filter2D(pic_color,-1,kernel)
images = [pic_color,pic_filter]
titles = ['original','low pass filtered']
# for i in range(2):
#     plt.subplot(1,2,i+1)
#     plt.imshow(images[i])
#     plt.title(titles[i])
# plt.show()

'''2.1 blur and boxFilter'''
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
pic_boxfilter = cv2.boxFilter(pic_color,-1,(5,5))
# cv2.imshow('boxFilter',pic_boxfilter)
# cv2.waitKey(0)

'''2.2 gaussian'''
#直接使用
pic_gau = cv2.GaussianBlur(pic_color,(9,9),0)
#自己构造高斯核
kernel_gau = cv2.getGaussianKernel(6,0)
pic_gau2 = cv2.filter2D(pic_color,-1,kernel_gau)
# cv2.imshow('gaussian',pic_gau)
# cv2.imshow('gaussian_kernel',pic_gau2)
# cv2.waitKey(0)

'''2.3medianBlur'''
pic_median = cv2.medianBlur(pic_color,7)
# cv2.imshow('median',pic_median)
# cv2.waitKey(0)

'''2.4bilateralFilter'''
pic_bilater = cv2.bilateralFilter(pic_color,9,101,101)
plt.subplot(131)
plt.imshow(pic_color)
plt.title('original')
plt.subplot(132)
plt.imshow(pic_gau)
plt.title('gaussian')
plt.subplot(133)
plt.imshow(pic_bilater)
plt.title('bilateral')
plt.show()


