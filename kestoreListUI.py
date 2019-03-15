# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kestoreListUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from fileinput import close
from KestoreUI import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from utils.taskManagerModule import taskManager
import utils.file_operate
from functools import partial
from utils.config import ConfigParse

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
    
    __keystoreDetails={}
    __key={}
    
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
"QWidget[objectName=\"Form\"]{\n"
"background-image: url(:/images/funcell_bg.png);\n"
"}\n"
"QListWidget[objectName=\"listWidget\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"}"))
        self.closetoolButton = QtGui.QToolButton(Form)
        self.closetoolButton.setGeometry(QtCore.QRect(469, 0, 27, 22))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon)
        self.closetoolButton.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 70, 498, 335))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 131, 31))
        self.label.setLineWidth(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(170, 28, 50, 18))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton.setStyleSheet("color: rgb(0, 0, 0);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.closetoolButton.clicked.connect(self.close)
        self.toolButton.clicked.connect(self.OpenKeystore)
        
        self.connect(taskManager.shareInstance(), SIGNAL("addKeyStoreFile"), self.addKeyStoreFile)
        self.initKeystoreList()
#         QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.ListWidgetClicked)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">配置签名文件</span></p></body></html>", None))
        self.toolButton.setText(_translate("Form", "添加", None))
    
    def OpenKeystore(self):
        keystoreUi_Class = KeystoreUIClass()
        keystoreUi_Class.setFixedSize(QSize(498, 406))
        keystoreUi_Class.pushButton_2.clicked.connect(partial(self.SaveConfig,keystoreUi_Class))
        keystoreUi_Class.exec_()
    
    def OpenKeystoreWithParameter(self,keystoreDetails):
        keystoreUi_Class = KeystoreUIClass()
        keystoreUi_Class.setFixedSize(QSize(498, 406))
        
        str_Default = "Default"
        Info = keystoreDetails.split('|')
        flag = False
        if str_Default in Info:
            flag = True
        
        keystoreUi_Class.lineEdit.setText(Info[0])
        keystoreUi_Class.lineEdit_2.setText(Info[1])
        keystoreUi_Class.lineEdit_3.setText(Info[2])
        keystoreUi_Class.lineEdit_4.setText(Info[3].strip())
        if flag:
            keystoreUi_Class.checkBox.setChecked(True)
        else:
            keystoreUi_Class.checkBox.setChecked(False)
        
        keystoreUi_Class.pushButton_2.clicked.connect(partial(self.updateConfig,keystoreUi_Class,keystoreDetails))
        
        keystoreUi_Class.exec_()
    
    def updateConfig(self,keystoreUi_Class,keystoreDetails):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        flag = False
        flag_modify = True
        old_str = keystoreDetails
        new_str = keystoreUi_Class.lineEdit.text()+ "|" +keystoreUi_Class.lineEdit_2.text() + "|" +keystoreUi_Class.lineEdit_3.text() +"|" +keystoreUi_Class.lineEdit_4.text()
        if keystoreUi_Class.checkBox.isChecked():
            new_str += "|Default"
            flag = True
        logDir = 'Log/'
        #-------------------start---------此步骤是为了查询当前需要修改的字符串是否需要删除'|Default' -------------
        productcode = ConfigParse.shareInstance().getProductCode()
        logFile = codecs.open(logDir +productcode +'/SignFile.log', 'a+', 'utf-8')
        for line in logFile.readlines():
            line = line.rstrip("\r\n")
            if keystoreDetails == line:
                idx = line.find('|Default')
                if idx > 0:
                    print '当前修改项中包含|Default字段,当前修改项不能删除|Default字段'
                    flag_modify = False
                
        logFile.close()
        #-------------------end-----------------------
        
        if flag and flag_modify: #先判断是否需要替换"|Default"
            self.modifyFileContent(logDir +productcode  + '/SignFile.log', "|Default", "")
        
        new_str = str(new_str)
        old_str = str(old_str)
        print 'old_str:',old_str
        print 'new_str:',new_str
#         self.modifyFileContent(logDir +productcode  + '/SignFile.log', str(old_str), str(new_str))
        self.modifyFileContent(logDir +productcode  + '/SignFile.log', old_str, new_str)
        if flag:
            taskManager.shareInstance().updateKeystore(new_str,False)
        keystoreUi_Class.close()
        self.initKeystoreList()
    
    def SaveConfig(self,keystoreUi_Class):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        flag = False
        info = keystoreUi_Class.lineEdit.text()+ "|" +keystoreUi_Class.lineEdit_2.text() + "|" +keystoreUi_Class.lineEdit_3.text() +"|" +keystoreUi_Class.lineEdit_4.text()
        if keystoreUi_Class.checkBox.isChecked():
            info += "|Default"
            flag = True
        print 'info',info
        info = str(info)
        info = info.decode('utf-8').encode('gb2312')
#         txtunicode=info.decode('utf-8')
#         txtunicode=txtunicode.encode('gb2312')
#         self.log(txtunicode, flag)
        self.log(info, flag)
        taskManager.shareInstance().addKeyStore(info)
        
        if flag:
            taskManager.shareInstance().updateKeystore(info,True)
        keystoreUi_Class.close()
    
    def log(self,str,flag = False):
        print 'flag:',flag
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
        
        if flag:
            self.modifyFileContent(logDir +productcode+ '/SignFile.log', "|Default", "")
        
        logFile = codecs.open(logDir +productcode+ '/SignFile.log', 'a+', 'utf-8')
        content = str + '\n'
        logFile.write(unicode(content, 'gbk'))
        logFile.close()
    
    
    def modifyFileContent(self,sourcefile, oldContent, newContent):
        if os.path.isdir(sourcefile):
            print("the source %s must be a file not a dir", sourcefile)
            return
    
        if not os.path.exists(sourcefile):
            print("the source is not exists.path:%s", sourcefile)
            return 
    
        f = open(sourcefile, 'r+')
        data = str(f.read())
        f.close()
        bRet = False
        idx = data.find(oldContent)
        while idx != -1:
            data = data[:idx] + newContent + data[idx + len(oldContent):]
            idx = data.find(oldContent, idx + len(oldContent))
            bRet = True
    
        if bRet:
            fw = open(sourcefile, 'w')
            fw.write(data)
            fw.close()
            print("modify file success.path:%s", sourcefile)
        else:
            print("there is no content matched in file:%s with content:%s", sourcefile, oldContent)
    
    
    
    def addKeyStoreFile(self,keystoreInfo):
        self.initKeystoreList()
    
    def initKeystoreList(self):
        self.listWidget.clear()
        self.__keystoreDetails.clear()
        
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        logFile = codecs.open(logDir +productcode+ '/SignFile.log', 'a+', 'utf-8')
        
        for line in logFile.readlines():
            
            if line.count > 0:
                line = line.rstrip("\r\n")  #此处需要去掉隐藏的\r\n，才能匹配
                Info = line.split('|')
#                 Kestore_basename = os.path.basename(utils.file_operate.getFullPath(str(Info[0])))
                Kestore_basename = os.path.basename(utils.file_operate.getFullPath(unicode(Info[0])))
                labelKestoreName = QLabel(Kestore_basename)
                labelKestoreName.setStyleSheet("color: rgb(0, 0, 0);")
                labelAliasName = QLabel(Info[2])
                labelAliasName.setStyleSheet("color: rgb(0, 0, 0);")
                button = QPushButton(u"详情")
                button.setStyleSheet("background-color: rgb(0, 170, 255);\n color: rgb(255, 255, 255);\n")
                
                layout = QHBoxLayout()
                layout.addWidget(labelKestoreName)
                layout.addStretch()
                layout.addWidget(labelAliasName)
                layout.addWidget(button)
                
                widget = QWidget() 
                widget.setLayout(layout)
                
                item = QtGui.QListWidgetItem()
                item.setSizeHint(QSize(0, 40))
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item,widget)
                self.__keystoreDetails[button] = line
                
        logFile.close()
        
        for key in self.__keystoreDetails.keys():
            key.clicked.connect(partial(self.KeyStoreDetails,self.__keystoreDetails[key]))
#             key.clicked.connect(lambda:self.KeyStoreDetails(self.__keystoreDetails[key]))
    
    
    def KeyStoreDetails(self,keystoreDetails):
        self.OpenKeystoreWithParameter(keystoreDetails)
    
    
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

class keystoreUI(QDialog,Ui_Form):  
    def __init__(self,parent=None):  
        super(keystoreUI,self).__init__(parent)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
