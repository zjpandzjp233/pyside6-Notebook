from PySide6.QtWidgets import QApplication,QPushButton,QLabel,QLineEdit,QDialog
from PySide6.QtCore import Qt
from Ui_登录框 import Ui_Dialog
class Mywindow(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.loginFuc) # pushButton名字可以在editer里面查看
    def loginFuc(self):
        account=self.lineEdit.text()
        passWord=self.lineEdit_2.text()
        if account=='123456' and passWord=='123456':
            print('登录成功')
        else :
            print('登录失败')



if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()