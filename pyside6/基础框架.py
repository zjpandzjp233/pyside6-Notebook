from PySide6.QtWidgets import QApplication,QStyle,QPushButton,QLabel,QLineEdit,QWidget# QWidget QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from Ui_登录框 import Ui_Form
class Mywindow(QWidget):# 继承取决于你在qt editer里面选择的初始模板叫什么，如dialog widget mainwindow
    def __init__(self):
        super().__init__()
        btn=QPushButton('一个按钮',self)
        btn.setEnabled(False) # 禁用按钮
        btn.setGeometry(300,300,100,50)
        btn.setToolTip('点我关机') # 按钮在指针悬停的提示
        btn.setText('按钮') # 重新设置名字

        self.iconLB=QLabel()
        self.iconLB.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogSaveButton)) # 给lable设置图标
        # self.标签名字.setAlignment(Qt.AlignmentFlag.AlignCenter) # 设置文本居中
        # self.标签名字.setFont(QFont('微软雅黑',50)) # 设置字体与大小
        # QLineEdit 的 EchoMode 枚举类型定义了四种不同的显示模式：（在editer里可以设置）
        # Normal：正常显示输入的字符。这是默认模式。
        # NoEcho：不显示任何输入的字符，适用于密码输入等需要完全隐藏输入的情况。
        # Password：显示一个替代字符（通常是星号 * 或点 •）来代替实际输入的字符。
        # PasswordEchoOnEdit：在编辑时显示实际输入的字符，但在失去焦点时显示替代字符。
        # lb=QLabel('按钮',self) # 一样有那些设置，可以改位置，文本格式，放置图片等等
        # lb.setGeometry(0,0,200,200)
        # lb.setText('一个按钮1')
        # lb.setAlignment(Qt.AlignmentFlag.AlignCenter) # 垂直水平居中对齐

        QL=QLineEdit(self) # 输入框
        QL.setPlaceholderText('请输入密码。')
        QL.returnPressed.connect() # 回车被按下时发出信号
        QL.textChanged.connect() # 文本变化发信号，附带传参输入框的文字


        #cmd的指令:pyside6-uic 目标文件名 -o 输出文件名.py   # 用于ui转py
        self.ui=Ui_Form() # 不同的初始项目，不同的名字，都是那个py文件里的第一个类
        self.ui.setupUi(self) # 类函数

        btn.clicked.connect(self.hello_world)
    def hello_world(self):
        print('hello world')


if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()

"""
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout

from Ui_计算器 import Ui_Form
class Mywindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()
"""

"""
from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QVBoxLayout
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        cb=QComboBox(self)
        mainlayout=QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()
"""