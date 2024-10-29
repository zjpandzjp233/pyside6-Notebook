import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt,QRect
from PySide6.QtGui import QMouseEvent
import os
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 200, 30)
        self.label.setText("Mouse Position: (0, 0)")

    def mouseMoveEvent(self, event: QMouseEvent):
        # 获取鼠标位置
        pos = event.pos()
        x, y = pos.x(), pos.y()
        self.update_label(x, y)
        # self.setMouseTracking(True)
        print('test')

    def mousePressEvent(self, event: QMouseEvent):
        # 获取鼠标位置
        pos = event.pos()
        x, y = pos.x(), pos.y()
        self.update_label(x, y)
        

    def update_label(self, x, y):
        # 更新标签显示鼠标位置
        self.label.setText(f"Mouse Position: ({x}, {y})")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())