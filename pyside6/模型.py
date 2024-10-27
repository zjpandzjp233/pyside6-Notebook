from PySide6.QtWidgets import QApplication,QWidget,QTableView,QHeaderView,QVBoxLayout 
from PySide6.QtWidgets import QTableWidget,QTableWidgetItem,QHeaderView,QPushButton,QHBoxLayout,QLineEdit
from faker import Faker
from PySide6.QtGui import QAction,QStandardItemModel,QStandardItem
from PySide6.QtCore import Qt,QSortFilterProxyModel,QRegularExpression


class Mywindow(QWidget):
    def __init__(self):
        self.vLayout=QVBoxLayout()
        super().__init__()
        #self.setupUi(self)
        self.resize(600,600) 
        self.fake=Faker(locale='zh_CN')
        self.data=[[self.fake.name(),self.fake.phone_number(),self.fake.address()] for _ in range(80)]
        # 创建模型
        self.model=QStandardItemModel()
        for index,sub_list in enumerate(self.data): # enumerate是枚举,index是序号(从零开始)，value是值
            for index_2,value in enumerate(sub_list):
                self.model.setItem(index,index_2,QStandardItem(value))
        # 创建视图层
        self.table=QTableView()
        self.table.setSortingEnabled(True)# 开启排序功能
        self.table2=QTableView()
        self.table2.setModel(self.model)
        self.vLayout.addWidget(self.table)
        self.vLayout.addWidget(self.table2) # 两张表同源，一张表的变动会影响另一张表
        self.table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers) # 静止编辑
        self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows) # 单击单元格直接选一整行
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # 表格拉伸的和窗口一样大
        self.table.setModel(self.model)
        
        #创建一个代理模型,类似于原模型上的装饰器
        self.agentmodel=QSortFilterProxyModel()
        self.agentmodel.setSourceModel(self.model)
        self.line=QLineEdit()
        self.line.textChanged.connect(lambda text:self.agentmodel.setFilterRegularExpression(QRegularExpression(text))) # 正则表达式
        self.agentmodel.setFilterKeyColumn(-1) # 表格依据第几列的数据来过滤，-1表示全部列
        self.table3=QTableView()
        self.table3.setModel(self.agentmodel) #代理模型套模型上
        self.vLayout.addWidget(self.table3)

        self.vLayout.addWidget(self.line)
        self.setLayout(self.vLayout)
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()