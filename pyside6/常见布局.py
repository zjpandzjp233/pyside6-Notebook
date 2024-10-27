from PySide6.QtWidgets import QApplication,QWidget,QHBoxLayout,QGridLayout,QFormLayout,QVBoxLayout
from PySide6.QtWidgets import QLabel,QLineEdit,QPushButton
# from Ui_计算器 import Ui_Form
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setupUi(self) 
        self.mainLayout=QVBoxLayout()
        # self.userlayout=QHBoxLayout()
        # self.userlayout2=QHBoxLayout()

        # self.userlayout.addWidget(QLabel('userName:')) # 两个水平布局
        # self.userlayout.addWidget(QLineEdit())
        # self.userlayout2.addWidget(QLabel('password:'))
        # self.userlayout2.addWidget(QLineEdit())

        # self.mainLayout.addLayout(self.userlayout) # 将水平布局嵌套入垂直布局
        # self.mainLayout.addLayout(self.userlayout2)
        # self.mainLayout.addWidget(QPushButton('login'))

        # self.formLayout=QFormLayout() # 表单布局
        # self.formLayout.addRow('用户名',QLineEdit()) # 给表单添加一行内容
        # self.mainLayout.addLayout(self.formLayout)
        # self.formLayout.addWidget(QPushButton('login'))
        self.gridLayout=QGridLayout()
        self.gridLayout.addWidget(QPushButton('button'),0,0) # 将按钮放在第一行第一列
        self.gridLayout.addWidget(QPushButton('button'),0,1) # 将按钮放在第一行第二列
        self.gridLayout.addWidget(QPushButton('button'),1,0,1,2) # 按钮放在第二行第一列，但是按钮占一行两列的大小
        self.setLayout(self.gridLayout) # 给窗口添加布局
        

if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()