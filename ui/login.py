# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(359, 351)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 40, 251, 241))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.User_label = QLabel(self.layoutWidget)
        self.User_label.setObjectName(u"User_label")
        font = QFont()
        font.setPointSize(10)
        self.User_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.User_label)

        self.user_name_LE = QLineEdit(self.layoutWidget)
        self.user_name_LE.setObjectName(u"user_name_LE")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.user_name_LE)

        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.password_label)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.frame)

        self.password_LE = QLineEdit(self.layoutWidget)
        self.password_LE.setObjectName(u"password_LE")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.password_LE)

        self.login_Btn = QPushButton(self.layoutWidget)
        self.login_Btn.setObjectName(u"login_Btn")
        self.login_Btn.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.login_Btn)

        self.Signup_Btn = QPushButton(self.layoutWidget)
        self.Signup_Btn.setObjectName(u"Signup_Btn")
        self.Signup_Btn.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.Signup_Btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(7, QFormLayout.FieldRole, self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 359, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.User_label.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.login_Btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Signup_Btn.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
    # retranslateUi

