"""
author : Zelin Yao
date : 2022-8-24
"""
#Goal
"""
通过摄像头读入图像进行实时彩色二位直方图（自己构建二维色图）显示

"""
from posixpath import split
import cv2
import numpy as np
import matplotlib.pyplot as plt
# from time import clock
import time
import sys

# pic = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
# b,g,r = cv2.split(pic)
# hsv = cv2.cvtColor(pic,cv2.COLOR_BGR2HSV)
# hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
# plt.subplot(121)
# plt.imshow(cv2.merge([r,g,b]))
# plt.subplot(122)
# plt.imshow(hist,interpolation='nearest')
# plt.show()

if __name__ == '__main__':
    #---------------根据不同的位置构建hsv彩色map-----------------------
    hsv_map = np.zeros((180,256,3),np.uint8)
    h,s = np.indices(hsv_map.shape[:2])
    hsv_map[:,:,0] = h
    hsv_map[:,:,1] = s
    hsv_map[:,:,2] = 255
    hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)
    cv2.imshow('hsv_map', hsv_map)

    cv2.namedWindow('hist',0)
    hist_scale = 10
    def set_scale(val):
        global hist_scale
        hist_scale = val
    cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

    try:fn = sys.argv[1]
    except:fn = 0
    cam = cv2.VideoCapture(0)
    while(True):
        flag,frame = cam.read()
        cv2.imshow('camera', frame)
        small = cv2.pyrDown(frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dark = hsv[:,:,2]<32
        hsv[dark] = 0
        h = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0,256])
        h = np.clip(h*0.005*hist_scale, 0, 1)
        vis = hsv_map*h[:,:,np.newaxis] / 255.0
        cv2.imshow('hist', vis)

        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break
    cv2.destroyAllWindows()