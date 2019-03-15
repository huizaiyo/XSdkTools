# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packLog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import *

#自定义ItemDelegate,重绘虚线边框，取消虚线边框
class MyItemDelegate(QtGui.QStyledItemDelegate):
    def __init__(self,parent=None):
        super(MyItemDelegate,self).__init__(parent)    
    
    def paint(self,painter,option,index):
        pass
    
