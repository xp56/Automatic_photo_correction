# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 00:11:57 2018

@author: XP
"""

import cv2
from math import *
import numpy as np

img = cv2.imread("C:/Users/XP/Pictures/test.jpg")

height,width=img.shape[:2]

degree=-7.96039409

#旋转后的尺寸
heightNew=int(width*fabs(sin(radians(degree)))+height*fabs(cos(radians(degree))))
widthNew=int(height*fabs(sin(radians(degree)))+width*fabs(cos(radians(degree))))

matRotation=cv2.getRotationMatrix2D((width/2,height/2),degree,1)

#matRotation[0,2] +=(widthNew-width)/2  #重点在这步，目前不懂为什么加这步
#matRotation[1,2] +=(heightNew-height)/2  #重点在这步

imgRotation=cv2.warpAffine(img,matRotation,(widthNew,heightNew),borderValue=(255,255,255))


# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值

face_cascade = cv2.CascadeClassifier('C:\\Users\XP\Desktop\opencv\haarcascade_frontalface_alt2.xml')
z
# 读取图片
image = imgRotation

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
# 探测图片中的人脸

faces = face_cascade.detectMultiScale(

    gray,

    scaleFactor = 1.2,

    minNeighbors = 2,

    minSize = (15,15),
)

print ("发现{0}个人脸!".format(len(faces)))



#wuguan = [[366, 503],[373, 547]]


for(x,y,w,h) in faces:
#    cv2.rectangle(image,(x-20,y-100),(x+w,y+h+50),(0,255,0),2)

#for(x,y) in wuguan:
#    cv2.rectangle(img,(x,y),(x+1,y+1),(0,255,0),2)

    x1 = x-75
    y1 = y-150
    x2 = x+413
    y2 = y+626
    a,b,c =np.shape(image)
#newimg = np.zeros_like(image) 
newimg = np.zeros((626,413,3),np.uint8)
for i in range(413):
    for j in range(626):
        newimg[j][i] = imgRotation[j+y1][i+x1]
            

cv2.imshow('v3_1.jpg',newimg)
#cv2.imshow('v3_2.jpg',image)
cv2.imshow('v3_3.jpg',img)
cv2.waitKey(0)