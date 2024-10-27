from PySide6.QtWidgets import QApplication,QWidget,QHBoxLayout,QLabel,QPushButton
from qt_material import apply_stylesheet
# from Ui_计算器 import Ui_Form
from PySide6.QtCore import Qt
import os
themeList=['dark_amber.xml',
'dark_blue.xml',
'dark_cyan.xml',
'dark_lightgreen.xml',
'dark_pink.xml',
'dark_purple.xml',
'dark_red.xml',
'dark_teal.xml',
'dark_yellow.xml',
'light_amber.xml',
'light_blue.xml',
'light_cyan.xml',
'light_cyan_500.xml',
'light_lightgreen.xml',
'light_pink.xml',
'light_purple.xml',
'light_red.xml',
'light_teal.xml',
'light_yellow.xml']
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        #self.setupUi(self) 
        self.miniButton=QPushButton('minimize')
        self.closeButton=QPushButton('close')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 去除窗口的上的标题栏
        self.hLayout=QHBoxLayout()
        self.hLayout.addWidget(self.miniButton)
        self.hLayout.addWidget(self.closeButton)
        self.miniButton.clicked.connect(self.showMinimized) # 最小化窗口
        self.closeButton.clicked.connect(self.close)
        self.setLayout(self.hLayout)

if __name__=='__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app=QApplication([])
    # apply_stylesheet(app,theme='light_blue.xml') # 一个简洁的加了色彩主题的样式
    # 另外还有Qtmodern、QDarkStyleSheet、PyQtDarkTheme等等更强大的主题，使用方法大同小异
    windows=Mywindow()
    windows.show()
    app.exec()

"""
os.chdir(os.path.dirname(os.path.abspath(__file__))) 这段代码的作用是将当前工作目录更改为当前脚本所在的目录。让我们逐步解析这段代码：

1. os.path.abspath(__file__)
__file__ 是一个内置变量，表示当前脚本文件的路径。
os.path.abspath(__file__) 返回当前脚本文件的绝对路径。
2. os.path.dirname(os.path.abspath(__file__))
os.path.dirname(path) 返回路径中目录的部分，去掉文件名。
结合 os.path.abspath(__file__)，os.path.dirname(os.path.abspath(__file__)) 返回当前脚本所在目录的绝对路径。
3. os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir(path) 将当前工作目录更改为指定的路径。
因此，os.chdir(os.path.dirname(os.path.abspath(__file__))) 将当前工作目录更改为当前脚本所在的目录
"""