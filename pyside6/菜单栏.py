from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QMenu,QStyle,QLineEdit,QToolBox,QLabel,QPushButton,QVBoxLayout
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt,QLocale, QTranslator, QLibraryInfo
from Ui_设置菜单栏 import Ui_MainWindow
class Mywindow(Ui_MainWindow,QWidget): # 只有QMainWindow里面有菜单栏
    def __init__(self):
        super().__init__()
        # self.setupUi(self) 
        
        

        # self.myMenuBar=self.menuBar() # 这个bar是QMainWindow自带的，不用自己创建
        # self.openfile=QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon),'openfile') # 设置图标与选项名称
        # self.closeWindow=QAction('closeWindow')
        # self.subMenu=QMenu('文件操作')
        # self.subMenu.addAction(self.openfile)
        # self.subMenu.addAction(self.closeWindow)
        # self.subMenu2=QMenu('more')
        # self.moreAction1=QAction('1')
        # self.subMenu2.addAction(self.moreAction1)
        # self.moreAction2=QAction('2')
        # self.subMenu2.addAction(self.moreAction2)
        # self.moreAction3=QAction('3')
        # self.subMenu2.addAction(self.moreAction3)
        # self.subMenu.addMenu(self.subMenu2)
        # self.myMenuBar.addMenu(self.subMenu)
        
        # 上下文菜单，即在窗口内右键的菜单
        # self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu) # 设置窗体的上下文菜单策略
        # self.undoAction=QAction('Undo')
        # self.RedoAction=QAction('Redo')
        # self.addAction(self.RedoAction) # 也可以传列表(addActions)
        # self.addAction(self.undoAction)
        # self.undoAction.triggered.connect(lambda:print('undoAction'))

        # self.QlineEdit=QLineEdit(self) # 给控件自定义右键菜单
        # self.QlineEdit.setGeometry(0,30,100,20)
        # self.QlineEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        # self.doAction123=QAction('input 123')
        # self.doAction456=QAction('input 456')
        # self.QlineEdit.addActions([self.doAction123,self.doAction456])
        # self.doAction123.triggered.connect(lambda:self.QlineEdit.setText('123'))
        # self.doAction456.triggered.connect(lambda:self.QlineEdit.setText('456'))
        
        # 制作选项卡类菜单
        self.arrowRight=self.style().standardPixmap(QStyle.StandardPixmap.SP_ArrowRight)# 用在选项卡侧边的图标，等下要做动态
        self.arrowdown=self.style().standardPixmap(QStyle.StandardPixmap.SP_ArrowDown)
        self.toolbox=QToolBox()
        self.littleWindow=QWidget() #创建子窗口 self需要继承QWidget
        self.layout1=QVBoxLayout()
        self.layout1.addWidget(QPushButton('button_1'))
        self.layout1.addWidget(QPushButton('button_2'))
        self.littleWindow.setLayout(self.layout1)
        self.toolbox.addItem(self.littleWindow,self.arrowRight,'选项卡1')
        self.littleWindow2=QWidget() #创建子窗口 self需要继承QWidget
        self.layout2=QVBoxLayout()
        self.layout2.addWidget(QPushButton('button_1'))
        self.layout2.addWidget(QPushButton('button_2'))
        self.littleWindow2.setLayout(self.layout2)
        self.toolbox.addItem(self.littleWindow2,self.arrowRight,'选项卡2')
        self.toolbox.currentChanged.connect(self.iconChange) # 默认传递变化了的选项卡的index
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addWidget(self.toolbox)
        self.setLayout(self.mainlayout)
        self.toolbox.setItemIcon(0,self.arrowdown)
    def iconChange(self,index):
        for i in range(self.toolbox.count()):
            # print(self.toolbox.count()) # 2
            self.toolbox.setItemIcon(i,self.arrowRight)
        self.toolbox.setItemIcon(index,self.arrowdown)

        # # self.action0.triggered.connect(lambda:print('全黑')) # 菜单栏信号绑定
        # self.action0.triggered.connect(lambda:self.close())



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