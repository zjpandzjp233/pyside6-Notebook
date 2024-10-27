# 核心bug print(int('1.0')) 和 print(int('01.0')) 如果int改成float就没事，可以转成1.0
# 核心bug2 verify(list1, self) 和 verify(self, list1) 之间的差别很大 用第二个
import re
from PySide6.QtWidgets import QApplication,QWidget
from Ui_单位转换 import Ui_widget
class Mywindow(QWidget,Ui_widget):
    mode=1
    length={'米':100,'分米':10,'厘米':1}
    weigth={'斤':500,'千克':1000,'克':1}
    dic_all={'米':100,'分米':10,'厘米':1,'斤':500,'千克':1000,'克':1}
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.lengthOrWeight_('长度转换')
        self.lengthOrWeight.addItems(['长度转换','重量转换'])
        self.change_signal()
    def change_signal(self):
        self.lengthOrWeight.currentIndexChanged.connect(lambda:self.lengthOrWeight_(self.lengthOrWeight.currentText()))
        self.option1.currentIndexChanged.connect(self.changeCalculate2)
        self.option2.currentIndexChanged.connect(self.changeCalculate4)
        self.input1.textChanged.connect(self.changeCalculate1)
        self.input2.textChanged.connect(self.changeCalculate3) # 文本框变化
    def changeCalculate1(self):
        value1=self.input1.text()
        value2=self.input2.text()
        if not self.verify([value1,value2]):
            print('returnreturnreturnreturnreturnreturnreturnreturn')
            return
        Unit1=self.option1.currentText()
        Unit2=self.option2.currentText()
        result=self.convert_to_number(value1)*self.convert_to_number(self.dic_all[Unit1])/self.convert_to_number(self.dic_all[Unit2])
        result=str(result)
        self.input2.setText(result)
    def changeCalculate2(self):
        value1=self.input1.text()
        value2=self.input2.text()
        if not self.verify([value1,value2]):
            print('returnreturnreturnreturnreturnreturnreturnreturnreturnreturn')
            return
        Unit1=self.option1.currentText()
        Unit2=self.option2.currentText()
        result=self.convert_to_number(value1)*self.convert_to_number(self.dic_all[Unit1])/self.convert_to_number(self.dic_all[Unit2])
        result=str(result)
        self.input2.setText(result)
    def changeCalculate3(self):
        value1=self.input1.text()
        value2=self.input2.text()
        if not self.verify([value1,value2]):
            print('returnreturnreturnreturnreturnreturnreturnreturnreturn')
            return
        Unit1=self.option1.currentText()
        Unit2=self.option2.currentText()
        result=self.convert_to_number(value2)*self.convert_to_number(self.dic_all[Unit2])/self.convert_to_number(self.dic_all[Unit1])
        result=str(result)
        self.input1.setText(result)
    def changeCalculate4(self):
        value1=self.input1.text()
        value2=self.input2.text()
        if not self.verify([value1,value2]):
            print('returnreturnreturnreturnreturnreturnreturnreturnreturn')
            return
        Unit1=self.option1.currentText()
        Unit2=self.option2.currentText()
        result=self.convert_to_number(value2)*self.convert_to_number(self.dic_all[Unit2])/self.convert_to_number(self.dic_all[Unit1])
        result=str(result)
        self.input1.setText(result)
    def verify(self,list1):
        i=0
        for one in list1:
            one=str(one)
            if(re.match(r'^\+?[1-9]\d*$',one) or re.match(r'^(-?[1-9]\d*\.\d+|-?0\.\d*[1-9])$',one)) or one=='0' or one=='0.0':
                i+=1
        if i==2:
            return True
        else:
            return False
    def lengthOrWeight_(self,mode):
        if mode=='长度转换':
            self.mode=1
            self.option1.clear()
            self.option2.clear()
            self.input1.setText('0')
            self.input2.setText('0')
            self.option1.addItems(self.length.keys())
            self.option2.addItems(self.length.keys())
        else:
            self.input1.setText('0')
            self.input2.setText('0')
            self.option1.clear()
            self.option2.clear()
            self.option1.addItems(self.weigth.keys())
            self.option2.addItems(self.weigth.keys())
            self.mode=2
    def convert_to_number(self,s):
        try:
            # 首先尝试将字符串转换为浮点数
            num = float(s)
            # 检查转换后的数字是否是整数
            if num.is_integer():
                # 如果是整数，则转换为 int 类型
                return int(num)
            else:
                # 否则保持为 float 类型
                return num
        except ValueError:
            # 如果转换失败，可以抛出异常或者返回 None 或者其他默认值
            return 0  # 或者 raise ValueError("无法转换为数字")


if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()



"""
示例
浮点数示例


# 浮点数
a = 0.1
b = 0.2
c = a + b
print(c)  # 输出: 0.30000000000000004
在这个例子中，0.1 和 0.2 都是浮点数，它们的相加结果由于二进制表示的限制，产生了一个微小的舍入误差。


小数示例
from decimal import Decimal
# 小数
a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c)  # 输出: 0.3

在这个例子中，Decimal 类提供了高精度的十进制浮点数支持，避免了浮点数的舍入误差。
"""