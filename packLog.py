# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packLog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from utils.taskManagerModule import taskManager
import os

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

class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(666, 460)
        Form.setStyleSheet(_fromUtf8("QToolButton[objectName=\"closetoolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:hover {\n"
"image:url(:/images/close_hover.png);\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:pressed {\n"
"image:url(:/images/close_pressed.png);\n"
"}\n"
"QWidget[objectName=\"Form\"]{\n"
"background-image: url(:/images/funcell_bg.png);\n"
"}\n"
"QLabel[objectName=\"label\"]{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
""))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 60, 665, 401))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.closetoolButton = QtGui.QToolButton(Form)
        self.closetoolButton.setGeometry(QtCore.QRect(635, 0, 27, 22))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon)
        self.closetoolButton.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.closetoolButton.clicked.connect(self.close)
        self.connect(taskManager.shareInstance(), SIGNAL("updateTextLog"), self.updateTextLog)
        self.initLog()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">日志信息</span></p></body></html>", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
    
    
    def updateTextLog(self,channelName,log):
        self.textBrowser.append(log)
    
    def initLog(self):
        sourcefile = 'Log/error.log'
        if not os.path.exists(sourcefile):
            return
        
        f = open(sourcefile, 'r+')
        data = str(f.read())
        f.close()
        self.textBrowser.append(data)
    
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

class packLogClass(QDialog,Ui_Form):
    
    def __init__(self,parent=None):  
        super(packLogClass,self).__init__(parent)  
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setupUi(self)

