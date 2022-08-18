"""
author : Zelin Yao
date : 2022-8-17
"""
#Goal
"""
• 检测程序的效率
• 一些能够提高程序效率的技巧
• 你要学到的函数有：cv2.getTickCount,cv2.getTickFrequency
等
"""

import cv2
import numpy as np
import time

'''• 检测程序的效率'''
#getTickCount,getTickFrequency
#算出的还要除以频率才能得到时间，以秒为单位
img1 = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",0)
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)
#time.time()
img2 = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",0)
time1 = time.time()
for i in range(5,49,2):
    img2 = cv2.medianBlur(img2,i)
time2 = time.time()
t = time2-time1
print(t)
#查看是否开启优化，和开启和关闭优化
print(cv2.useOptimized())
#比较
img1 = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",0)
time1 = time.time()
for i in range(10000):
    cv2.countNonZero(img1)
time2 = time.time()
t = time2-time1
print('opencv',t)
time1 = time.time()
for i in range(10000):
    np.count_nonzero(img1)
time2 = time.time()
t = time2-time1
print('numpy',t)