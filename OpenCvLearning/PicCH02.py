"""
author : Zelin Yao
date : 2022-8-28
"""
#Goal
"""
图像运算：加法，减法，图像混合（addweighted
其中加法多用cv2.add(),他对于超过最大值255的处理方式是保持，而x+y是循环从1开始
减法多用cv2.subtract()
"""
import cv2
import matplotlib.pyplot as plt

pic_color1 = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
pic_color2 = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0617(a).tif",1)
pic_color2 = pic_color2[0:600,0:600]
#创建幻灯片用来演示一张图如何到另一张图
cv2.namedWindow('dst')
for i in range(100):
    alpha = i*1/100
    img = cv2.addWeighted(pic_color1,alpha,pic_color2,1-alpha,0)
    cv2.imshow('dst',img)
    cv2.waitKey(100)