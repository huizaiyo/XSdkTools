# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from MyLabel import MyLabel
from utils.http_manager import httpManager
import json
from utils.taskManagerModule import taskManager
from utils import file_operate
import os
import codecs
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
        Form.resize(1081, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/funcell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
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
"QToolButton[objectName=\"closetoolButton_2\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closetoolButton_2\"]:hover {\n"
"image:url(:/images/min_hover.png);\n"
"}\n"
"QToolButton[objectName=\"closetoolButton_2\"]:pressed {\n"
"image:url(:/images/min_pressed.png);\n"
"}\n"
"\n"
"QWidget[objectName=\"Form\"]{\n"
"border-image:url(\":/images/funcell_bg.png\");\n"
"}\n"
"\n"
"QToolButton[objectName=\"toolButton\"]{\n"
"background-color: rgb(85, 255, 127);\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"]{\n"
"border:0px;\n"
"background-color:transparent;\n"
"}\n"
"QCheckBox[objectName=\"checkBox\"],QLabel[objectName=\"label_3\"],QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"]{\n"
"font-family:\'微软雅黑\';\n"
"color:white;\n"
"}\n"
"\n"
"QLabel[objectName=\"label_4\"],QLabel[objectName=\"label_5\"]{\n"
"font-family:\'微软雅黑\';\n"
"color:red;\n"
"}\n"
""))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 1081, 601))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(320, 225, 420, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 182, 30, 30))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/use.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_3 = QtGui.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(320, 295, 420, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(670, 365, 71, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(320, 425, 420, 61))
        self.toolButton.setAutoRepeat(False)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 185, 321, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        self.lineEdit.setFont(font)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line_4 = QtGui.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(360, 255, 3, 25))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 255, 321, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.line = QtGui.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(360, 185, 3, 25))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
#         self.label_3 = QtGui.QLabel(self.widget)
#         self.label_3.setGeometry(QtCore.QRect(640, 525, 105, 31))
#         self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3 = MyLabel(self)
        self.label_3.setGeometry(QtCore.QRect(640, 525, 105, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(320, 250, 30, 30))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/suo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.closetoolButton = QtGui.QToolButton(self.widget)
        self.closetoolButton.setGeometry(QtCore.QRect(1050, 5, 27, 22))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon)
        self.closetoolButton.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))
        self.closetoolButton_2 = QtGui.QToolButton(self.widget)
        self.closetoolButton_2.setGeometry(QtCore.QRect(1020, 5, 27, 22))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/min_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton_2.setIcon(icon1)
        self.closetoolButton_2.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton_2.setObjectName(_fromUtf8("closetoolButton_2"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(770, 210, 105, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(770, 280, 105, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.closetoolButton.clicked.connect(self.close)
        self.closetoolButton_2.clicked.connect(self.showMinimized)
        self.toolButton.clicked.connect(self.LoginTask)
        self.initUserInfo()
        
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "请登录", None))
        self.checkBox.setText(_translate("Form", "记住密码", None))
        self.toolButton.setText(_translate("Form", "登 录", None))
        self.label_3.setText(_translate("Form", "没有帐号?立即注册", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.closetoolButton_2.setText(_translate("Form", "...", None))
        self.label_4.setText(_translate("Form", "游戏ProductCode", None))
        self.label_5.setText(_translate("Form", "游戏ProductKey", None))
    
    def mouseMoveEvent(self, event):
        if (event.buttons() == Qt.LeftButton):
            self.endPos = event.globalPos() - self.startPos
            self.move(self.endPos)
    
    def mousePressEvent(self, event):
        
        if (event.button() == Qt.LeftButton):
            self.startPos = event.globalPos() - self.frameGeometry().topLeft()
            
        elif (event.button() == Qt.MiddleButton):
            self.closeWindowAnimation()
        
    def registerTask(self):
        print 'register user'
    
    def saveUserInfo(self):
        GameFile = file_operate.getFullPath("Log/GameFile.log")
        checkflag = "False"
        if self.checkBox.isChecked():
            checkflag ="True"
        info = self.lineEdit.text() +'|' + self.lineEdit_2.text() +'|'+checkflag
        
        logFile = codecs.open(GameFile, 'w', 'utf-8')
        content = info + '\r\n'
        logFile.write(unicode(content, 'gbk'))
        logFile.close()
    
    def initUserInfo(self):
        GameFile = file_operate.getFullPath("Log/GameFile.log")
        if not os.path.exists('Log'):
            os.makedirs('Log')
        if os.path.exists(GameFile):
            f = open(GameFile, 'a+')
            data = str(f.read())
            f.close()
            if len(data) > 0 and data.find('|') != -1:
                logFile = codecs.open(GameFile, 'a+', 'utf-8')
                for line in logFile.readlines():
                    line = line.rstrip("\r\n")
                    Info = line.split('|')
                    if Info[2] == "True":
                        self.lineEdit.setText(Info[0])
                        self.lineEdit_2.setText(Info[1])
                        self.checkBox.setChecked(True)
                    else:
                        self.checkBox.setChecked(False)
                    break
    
    def getHostAddress(self):
        address =''
        try:
            config = ET.parse(file_operate.getCommonXmlPath())
            root = config.getroot()
            host = root.find("host")
            address = host.get("address")
        except Exception,e:
            print e
            print "Error: cannot parse file: commonconfig.xml."
            return -1
        return address
    
    def getHostAddressByUpdateXml(self):
        address =''
        try:
            old_updateFile = file_operate.getFullPath('update.xml')
            config = ET.parse(old_updateFile)
            
            root = config.getroot()
            address = root.find('auth').text
        except Exception,e:
            print e
            print "Error: cannot parse file: update.xml."
            return -1
        return address
    
    def LoginTask(self):
        
        self.toolButton.setText(u'登录中...')
#         url = 'http://auth-beta.funcell123.com/product/pack' #测试环境
#         self.lineEdit.setText('100')
#         self.lineEdit_2.setText('fds415651d65ht23fd2')
#         url = 'https://auth.funcell123.com/product/pack' #正式环境
#         url = self.getHostAddress()
        url = self.getHostAddressByUpdateXml()
        parameters = 'product_code='+unicode(self.lineEdit.text()) +'&'+'product_key=' + unicode(self.lineEdit_2.text())
        response = httpManager.shareInstance().http_post(url,parameters)
        data = json.loads(response)
        # print 'response:',response
        for key in data:
#             print key
            if 'data' == key:
#                 print 'data渠道数据个数:',str(len(data[key]))
                taskManager.shareInstance().updateChanelList(data[key])
            elif 'message' == key:
                pass
            elif 'error_code' == key:
                if 'P1111' == data[key]:
                    print '--------登录成功--------'
                    if len(self.lineEdit.text()) > 0 and len(self.lineEdit_2.text()) > 0:
                        self.saveUserInfo()
                    self.accept()
                else:
                    self.toolButton.setText(u'登录')
                    QtGui.QMessageBox.critical(None, u'错误', u'用户名或密码错误!')
            elif 'level' == key:
                pass
    
import res

class LoginClass(QDialog,Ui_Form):  
    def __init__(self,parent=None):  
        super(LoginClass,self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
