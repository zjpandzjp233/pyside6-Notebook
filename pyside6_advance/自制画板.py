import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit
from PySide6.QtGui import QShortcut,QMouseEvent, QPainter,QKeySequence,QColor,QFont,QPen,QPolygon,QImage,QBrush,QPixmap
from PySide6.QtCore import Qt,QRect,QPoint
import math
import os
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))# 将工作目录设置为代码所在的文件夹里面，不然就在vscode选择打开的文件夹上
        # 确保窗口获得初始焦点
        self.setFocus()
        # 连接应用程序的焦点变化信号
        QApplication.instance().focusChanged.connect(self.on_focus_changed)
        self.resize(600,630)
        self.pix=QPixmap(600,600)# 默认透明
        self.pix.fill(Qt.white)
        self.point1=QPoint()
        self.point0=QPoint()
        self.i=0
        self.butt=QPushButton('保存图片(Ctrl+X)',self)
        self.butt.clicked.connect(self.savePix)
        self.butt.setGeometry(0,600,150,30)
        self.butt=QPushButton('清空图片(Ctrl+Z)',self)
        self.butt.clicked.connect(self.clearPix)
        self.butt.setGeometry(151,600,150,30)
        self.labo=QLineEdit(self)
        self.labo.setGeometry(301,600,299,30)
        self.i2=1
        self.shortcut = QShortcut(QKeySequence('Ctrl+X'), self)
        self.shortcut.activated.connect(self.savePix)
        self.shortcut = QShortcut(QKeySequence('Ctrl+Z'), self)
        self.shortcut.activated.connect(self.clearPix)
    def leaveEvent(self, event):
        """鼠标离开窗口时触发"""
        self.i=0
        print("Mouse left the window")
        super().leaveEvent(event)

    def focusOutEvent(self, event):
        """窗口失去焦点时触发"""
        self.i=0
        print("Window lost focus")
        super().focusOutEvent(event)

    def on_focus_changed(self, old_widget, new_widget):
        """应用程序焦点变化时触发"""
        if old_widget == self and new_widget != self:
            self.i=0
            print("Window lost focus (via focusChanged)")
    def clearPix(self):
        self.pix.fill(Qt.white)
        self.i=0
        self.update()
    def savePix(self):
        self.i2=str(self.i2)
        fileName=self.labo.text()
        self.pix.save('./'+fileName+'_'+self.i2+'.png','PNG')
        self.i2=int(self.i2)
        self.i2+=1
    def paintEvent(self,event):
        if self.i<2:
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

