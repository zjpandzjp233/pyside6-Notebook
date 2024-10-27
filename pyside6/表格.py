from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QTableWidget,QTableWidgetItem,QHeaderView,QPushButton,QHBoxLayout,QLineEdit
from faker import Faker
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class Mywindow(QWidget,):
    result_globo=None
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        # self.setupUi(self) 
        self.line=QLineEdit()
        self.button2=QPushButton('搜索')
        self.hLayout=QHBoxLayout()
        self.hLayout.addWidget(self.line)
        self.hLayout.addWidget(self.button2)
        self.button2.clicked.connect(self.search)
        self.button=QPushButton('输出所有被选中的单元格')
        self.fake=Faker(locale='zh_CN')
        self.data=[[self.fake.name(),self.fake.address(),self.fake.ascii_free_email()] for _ in range(80)]
        self.mainLayout=QVBoxLayout()
        self.table=QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # 列的大小随着窗口大小自动伸缩，空间均匀分布
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) # 列元素多的分配更多空间,列元素少的保持不变
        self.table.setColumnCount(3)# 行列数
        self.table.setRowCount(99)
        self.table.setHorizontalHeaderLabels(['姓名','地址','邮箱']) # 每列的最上方元素，表头
        # self.table.setItem(0,0,QTableWidgetItem('名字')) #给 行 列 赋值
        """
        [a,b,c,d]
        枚举后：
        0,a
        1,b
        2,c
        3,d 
        分别赋值给index和sub_list
        """
        for index,sub_list in enumerate(self.data): # enumerate是枚举,index是序号(从零开始)，value是值
            for index_2,value in enumerate(sub_list):
                self.table.setItem(index,index_2,QTableWidgetItem(value))
            pass
        self.table.item(0,0).setText('刘麻子') # 改表格的值
        self.table.item(0,0).setBackground(Qt.GlobalColor.red) # 表格颜色
        self.table.setSortingEnabled(True) # 增加表头排序功能
        # self.table.cellClicked.connect(lambda row,column:print(f'row{row+1},column:{column+1}')) # 这个函数默认传行和列两个参数
        self.table.itemClicked.connect(lambda item:print(f'row:{item.row()},column:{item.column()},内容为：{item.text()}'))
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.table)
        self.mainLayout.addLayout(self.hLayout)
        self.button.clicked.connect(self.selectedItem)
        self.setLayout(self.mainLayout)
        self.table.takeItem(0,0) # 移除元素单元格
        self.table.setSpan(1,0,1,2)# 使第二行第一列的元素行占一行列占两列
        self.gettext=QAction('获取此元素')
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.table.addAction(self.gettext)
        self.gettext.triggered.connect(self.selectedItem)
    def selectedItem(self):
        # print(self.table.selectedItems())# 输出所有被选中的单元格对象，因为单元格可以拖动多选
        for a in self.table.selectedItems():
            print(a.text(),end=',')
    def search (self):
        lineValue=self.line.text()
        if self.result_globo!=None:
            for a in self.result_globo:
                a.setBackground(Qt.GlobalColor.white)
        self.result_globo=self.table.findItems(lineValue,Qt.MatchFlag.MatchContains) # 返回包含搜索词的item list
        print('='*20)
        for a in self.result_globo:
            a.setBackground(Qt.GlobalColor.red) # 搜到的标红
        self.table.scrollToItem(self.result_globo[0],QTableWidget.ScrollHint.PositionAtTop) # 滚动到指定单元格对象，并对齐其顶部
        
"""
###项目###
设计一个展示几十万数据不卡的表格
###项目###
###技巧###
利用分页，一页就展示十个，点击下一页后再将下一个分页的数据逐一替换本页面的元素
列表切片data[0:11]
###技巧###
import math
# 浮点数向上取整
print(math.ceil(3.14))  # 输出: 4
"""
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec() 