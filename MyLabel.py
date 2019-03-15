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

#自定义Label,实现各种事件
class MyLabel(QtGui.QLabel):
    def __init__(self,parent=None):
        super(MyLabel,self).__init__(parent)    
    
    def mouseDoubleClickEvent(self,e):
        print 'mouse double clicked'
    def mousePressEvent(self,e):
        print 'mousePressEvent'
#         QDesktopServices.openUrl(QUrl('http://www.baidu.com', QUrl.TolerantMode))
        #打开官网注册界面
        webbrowser.open('http://ums.funcell123.com/site/register')
        
    def focusInEvent(self,e):
        print 'focusInEvent'  
    def focusOutEvent(self,e):
        print 'focusOutEvent' 
    def moveEvent(self,e):
        print 'moveEvent'   
    def leaveEvent(self,e): #鼠标离开label
        print 'leaveEvent'
        self.setStyleSheet("color:white;")
    def enterEvent(self,e): #鼠标移入label
        print 'enterEvent' 
        self.setStyleSheet("color:red;")
    def mouseMoveEvent(self,e):
        print 'mouseMoveEvent'

    

