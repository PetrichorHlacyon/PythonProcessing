#-*- coding : UTF-8 -*-
import cv2
import numpy as np

#通过滑块设置画笔颜色，然后画图

# 创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,pen_color
    # 当按下左键是返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img1,(ix,iy),(x,y),pen_color,-1)
            else:# 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
                cv2.circle(img1,(x,y),3,pen_color,-1) # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)
# 当鼠标松开停止绘画。
    elif event==cv2.EVENT_LBUTTONUP:
        drawing==False
# if mode==True:
# cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
# else:
# cv2.circle(img,(x,y),5,(0,0,255),-1)
def nothing(x):
    # print(x)
    pass


drawing = False
# 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。
mode = True
ix, iy = -1, -1
pen_color = (0, 0, 0)
s_name = '0:off\n1:on'
img = np.zeros((300, 512, 3), np.uint8)
img1 = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar(s_name, 'image', 0, 1, nothing)
while True:
    #-----------这里的waitkey(1)是重点，如果是0就会一直等导致结果出来不了-----------------------------
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    #----------------------------------------
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(s_name, 'image')
    if s == 0:
        pen_color = 0
        img[:] = 0
    else:
        pen_color = [b, g, r]
        img[:] = pen_color

    cv2.imshow('image', img1)
    cv2.setMouseCallback('image', draw_circle)
cv2.destroyAllWindows()
