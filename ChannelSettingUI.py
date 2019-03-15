# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChannelSettingUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui  import *  
from PyQt4.QtCore import *   
import sys

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(500, 370)
        Form.setStyleSheet(_fromUtf8("QToolButton[objectName=\"closetoolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:hover {\n"
"image:url(:/images/close_hover.png);\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:pressed {\n"
"image:url(:/images/close_pressed.png);\n"
"}\n"
"\n"
"QWidget[objectName=\"widget\"]{\n"
"background-image: url(:/images/funcell_bg.png);\n"
"}\n"
"QPushButton[objectName=\"pushButton\"],QPushButton[objectName=\"pushButton_3\"],QComboBox[objectName=\"comboBox\"],QComboBox[objectName=\"comboBox_2\"],QPushButton[objectName=\"pushButton_7\"]{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton[objectName=\"pushButton_2\"],QPushButton[objectName=\"pushButton_4\"],QPushButton[objectName=\"pushButton_5\"],QPushButton[objectName=\"pushButton_6\"]{\n"
"background-color: rgb(0, 165, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox[objectName=\"checkBox\"],QCheckBox[objectName=\"checkBox_3\"],QCheckBox[objectName=\"checkBox_4\"],QCheckBox[objectName=\"checkBox_5\"]{\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"QWidget[objectName=\"Form\"],QWidget[objectName=\"parameter\"],QWidget[objectName=\"apk\"],QWidget[objectName=\"multidex\"],QWidget[objectName=\"other\"],QWidget[objectName=\"splash_icon\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget[objectName=\"listWidget\"]{\n"
"background-color:transparent;\n"
"border:0px;\n"
"}\n"
"QTextBrowser[objectName=\"textBrowser\"]{\n"
"border:0px;\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 501, 111))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 400, 31))
        self.label.setLineWidth(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.closetoolButton = QtGui.QToolButton(self.widget)
        self.closetoolButton.setGeometry(QtCore.QRect(470, 0, 27, 22))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon)
        self.closetoolButton.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 501, 301))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.apk = QtGui.QWidget()
        self.apk.setObjectName(_fromUtf8("apk"))
        self.label_4 = QtGui.QLabel(self.apk)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 51, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.apk)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 20, 140, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_9 = QtGui.QLabel(self.apk)
        self.label_9.setGeometry(QtCore.QRect(320, 20, 120, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_12 = QtGui.QLabel(self.apk)
        self.label_12.setGeometry(QtCore.QRect(60, 50, 70, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.apk)
        self.label_13.setGeometry(QtCore.QRect(320, 50, 170, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_6 = QtGui.QLineEdit(self.apk)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 50, 140, 20))
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_14 = QtGui.QLabel(self.apk)
        self.label_14.setGeometry(QtCore.QRect(320, 80, 170, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_7 = QtGui.QLineEdit(self.apk)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 80, 140, 20))
        self.lineEdit_7.setText(_fromUtf8(""))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_15 = QtGui.QLabel(self.apk)
        self.label_15.setGeometry(QtCore.QRect(60, 80, 70, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.pushButton_4 = QtGui.QPushButton(self.apk)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 230, 91, 33))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.checkBox_3 = QtGui.QCheckBox(self.apk)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 200, 121, 21))
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.lineEdit_8 = QtGui.QLineEdit(self.apk)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 110, 140, 20))
        self.lineEdit_8.setText(_fromUtf8(""))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_16 = QtGui.QLabel(self.apk)
        self.label_16.setGeometry(QtCore.QRect(60, 110, 80, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.apk)
        self.label_17.setGeometry(QtCore.QRect(320, 110, 170, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit_9 = QtGui.QLineEdit(self.apk)
        self.lineEdit_9.setGeometry(QtCore.QRect(160, 140, 140, 20))
        self.lineEdit_9.setText(_fromUtf8(""))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label_18 = QtGui.QLabel(self.apk)
        self.label_18.setGeometry(QtCore.QRect(60, 140, 95, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.apk)
        self.label_19.setGeometry(QtCore.QRect(320, 140, 170, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_26 = QtGui.QLabel(self.apk)
        self.label_26.setGeometry(QtCore.QRect(60, 170, 95, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.apk)
        self.label_27.setGeometry(QtCore.QRect(320, 170, 170, 16))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.lineEdit_13 = QtGui.QLineEdit(self.apk)
        self.lineEdit_13.setGeometry(QtCore.QRect(160, 170, 140, 20))
        self.lineEdit_13.setText(_fromUtf8(""))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.tabWidget.addTab(self.apk, _fromUtf8(""))
        self.multidex = QtGui.QWidget()
        self.multidex.setObjectName(_fromUtf8("multidex"))
        self.textBrowser = QtGui.QTextBrowser(self.multidex)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 501, 90))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.checkBox = QtGui.QCheckBox(self.multidex)
        self.checkBox.setGeometry(QtCore.QRect(50, 200, 121, 21))
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_3 = QtGui.QLabel(self.multidex)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.multidex)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 230, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_8 = QtGui.QLabel(self.multidex)
        self.label_8.setGeometry(QtCore.QRect(410, 100, 60, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_2 = QtGui.QPushButton(self.multidex)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 230, 91, 33))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_30 = QtGui.QLabel(self.multidex)
        self.label_30.setGeometry(QtCore.QRect(50, 170, 81, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.comboBox_2 = QtGui.QComboBox(self.multidex)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 170, 111, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_31 = QtGui.QLabel(self.multidex)
        self.label_31.setGeometry(QtCore.QRect(300, 170, 160, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lineEdit_14 = QtGui.QLineEdit(self.multidex)
        self.lineEdit_14.setGeometry(QtCore.QRect(170, 132, 230, 20))
        self.lineEdit_14.setText(_fromUtf8(""))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_32 = QtGui.QLabel(self.multidex)
        self.label_32.setGeometry(QtCore.QRect(50, 132, 111, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.pushButton_7 = QtGui.QPushButton(self.multidex)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 130, 75, 23))
        self.pushButton_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabWidget.addTab(self.multidex, _fromUtf8(""))
        self.splash_icon = QtGui.QWidget()
        self.splash_icon.setObjectName(_fromUtf8("splash_icon"))
        self.groupBox_2 = QtGui.QGroupBox(self.splash_icon)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 481, 191))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(140, 140, 181, 20))
        self.lineEdit_11.setText(_fromUtf8(""))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 22, 181, 20))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_24 = QtGui.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 22, 101, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(340, 20, 75, 23))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 138, 75, 23))
        self.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_25 = QtGui.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(10, 170, 411, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_28 = QtGui.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(140, 110, 111, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_29 = QtGui.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(270, 110, 201, 16))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(140, 50, 181, 20))
        self.lineEdit_12.setText(_fromUtf8(""))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_23 = QtGui.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(340, 50, 121, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_35 = QtGui.QLabel(self.groupBox_2)
        self.label_35.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(140, 80, 181, 20))
        self.lineEdit_16.setText(_fromUtf8(""))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_36 = QtGui.QLabel(self.groupBox_2)
        self.label_36.setGeometry(QtCore.QRect(340, 80, 131, 16))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.checkBox_5 = QtGui.QCheckBox(self.splash_icon)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 210, 121, 21))
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.pushButton_6 = QtGui.QPushButton(self.splash_icon)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 230, 91, 33))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.tabWidget.addTab(self.splash_icon, _fromUtf8(""))
        self.other = QtGui.QWidget()
        self.other.setObjectName(_fromUtf8("other"))
        self.groupBox = QtGui.QGroupBox(self.other)
        self.groupBox.setGeometry(QtCore.QRect(10, 19, 481, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(150, 60, 140, 20))
        self.lineEdit_10.setText(_fromUtf8(""))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(310, 30, 120, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 30, 140, 20))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(50, 60, 70, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(310, 60, 170, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 30, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(50, 90, 411, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_22 = QtGui.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(50, 110, 421, 51))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.checkBox_4 = QtGui.QCheckBox(self.other)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 200, 121, 21))
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.pushButton_5 = QtGui.QPushButton(self.other)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 230, 91, 33))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tabWidget.addTab(self.other, _fromUtf8(""))
        self.parameter = QtGui.QWidget()
        self.parameter.setObjectName(_fromUtf8("parameter"))
        self.label_2 = QtGui.QLabel(self.parameter)
        self.label_2.setGeometry(QtCore.QRect(90, 5, 301, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.parameter, _fromUtf8(""))
        
#         self.tabWidget.setStyleSheet("QTabBar::tab{min-width:30ex; min-height:10ex;}")
        self.tabWidget.setStyleSheet("QTabBar::tab{min-height:10ex;}")
        self.closetoolButton.clicked.connect(self.close)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">渠道</span></p></body></html>", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.label_4.setText(_translate("Form", "AppName", None))
        self.label_9.setText(_translate("Form", "应用安装名称", None))
        self.label_12.setText(_translate("Form", "VersionCode", None))
        self.label_13.setText(_translate("Form", "应用版本号,整形数字,如：100", None))
        self.label_14.setText(_translate("Form", "应用安装显示的版本,如：1.0", None))
        self.label_15.setText(_translate("Form", "VersionName", None))
        self.pushButton_4.setText(_translate("Form", "保存配置", None))
        self.checkBox_3.setText(_translate("Form", "使用当前配置", None))
        self.label_16.setText(_translate("Form", "MinSdkVersion", None))
        self.label_17.setText(_translate("Form", "应用安装最小值", None))
        self.label_18.setText(_translate("Form", "TargetSdkVersion", None))
        self.label_19.setText(_translate("Form", "应用安装当前值", None))
        self.label_26.setText(_translate("Form", "PackageName", None))
        self.label_27.setText(_translate("Form", "应用包名", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.apk), _translate("Form", "Apk功能", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">*-</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:10pt; color:#ff0000; background-color:#ffffff;\">方法id的数目超过65536个,需要将该dex文件拆成两个或多个,使用Multidex兼容包-*实现了一个APK包含多个dex的功能</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:10pt; color:#ff0000; background-color:#ffffff;\">*-使用本地JAR的前提是中间层未继承渠道Application-*</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:10pt; color:#ff0000; background-color:#ffffff;\">若中间层继承后请勿使用本地JAR功能</span></p></body></html>", None))
        self.checkBox.setText(_translate("Form", "使用当前配置", None))
        self.label_3.setText(_translate("Form", "单个dex方法数", None))
        self.lineEdit_2.setText(_translate("Form", "65000", None))
        self.label_8.setText(_translate("Form", "默认65000", None))
        self.pushButton_2.setText(_translate("Form", "保存配置", None))
        self.label_30.setText(_translate("Form", "使用本地JAR", None))
        self.comboBox_2.setItemText(0, _translate("Form", "False", None))
        self.comboBox_2.setItemText(1, _translate("Form", "True", None))
        self.label_31.setText(_translate("Form", "False：不使用 True：使用", None))
        self.label_32.setText(_translate("Form", "自定义Multidex文件", None))
        self.pushButton_7.setText(_translate("Form", "选择", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multidex), _translate("Form", "Multidex拆分功能", None))
        self.groupBox_2.setTitle(_translate("Form", "闪屏、ICON图片设置", None))
        self.label_24.setText(_translate("Form", "应用ICON图片路径", None))
        self.label_6.setText(_translate("Form", "应用闪屏图片路径", None))
        self.pushButton.setText(_translate("Form", "选择", None))
        self.pushButton_3.setText(_translate("Form", "选择", None))
        self.label_25.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">若配置了当前选项,则默认使用当前客户端配置的闪屏和ICON图片</span></p></body></html>", None))
        self.label_28.setText(_translate("Form", "闪屏横竖屏设置", None))
        self.comboBox.setItemText(0, _translate("Form", "landscape", None))
        self.comboBox.setItemText(1, _translate("Form", "portrait", None))
        self.label_29.setText(_translate("Form", "landscape：横屏 portrait：竖屏", None))
        self.label_7.setText(_translate("Form", "闪屏持续时长", None))
        self.label_23.setText(_translate("Form", "单位/毫秒(秒*1000)", None))
        self.label_35.setText(_translate("Form", "闪屏图片透明度", None))
        self.label_36.setText(_translate("Form", "0.0至1.0（0.5:半透明）", None))
        self.checkBox_5.setText(_translate("Form", "使用当前配置", None))
        self.pushButton_6.setText(_translate("Form", "保存配置", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.splash_icon), _translate("Form", "闪屏/ICON", None))
        self.groupBox.setTitle(_translate("Form", "文件夹拷贝", None))
        self.label_10.setText(_translate("Form", "原目录", None))
        self.label_20.setText(_translate("Form", "Target", None))
        self.label_21.setText(_translate("Form", "目标目录(apk中的相关目录)", None))
        self.label_5.setText(_translate("Form", "Source", None))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">原目录及目标目录均为文件夹路径</span></p></body></html>", None))
        self.label_22.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">目标目录为apk中相对路径,如需要将原目录拷贝到apk中assets目录,</span></p><p><span style=\" color:#ff0000;\">Target项值:assets,若拷贝到assets目录下test目录.Target项值:assets\\test</span></p></body></html>", None))
        self.checkBox_4.setText(_translate("Form", "使用当前配置", None))
        self.pushButton_5.setText(_translate("Form", "保存配置", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other), _translate("Form", "其他设置", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">*此处的显示的参数为客户端使用参数,服务器参数不显示</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameter), _translate("Form", "参数检查", None))
    
    def mouseMoveEvent(self, event):
        if (event.buttons() == Qt.LeftButton):
            self.endPos = event.globalPos() - self.startPos
            self.move(self.endPos)
    
    def mousePressEvent(self, event):
    
        if (event.button() == Qt.LeftButton):
            self.startPos = event.globalPos() - self.frameGeometry().topLeft()
          
        elif (event.button() == Qt.MiddleButton):
            self.closeWindowAnimation()
        elif(event.button() == Qt.RightButton):
            self.shakeWindow()
    
    
import res

class ChannelSettingUI(QDialog,Ui_Form):  
    def __init__(self,parent=None):
        super(ChannelSettingUI,self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setupUi(self)

  
if __name__ == '__main__':
    
    import sys
    app = QApplication(sys.argv)
    aboutus = ChannelSettingUI()
    aboutus.show()
    sys.exit(app.exec_())    