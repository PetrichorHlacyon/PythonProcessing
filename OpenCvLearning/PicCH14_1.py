"""
author : Zelin Yao
date : 2022-8-25
"""
#Goal
"""
1.使用numpy进行频率域的滤波与重建
2.使用opencv进行频率域的滤波与重建

opencv的dft函数比numpy更快
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

pic = cv2.imread('D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif',0)
#use opencv to dft and fftshift
dft = cv2.dft(np.float32(pic),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#create mask
rows,cols = dft.shape[0:2]
mask = np.ones((rows,cols,2),np.uint8)
center_row = np.floor(rows/2)
center_col = np.floor(cols/2)
center_row = int(center_row)
center_col = int(center_col)
mask[center_col-3:center_col+3,:,:] = 0
mask[:,center_row-3:center_row+3,:] = 0
#use mask to deal with shiftted matrix
f_shift = dft_shift*mask
#ifftshift and idft
f_ishift = np.fft.ifftshift(f_shift)
back_img = cv2.idft(f_ishift)
img = cv2.magnitude(back_img[:,:,0],back_img[:,:,1])

plt.imshow(img,cmap='gray')
plt.show()