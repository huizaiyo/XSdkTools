# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginListUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from utils.taskManagerModule import taskManager
from pluginListItem import pluginListItem 
from PyQt4.Qt import QString
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
    
    __ChannelPluginListData = ''
    
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
"\n"
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
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 140, 497, 261))
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.closetoolButton.clicked.connect(self.close)
#         self.initPluginList()
    
    def initPluginList(self):
        self.__ChannelPluginListData = taskManager.shareInstance().getChannelPluginListData()
        for key_data in  self.__ChannelPluginListData:
            print 'key_data:',key_data
            for key in key_data:
                typePlugin = key_data['typePlugin']
                channel = key_data['channel']
                version = key_data['version']
#                 status = key_data['status']
#             if 'enable' == status:
            item1 = QtGui.QListWidgetItem()
            item1.setSizeHint(QSize(0, 42))
            
            item = pluginListItem()
            item.label.setText(typePlugin)
            item.label_2.setText(channel)
            item.pushButton.setText(version)
            
            self.listWidget.addItem(item1)
            self.listWidget.setItemWidget(item1,item)
                
                
            
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">三方插件</span></p></body></html>", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">类型</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">渠道</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">版本</span></p></body></html>", None))
    
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


class pluginListUI(QDialog,Ui_Form):
    def __init__(self,parent=None):  
        super(pluginListUI,self).__init__(parent)  
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setupUi(self)
