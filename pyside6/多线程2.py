from PySide6.QtWidgets import QApplication,QPushButton,QWidget,QVBoxLayout,QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer,QThread,Signal
import os
import time
class ThreadWindow(QThread):
    Signal=Signal(str)
    def __init__(self):
        super().__init__()
        print('ThreadWindow run')
    def run(self): # 重写QThread里面的run函数，也就是线程的任务函数
        for i in range(3):
            self.Signal.emit(str(i))
            time.sleep(1)

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb=QLabel(f'value:0')
        self.thread1=ThreadWindow()
        self.thread1.Signal.connect(lambda x:self.lb.setText(f'value:{x}'))
        self.thread1.started.connect(lambda:print('线程开始时执行'))
        # self.thread1.finished.connect(lambda:print('线程结束时执行'))
        self.thread1.finished.connect(lambda:self.thread1.deleteLater())# 线程结束自动回收内存，删了这个线程
        self.thread1.start()
        self.thread1.wait() # 线程thread1没结束,所有代码都卡住等他
        self.mainL=QVBoxLayout()
        self.mainL.addWidget(self.lb)
        self.setLayout(self.mainL)


if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()