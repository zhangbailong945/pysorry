#-*- coding:utf-8 -*-*
'''
#功能：python 生成将mp4转为带字幕的gif图片
#需要手动安装的库
(1)、python -m pip install PyQt5  #用于创建桌面应用程序
(2)、python -m pip install opencv-python #用于mp4 转png 帧图片
(3)、python -m pip install Pillow   #用于 cv2和pil之间的转换
(4)、python -m pip install imageio  #用于多个png帧图片 生成 gif图片
'''
__author__='loach'

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QGroupBox,QHBoxLayout,QFormLayout,QLineEdit,QFileDialog,QProgressDialog,QMessageBox
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QCoreApplication,Qt
import cv2.cv2 as cv
from PIL import Image,ImageDraw,ImageFont
import numpy as np
import imageio
import os
import os.path
import time

class SorryEmoji(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    #初始化UI
    def initUI(self):
        self.createImageLayOut()
        self.createFromLayOut()
        self.createButtonLayOut()
        mainLayOut=QVBoxLayout()#平直布局
        imageLay=QVBoxLayout() #显示图片
        imageLay.addWidget(self.gridGroupBox)
        imageLay.addWidget(self.formGroupBox)
        imageLay.addWidget(self.actionGroupBox)
        mainLayOut.addLayout(imageLay)
        self.resize(300,500)
        self.setWindowTitle("Sorry,有钱就是了不起啊。")
        self.setWindowIcon(QIcon('source/images/favicon.ico'))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(),self.height())
        self.setLayout(mainLayOut)
        self.show()

    #表情参考图
    def createImageLayOut(self):
        self.gridGroupBox=QGroupBox("图片")
        self.gridGroupBox.setFixedSize(300,200)
        imageH=QVBoxLayout()
        label=QLabel(self)
        label.resize(300,200)    
        sorryImage=QPixmap()   
        sorryImage.load('source/images/sorryimage.png')
        si=sorryImage.scaled(300,200) #缩放原始图片的大小
        label.setPixmap(si)
        imageH.addWidget(label)
        self.gridGroupBox.setLayout(imageH)

    #表情参数
    def createFromLayOut(self):
        self.formGroupBox=QGroupBox("表情参数")
        flayout=QFormLayout()

        wordLabel1=QLabel("第一句话:")
        self.wordTextEdit1=QLineEdit("好啊")

        wordLabel2=QLabel("第二句话:")
        self.wordTextEdit2=QLineEdit("就算你是一流的程序员")

        wordLabel3=QLabel("第三句话:")
        self.wordTextEdit3=QLineEdit("就算你写的代码再完美")

        wordLabel4=QLabel("第四句话:")
        self.wordTextEdit4=QLineEdit("我叫你加班，你就得加班")

        wordLabel5=QLabel("第五句话:")
        self.wordTextEdit5=QLineEdit("毕竟我是老板")

        wordLabel6=QLabel("第六句话:")
        self.wordTextEdit6=QLineEdit("老板了不起啊")

        wordLabel7=QLabel("第七句话:")
        self.wordTextEdit7=QLineEdit("Sorry,老板就是了不起")

        wordLabel8=QLabel("第八句话:")
        self.wordTextEdit8=QLineEdit("以后叫他天天加班")

        wordLabel9=QLabel("第九句话:")
        self.wordTextEdit9=QLineEdit("天天加，天天加！")

        flayout.addRow(wordLabel1,self.wordTextEdit1)
        flayout.addRow(wordLabel2,self.wordTextEdit2)
        flayout.addRow(wordLabel3,self.wordTextEdit3)
        flayout.addRow(wordLabel4,self.wordTextEdit4)
        flayout.addRow(wordLabel5,self.wordTextEdit5)
        flayout.addRow(wordLabel6,self.wordTextEdit6)
        flayout.addRow(wordLabel7,self.wordTextEdit7)
        flayout.addRow(wordLabel8,self.wordTextEdit8)
        flayout.addRow(wordLabel9,self.wordTextEdit9)
        self.formGroupBox.setLayout(flayout)
        
    #操作按钮
    def createButtonLayOut(self):
        self.actionGroupBox=QGroupBox("操作")
        alayout=QHBoxLayout()
        composeBtn=QPushButton('生成')
        quitBtn=QPushButton('退出')
        quitBtn.clicked.connect(QCoreApplication.quit)
        composeBtn.clicked.connect(self.saveGifFile)
        alayout.addWidget(composeBtn)
        alayout.addWidget(quitBtn)
        self.actionGroupBox.setLayout(alayout)
    
    #打开本地存储目录，保存gif图片位置
    def saveGifFile(self):    
        #选择gif图保存的文职
        gifSaveDirectory=QFileDialog.getExistingDirectory(self,"保存到","C:/")
        self.processDialog=QProgressDialog()
        self.processDialog.setWindowTitle("请稍等")
        self.processDialog.setLabelText("正在生成...")
        self.processDialog.setCancelButtonText("取消")
        self.processDialog.setMinimumDuration(5)
        self.processDialog.setWindowModality(Qt.WindowModal)
        self.processDialog.setRange(0,99)
        self.processDialog.setValue(10)

        
        #将mp4转为多个png图片
        pngPath='temp/images'
        if not os.listdir(pngPath):
            self.mp4ToPng()
        else:
            for i in os.listdir(pngPath):
                path_file=os.path.join(pngPath,i)
                if os.path.isfile(path_file):
                    os.remove(path_file)
            time.sleep(5)
            self.mp4ToPng()

        self.processDialog.setValue(60)
        QApplication.processEvents()
        #将多个png图片转为gif
        self.pngToGif(gifSaveDirectory)
        self.processDialog.setValue(99)
        QMessageBox.information(self,'提示',"合成成功!")
    
    #将mp4视频分解为多个帧图片png格式
    def mp4ToPng(self):
        #判断是否已经生成个png图片,如果有则先删除
        vc =cv.VideoCapture('source/mp4/sorry.mp4')
        c=1
        if vc.isOpened():
            rval,frame=vc.read()
        else:
            print("no mp4!")
            rval=False

        timeF=3

        while rval: #循环读取
            rval,frame=vc.read()
            if rval==True:
                if(c%timeF==0):#每隔timeF进行帧存储操作
                    font=cv.FONT_HERSHEY_COMPLEX
                    #CV2转PIL
                    cv_im=cv.cvtColor(frame,cv.COLOR_RGB2BGR)
                    im_resize=cv.resize(cv_im,(320,160),interpolation=cv.INTER_AREA)
                    pil_im=Image.fromarray(im_resize)
                    #中文字幕
                    draw=ImageDraw.Draw(pil_im)
                    font=ImageFont.truetype("source/fonts/xiaowanzi.TTF",18,encoding='utf-8')
                    if(c>12 and c<39):
                            draw.text((50,135),self.wordTextEdit1.text(),(255,255,255),font=font)
                    elif(c>63 and c<93):
                            draw.text((50,135),self.wordTextEdit2.text(),(255,255,255),font=font)
                    elif(c>105 and c<136):
                            draw.text((50,135),self.wordTextEdit3.text(),(255,255,255),font=font)
                    elif(c>136 and c<171):
                            draw.text((50,135),self.wordTextEdit4.text(),(255,255,255),font=font)
                    elif(c>192 and c<228):
                            draw.text((50,135),self.wordTextEdit5.text(),(255,255,255),font=font)
                    elif(c>228 and c<255):
                            draw.text((50,135),self.wordTextEdit6.text(),(255,255,255),font=font)
                    elif(c>273 and c<315):
                            draw.text((50,135),self.wordTextEdit7.text(),(255,255,255),font=font)
                    elif(c>351 and c<381):
                            draw.text((50,135),self.wordTextEdit8.text(),(255,255,255),font=font)
                    elif(c>381 and c<411):
                            draw.text((50,135),self.wordTextEdit9.text(),(255,255,255),font=font)
                    else:
                        draw.text((50,135),' ',(255,255,255),font=font)

                    #PIL图片转CV2
                    cv2_text_im = cv.cvtColor(
                        np.array(pil_im), cv.COLOR_BGR2RGB)
                    
                    cv.imwrite('temp/images/'+str(c)+'.png',cv2_text_im,[int(cv.IMWRITE_PNG_COMPRESSION), 0])
                    QApplication.processEvents()
                c=c+1
            else:
                break

            cv.waitKey(1)

        vc.release()
        
        
        #将png图片生成为gif
    def pngToGif(self,gifSaveDirectory):
        gif_name='sorry.gif'
        duration=0.1
        frames=[]
        path='temp/images'
        pngFiles=os.listdir(path)
        images_list=[os.path.join(path,f) for f in pngFiles]
        for image_name in images_list:
            frames.append(imageio.imread(image_name))
            QApplication.processEvents()
            #保存为gif图片
        imageio.mimsave(gifSaveDirectory+'/'+gif_name,frames,'GIF',duration=duration)

if __name__=='__main__':
    app=QApplication(sys.argv)
    se=SorryEmoji()
    sys.exit(app.exec_())
