from PySide6.QtWidgets import QApplication,QPushButton,QLabel,QLineEdit,QWidget

from Ui_计算器 import Ui_Form
class Mywindow(QWidget,Ui_Form):
    result:str=''
    result_last=''
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.bind()
    def bind(self):
        self.p0.clicked.connect(lambda:self.addExpression('0'))
        self.p1.clicked.connect(lambda:self.addExpression('1'))
        self.p2.clicked.connect(lambda:self.addExpression('2'))
        self.p3.clicked.connect(lambda:self.addExpression('3'))
        self.p4.clicked.connect(lambda:self.addExpression('4'))
        self.p5.clicked.connect(lambda:self.addExpression('5'))
        self.p6.clicked.connect(lambda:self.addExpression('6'))
        self.p7.clicked.connect(lambda:self.addExpression('7'))
        self.p8.clicked.connect(lambda:self.addExpression('8'))
        self.p9.clicked.connect(lambda:self.addExpression('9'))
        self.pAdd.clicked.connect(lambda:self.addExpression('+'))
        self.pCompute.clicked.connect(lambda:self.addExpression('='))
        self.pDe.clicked.connect(lambda:self.addExpression('-'))
        self.pMuti.clicked.connect(lambda:self.addExpression('*'))
        self.pDivide.clicked.connect(lambda:self.addExpression('/'))
        self.pBack.clicked.connect(lambda:self.addExpression('#'))
        self.pClear.clicked.connect(lambda:self.addExpression('^'))
    def addExpression(self,e):
        if e=='=':
            try:
                result_num=eval(self.result)
                result_num=round(result_num, 15)
                result_num=str(result_num)
                self.result_last=result_num
                self.showScreen.clear()
                self.showScreen.setText(result_num)
                self.result=''
            except Exception as e:
                self.result=''
                self.showScreen.setText('计算错误')
        elif e=='#':
            self.result=self.result[:-1]
            self.showScreen.setText(self.result)
            self.result_last=''
        elif e=='^':
            self.showScreen.clear()
            self.result=''
            self.result_last=''
            self.showScreen.setText(self.result)
        elif (e=='+' or e=='-' or e=='/' or e=='*') and (self.result_last!=''):
            self.showScreen.clear()
            self.result+=(self.result_last+e)
            self.showScreen.setText(self.result)
            self.result_last=''
        else:
            self.result+=e
            self.showScreen.clear()
            self.showScreen.setText(self.result)


if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()