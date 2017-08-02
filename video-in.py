#-*- coding: UTF-8 -*-
__author__ = "xiongzongyang"

#将视频截帧

import cv2

vc = cv2.VideoCapture("4.mp4")  # 读入视频文件
c = 1

if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    print "视频未能正常打开"
    rval = False
#test size of the video
size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print 'size:' + repr(size)
timeF = 50  # 视频帧计数间隔频率
i=1
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (c % timeF == 0):  # 每隔timeF帧进行存储操作
        cv2.imwrite('image/445-2/image' + str(i) + '.jpg', frame)  # 存储为图像
        i=i+1
        print c
    c = c + 1
    cv2.waitKey(1)
vc.release()

