from PySide6.QtWidgets import QApplication,QWidget,QListWidget,QVBoxLayout,QListWidgetItem,QWidgetAction
from faker import Faker
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
#from Ui_计算器 import Ui_Form
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setupUi(self) 
        self.fake=Faker(locale='zh_CN') # 人名生成对象的初始化
        self.listWidet=QListWidget()
        self.mainLayout=QVBoxLayout()
        self.mainLayout.addWidget(self.listWidet)
        # for a in range(20):
        #     self.listWidet.addItem(self.fake.name())
        #     # 或 # self.listWidet.addItem(QListWidgetItem(self.fake.name()))
        self.listWidet.addItems([self.fake.name() for a in range(6)])
        self.listWidet.insertItem(0,'zjp') # （位置，和内容）
        #或# self.listWidet.insertItem(0,QListWidgetItem('zjp'))
        self.listWidet.insertItems(1,['123','456','789','159','753'])
        self.listWidet.takeItem(0) # 删除
        Item=self.listWidet.item(0) # 获取元素
        Item.setText('忐忐忑忑突突突') # 改元素
        result=self.listWidet.findItems('张',Qt.MatchFlag.MatchContains) # 查出所有包含张的
        for a in result:
            try:
                print(a.text()) # 拿到查找结果 
            except Exception as e:
                print(e)
        """
        类似的还有:
        MatchStartWith 以XX开头
        MatchEndWith 以XX结尾
        MatchRegularExpression 以正则表达式搜索
        """
        print(self.listWidet.count()) # 元素个数
        # self.listWidet.clear() 清空
        self.setLayout(self.mainLayout)
        self.listWidet.currentItemChanged.connect(self.Changed_to_who)
        # scrollToitem() 给定一个值后，列表的滑动条滚动到指定元素
        # itemDoubleClicked()双击的信号
        # self.listWidet.sortItems(Qt.SortOrder.AscendingOrder)# 升序排列 如1 111 12 21 202
        # self.listWidet.sortItems(Qt.SortOrder.DescendingOrder) # 降序
        self.Hello=QAction('hello')
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu) # 表示该窗口部件的右键菜单将由其所有的QAction对象组成。也就是说，当你在这个窗口部件上右击时，会弹出一个包含所有已添加动作的上下文菜单。
        self.addAction(self.Hello)
        self.Hello.triggered.connect(lambda:print('hello'))

        self.choose=QAction('输出选中的值')
        self.listWidet.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listWidet.addAction(self.choose)
        self.choose.triggered.connect(self.showChoose)

        self.deleteItem=QAction('删除当前元素')
        self.listWidet.addAction(self.deleteItem)
        self.deleteItem.triggered.connect(lambda:self.listWidet.takeItem(self.listWidet.currentRow())) # 当前选择的行

        self.listWidet.item(0).setCheckState(Qt.CheckState.Unchecked)
        self.listWidet.item(1).setCheckState(Qt.CheckState.Unchecked)
        self.listWidet.itemChanged.connect(lambda:print(f'选中了')) # 任意一个选项状态变化
        self.listWidet.itemChanged.connect(self.ifListChecked)
    def ifListChecked(self):
        state=self.listWidet.item(1).checkState() # 有CheckState.Unchecked和CheckState.Checked两种返回值
        if state==Qt.CheckState.Checked:
            print('你已勾选第二个选项')
    def showChoose(self):
        print(self.listWidet.currentItem().text()) # 当前选中元素的文字
    def Changed_to_who(self,item,previous):
        # print(self.listWidet.currentItem().text())
        print(item.text()) # 和上面一样
        print('previous:',previous.text()) # 上一个选中的
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()