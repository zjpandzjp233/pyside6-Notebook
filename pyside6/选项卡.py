from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QTabWidget,QLabel


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setupUi(self) 
        self.tab1 = QWidget()
        self.tab1Layout = QVBoxLayout()
        self.tab1Layout.addWidget(QPushButton('按钮1'))
        self.tab1Layout.addWidget(QLabel('标签1'))
        self.tab1.setLayout(self.tab1Layout)

        self.tab2 = QWidget()
        self.tab2Layout = QVBoxLayout()
        self.tab2Layout.addWidget(QPushButton('按钮2'))
        self.tab2Layout.addWidget(QLabel('标签2'))
        self.tab2.setLayout(self.tab2Layout)

        self.tab3 = QWidget()
        self.tab3Layout = QVBoxLayout()
        self.tab3Layout.addWidget(QPushButton('按钮3'))
        self.tab3Layout.addWidget(QLabel('标签3'))
        self.tab3.setLayout(self.tab3Layout)

        self.tab = QTabWidget()
        self.tab.addTab(self.tab1, "选项卡1")
        self.tab.addTab(self.tab2, "选项卡2")
        self.tab.addTab(self.tab3, "选项卡3")
        self.tab.setTabsClosable(True) # 每个选项卡后面是否跟着一个叉，用来关闭
        self.tab.setMovable(True) # 是否可拖
        self.tab.setTabPosition(QTabWidget.TabPosition.West) # 选项卡放置方向，默认上
        self.tab.setTabShape(QTabWidget.TabShape.Triangular) # 设置样式

        self.tab.tabCloseRequested.connect(lambda index:self.tab.removeTab(index)) # 给那个叉赋予功能

        self.mainLayout=QVBoxLayout()
        self.mainLayout.addWidget(self.tab)
        self.setLayout(self.mainLayout)
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()