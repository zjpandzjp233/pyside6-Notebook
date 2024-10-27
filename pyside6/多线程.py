from PySide6.QtWidgets import QApplication,QPushButton,QWidget,QVBoxLayout,QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer,QThread,Signal
import os
class Mywindow(QWidget):
    counter=0
    def __init__(self):
        super().__init__()
        # self.setupUi(self) 
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.img_list=['./img_轮播用/蝴蝶.jpg','./img_轮播用/垃圾.jpg','./img_轮播用/dance.jpg','./img_轮播用/zjx.jpg']
        self.resize(600,600)
        
        self.timer=QTimer()
        self.timer.timeout.connect(self.timerOut)
        self.timer.setSingleShot(True) # 计时器只在延时后工作一次
        self.timer.setInterval(5000)# 重新设置延时
        self.timer.stop() # 急停
        QTimer.singleShot(2000,lambda:print('延时调用一个函数的方法，且不阻塞其他部分'))
        self.lb=QLabel()
        self.lb.setGeometry(0,0,100,100)
        self.lb.setMaximumSize(100, 100)
        self.lb.setPixmap(QPixmap('./img_轮播用/蝴蝶.jpg'))
        self.lb.setScaledContents(True)
        self.button=QPushButton('开始')
        self.Vlayout=QVBoxLayout()
        self.Vlayout.addWidget(self.lb)
        self.Vlayout.addWidget(self.button)
        self.button.clicked.connect(lambda:self.timer.start(1000)) # 让计时器开始并设置1000秒的延迟
        self.setLayout(self.Vlayout)
    def timerOut(self):
        QApplication.processEvents()
        self.counter+=1
        if self.counter==4:
            self.counter=0
        self.lb.setPixmap(QPixmap(self.img_list[self.counter]))


if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()