# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
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


class Ui_awsDialog(object):
    def setupUi(self, awsDialog):
        if not awsDialog.objectName():
            awsDialog.setObjectName(u"awsDialog")
        awsDialog.resize(802, 555)
        font = QFont()
        font.setPointSize(10)
        awsDialog.setFont(font)
        self.S3Widget = QTreeWidget(awsDialog)
        self.S3Widget.setObjectName(u"S3Widget")
        self.S3Widget.setGeometry(QRect(30, 80, 501, 381))
        self.awsConfig_PB = QPushButton(awsDialog)
        self.awsConfig_PB.setObjectName(u"awsConfig_PB")
        self.awsConfig_PB.setGeometry(QRect(580, 230, 161, 28))
        self.awsConfig_PB.setFont(font)
        self.CreateBucket_PB = QPushButton(awsDialog)
        self.CreateBucket_PB.setObjectName(u"CreateBucket_PB")
        self.CreateBucket_PB.setGeometry(QRect(580, 20, 161, 28))
        self.CreateBucket_PB.setFont(font)
        self.ShowBucket_PB = QPushButton(awsDialog)
        self.ShowBucket_PB.setObjectName(u"ShowBucket_PB")
        self.ShowBucket_PB.setGeometry(QRect(580, 80, 161, 28))
        self.ShowBucket_PB.setFont(font)
        self.DownloadObject_PB = QPushButton(awsDialog)
        self.DownloadObject_PB.setObjectName(u"DownloadObject_PB")
        self.DownloadObject_PB.setGeometry(QRect(580, 130, 161, 28))
        self.DownloadObject_PB.setFont(font)
        self.UplpadObject_PB = QPushButton(awsDialog)
        self.UplpadObject_PB.setObjectName(u"UplpadObject_PB")
        self.UplpadObject_PB.setGeometry(QRect(580, 480, 161, 28))
        self.UplpadObject_PB.setFont(font)
        self.DeleteObject_PB = QPushButton(awsDialog)
        self.DeleteObject_PB.setObjectName(u"DeleteObject_PB")
        self.DeleteObject_PB.setGeometry(QRect(580, 180, 161, 28))
        self.BucketName_LE = QLineEdit(awsDialog)
        self.BucketName_LE.setObjectName(u"BucketName_LE")
        self.BucketName_LE.setGeometry(QRect(30, 20, 501, 22))
        self.UploadObjName_LE = QLineEdit(awsDialog)
        self.UploadObjName_LE.setObjectName(u"UploadObjName_LE")
        self.UploadObjName_LE.setGeometry(QRect(30, 490, 501, 22))

        self.retranslateUi(awsDialog)

        QMetaObject.connectSlotsByName(awsDialog)
    # setupUi

    def retranslateUi(self, awsDialog):
        awsDialog.setWindowTitle(QCoreApplication.translate("awsDialog", u"Dialog", None))
        ___qtreewidgetitem = self.S3Widget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("awsDialog", u"Date", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("awsDialog", u"Object Name", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("awsDialog", u"S. No", None));
        self.awsConfig_PB.setText(QCoreApplication.translate("awsDialog", u"Config AWS", None))
        self.CreateBucket_PB.setText(QCoreApplication.translate("awsDialog", u"Create Bucket", None))
        self.ShowBucket_PB.setText(QCoreApplication.translate("awsDialog", u"Show Bucket", None))
        self.DownloadObject_PB.setText(QCoreApplication.translate("awsDialog", u"Download Object", None))
        self.UplpadObject_PB.setText(QCoreApplication.translate("awsDialog", u"Upload Object", None))
        self.DeleteObject_PB.setText(QCoreApplication.translate("awsDialog", u"Delete Object", None))
    # retranslateUi

