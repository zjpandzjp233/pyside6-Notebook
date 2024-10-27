from PySide6.QtWidgets import QApplication,QWidget,QLabel
import QRC的资源文件_rc
from PySide6.QtGui import QPixmap


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb=QLabel(self)
        self.lb.setPixmap(QPixmap(':/图片/5915124c0d98f57c84c002c1bbf89a8.png')) # 读取的是QRC文件，也就是QTdesigner里面的资源浏览器里的文件路径

if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()