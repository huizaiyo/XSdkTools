# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginListItem.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import *
from channelItem_pushButton import channelItem_pushButton

class pluginListItem(QtGui.QWidget):
    def __init__(self, parent=None):
        super(pluginListItem, self).__init__(parent)
        self.resize(498, 42)
        self.setStyleSheet(("QPushButton[objectName=\"pushButton\"]{\n"
"color: rgb(255, 0, 0);\n"
"border:1px;\n"
"}"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 15, 110, 12))
        self.label.setObjectName(("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(200, 15, 110, 12))
        self.label_2.setObjectName(("label_2"))
#         self.pushButton = QtGui.QPushButton(self)
        self.pushButton = channelItem_pushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 15, 110, 15))
        font = QtGui.QFont()
        font.setFamily(("Aharoni"))
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet((""))
        self.pushButton.setObjectName(("pushButton"))
        self.pushButton.setStyleSheet("QPushButton{text-align : left;}")
        
        
        self.label.setText(u"类型")
        self.label_2.setText(u"渠道")
        self.pushButton.setText(u"版本")
