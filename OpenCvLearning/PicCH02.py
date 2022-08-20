import cv2
import matplotlib.pyplot as plt

pic_color1 = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",0)
pic_color2 = cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0617(a).tif",0)
pic_color2 = pic_color2[0:600,0:600]
#创建幻灯片用来演示一张图如何到另一张图
cv2.namedWindow('dst')
for i in range(100):
    alpha = i*1/100
    img = cv2.addWeighted(pic_color1,alpha,pic_color2,1-alpha,0)
    cv2.imshow('dst',img)
    cv2.waitKey(100)