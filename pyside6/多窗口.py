from PySide6.QtWidgets import QApplication,QVBoxLayout,QTextEdit,QWidget,QPushButton,QMessageBox,QInputDialog,QLineEdit,QFileDialog
from PySide6.QtWidgets import QFontDialog,QColorDialog
import time
from PySide6.QtCore import QLocale, QTranslator, QLibraryInfo,Signal,QTimer
import sys
#from Ui_计算器 import Ui_Form
class Mywindow2(QWidget):
    子窗口向主窗口传递信号=Signal(str)
    def __init__(self,parent=None): # 对子窗口的初始函数多一个父窗口位置，方便子窗口给父窗口发信号
        super().__init__()
        self.Pclose=QPushButton("我是子窗口的按钮",self)
        self.Pclose.clicked.connect(self.close_window)
        self.qline=QLineEdit(self)
        self.resize(300,300)
        self.qline.setGeometry(0,150,150,20)
        self.move(700,0) # 窗口创建后的位移
        self.parent_object=parent
    def close_window(self):
        # self.close() # 关闭窗口
        if self.parent_object!=None:
            self.子窗口向主窗口传递信号.connect(self.parent_object.qline.setText)
            self.子窗口向主窗口传递信号.emit('子窗口给父窗口的信息')
            # 也可以直接 self.parent_object.qline.setText('子窗口给父窗口的信息') 但是这样无法利用到多线程

        self.hide() # 隐藏窗口，资源没有被清空

class Mywindow(QWidget):
    把我们的值发送给子窗口=Signal(str) # 参数为传递类型
    def __init__(self):
        super().__init__()
        # self.setupUi(self) 
        # self.resize(300,200) # 窗口大小
        # self.setWindowTitle('多语言示例') # 窗口名字
        # NonModal
        # windowsModal,悬浮在自己的程序最上方，不关闭就无法操作其他
        # ApplicantionModal 悬浮在系统最上方，不关闭这个窗口无法交互任何地方
        # qp=QPushButton('打开一个messageBox',self)
        # qp.clicked.connect(self.buttonChange)

        # self.myLayout=QVBoxLayout()
        # self.myButton=QPushButton('点我切换字体')
        # self.myButton2=QPushButton('点我切换字体颜色')
        # self.myTextEdit=QTextEdit()
        # self.myLayout.addWidget(self.myTextEdit)
        # self.myLayout.addWidget(self.myButton)
        # self.myLayout.addWidget(self.myButton2)
        # self.setLayout(self.myLayout)
        # self.myButton.clicked.connect(self.buttonChange)
        # self.myButton2.clicked.connect(self.buttonChange2)
        self.qline=QLineEdit(self)
        self.qline.setGeometry(100,0,200,20)
        self.secondWindow=Mywindow2(self) # 如果这里没有self会被垃圾回收机制瞬间回收
        self.PB=QPushButton("打开一个新窗口.",self)
        self.PB.clicked.connect(self.onpen_new_window2)

        self.把我们的值发送给子窗口.connect(self.secondWindow.qline.setText) # 创建对子窗口lineEdit的连接
        self.把我们的值发送给子窗口.emit('这是一条来自主窗口发送给子窗口的文本') # 发送给子窗口信号
        self.secondWindow.qline.setText('122222222223') # 也可以直接设置，但是这样无法利用多线程，上面的信号方式可以利用多线程。
    def onpen_new_window2(self):
        QTimer.singleShot(3000,self.onpen_new_window) # 延时，且这个函数是非阻塞的
    def onpen_new_window(self):
        
        self.secondWindow.show()
    
    def buttonChange2(self):
        color=QColorDialog.getColor()
        self.myTextEdit.setTextColor(color) # 如果只选择了文本框内部分文字在传入这个颜色，则就能改到指定部分的颜色
        pass
    def buttonChange(self):
        
        isOk,font=QFontDialog.getFont() # 打开字体窗口
        if not isOk:return
        self.myTextEdit.setFont(font) # 给text窗口设置字体

        # path,option=QFileDialog.getOpenFileName(self,'标题:选择文件','.','所有文件(*.*);;py文件(*.py);;音频文件(*.wav *.mp3)') #  . 表示当前路径 
        # print(path,option) # C:/Users/机械革命/Desktop/HTML/Python/py_advance/单例模式_实现部分.py    py文件(*.py)

        # option=QFileDialog.getOpenFileNames(self,'标题:选择多个文件','.','所有文件(*.*);;py文件(*.py);;音频文件(*.wav *.mp3)') 
        # print(option) # (['C:/Users/机械革命/Desktop/HTML/Python/py_advance/ATM.py', 'C:/Users/机械革命/Desktop/HTML/Python/py_advance/socket服务端.py', 'C:/Users/机械革命/Desktop/HTML/Python/py_advance/socket客户端.py', 'C:/Users/机械革命/Desktop/HTML/Python/py_advance/闭包.py'], '所有文件(*.*)')

        # path=QFileDialog.getExistingDirectory(self,'标题:选择文件夹','.') 
        # print(path) # C:/Users/机械革命/Desktop/HTML/Python/资料   # 取消返回none

        # tuple2=QFileDialog.getSaveFileName(self,'标题:选择文件夹','.','py文件(*.py);;txt文件(*.txt)') # 这个方法本身不会创建或保存任何文件；它只是提供一个对话框让用户选择文件名和路径。你需要自己编写代码来实际保存文件。
        # print(tuple2) # ('', '') 取消时返回值         # 'C:/Users/机械革命/Desktop/新建 文本文档.txt', 'txt文件(*.txt)' 

        # returns2,ok=QInputDialog.getInt(self,'title','输入你的年龄。') #返回值 (88, True) (输入的数字，是否点ok)
        # if ok:
        #     print(returns2)

        # returns2222,ok=QInputDialog.getDouble(self,'title','输入你的年龄。',0.5,0,100,10)#(默认值，最小值，最大值，调节步长) # 对double数5变5.0 
        # if ok:
        #     print(returns2222)

        # returns222,ok=QInputDialog.getItem(self,'title','输入你的职位。',['医生','老师','流水线工人','施工员'],2,False) # (可选列表，默认值，是否可被编辑)
        # if ok:
        #     print(returns222)

        # returns22,ok=QInputDialog.getText(self,'title','输入你的建议',QLineEdit.EchoMode.PasswordEchoOnEdit,'输入框默认输入的')
        # if ok:
        #     print(returns22)
        # returns22222222,ok=QInputDialog.getMultiLineText(self,'title','输入你的建议')
        # if ok:
        #     print(returns22222222)
        # returns=QMessageBox.information(self,'这个窗口的title：提示框','这是一个提示框！',QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.No,QMessageBox.StandardButton.Ok) # 设置按钮,并设置一个默认按钮
        # if returns==QMessageBox.StandardButton.Ok:
        #     print('OK')
        
        # QMessageBox.information(self,'这个窗口的title：提示框','这是一个提示框！')
        # QMessageBox.question(self,'title','你确定要继续么？')
        # QMessageBox.warning(self,'title','这是一个警示框！')
        # QMessageBox.critical(self,'title','程序严重错误，请重新启动。')
        # QMessageBox.about(self,'title','和你说个事')
        pass





if __name__=='__main__':
    app=QApplication([])

    locale = QLocale(QLocale.Chinese, QLocale.China) # 设置语言环境为中文 让 QFontDialog,QColorDialog 等窗口变成中文样式
    QLocale.setDefault(locale)
    translator = QTranslator()
    if translator.load("qtbase_zh_CN", QLibraryInfo.location(QLibraryInfo.TranslationsPath)): # 加载翻译文件
        app.installTranslator(translator)

    windows=Mywindow()
    windows.show()
    app.exec()