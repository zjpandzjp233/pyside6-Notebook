# bug1 json的str必须要用""而不能用''不然不能load
# pyside6/src/dlls/5915124c0d98f57c84c002c1bbf89a8.png 在vscode里面相对路径先写代码所在文件起头，用installer后，
# pyside6/src/dlls/5915124c0d98f57c84c002c1bbf89a8.png又表示exe所在文件夹里面的pyside6文件夹里面的src/dlls/5915124c0d98f57c84c002c1bbf89a8.png
from PySide6.QtWidgets import QApplication,QWidget,QButtonGroup
import json
from Ui_translation import Ui_translation
import WebITS
import time
from WebITS import get_result
class Mywindow(QWidget,Ui_translation):
    buttonChoose='cn'
    comboChose='en'
    current_input=''
    host = "itrans.xfyun.cn"
    #初始化类
    gClass=get_result(host)
    
    dict1={'英语':'en','俄语':'ru','韩语':'ko','日语':'ja','中文':'cn'}
    result=''
    def __init__(self):
        ##示例:  host="itrans.xfyun.cn"域名形式
        super().__init__() # init里面的变量前面如果没有加self就不算成员变量，是局部变量
        self.setupUi(self) 
        self.bG=QButtonGroup()
        self.bG.addButton(self.ko)
        self.bG.addButton(self.ru)
        self.bG.addButton(self.ja)
        self.bG.addButton(self.cn)
        self.bG.addButton(self.en)
        self.changes()
    def changes(self):
        self.pushButton.clicked.connect(self.after_puttonPush)
        self.bG.buttonClicked.connect(self.bottonGruopChange)
        self.comboBox.currentIndexChanged.connect(self.comboChange) 
        self.cD.clicked.connect(self.cD_change)
    def cD_change(self):
        self.plainTextEdit.setPlainText('全八中最帅的男人。')
        self.plainTextEdit2.setPlainText('全八中最もハンサムな男の人.')
        self.current_input='@#'
    def bottonGruopChange(self):
        self.buttonChoose=self.bG.checkedButton().objectName()
        self.gClass.BusinessArgs['from']=self.buttonChoose
    def comboChange(self):
        self.comboChose=self.comboBox.currentText()
        self.comboChose=self.dict1[self.comboChose]
        self.gClass.BusinessArgs['to']=self.comboChose
        print(self.comboChose,'self.comboChose')
    def after_puttonPush(self):
        if self.plainTextEdit.toPlainText()=='':
            return
        if self.current_input=='@#':
            self.plainTextEdit.setPlainText('')
            self.plainTextEdit2.setPlainText('')
            self.current_input=''
            return
        print(self.comboChose,self.buttonChoose)
        if self.comboChose==self.buttonChoose:
            self.plainTextEdit2.setPlainText(self.plainTextEdit.toPlainText())
            return
        self.current_input=self.plainTextEdit.toPlainText()
        print('self.current_input',self.current_input)
        self.gClass.Text=self.current_input
        self.result=self.gClass.call_url()
        self.result=self.convertJson(self.result)
        print('self.result',self.result)
        self.plainTextEdit2.setPlainText(self.result)
    def convertJson(self,json_string:dict):
        dst_value = json_string['data']['result']['trans_result']['dst']
        return dst_value


if __name__=='__main__':
    app=QApplication([])
    windows=Mywindow()
    windows.show()
    app.exec()





"""
汉语普通话	cn	波斯语	fa	僧伽罗语	si
英语	en	芬兰语	fi	斯洛伐克语	sk
彝语	ii	希伯来语	he	斯洛文尼亚语	sl
广东话	yue	印地语	hi	塞尔维亚语	sr
日语	ja	克罗地亚语	hr	巽他语	su
俄语	ru	匈牙利语	hu	瑞典语	sv
法语	fr	亚美尼亚语	hy	斯瓦希里语	sw
西班牙语	es	印尼语	id	泰米尔语	ta
阿拉伯语	ar	冰岛语	is	泰卢固语	te
意大利语	it	塔加路语（菲律宾）	tl	爪哇语	jv
土耳其语	tr	罗马尼亚语	ro	马来语	ms
越南语	vi	格鲁吉亚语	ka	乌克兰语	uk
泰语	th	高棉语	km	乌尔都语	ur
韩语	ko	老挝语	lo	南非祖鲁语	zu
德语	de	立陶宛语	lt	内蒙语	mn
哈萨克语	kka	拉脱维亚语	lv	缅甸语	my
南非荷兰语	af	马拉雅拉姆语	ml	外蒙语	nm
阿姆哈拉语	am	马拉地语	mr	普什图语	ps
阿塞拜疆语	az	博克马尔挪威语	nb	豪萨语	ha
孟加拉语	bn	尼泊尔语	ne	乌兹别克语	uz
加泰罗尼亚语	ca	荷兰语	nl	土库曼语	tk
捷克语	cs	波兰语	pl	塔吉克语	tg
丹麦语	da	葡萄牙语	pt	保加利亚语	bg
希腊语	el				
#常见问题
"""