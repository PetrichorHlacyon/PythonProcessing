"""
author : Zelin Yao
date : 2022-8-19
"""
#Goal
"""
1.threshold
2.adaptivethreshold
3.Otsu
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''1.threshold'''
#通过滑动条调节阈值，然后实时显示阈值分割情况
def nothing(x):
    pass

pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
gray = cv2.cvtColor(pic_color,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image')
cv2.createTrackbar('threshold','image',100,255,nothing)
while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    threshold = cv2.getTrackbarPos('threshold','image')
    ret,thres = cv2.threshold(gray,threshold,255,cv2.THRESH_TOZERO)
    # cv2.imshow('image', thres)
    # cv2.waitKey(100)
    # plt.imshow(pic_binary)
    # plt.show()
cv2.destroyAllWindows()

'''2.adaptiveThreshold'''
pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\DIPUM2E_International_Ed_CH10_Images\\Fig1019(d).tif',0)
pic_adap_gaussian = cv2.adaptiveThreshold(pic,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)
pic_adap_mean = cv2.adaptiveThreshold(pic,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)
# cv2.namedWindow('mean',cv2.WINDOW_NORMAL)
# cv2.imshow('mean', pic_adap_mean)
# cv2.namedWindow('guassian',cv2.WINDOW_NORMAL)
# cv2.imshow('guassian', pic_adap_gaussian)
# cv2.waitKey(0)

'''3.Otsu'''
pic = cv2.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\DIPUM2E_International_Ed_CH10_Images\\Fig1019(d).tif',0)
ret1 , pic_otsu = cv2.threshold(pic,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(pic,(5,5),0)
ret2 , pic_otsu_gau = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img = [pic,pic_otsu,blur,pic_otsu_gau]
titles = ['original pic','original pic hist','otsu directly','gaussian blur','blurred pic hist','blur and stsu']
for i in range(2):
    plt.subplot(2,3,3*i+1)
    plt.imshow(img[i*2])
    plt.title(titles[i*3])

    plt.subplot(2,3,3*i+2)
    plt.hist(img[i*2])
    plt.title(titles[i*3+1])

    plt.subplot(2,3,3*i+3)
    plt.imshow(img[i*2+1])
    plt.title(titles[i*3+2])
plt.show()