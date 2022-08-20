"""
author : Zelin Yao
date : 2022-8-20
"""
#Goal
"""

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''sobel,scharr,laplacian'''
img = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH04\\Fig0407(a).tif")
ret,img_binarization = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
sobel_x = cv2.Sobel(img_binarization,-1,1,0,ksize=1)
sobel_y = cv2.Sobel(img_binarization,-1,0,1,ksize=1)
scharr_x = cv2.Sobel(img_binarization,-1,1,0,ksize = -1)
scharr_y = cv2.Sobel(img_binarization,-1,0,1,ksize = -1)
laplacian = cv2.Laplacian(img_binarization,-1)
# plt.subplot(231)
# plt.imshow(img)
# plt.title('original')
# plt.subplot(232)
# plt.imshow(sobel_x)
# plt.title('sobel_x')
# plt.subplot(233)
# plt.imshow(sobel_y)
# plt.title('sobel_y')
# plt.subplot(234)
# plt.imshow(scharr_x)
# plt.title('scharr_x')
# plt.subplot(235)
# plt.imshow(scharr_y)
# plt.title('scharr_y')
# plt.subplot(236)
# plt.imshow(laplacian)
# plt.title('laplacian')
# plt.show()

'''2.数据类型对边界截取的影响实验'''
img = cv2.imread("D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\ImgSet\\CH04\\Fig0418(a).tif")
ret,img_binarization = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
sobel_x_8U = cv2.Sobel(img_binarization,cv2.CV_8U,1,0,ksize=5)
sobel_y_8U = cv2.Sobel(img_binarization,cv2.CV_8U,0,1,ksize=5)

sobel_x_16S = cv2.Sobel(img_binarization,cv2.CV_16S,1,0,ksize=5)
sobel_y_16S = cv2.Sobel(img_binarization,cv2.CV_16S,0,1,ksize=5)
abs_sobel_x_16S = np.absolute(sobel_x_16S)
abs_sobel_y_16S = np.absolute(sobel_y_16S)
U8_abs_sobel_x_16S = np.uint8(abs_sobel_x_16S)
U8_abs_sobel_y_16S = np.uint8(abs_sobel_y_16S)

plt.subplot(231)
plt.imshow(img)
plt.title('original')
plt.subplot(232)
plt.imshow(sobel_x_8U)
plt.title('sobel_x_8U')
plt.subplot(233)
plt.imshow(sobel_y_8U)
plt.title('sobel_y_8U')
plt.subplot(234)
plt.imshow(img)
plt.title('original')
plt.subplot(235)
plt.imshow(U8_abs_sobel_x_16S)
plt.title('U8_abs_sobel_x_16S')
plt.subplot(236)
plt.imshow(U8_abs_sobel_y_16S)
plt.title('U8_abs_sobel_y_16S')
plt.show()