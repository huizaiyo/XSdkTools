# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KestoreUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from PyQt4.QtCore import *
import threading
from utils.taskManagerModule import taskManager
import os
import codecs
import re

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
""))
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
        self.label_2.setGeometry(QtCore.QRect(50, 120, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 115, 251, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 112, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 165, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 165, 251, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 210, 251, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 212, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 260, 71, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 260, 251, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(400, 260, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 342, 91, 33))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(50, 320, 121, 21))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(400, 165, 71, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.selectKeystore)
        self.closetoolButton.clicked.connect(self.close)
#         self.pushButton_2.clicked.connect(self.SaveConfig)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">新增签名文件</span></p></body></html>", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.label_2.setText(_translate("Form", "签名文件", None))
        self.pushButton.setText(_translate("Form", "选择文件", None))
        self.label_3.setText(_translate("Form", "keystore密码", None))
        self.label_4.setText(_translate("Form", "Alias", None))
        self.label_5.setText(_translate("Form", "证书别名", None))
        self.label_6.setText(_translate("Form", "Alias密码", None))
        self.label_7.setText(_translate("Form", "证书别名密码", None))
        self.pushButton_2.setText(_translate("Form", "保存配置", None))
        self.checkBox.setText(_translate("Form", "使用当前证书", None))
        self.label_8.setText(_translate("Form", "证书密码", None))
    
     
    def selectKeystore(self):
        s=QtGui.QFileDialog.getOpenFileName(self,u"选择证书文件","/","*")  
        if s.length() > 0:
            self.lineEdit.setText(unicode(s))
    
#     def SaveConfig(self):
#         flag = False
#         info = self.lineEdit.text()+ "|" +self.lineEdit_2.text() + "|" +self.lineEdit_3.text() +"|" +self.lineEdit_4.text()
#         if self.checkBox.isChecked():
#             info += "|Default"
#             flag = True
#         self.log(info, flag)
#         taskManager.shareInstance().addKeyStore(info)
#         self.close()
    
#     def log(self,str,flag = False):
#         print 'flag:',flag
#         logDir = 'Log/'
#         if not os.path.exists(logDir):
#             os.makedirs(logDir)
#         
#         if flag:
#             self.modifyFileContent(logDir + 'SignFile.log', "|Default", "")
#         
#         logFile = codecs.open(logDir + 'SignFile.log', 'a+', 'utf-8')
#         content = str + "\n"
#         logFile.write(unicode(content, 'gbk'))
#         logFile.close()
#     
#     
#     def modifyFileContent(self,sourcefile, oldContent, newContent):
#         if os.path.isdir(sourcefile):
#             print("the source %s must be a file not a dir", sourcefile)
#             return
#     
#         if not os.path.exists(sourcefile):
#             print("the source is not exists.path:%s", sourcefile)
#             return 
#     
#         f = open(sourcefile, 'r+')
#         data = str(f.read())
#         f.close()
#         bRet = False
#         idx = data.find(oldContent)
#         while idx != -1:
#             data = data[:idx] + newContent + data[idx + len(oldContent):]
#             idx = data.find(oldContent, idx + len(oldContent))
#             bRet = True
#     
#         if bRet:
#             fw = open(sourcefile, 'w')
#             fw.write(data)
#             fw.close()
#             print("modify file success.path:%s", sourcefile)
#         else:
#             print("there is no content matched in file:%s with content:%s", sourcefile, oldContent)
    
    
import res

class KeystoreUIClass(QDialog,Ui_Form):
    
    def __init__(self,parent=None):  
        super(KeystoreUIClass,self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setupUi(self)
