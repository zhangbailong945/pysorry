
import sys

from PyQt5.QtWidgets import QApplication,QWidget

class SorryEmoji(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.resize(300,400)
        self.setWindowTitle("Sorry,有钱就是了不起啊。")
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    se=SorryEmoji()

    sys.exit(app.exec_())