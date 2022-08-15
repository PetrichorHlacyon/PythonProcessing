import cv2
import numpy as np
import matplotlib as plt

#显示当前opencv版本
print(cv2.__version__)

#小任务
#加载一个灰度图，显示图片，按下“s”保存并退出，按下ESC退出不保存

print(bin(-1))
cv2.namedWindow('Test input and show pic',cv2.WINDOW_NORMAL )
#加载灰度图
gray = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",cv2.IMREAD_GRAYSCALE)
cv2.imshow('Test input and show pic',gray)
if cv2.waitKey(0) & 0xFF== ord('s'):
    cv2.destroyWindow("Test input and show pic")
    cv2.imwrite('gray.png',gray)
elif cv2.waitKey(0) & 0xFF== 27:
    cv2.destroyWindow("Test input and show pic")
print(ord(-1))


