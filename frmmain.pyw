#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pack import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import Qt
from LoginUI import LoginClass
from utils.config import ConfigParse
from FuncellSdkToolsUpdateUI import FuncellSdkToolUpdateUI
from UpdateUI import UpdateUI
from utils import file_operate
from setting_menu import *
import os
import codecs
from utils.http_manager import httpManager
import json
from utils.taskManagerModule import taskManager
from SwitchAccountUI import SwitchAccountClass
from xml.etree import ElementTree as ET
from SetCustomConfig import SetCustomConfigClass
from loading import loadingUI
import utils.start
import utils.startIcon
import signal

class MyForm(QtGui.QMainWindow):
    __loading = None
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        
        self.__loading = loadingUI()
        taskManager.shareInstance().setLoadingUI(self.__loading)
        
#         taskManager.shareInstance().getLoadingUI().setWindowModality(Qt.ApplicationModal)
#         taskManager.shareInstance().getLoadingUI().show()
        
        self.ui.setupUi(self)
    
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.startAnimation()
        
        self.ui.closetoolButton.clicked.connect(self.on_closeToolButton_clicked)
        self.ui.toolButton_2.clicked.connect(self.on_minToolButton_clicked)
        self.ui.toolButton.clicked.connect(self.on_toolButton_clicked)
        self.ui.toolButton_3.clicked.connect(self.on_toolButton_3_clicked)
        self.ui.toolButton_4.clicked.connect(self.on_toolButton_4_clicked)
        self.ui.toolButton_5.clicked.connect(self.on_toolButton_3_clicked)
        self.ui.toolButton_6.clicked.connect(self.on_toolButton_4_clicked)
        self.ui.toolButton_10.clicked.connect(self.on_toolButton_clicked)
        self.ui.toolButton_11.clicked.connect(self.on_toolButton_3_clicked)
        
        self.setting_menu = SettingMenu()
        self.connect(self.ui,SIGNAL("showSettingMenu()"), self, SLOT("showSettingMenu()"))
        self.connect(self.setting_menu, SIGNAL("refreshData()"), self, SLOT("refreshData()"))
        self.connect(self.setting_menu, SIGNAL("switchAccount()"), self, SLOT("switchAccount()"))
        self.connect(self.setting_menu, SIGNAL("setCustomConfig()"), self, SLOT("setCustomConfig()"))
        
        self.center()
        
#         taskManager.shareInstance().getLoadingUI().stopAnimation()
#         taskManager.shareInstance().getLoadingUI().close()
      
    def center(self):  #主窗口居中显示函数
        screen=QtGui.QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2 - 15, (screen.height()-size.height())/2 -60)
        
    def mousePressEvent(self, event):
    
        if (event.button() == Qt.LeftButton):
          
            self.startPos = event.globalPos() - self.frameGeometry().topLeft()
          
        elif (event.button() == Qt.MiddleButton):
            self.closeWindowAnimation()
        elif(event.button() == Qt.RightButton):
            self.shakeWindow()
    
    @pyqtSlot()
    def switchAccount(self):
        print 'switch account...'
        dialog = SwitchAccountClass()
        if dialog.exec_():
            taskManager.shareInstance().refreshPackUi()
    
    @pyqtSlot()
    def setCustomConfig(self):
        print 'set custom config...'
        dialog = SetCustomConfigClass()
        dialog.exec_()
        
        
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
    
    @pyqtSlot()    
    def refreshData(self):
        print 'refresh data...'
        accounts =""
        password = ""
        if os.path.exists(file_operate.getFullPath("Log/GameFile.log")):
            logFile = codecs.open('Log/' + 'GameFile.log', 'a+', 'utf-8')
            for line in logFile.readlines():
                line = line.rstrip("\r\n")
                Info1 = line.split('|')
                accounts = Info1[0]
                password = Info1[1]
                break
        if len(accounts) > 0 and len(password) > 0:
#             url = 'http://auth-beta.funcell123.com/product/pack' #测试环境
#             url = 'https://auth.funcell123.com/product/pack' #正式环境
            url = self.getHostAddress()
            parameters = 'product_code='+unicode(accounts) +'&'+'product_key=' + unicode(password)
            response = httpManager.shareInstance().http_post(url,parameters)
            data = json.loads(response)
            for key in data:
                if 'error_code' == key:
                    if 'P1111' == data[key]:
                        print '--------刷新成功--------'
                        taskManager.shareInstance().updateChanelList(data['data'])
                        taskManager.shareInstance().refreshPackUi()
                    else:
                        QtGui.QMessageBox.critical(None, u'错误', u'刷新失败,请重新登录!')
        else:
            QtGui.QMessageBox.critical(None, u'错误', u'刷新失败,请重新登录!')
    
    @pyqtSlot()    
    def showSettingMenu(self):
        p = self.rect().topRight() #QPoint
        p.setX(p.x() - 170)
        p.setY(p.y() + 60)
        self.setting_menu.setFixedSize(QSize(170, 102))
        self.setting_menu.exec_(self.mapToGlobal(p))
    
    def mouseMoveEvent(self, event):
        if (event.buttons() == Qt.LeftButton):
            self.endPos = event.globalPos() - self.startPos
            self.move(self.endPos)


    
    def on_closeToolButton_clicked(self):
        self.closeWindowAnimation()
    
    def closeWindowAnimation(self):
        self.animation = QPropertyAnimation(self, "windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
        self.animation.finished.connect(self.close)
        
        #退出时候强制关闭所有后台进程,线程
        try:
            pid = os.getpid()
            file_operate.execFormatCmd("taskkill -f -t /pid %i"%pid)
#             os.system("taskkill -f -t /pid %i"%pid) #这个会有cmd控制台
        except Exception,e:
            print e
        
      
    def on_minToolButton_clicked(self):
        self.showMinimized()

    
    def on_toolButton_clicked(self):
        self.setStackCurrentPage(0)
    
    def on_toolButton_3_clicked(self):
        self.setStackCurrentPage(1)
    
    def on_toolButton_4_clicked(self):
        self.setStackCurrentPage(2)
    
    def setStackCurrentPage(self, index):
        widget = self.ui.stackedWidget.widget(index)
        self.ui.stackedWidget.setCurrentWidget(widget)
    
    def startAnimation(self):
        self.animation = QPropertyAnimation(self, "windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
    
    def shakeWindow(self):
        animation = QPropertyAnimation(self, "geometry")
        animation.setDuration(500)
        animation.setKeyValueAt(0, QRect(QPoint(self.frameGeometry().x() - 3, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.1, QRect(QPoint(self.frameGeometry().x() + 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.2, QRect(QPoint(self.frameGeometry().x() - 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.3, QRect(QPoint(self.frameGeometry().x() + 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.4, QRect(QPoint(self.frameGeometry().x() - 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.5, QRect(QPoint(self.frameGeometry().x() + 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.6, QRect(QPoint(self.frameGeometry().x() - 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.7, QRect(QPoint(self.frameGeometry().x() + 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.8, QRect(QPoint(self.frameGeometry().x() - 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(0.9, QRect(QPoint(self.frameGeometry().x() + 6, self.frameGeometry().y()), self.size()))
        animation.setKeyValueAt(1, QRect(QPoint(self.frameGeometry().x() - 3, self.frameGeometry().y()), self.size()))
        animation.start()
    

    
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #------------------------以下为客户端更新逻辑-------------------
    updateFlag = False
    result = ConfigParse.shareInstance().updateExeFlag()
    if(isinstance(result,bool)):
        pass
    else:
        dictTemp={}
        dictTemp = result
        updateFlag = dictTemp.get('updateflag')
    print 'updateFlag:',updateFlag
    if updateFlag:
        forceFlag = dictTemp.get('force')
        print 'forceFlag:',forceFlag
        if str(forceFlag) == 'true' or str(forceFlag) == 'True':
            QProcess.startDetached(QString("FuncellSDKToolBase.exe"))
            qApp.quit()
        else:
            dialog = FuncellSdkToolUpdateUI()
            dialog.setFixedSize(QSize(498, 197))
            if dialog.exec_():
                print '点击了确定升级按钮....'
                QProcess.startDetached(QString("FuncellSDKToolBase.exe"))
                qApp.quit()
            else:
                print '点击了取消按钮....'
                dialog = LoginClass()
                if dialog.exec_():
                    myapp = MyForm()
                    myapp.show()
                    sys.exit(app.exec_())
    else:
        dialog = LoginClass()
        if dialog.exec_():
            myapp = MyForm()
            myapp.show()
            sys.exit(app.exec_())
    #----------------------------------------------------------
    
#     dialog = LoginClass()
#     if dialog.exec_():
#         myapp = MyForm()
#         myapp.show()
#         sys.exit(app.exec_())
#     myapp = MyForm()
#     myapp.show()
#     sys.exit(app.exec_())
