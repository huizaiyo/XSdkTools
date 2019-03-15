# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyAndroidPackage_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName(_fromUtf8("frmMain"))
        frmMain.resize(1000, 600)
        frmMain.setStyleSheet(_fromUtf8("* {\n"
"font-family:\'微软雅黑\';\n"
"color:white;\n"
"}\n"
"\n"
"QToolButton[objectName=\"closeToolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closeToolButton\"]:hover {\n"
"image: url(:/background/open_over.png);\n"
"}\n"
"QToolButton[objectName=\"closeToolButton\"]:pressed {\n"
"image: url(:/background/open_over.png);\n"
"}\n"
"\n"
"QToolButton::hover{\n"
"border:0px;\n"
"}"))
        self.centralwidget = QtGui.QWidget(frmMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 71))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/background/funcellimg_01.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/background/funcellimg_02.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 70, 265, 531))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/background/version.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(270, 150, 731, 451))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.page_5)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(-10, 399, 741, 51))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_9 = QtGui.QLabel(self.page_5)
        self.label_9.setGeometry(QtCore.QRect(70, 40, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.page_5)
        self.label_10.setGeometry(QtCore.QRect(240, 40, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.page_5)
        self.label_11.setGeometry(QtCore.QRect(70, 80, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.page_5)
        self.label_12.setGeometry(QtCore.QRect(240, 80, 54, 12))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(70, 120, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.page_5)
        self.label_14.setGeometry(QtCore.QRect(240, 120, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.page_5)
        self.label_15.setGeometry(QtCore.QRect(70, 160, 54, 12))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.page_5)
        self.label_16.setGeometry(QtCore.QRect(240, 160, 141, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.page_5)
        self.label_17.setGeometry(QtCore.QRect(70, 200, 54, 12))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit = QtGui.QLineEdit(self.page_5)
        self.lineEdit.setGeometry(QtCore.QRect(240, 195, 181, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.page_5)
        self.pushButton.setGeometry(QtCore.QRect(430, 193, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_18 = QtGui.QLabel(self.page_5)
        self.label_18.setGeometry(QtCore.QRect(70, 240, 54, 12))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lineEdit_2 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 230, 181, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.page_5)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 230, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_19 = QtGui.QLabel(self.page_5)
        self.label_19.setGeometry(QtCore.QRect(70, 280, 54, 12))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lineEdit_3 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 270, 181, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_3 = QtGui.QPushButton(self.page_5)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 267, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.stackedWidget.addWidget(self.page_6)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 70, 240, 82))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/background/sm_img_03.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 70, 240, 82))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/background/btn_07.png")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(750, 70, 240, 82))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8(":/background/btn_08.png")))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.closeToolButton = QtGui.QToolButton(self.centralwidget)
        self.closeToolButton.setGeometry(QtCore.QRect(930, 0, 52, 62))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/background/btn_04.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeToolButton.setIcon(icon)
        self.closeToolButton.setIconSize(QtCore.QSize(52, 62))
        self.closeToolButton.setObjectName(_fromUtf8("closeToolButton"))
        frmMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(_translate("frmMain", "MainWindow", None))
        self.label_4.setText(_translate("frmMain", "下一步", None))
        self.label_9.setText(_translate("frmMain", "产品状态", None))
        self.label_10.setText(_translate("frmMain", "已上线", None))
        self.label_11.setText(_translate("frmMain", "AppId", None))
        self.label_12.setText(_translate("frmMain", "100", None))
        self.label_13.setText(_translate("frmMain", "AppKey", None))
        self.label_14.setText(_translate("frmMain", "1000", None))
        self.label_15.setText(_translate("frmMain", "通知地址", None))
        self.label_16.setText(_translate("frmMain", "www.haowan123.com", None))
        self.label_17.setText(_translate("frmMain", "母包地址", None))
        self.pushButton.setText(_translate("frmMain", "选择", None))
        self.label_18.setText(_translate("frmMain", "输出路径", None))
        self.pushButton_2.setText(_translate("frmMain", "选择", None))
        self.label_19.setText(_translate("frmMain", "签名文件", None))
        self.pushButton_3.setText(_translate("frmMain", "配置", None))
        self.closeToolButton.setText(_translate("frmMain", "...", None))

import img_rc
import res_rc
