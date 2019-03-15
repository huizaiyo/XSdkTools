# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from PyQt4.Qt import QString
import utils.http_manager
import utils.config
import thread
from utils import file_operate
import utils.taskManagerModule
from xml.etree import ElementTree as ET
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
    __m_nIndex = 1;
    __dictTemp_new={}
    __dictTemp_old={}
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(498, 197)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/funcell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("QWidget[objectName=\"Form\"]{\n"
"background-image: url(:/images/funcell_bg.png);\n"
"}\n"
"\n"
"\n"
""))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 50, 45, 45))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/loading1.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 110, 111, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 140, 78, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 140, 71, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        self.connect(utils.taskManagerModule.taskManager.shareInstance(), SIGNAL("updateThreadFinish"), self.updateThreadFinish)
        self.connect(utils.taskManagerModule.taskManager.shareInstance(), SIGNAL("updateDownloadProgress"), self.updateDownloadProgress)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(150)
        self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.updatePixmap)
        self.startAnimation()
        
#         self.updateFlag()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "更新程序", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">应用更新中...</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">下载进度:</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">0%</span></p></body></html>", None))
    
    def startAnimation(self):
        self.timer.start()
    
    def stopAnimation(self):
        self.timer.stop()
    
    def updatePixmap(self):
        self.__m_nIndex += 1
        if self.__m_nIndex > 8 :
            self.__m_nIndex = 1
        pixmap = QtGui.QPixmap(QString(":/images/loading%1").arg(self.__m_nIndex))
        self.label.setPixmap(pixmap)
    
    def updateFlag(self):
        dictTemp = {}
        utils.http_manager.httpManager.shareInstance().downloadUpdateFile()
        UpdateDir = file_operate.getFullPath("Update/")
        new_updateFile = file_operate.getFullPath(UpdateDir+'UpdateFile/update.xml')
        old_updateFile = file_operate.getFullPath('update.xml')
        
        config = ET.parse(new_updateFile)
        root = config.getroot()
        self.__dictTemp_new['version'] = root.find('version').text
        self.__dictTemp_new['force'] = root.find('force').text
        self.__dictTemp_new['url'] = root.find('url').text
        self.__dictTemp_new['md5'] = root.find('md5').text
        self.__dictTemp_new['date'] = root.find('date').text
        self.__dictTemp_new['descript'] = root.find('descript').text
        
        config = ET.parse(old_updateFile)
        root = config.getroot()
        self.__dictTemp_old['version'] = root.find('version').text
        self.__dictTemp_old['force'] = root.find('force').text
        self.__dictTemp_old['url'] = root.find('url').text
        self.__dictTemp_old['md5'] = root.find('md5').text
        self.__dictTemp_old['date'] = root.find('date').text
        self.__dictTemp_old['descript'] = root.find('descript').text
        
        if self.__dictTemp_new.get('version') == self.__dictTemp_old.get('version'):
            dictTemp['updateflag'] = False
        else:
            dictTemp['updateflag'] = True
        return dictTemp
    
    
    def updateDownloadProgress(self,progressNum):
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">%s</span></p></body></html>"%str(progressNum), None))
    
    def downloadTask(self,url,md5):
        downloadFlag = utils.http_manager.httpManager.shareInstance().downloadExe(url,md5)
        if downloadFlag:
            UpdateDir = file_operate.getFullPath("Update/")
            file_operate.copyFile(UpdateDir+'FuncellSDKTool.exe', "FuncellSDKTool.exe")
            utils.taskManagerModule.taskManager.shareInstance().updateThreadFinish()
        thread.exit_thread()
        
    def updateThreadFinish(self):
        UpdateDir = file_operate.getFullPath("Update/")
        file_operate.copyFile(UpdateDir+'UpdateFile/'+'update.xml', "update.xml")
        QProcess.startDetached(QString("FuncellSDKTool.exe"))
        qApp.quit()
        
    def downloadExe(self):
        UpdateDir = file_operate.getFullPath("Update/")
        new_updateFile = file_operate.getFullPath(UpdateDir+'UpdateFile/update.xml')
        config = ET.parse(new_updateFile)
        root = config.getroot()
        url = root.find('url').text
        print 'url:',url
        md5 = root.find('md5').text
        print 'md5:',md5
        thread.start_new_thread(self.downloadTask, (url,md5))
    
    def mousePressEvent(self, event):
    
        if (event.button() == Qt.LeftButton):
          
            self.startPos = event.globalPos() - self.frameGeometry().topLeft()
          
        elif (event.button() == Qt.MiddleButton):
            self.closeWindowAnimation()
        elif(event.button() == Qt.RightButton):
            self.shakeWindow()
    
    def mouseMoveEvent(self, event):
        if (event.buttons() == Qt.LeftButton):
            self.endPos = event.globalPos() - self.startPos
            self.move(self.endPos)
    
import res

class UpdateUI(QDialog,Ui_Form):
    def __init__(self,parent=None):
        super(UpdateUI,self).__init__(parent)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    updateapp = UpdateUI()
    dictTemp = updateapp.updateFlag()
    if dictTemp.get('updateflag'):
        updateapp.downloadExe()
        updateapp.exec_()
        sys.exit(app.quit())
    else:
        QProcess.startDetached(QString("FuncellSDKTool.exe"))
        qApp.quit()
        sys.exit(app.quit())
