from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QSlider,QCheckBox,QVBoxLayout # 垂直布局
from PySide6.QtWidgets import QRadioButton,QButtonGroup
# from Ui_textedit import Ui_Form
from PySide6.QtCore import Qt
# from Ui_简单radio选项 import Ui_Form
html1="""
<h1>hello</h1>
<h>world<h>
"""
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)

        cb=QComboBox(self) # 可以设置placeHolder
        cb.addItems(['11','22','33']) # 给combo添加项
        cb.currentIndexChanged.connect(lambda:print(cb.currentText())) # 选框变化时输出变化后的选项
        cb.removeItem(0) # 删除第一个选项

        # cb=QCheckBox('是否选中')
        # cb.stateChanged.connect(lambda:print('checked')) # 每次点选都输出checked  信号会默认传递状态0、2，槽可以接收，
        # print(cb.isChecked()) #True 或 False
        # cb.stateChanged.connect(self.showState)# 0表示没有选上，2表示选了 # cb.stateChanged.connect()默认传递一个参数给showState
        # mainlayout=QVBoxLayout()
        # mainlayout.addWidget(cb)
        # self.setLayout(mainlayout)

        # qr=QRadioButton(self,'检测是否按下.')
        # qr.clicked.connect(lambda:print(qr.isChecked()) )# 是否被按下
        # radio可以gruopbox来给radio分组
        # self.bG=QButtonGroup()
        # self.bG.addButton(self.China)
        # self.bG.addButton(self.japan)
        # self.bG.buttonClicked.connect(self.bottonGruopChange) # 按钮组任何按钮被按下发出信号
        
        # self.textEdit.setHtml(html1) # 给富文本编辑框加html元素
        # self.textEdit.setMarkdown('# 这是一个大标题') # 设置markdown格式文本
        # self.textEdit.setText('123456') # 给富文本设置纯文本
        # self.plainTextEdit.setPlainText('456789699969966986/969896*9')# 非富文本设置文本内容
        # self.textEdit.append('appended') # 追加文本
        # self.plainTextEdit.appendPlainText('appendPlainText')
        # self.plainTextEdit.clear() # 清空
        # self.textEdit.insertHtml(html1)# 插入html到最前面
        # self.textEdit.append(html1) # 插入html在后面
        # self.textEdit.textChanged.connect() # 文本变化信号

        slider1=QSlider(self,Qt.Orientation.Horizontal) # 创建垂直滑条
        
        slider1.setTickPosition(QSlider.TickPosition.TicksBelow) # 刻度位置
        slider1.setTickInterval(20) # 刻度间距
        slider1.setMinimum(0)
        slider1.setMaximum(200)# 设置最大最小值
        # 信号描述
        # valueChanged在滑块的值更改时发出的（）。
        # sliderPressed用户开始拖动滑块时发出的（）。
        # sliderMoved用户拖动滑块时发出的（）。
        # sliderReleased用户释放滑块时发出的（）。
        slider1.setObjectName('slider1')
        slider1.valueChanged.connect(self.sharedSlot) # 默认传递一个参数,滑条的数值
    def sharedSlot(self,value):
        print(self.sender().objectName()) # 但信号发送过来时，打印发信号那方的名字，用于多个控件调用同一个函数时的区分
        print(f'滑条当前值为：{value}')

    def bottonGruopChange(self):
        print(self.bG.checkedButton().objectName()) # 返回按钮组里面的被选中的按钮名字 # 也可以.text()来获取按钮上的标签
    def showState(self,name):
        print(name)
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()

