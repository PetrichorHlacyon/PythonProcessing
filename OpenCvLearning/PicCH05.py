"""
author : Zelin Yao
date : 2022-8-19
"""
#Goal
"""
• 扩展缩放
• 平移
• 旋转
• 仿射
• 透视
"""

from multiprocessing.connection import wait
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math 
'''• 扩展缩放'''
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
pic_large = cv2.resize(pic_color,None,fx=2,fy=3,interpolation=cv2.INTER_CUBIC)
pic_width = pic_color.shape[0:1]
pic_height = pic_color.shape[1:2]

#-------------------TypeError:can't multiply sequence by non-int of type 'float'----------------------
# pic_small = cv2.resize(pic_color,(int(0.5*pic_width),int(0.5*pic_height)),interpolation=cv2.INTER_AREA)
#-----------------------------------------------------------------------------------------------------

pic_small = cv2.resize(pic_color,None,fx= 0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# cv2.imshow('large',pic_large)
# cv2.imshow('small',pic_small)
# cv2.waitKey(0)

'''• 平移'''
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
mat_shift = np.float32([[1,0,100],[0,1,30]])
pic_shift = cv2.warpAffine(pic_color,mat_shift,(500,1000))
# cv2.imshow('shift',pic_shift)
# cv2.waitKey(0)

'''• 旋转'''
pic_color = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
pic_height = pic_color.shape[0:1]
pic_width = pic_color.shape[1:2]
mat_rotation = cv2.getRotationMatrix2D((pic_width[0]/2,pic_height[0]/2),37,1)
pic_rotated = cv2.warpAffine(pic_color,mat_rotation,(500,600))
# cv2.imshow('rotated',pic_rotated)
# cv2.waitKey(0)

'''• 仿射'''
pic = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH04\\Fig0407(a).tif",0)
pst1 = np.float32([[50,50],[200,50],[50,200]])
pst2 = np.float32([[10,100],[200,50],[100,250]])
mat_affine = cv2.getAffineTransform(pst1,pst2)
pic_affined = cv2.warpAffine(pic,mat_affine,(1000,1200))
# cv2.imshow('affined',pic_affined)
# cv2.waitKey(0)

'''• 透视'''
pic = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH04\\Fig0407(a).tif",0)
pst1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pst2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
mat_pers = cv2.getPerspectiveTransform(pst1,pst2)
pic_pers = cv2.warpPerspective(pic,mat_pers,(1000,1200))
cv2.imshow('affined',pic_pers)
cv2.waitKey(0)