#-*- coding:utf-8 -*-*
'''
测试功能：python mp4提取帧并生成png图片
需要手动安装的库
(1)、python -m pip install opencv-python #用于mp4 转png 帧图片
'''
__author__='loach'

#python 将mp4视频转为png图片
#并在图片加上文字
import cv2.cv2 as cv
from PIL import Image,ImageDraw,ImageFont
import numpy as np

vc =cv.VideoCapture('source/mp4/sorry.mp4')
c=1
if vc.isOpened():
    rval,frame=vc.read()
else:
    print("no mp4!")
    rval=False

timeF=100


while rval: #循环读取
    rval,frame=vc.read()
    if(c%timeF==0):#每隔timeF进行帧存储操作
        font=cv.FONT_HERSHEY_COMPLEX
        #CV2转PIL
        cv_im=cv.cvtColor(frame,cv.COLOR_RGB2BGR)
        pil_im=Image.fromarray(cv_im)
        #中文
        draw=ImageDraw.Draw(pil_im)
        font=ImageFont.truetype("source/fonts/xiaowanzi.TTF",30,encoding='utf-8')
        draw.text((150,260),"我就是大佬",(255,255,255),font=font)   
        #PIL图片转CV2
        cv2_text_im=cv.cvtColor(np.array(pil_im),cv.COLOR_RGB2BGR)
        cv.imwrite('temp/images/'+str(c)+'.png',cv2_text_im)

    c=c+1
    cv.waitKey(1)

vc.release()
