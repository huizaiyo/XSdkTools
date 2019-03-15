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
from scrollTextLabel import scrollTextLabel
from listwidget2_scrollTextLabel import listwidget2_scrollTextLabel

#自定义QWidget,用于布局显示
class MyItem(QtGui.QWidget):
    def __init__(self,parent=None):
        super(MyItem,self).__init__(parent)
        self.resize(800, 72)
        
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 6, 60, 60))
        self.label.setText((""))
        self.label.setPixmap(QtGui.QPixmap((":/images/channel_default.png")))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(("label"))
#         self.label_2 = QtGui.QLabel(self)
        self.label_2 = scrollTextLabel(self)
        self.label_2.setGeometry(QtCore.QRect(129, 25, 181, 30))
        self.label_2.setObjectName(("label_2"))
        self.label_2.setText(u"渠道名")
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(330, 23, 231, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(("progressBar"))
        style ="""
        QProgressBar {
            border: 2px solid grey;
            border-radius: 4px;
            text-align: center;
            color:black
        }

        QProgressBar::chunk {
            background-color: #88B0EB;
            width: 8px;
        }"""
        
#         QProgressBar::chunk {
#             background-color: #88B0EB;
#             width: 8px;
#             margin:0.5px;

        self.progressBar.setStyleSheet(style)
#         self.label_3 = QtGui.QLabel(self)
        self.label_3 = listwidget2_scrollTextLabel(self)
        self.label_3.setGeometry(QtCore.QRect(600, 26, 171, 16))
        self.label_3.setObjectName(("label_3"))
#         self.label_3.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_3.setText(u"打包中...")
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 70, 800, 1))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(("line"))

import res
