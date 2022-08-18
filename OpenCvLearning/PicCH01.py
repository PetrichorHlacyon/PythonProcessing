"""
author : Zelin Yao
date : 2022-8-17
"""
#Goal
"""
• 获取像素值并修改
• 获取图像的属性（信息）
• 图像的 ROI（）
• 图像通道的拆分及合并
• 图像扩边
"""

import cv2
import numpy as np

'''• 获取像素值并修改'''
#读入彩色图像
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
#获取第100，100位置的元素的BGR值
print(pic_color[100,100])
#获取该点出的R通道（从0开始索引）
print(pic_color[100,100,2])

#更快捷的一种方法通过内置函数

'''• 图像通道的拆分及合并'''
b,g,r = cv2.split(pic_color)
img = cv2.merge((r,g,b))
cv2.imshow('1',img)

'''• 图像扩边'''
img = cv2.copyMakeBorder(pic_color,60,60,60,60,cv2.BORDER_REFLECT)
cv2.imshow('1',img)
cv2.waitKey(0)