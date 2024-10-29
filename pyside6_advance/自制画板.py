from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PySide6.QtGui import QMouseEvent, QPainter,QColor,QFont,QPen,QPolygon,QImage,QBrush,QPixmap
from PySide6.QtCore import Qt,QRect,QPoint
import math
import os
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))# 将工作目录设置为代码所在的文件夹里面，不然就在vscode选择打开的文件夹上
        self.resize(600,600)
        self.pix=QPixmap(600,600)# 默认透明
        self.pix.fill(Qt.white)
        self.point1=QPoint()
        self.point0=QPoint()
        self.i=1

    def paintEvent(self,event):
        if self.i==1:
            self.i+=1
            return
        painter1=QPainter(self.pix) # 创建了一个 `QPainter` 实例 `pp`，并将 `self.pix` 作为目标对象。这里的 `self.pix` 应该是一个 `QPixmap` 对象，用于保存绘制的内容。
        pen = QPen(QColor(0, 0, 0))  # 设置线条颜色为黑色
        pen.setWidth(30)  # 设置线条宽度为5像素
        painter1.setPen(pen)
        painter1.drawLine(self.point0,self.point1) # 点到点
        self.point0=self.point1
        painter_show=QPainter(self)
        painter_show.drawPixmap(0,0,self.pix) #  使用 `painter` 的 `drawPixmap` 方法，将 `self.pix` 上的内容绘制到窗口的 `(0, 0)` 位置处。这里假设 `self.pix` 的大小与窗口匹配，否则可能只有一部分会被显示出来。
    def mousePressEvent(self, event: QMouseEvent) -> None: # 这是一个事件处理方法，用于处理鼠标按下事件。当用户按下鼠标按钮时，这个方法会被调用。
        if event.button()==Qt.LeftButton:
            # event.button()：返回一个枚举值，表示按下的鼠标按钮。可能的值包括 Qt.LeftButton（左键）、Qt.RightButton（右键）、Qt.MiddleButton（中键）等。
            self.point0=event.pos()
    def mouseMoveEvent(self, event: QMouseEvent) -> None: # 当用户移动鼠标时，这个方法会被调用。
        self.setMouseTracking(False) # true的话，只要在拖拽了鼠标，就会一直调用mouseMoveEvent
        if event.button() == Qt.NoButton: # 检查event.button()的返回值,按动任意键时拖拽event.button() 值为 Qt.NoButton
            self.point1=event.pos()
            self.update() # 更新界面，简单说即调用 paintEvent
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button()==Qt.LeftButton:
            self.point1=event.pos()
            self.update()
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()

