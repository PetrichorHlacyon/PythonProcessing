"""
author : Zelin Yao
date : 2022-8-25
"""
#Goal
"""
1.单目标
2.多目标

"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''1.单目标'''
# 1.模板匹配
img = cv.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH15\\single_goal\\source.jpg', 0)
template = cv.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH15\\single_goal\\target.jpg', 0)
h, w = template.shape[:2]  # rows->h, cols->w

# 6种匹配方法
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    img2 = img.copy()

    # 匹配方法的真值
    method = eval(meth)
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    # 如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED，取最小值
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 画矩形
    cv.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()


'''2.多目标'''
# 2.匹配多个物体
img_rgb = cv.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH15\\variant_goal\\source.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('D:\\Git\\2=Python\\1=ImgProcessing\\OpenCvLearning\\PicCH15\\variant_goal\\target.jpg', 0)
h, w = template.shape[:2]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
# 取匹配程度大于%80的坐标
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # *号表示可选参数
    bottom_right = (pt[0] + w, pt[1] + h)
    cv.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 2)

cv.imshow('img_rgb', img_rgb)
cv.waitKey(0)
cv.destroyAllWindows()
