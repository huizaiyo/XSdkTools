# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChannelPluginVersionUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt

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
        Form.resize(498, 406)
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
"QPushButton[objectName=\"pushButton\"]{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton[objectName=\"pushButton_2\"]{\n"
"background-color: rgb(0, 165, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox[objectName=\"checkBox\"]{\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"QWidget[objectName=\"Form\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget[objectName=\"listWidget\"]{\n"
"background-color:transparent;\n"
"border:0px;\n"
"}"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 501, 80))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 131, 31))
        self.label.setLineWidth(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.closetoolButton = QtGui.QToolButton(self.widget)
        self.closetoolButton.setGeometry(QtCore.QRect(470, 0, 27, 22))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon)
        self.closetoolButton.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 112, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(360, 112, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 370, 91, 33))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 140, 497, 225))
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.closetoolButton.clicked.connect(self.close)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">插件SDK版本</span></p></body></html>", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">更新时间</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">SDK版本</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">备注</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("Form", "确认使用", None))
    
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

class ChannelPluginVersionListUI(QDialog,Ui_Form):  
    def __init__(self,parent=None):  
        super(ChannelPluginVersionListUI,self).__init__(parent)  
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setupUi(self)
