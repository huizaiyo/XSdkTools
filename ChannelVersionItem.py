# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'packLog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import *
from scrollTextLabelByEnterEvent import scrollTextLabelByEnterEvent

# 自定义QWidget,用于布局显示
class ChannelVersionItem(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ChannelVersionItem, self).__init__(parent)
        self.resize(498, 42)
        
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 15, 110, 12))
        self.label.setObjectName(("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(200, 15, 110, 12))
        self.label_2.setObjectName(("label_2"))
#         self.label_3 = QtGui.QLabel(self)
        self.label_3 = scrollTextLabelByEnterEvent(self)
        self.label_3.setGeometry(QtCore.QRect(360, 15, 138, 12))
        self.label_3.setObjectName(("label_3"))
        
        
        self.label.setText(u"时间")
        self.label_2.setText(u"版本")
#         self.label_3.setText(u"描述")
