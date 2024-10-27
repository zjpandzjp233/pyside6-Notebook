# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_translation(object):
    def setupUi(self, translation):
        if not translation.objectName():
            translation.setObjectName(u"translation")
        translation.resize(998, 338)
        translation.setMaximumSize(QSize(1200, 338))
        self.groupBox = QGroupBox(translation)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 431, 321))
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 70, 421, 211))
        self.plainTextEdit.setCenterOnScroll(False)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 280, 421, 41))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 401, 21))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ko = QRadioButton(self.widget)
        self.ko.setObjectName(u"ko")

        self.horizontalLayout.addWidget(self.ko)

        self.ru = QRadioButton(self.widget)
        self.ru.setObjectName(u"ru")

        self.horizontalLayout.addWidget(self.ru)

        self.ja = QRadioButton(self.widget)
        self.ja.setObjectName(u"ja")

        self.horizontalLayout.addWidget(self.ja)

        self.cn = QRadioButton(self.widget)
        self.cn.setObjectName(u"cn")
        self.cn.setChecked(True)

        self.horizontalLayout.addWidget(self.cn)

        self.en = QRadioButton(self.widget)
        self.en.setObjectName(u"en")

        self.horizontalLayout.addWidget(self.en)

        self.groupBox_2 = QGroupBox(translation)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(530, 10, 441, 321))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 30, 261, 22))
        self.plainTextEdit2 = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit2.setObjectName(u"plainTextEdit2")
        self.plainTextEdit2.setGeometry(QRect(3, 73, 431, 241))
        self.label = QLabel(translation)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1000, 20, 171, 261))
        self.label.setPixmap(QPixmap(u"pyside6/src/dlls/5915124c0d98f57c84c002c1bbf89a8.png"))
        self.label.setScaledContents(True)
        self.cD = QPushButton(translation)
        self.cD.setObjectName(u"cD")
        self.cD.setGeometry(QRect(990, 300, 191, 31))

        self.retranslateUi(translation)

        QMetaObject.connectSlotsByName(translation)
    # setupUi

    def retranslateUi(self, translation):
        translation.setWindowTitle(QCoreApplication.translate("translation", u"\u5218\u4fca\u4e13\u7528\u7ffb\u8bd1", None))
        self.groupBox.setTitle(QCoreApplication.translate("translation", u"\u8f93\u5165\u8bed\u8a00", None))
        self.plainTextEdit.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("translation", u"\u7ffb\u8bd1", None))
        self.ko.setText(QCoreApplication.translate("translation", u"\u97e9\u8bed", None))
        self.ru.setText(QCoreApplication.translate("translation", u"\u4fc4\u8bed", None))
        self.ja.setText(QCoreApplication.translate("translation", u"\u65e5\u8bed", None))
        self.cn.setText(QCoreApplication.translate("translation", u"\u6c49\u8bed", None))
        self.en.setText(QCoreApplication.translate("translation", u"\u82f1\u8bed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("translation", u"\u8f93\u51fa\u7ed3\u679c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("translation", u"\u82f1\u8bed", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("translation", u"\u4fc4\u8bed", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("translation", u"\u97e9\u8bed", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("translation", u"\u65e5\u8bed", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("translation", u"\u4e2d\u6587", None))

        self.label.setText("")
        self.cD.setText(QCoreApplication.translate("translation", u"\u70b9\u51fb\u67e5\u770b\u4eba\u7269\u8bf4\u660e", None))
    # retranslateUi

