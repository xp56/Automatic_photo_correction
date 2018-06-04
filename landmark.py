import os

import face_recognition



def opcv(rootDir,doc,c):

    for root,dirs,files in os.walk(rootDir):
        for file in files:
            
            a = os.path.join(root,file)
            image = face_recognition.load_image_file(a)
            face_landmarks_list = face_recognition.face_landmarks(image)

            print(os.path.join(root,file),file = doc)   #将文件名输出至txt文件
                                                       #将总共检测到的人脸数 输出至txt文件
            print (face_landmarks_list,file = doc)


            c = c+1
            if c/110 in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:    #count计数 输出总共计算了多少了 3000是val文件夹下的文件个数
                print("complit   ",c/110)
#        for dir in dirs:
 #           opcv(dir,doc,modle,c)
count = 0
doc = open('val.txt','w')  #将数据输出的文件名
rootDir = "zhengjianzhao"   # 待检测的图片路径
opcv(rootDir,doc,count)  #将文件传入函数
print("finish")
doc.close()
