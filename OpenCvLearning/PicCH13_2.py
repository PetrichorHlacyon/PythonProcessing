"""
author : Zelin Yao
date : 2022-8-24
"""
#Goal
"""

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''1.统计直方图'''
pic = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",0)
local_prossed_pic = cv2.createCLAHE(clipLimit = 2.0,tileGridSize=(8,8))
local_prossed_pic = local_prossed_pic.apply(pic)
# pic_all = np.hstack((pic,local_prossed_pic))
plt.subplot(221)
plt.imshow(pic,'gray')
plt.subplot(222)
hist1 = cv2.calcHist([pic],[0],None,[256],[0,256])
plt.plot(hist1,color='g')
plt.subplot(223)
plt.imshow(local_prossed_pic,'gray')
plt.subplot(224)
hist2 = cv2.calcHist([local_prossed_pic],[0],None,[256],[0,256])
plt.plot(hist2,color='r')

plt.show()