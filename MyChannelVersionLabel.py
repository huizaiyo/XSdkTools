# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packLog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import *
import webbrowser
from ChannelVersionUI import *
from ChannelVersionItem import ChannelVersionItem
from functools import partial

#自定义Label,实现各种事件
class MyChannelVersionLabel(QtGui.QLabel):
    
    __VersionData=''
    __Channel_Type =''
    __ChannelItem=''
    __DataList={}
    
    def __init__(self,parent=None):
        super(MyChannelVersionLabel,self).__init__(parent)    
    
    def mouseDoubleClickEvent(self,e):
        pass
    def mousePressEvent(self,e):
        
        self.dialog.exec_()
        
    def focusInEvent(self,e):
        pass
    def focusOutEvent(self,e):
        pass
    def moveEvent(self,e):
        pass
    def leaveEvent(self,e): #鼠标离开label
        pass
#         self.setStyleSheet("color:white;")
    def enterEvent(self,e): #鼠标移入label
        pass
#         self.setStyleSheet("color:red;")
    def mouseMoveEvent(self,e):
        pass

    def setVersionData(self,channel_type,data):
        print '-----------------data:',data
        self.__Channel_Type = channel_type
        self.__VersionData = data
#         self.__ChannelItem = chanel_item
        self.initChannelVersion()
        
    
    def initChannelVersion(self):
        self.dialog = ChannelVersionListUI()
        self.dialog.setFixedSize(QSize(498, 406))
#         self.connect(taskManager.shareInstance(), SIGNAL("updateChannelVersionLabel"), self.updateChannelVersionLabel)
        for key in self.__VersionData:
#             print 'key:',key
            versionTime = key['date']
            sdkVersion = key['version']
            
            item1 = QtGui.QListWidgetItem()
            item1.setSizeHint(QSize(0, 42))
            
            item = ChannelVersionItem()
            item.label.setText(versionTime)
            item.label_2.setText(sdkVersion)
            item.label_3.setText('')
             
            self.dialog.listWidget.addItem(item1)
            self.dialog.listWidget.setItemWidget(item1,item)
            
#             self.__DataList[self.dialog.pushButton_2] = self.dialog.listWidget
        
#         for key in self.__DataList.keys():
#             key.clicked.connect(partial(self.pushButton_2Click,self.__DataList[key]))
            
#         self.dialog.pushButton_2.clicked.connect(self.pushButton_2Click)
        
    
    def updateChannelVersionLabel(self,versionCode):
        print 'versionCode:',versionCode
        print 'channel_type:',self.__Channel_Type
#         print 'channel_type:',self.__Channel_Type
#         self.setText("<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ff0000;\">"+versionCode+"</span></p></body></html>")
        
        
