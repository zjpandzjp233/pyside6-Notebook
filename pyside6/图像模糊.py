from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QFileDialog,QSlider,QLabel
from PySide6.QtCore import Qt
from PIL import Image, ImageFilter, ImageQt
# from PySide6.QtGui import QPixmap 如果不用pillow，可以这样设置lable的照片，
# self.myLable.setPixmap(QPixmap('路径'))
width=0
height=0
class Mywindow(QWidget):
    def __init__(self): 
        super().__init__()
        self.resize(600,600)
        self.mybutton=QPushButton('点我导入图片。')
        self.mybutton.setEnabled(False) # 禁用按钮
        self.myImglable=QLabel()
        self.myImglable.setScaledContents(True) # 使图片伸缩为lable的尺寸
        self.mySlider=QSlider(Qt.Orientation.Horizontal)
        self.mySlider.setRange(0,50)
        self.mySlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.mySlider.setTickInterval(5)
        self.mainLayout=QVBoxLayout()
        self.mainLayout.addWidget(self.mybutton)
        self.mainLayout.addWidget(self.myImglable)
        self.mainLayout.addWidget(self.mySlider)
        self.setLayout(self.mainLayout)
        self.mybutton.clicked.connect(self.getImg)
        self.mySlider.valueChanged.connect(self.slidervalue)
    def getImg(self):
        self.img=Image.open(QFileDialog.getOpenFileName(self,'选择图像','.','图像文件(*.jpg *.png)')[0]) # 用的pillow库来打开浏览文件
        width, height = self.img.size # 获取图片分辨率
        if width>500 or width>500:
            while width>500 or height>500: # 等比例缩放分辨率 ，不缩放会导致图像巨大无比
                width/=1.2
                height/=1.2
        self.myImglable.setMaximumSize(int(width), int(height)) # 设置lable的最大尺寸为等比例缩放后的大小，于是图片就会缩放为等比例缩小后的尺寸
        self.myImglable.setPixmap(ImageQt.toqpixmap(self.img)) # 用pillow库将图片变成qt里的lable的setPixmap可以识别的格式
    def slidervalue(self,value):
        try:
            if self.img != None:
                self.bluredPic=self.img.filter(ImageFilter.GaussianBlur(value)) # 高斯模糊
                self.myImglable.setPixmap(ImageQt.toqpixmap(self.bluredPic))
            else:
                return
        except Exception as e:
            print('Exception:',e)
            return
if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()
