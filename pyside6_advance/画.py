from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PySide6.QtGui import QPainter,QColor,QFont,QPen,QPolygon,QImage,QBrush
from PySide6.QtCore import Qt,QRect,QPoint
import math
import os
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))# 将工作目录设置为代码所在的文件夹里面，不然就在vscode选择打开的文件夹上
        """
        os.path.abspath(__file__) 获取当前脚本的绝对路径。
        os.path.dirname(os.path.abspath(__file__)) 获取当前脚本所在目录的路径。
        os.chdir(os.path.dirname(os.path.abspath(__file__))) 将当前工作目录改变为上述获取的目录
        """
        # self.setupUi(self) 
        self.resize(600,600)
        self.text='红'
    def paintEvent(self,event): #自带的函数
        painter=QPainter(self)
        painter.setPen(QColor(0,0,0))
        painter.setFont(QFont('SimSun',25)) # 字体和字高
        # 画文字
        # painter.drawText(event.rect(),Qt.AlignmentFlag.AlignCenter,self.text)# event.rect()说明我们绘画在一个矩形区域
        
        # 画sin
        sizes=self.size()
        y=sizes.height()//2
        x=sizes.width()//2
        """
        PySide中，窗口内部的坐标系统是以像素为单位的笛卡尔坐标系。
        原点 (0, 0) 位于窗口的左上角，向右方向为 x 轴正方向，向下方向为 y 轴正方向。
        """
        # for i in range(600):
        #     x1=i/3
        #     y1=math.sin(math.tau/600*i)*100
        #     painter.drawPoint(x+x1,y+y1)# 平移图像

        pen1=QPen(Qt.red,3,Qt.CustomDashLine) #创建笔 3是笔宽度
        pen1.setDashPattern([10,2,5,2])# 画10个像素再空2个像素，再画5个空2个
        """
        Qt.SolidLine：实线。
        Qt.DashLine：虚线。
        Qt.DotLine：点线。
        Qt.DashDotLine：虚点线（先虚线后点线）。
        Qt.DashDotDotLine：虚点点线（先虚线后点点线）。
        Qt.CustomDashLine：自定义虚线样式。
        """
        # 画直线
        painter2=QPainter(self)
        painter2.setPen(pen1)
        painter2.drawLine(x,y,x+100,y+100)
        # 画弧线
        """
        QRect(int x, int y, int width, int height)：
        x：矩形左上角的 x 坐标。
        y：矩形左上角的 y 坐标。
        width：矩形的宽度。
        height：矩形的高度
        """
        # 从3点钟方向开始画的，逆时针
        rect1=QRect(x,y,100,100)
        painter2.drawArc(rect1,0,30*16) # 参数分别是矩形区域，起始alen，结束alen,16alen=1度
        # painter2.drawChord(0,0,200,200,0,60*16) # 带弦的弧
        painter2.drawPie(0,0,200,200,0,60*16) # 扇形
        painter2.drawEllipse(200,200,300,100)# 椭圆 坐标与宽高

        # 点对象
        point1=QPoint(250,250)
        point2=QPoint(50,0)
        point3=QPoint(250,25)
        point4=QPoint(25,25)
        point5=QPoint(20,100)
        # 多边形
        poly=QPolygon([point1,point2,point3,point4,point5]) # 逐点相连
        painter2.drawPolygon(poly)
        #绘制图片
        images=QImage('../5915124c0d98f57c84c002c1bbf89a8.png')
        rect2=QRect(300,0,images.width()//2,images.height()//3)
        painter2.drawImage(rect2,images)
        # images.save(r"C:\Users\机械革命\Desktop\lj.jpg",'JPEG',1)# 保存路径，格式 压缩率 ，仅对jpeg有效

        # 画实心图案
        painter3=QPainter()
        painter3.begin(self)
        brush=QBrush(Qt.SolidPattern)# 还有Dense1Pattern和Dense2Pattern,Dense3Pattern,HorPattern
        painter3.setBrush(brush)
        painter3.drawRect(500,500,600,600)
        painter3.end()

if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()