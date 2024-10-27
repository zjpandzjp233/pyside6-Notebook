# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '设置菜单栏.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self.action3 = QAction(MainWindow)
        self.action3.setObjectName(u"action3")
        self.action5 = QAction(MainWindow)
        self.action5.setObjectName(u"action5")
        self.action6 = QAction(MainWindow)
        self.action6.setObjectName(u"action6")
        self.action7 = QAction(MainWindow)
        self.action7.setObjectName(u"action7")
        self.action8 = QAction(MainWindow)
        self.action8.setObjectName(u"action8")
        self.action4_2 = QAction(MainWindow)
        self.action4_2.setObjectName(u"action4_2")
        self.action0 = QAction(MainWindow)
        self.action0.setObjectName(u"action0")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menu1 = QMenu(self.menubar)
        self.menu1.setObjectName(u"menu1")
        self.menu = QMenu(self.menu1)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu1.menuAction())
        self.menu1.addAction(self.action2)
        self.menu1.addAction(self.action3)
        self.menu1.addAction(self.menu.menuAction())
        self.menu.addAction(self.action5)
        self.menu.addAction(self.action6)
        self.menu.addAction(self.action7)
        self.menu.addAction(self.action8)
        self.menu.addAction(self.action4_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action0)
        self.toolBar.addAction(self.action0)
        self.toolBar.addAction(self.action8)
        self.toolBar.addAction(self.action2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.action5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.action6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.action7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.action8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.action4_2.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.action0.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9ed1", None))
#if QT_CONFIG(shortcut)
        self.action0.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.menu1.setTitle(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

