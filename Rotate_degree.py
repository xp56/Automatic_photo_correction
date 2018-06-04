# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 08:21:26 2018

@author: XP
"""

# encoding:utf-8  


'''根据眼睛位置 '''
  
import numpy as np  
import cv2  
from matplotlib import pyplot as plt  
from math import *
  


left_eye =[[292, 514], [304, 506], [319, 504], [333, 513], [320, 518], [305, 519]]
right_eye =[[396, 506], [406, 493], [421, 490], [435, 495], [425, 504], [410, 507]]

a_eye = [0,0,0,0,0,0]

for i in range(4):
    cv2.line(img, (left_eye[i][0],left_eye[i][1]), (right_eye[3-i][0],right_eye[3-i][1]), (0,255,0),2)
    a_eye[i] =degrees(atan(fabs((right_eye[3-i][1]-left_eye[i][1])/(right_eye[3-i][0]-left_eye[i][0]))))
a_eye[4] = degrees(atan(fabs((right_eye[5][1]-left_eye[4][1])/(right_eye[5][0]-left_eye[4][0]))))
a_eye[5] = degrees(atan(fabs((right_eye[4][1]-left_eye[5][1])/(right_eye[4][0]-left_eye[5][0]))))   

cv2.line(img, (left_eye[5][0],left_eye[5][1]), (right_eye[4][0],right_eye[4][1]), (0,255,0),2)    
cv2.line(img, (left_eye[4][0],left_eye[4][1]), (right_eye[5][0],right_eye[5][1]), (0,255,0),2)

#for i in range(6):
#    print(a_eye[i])

b_eye = sum(a_eye)/len(a_eye)


print('b_eye',b_eye)


#cv2.imshow('v3_3.jpg',img)



''' 根据鼻梁位置'''


def xielv (a,b):
    return degrees(atan(fabs((a[0]-b[0])/(a[1]-b[1]))))
  

nose_bridge = [[366,503], [369, 525], [373, 547], [376, 569]]

count = 0
a_nsoe = np.zeros((6,1))
for tem in range(3):
    for j in range(1,4):
        if(tem+j>3):
            break
        a_nsoe[count] = xielv(nose_bridge[tem],nose_bridge[tem+j])
        count= count + 1


#print("count",count)
b_nsoe = sum(a_nsoe)/count
#print("a_nsoe",a_nsoe)
print("\n")
print("b_nsoe",b_nsoe)



'''所以 对眼睛和鼻子的数据取平均'''
degree = ( b_eye + b_nsoe )/2
print(degree)























