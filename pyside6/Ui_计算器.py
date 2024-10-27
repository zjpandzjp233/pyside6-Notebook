# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '计算机.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(420, 428)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(600, 600))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.showScreen = QLineEdit(Form)
        self.showScreen.setObjectName(u"showScreen")
        self.showScreen.setMinimumSize(QSize(400, 50))
        self.showScreen.setMaximumSize(QSize(25, 16777215))
        self.showScreen.setReadOnly(True)

        self.verticalLayout.addWidget(self.showScreen)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pCompute = QPushButton(Form)
        self.pCompute.setObjectName(u"pCompute")
        self.pCompute.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pCompute, 3, 2, 1, 1)

        self.p8 = QPushButton(Form)
        self.p8.setObjectName(u"p8")
        self.p8.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p8, 2, 1, 1, 1)

        self.p0 = QPushButton(Form)
        self.p0.setObjectName(u"p0")
        self.p0.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p0, 3, 0, 1, 1)

        self.p9 = QPushButton(Form)
        self.p9.setObjectName(u"p9")
        self.p9.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p9, 2, 2, 1, 1)

        self.p7 = QPushButton(Form)
        self.p7.setObjectName(u"p7")
        self.p7.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p7, 2, 0, 1, 1)

        self.p5 = QPushButton(Form)
        self.p5.setObjectName(u"p5")
        self.p5.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p5, 1, 1, 1, 1)

        self.pDot = QPushButton(Form)
        self.pDot.setObjectName(u"pDot")
        self.pDot.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pDot, 3, 1, 1, 1)

        self.p2 = QPushButton(Form)
        self.p2.setObjectName(u"p2")
        self.p2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p2, 0, 1, 1, 1)

        self.p4 = QPushButton(Form)
        self.p4.setObjectName(u"p4")
        self.p4.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p4, 1, 0, 1, 1)

        self.pDe = QPushButton(Form)
        self.pDe.setObjectName(u"pDe")
        self.pDe.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pDe, 1, 3, 1, 1)

        self.pMuti = QPushButton(Form)
        self.pMuti.setObjectName(u"pMuti")
        self.pMuti.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pMuti, 2, 3, 1, 1)

        self.p3 = QPushButton(Form)
        self.p3.setObjectName(u"p3")
        self.p3.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p3, 0, 2, 1, 1)

        self.pAdd = QPushButton(Form)
        self.pAdd.setObjectName(u"pAdd")
        self.pAdd.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pAdd, 0, 3, 1, 1)

        self.pDivide = QPushButton(Form)
        self.pDivide.setObjectName(u"pDivide")
        self.pDivide.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pDivide, 3, 3, 1, 1)

        self.p1 = QPushButton(Form)
        self.p1.setObjectName(u"p1")
        self.p1.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p1, 0, 0, 1, 1)

        self.p6 = QPushButton(Form)
        self.p6.setObjectName(u"p6")
        self.p6.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.p6, 1, 2, 1, 1)

        self.pBack = QPushButton(Form)
        self.pBack.setObjectName(u"pBack")
        self.pBack.setMinimumSize(QSize(100, 50))
        self.pBack.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.pBack, 4, 0, 1, 1)

        self.pClear = QPushButton(Form)
        self.pClear.setObjectName(u"pClear")
        self.pClear.setMinimumSize(QSize(100, 50))

        self.gridLayout.addWidget(self.pClear, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.pCompute.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.p8.setText(QCoreApplication.translate("Form", u"8", None))
        self.p0.setText(QCoreApplication.translate("Form", u"0", None))
        self.p9.setText(QCoreApplication.translate("Form", u"9", None))
        self.p7.setText(QCoreApplication.translate("Form", u"7", None))
        self.p5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pDot.setText(QCoreApplication.translate("Form", u".", None))
        self.p2.setText(QCoreApplication.translate("Form", u"2", None))
        self.p4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pDe.setText(QCoreApplication.translate("Form", u"-", None))
        self.pMuti.setText(QCoreApplication.translate("Form", u"*", None))
        self.p3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pAdd.setText(QCoreApplication.translate("Form", u"+", None))
        self.pDivide.setText(QCoreApplication.translate("Form", u"/", None))
        self.p1.setText(QCoreApplication.translate("Form", u"1", None))
        self.p6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pBack.setText(QCoreApplication.translate("Form", u"\u56de\u9000", None))
        self.pClear.setText(QCoreApplication.translate("Form", u"\u6e05\u5c4f", None))
    # retranslateUi

