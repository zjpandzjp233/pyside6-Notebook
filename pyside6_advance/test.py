import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPainter, QBrush, QLinearGradient, QRadialGradient, QColor, QPen, QPainterPath
from PySide6.QtCore import Qt, QPointF, QRectF

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('渐变透明度画笔示例')
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.drawing = False
        self.last_point = None

        self.view.mousePressEvent = self.mousePressEvent
        self.view.mouseMoveEvent = self.mouseMoveEvent
        self.view.mouseReleaseEvent = self.mouseReleaseEvent

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            self.draw_gradient_brush(event.pos())

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.draw_gradient_brush(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def draw_gradient_brush(self, pos):
        # 创建一个圆形路径
        path = QPainterPath()
        path.addEllipse(pos, 20, 20)

        # 创建一个径向渐变
        gradient = QRadialGradient(pos, 20)
        gradient.setColorAt(0, QColor(255, 255, 255, 255))  # 中心颜色，不透明
        gradient.setColorAt(1, QColor(255, 255, 255, 0))    # 边缘颜色，完全透明

        # 设置渐变笔刷
        brush = QBrush(gradient)

        # 创建一个填充路径的图形项
        item = self.scene.addPath(path, QPen(Qt.NoPen), brush)
        self.scene.addItem(item)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.setGeometry(100, 100, 800, 600)

        self.custom_widget = CustomWidget()
        self.setCentralWidget(self.custom_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())