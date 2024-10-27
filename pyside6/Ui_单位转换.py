# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '单位转换.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLayout,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(370, 130)
        widget.setMaximumSize(QSize(400, 130))
        widget.setStyleSheet(u"/* \u8bbe\u7f6e\u7a97\u53e3\u80cc\u666f\u989c\u8272 */\n"
"QWidget {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u6807\u7b7e\u6837\u5f0f */\n"
"QLabel {\n"
"    color: #333333; /* \u6587\u5b57\u989c\u8272 */\n"
"    font-size: 16px; /* \u5b57\u4f53\u5927\u5c0f */\n"
"    padding: 10px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton {\n"
"    border-radius: 19px; /* \u5706\u89d2\u534a\u5f84 */\n"
"    background-color: #EDEDED; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: #333333; /* \u6587\u5b57\u989c\u8272 */\n"
"    font-size: 14px; /* \u5b57\u4f53\u5927\u5c0f */\n"
"    padding: 8px 16px; /* \u5185\u8fb9\u8ddd */\n"
"    margin: 10px; /* \u5916\u8fb9\u8ddd */\n"
"}\n"
"\n"
"/* \u6309\u94ae\u60ac\u505c\u6548\u679c */\n"
"QPushButton:hover {\n"
"    background-color: #DADADA;\n"
"}\n"
"\n"
"/* \u6309\u94ae\u6309\u4e0b\u6548\u679c */\n"
"QPushButton:pressed {\n"
"    background-color: #CFCFCF;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lengthOrWeight = QComboBox(widget)
        self.lengthOrWeight.setObjectName(u"lengthOrWeight")
        self.lengthOrWeight.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(11)
        self.lengthOrWeight.setFont(font)
        self.lengthOrWeight.setStyleSheet(u"color: rgb(255, 0, 4);")

        self.verticalLayout.addWidget(self.lengthOrWeight)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.input1 = QLineEdit(widget)
        self.input1.setObjectName(u"input1")
        self.input1.setMinimumSize(QSize(0, 30))
        self.input1.setStyleSheet(u"color:rgb(255, 0, 255);font: 9pt \"\u5e7c\u5706\";")

        self.horizontalLayout.addWidget(self.input1)

        self.option1 = QComboBox(widget)
        self.option1.setObjectName(u"option1")
        self.option1.setMinimumSize(QSize(0, 30))
        self.option1.setStyleSheet(u"color: rgb(73, 255, 17);")

        self.horizontalLayout.addWidget(self.option1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input2 = QLineEdit(widget)
        self.input2.setObjectName(u"input2")
        self.input2.setMinimumSize(QSize(0, 30))
        self.input2.setStyleSheet(u"color:rgb(255, 0, 255);font: 9pt \"\u5e7c\u5706\";")

        self.horizontalLayout_2.addWidget(self.input2)

        self.option2 = QComboBox(widget)
        self.option2.setObjectName(u"option2")
        self.option2.setMinimumSize(QSize(0, 30))
        self.option2.setStyleSheet(u"\n"
"color: rgb(0, 255, 127);")

        self.horizontalLayout_2.addWidget(self.option2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u5355\u4f4d\u8f6c\u6362", None))
    # retranslateUi

