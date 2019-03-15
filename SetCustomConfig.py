# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetCustomConfig.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
import os
from PyQt4.QtCore import Qt
import xml.dom.minidom
from utils import file_operate
import sys
from xml.etree import ElementTree as ET

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
        self.label_2.setGeometry(QtCore.QRect(50, 98, 65, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 93, 251, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 90, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 366, 91, 33))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(50, 345, 121, 21))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 140, 425, 201))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 118, 461, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.closetoolButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.savaconfig)
        self.pushButton.clicked.connect(self.openCustomFile)
        self.initConfig()
    
    def initConfig(self):
        if os.path.exists(file_operate.getFullPath(file_operate.getCommonXmlPath())):
            config = ET.parse(file_operate.getFullPath(file_operate.getCommonXmlPath()))
            root = config.getroot()
            customfile = root.find('custom_file')
            if customfile is not None:
                self.lineEdit.setText(customfile.get("path"))
                checkBoxflag = False
                if customfile.get("checkBoxflag") == "True":
                    checkBoxflag = True
                self.checkBox.setChecked(checkBoxflag)
    
    def beautifulFormat(self, xmlDomObject):
        if xmlDomObject:
            xmlStr = xmlDomObject.toprettyxml(indent = '', newl = '', encoding = 'utf-8')
            xmlStr = xmlStr.replace('\t', '').replace('\n', '')
            xmlDomObject = xml.dom.minidom.parseString(xmlStr)
            xmlStr = xmlDomObject.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8')
            return xmlStr
    
    def savaconfig(self):
        xmlpath = file_operate.getFullPath(file_operate.getCommonXmlPath())
        dom = xml.dom.minidom.parse(file_operate.getCommonXmlPath())
        root = dom.documentElement
        customfile = root.getElementsByTagName('custom_file')
        if len(customfile) == 0:
            print 'create custom_file Element '
            customNode = dom.createElement('custom_file')
            root.appendChild(customNode)
        else:
            print 'modify  '
            customNode = customfile[0]
            
        checkBoxflag = "False"
        if self.checkBox.isChecked():
            checkBoxflag = "True"
            
        customNode.setAttribute('path',unicode(self.lineEdit.text()))
        customNode.setAttribute('checkBoxflag',checkBoxflag)
        
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        f = open(xmlpath, 'w')
        dom.writexml(f, addindent=' ', newl='\n',encoding='utf-8')
        f.close()
        
        f = open(xmlpath, "w")
        content = self.beautifulFormat(dom)
        f.write(content)
        f.close()
        QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
        
    
    def openCustomFile(self):
        s=QtGui.QFileDialog.getOpenFileName(self,u"选择自定义文件","/","files(*)")
        if s.length() > 0:
            self.lineEdit.setText(unicode(s))
    
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">自定义配置</span></p></body></html>", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.label_2.setText(_translate("Form", "自定义文件", None))
        self.pushButton.setText(_translate("Form", "选择文件", None))
        self.pushButton_2.setText(_translate("Form", "保存配置", None))
        self.checkBox.setText(_translate("Form", "使用当前配置", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;manifestConfig xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;applicationCfg keyword=&quot;custom.config&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;!-- <span style=\" color:#ff0000;\">该节点下存放activity、meta-data等配置 </span>--&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;meta-data android:name=&quot;android.max_aspect&quot; android:value=&quot;ratio_float&quot; /&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;/applicationCfg&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;permissionCfg&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;!-- <span style=\" color:#ff0000;\">该节点下存放权限等配置 </span>--&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;uses-permission android:name=&quot;android.permission.INTERNET&quot;/&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;/permissionCfg&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;/manifestConfig&gt;</p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">自定义文件要求及格式(文件名无要求,文件内容需按照如下格式进行)推荐使用xml文件</span></p></body></html>", None))

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

class SetCustomConfigClass(QDialog,Ui_Form):  
    def __init__(self,parent=None):  
        super(SetCustomConfigClass,self).__init__(parent)  
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setupUi(self)
