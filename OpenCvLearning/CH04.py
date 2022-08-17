"""
Created on Sun Jan 5 11:31:53 2014
@author: duan
"""
import cv2
import numpy as np
#----------------------------鼠标回调----------------------------------------
#mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDBLCLK: #双击
#         cv2.circle(img,(x,y),2,(255,0,0),-1) # 创建图像与窗口并将窗口与回调函数绑定
#     elif event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),2,(0,255,0),-1)

# #查看所有鼠标相关的事件
# events=[i for i in dir(cv2) if 'EVENT'in i]
# print(events)

# img=cv2.imread("D:\\1=code_store\\2-1=PythonOpenCvLearning\\ImgSet\\CH06\\Fig0604(a).tif",1)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20)&0xFF==27:
#         break
# cv2.destroyAllWindows()

# # 当鼠标按下时变为 True
# drawing=False
# # 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。
# mode=True
# ix,iy=-1,-1 
# # 创建回调函数
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode
#     # 当按下左键是返回起始位置坐标
#     if event==cv2.EVENT_LBUTTONDOWN:
#         drawing=True
#         ix,iy=x,y
#     # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
#     elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
#         if drawing==True:
#             if mode==True:
#                 cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:# 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
#                 cv2.circle(img,(x,y),3,(0,0,255),-1) # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
#                 # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
#                 # cv2.circle(img,(x,y),r,(0,0,255),-1)
# # 当鼠标松开停止绘画。
#     elif event==cv2.EVENT_LBUTTONUP:
#         drawing==False
# # if mode==True:
# # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
# # else:
# # cv2.circle(img,(x,y),5,(0,0,255),-1)

# img=np.zeros((512,512,3),np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# while(1):
#     cv2.imshow('image',img)
#     k=cv2.waitKey(1)&0xFF
#     if k==ord('m'):
#         mode=not mode
#     elif k==27:
#         break
#----------------------------------------------------------------------------
#---------------------------滑动条--------------------------------------------
def nothing(x):
    # print(x)
    pass
s_name = '0:off\n1:on'
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar(s_name,'image',0,1,nothing)
while True:
    cv2.imshow('imgae',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(s_name,'image')
    if s == 0:
        img[:] = 0
    else :
        img[:] = [b,g,r]
cv2.destroyAllWindows()
