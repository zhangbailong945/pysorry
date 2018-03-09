
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QGroupBox,QHBoxLayout,QFormLayout,QLineEdit
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QCoreApplication

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
        wordTextEdit1=QLineEdit("好啊")

        wordLabel2=QLabel("第二句话:")
        wordTextEdit2=QLineEdit("就算你是一流的程序员")

        wordLabel3=QLabel("第三句话:")
        wordTextEdit3=QLineEdit("就算你写的代码再完美")

        wordLabel4=QLabel("第四句话:")
        wordTextEdit4=QLineEdit("我叫你加班，你就得加班")

        wordLabel5=QLabel("第五句话:")
        wordTextEdit5=QLineEdit("毕竟我是老板")

        wordLabel6=QLabel("第六句话:")
        wordTextEdit6=QLineEdit("老板了不起啊")

        wordLabel7=QLabel("第七句话:")
        wordTextEdit7=QLineEdit("不好意思，老板就是了不起")

        wordLabel8=QLabel("第八句话:")
        wordTextEdit8=QLineEdit("以后叫他天天加班")

        wordLabel9=QLabel("第九句话:")
        wordTextEdit9=QLineEdit("天天加，天天加！")
        flayout.addRow(wordLabel1,wordTextEdit1)
        flayout.addRow(wordLabel2,wordTextEdit2)
        flayout.addRow(wordLabel3,wordTextEdit3)
        flayout.addRow(wordLabel4,wordTextEdit4)
        flayout.addRow(wordLabel5,wordTextEdit5)
        flayout.addRow(wordLabel6,wordTextEdit6)
        flayout.addRow(wordLabel7,wordTextEdit7)
        flayout.addRow(wordLabel8,wordTextEdit8)
        flayout.addRow(wordLabel9,wordTextEdit9)
        self.formGroupBox.setLayout(flayout)
    #操作按钮
    def createButtonLayOut(self):
        self.actionGroupBox=QGroupBox("操作")
        alayout=QHBoxLayout()
        composeBtn=QPushButton('合成')
        quitBtn=QPushButton('退出')
        quitBtn.clicked.connect(QCoreApplication.quit)
        alayout.addWidget(composeBtn)
        alayout.addWidget(quitBtn)
        self.actionGroupBox.setLayout(alayout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    se=SorryEmoji()
    sys.exit(app.exec_())