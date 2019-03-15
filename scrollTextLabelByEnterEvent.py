# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packLog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class scrollTextLabelByEnterEvent(QLabel):
    def __init__(self, parent=None):
        super(scrollTextLabelByEnterEvent, self).__init__(parent)
        self.txt = QString()
        self.newX = 0       
        self.t = QTimer()
        self.font = QFont(_fromUtf8('微软雅黑, verdana'), 9)
        self.connect(self.t, SIGNAL("timeout()"), self.changeTxtPosition)

    def changeTxtPosition(self):
        if not self.parent().isVisible():
            self.t.stop()
            self.newX = 0
            return
        if self.textRect.width() + self.newX > 0:
            self.newX -= 5
        else:
            self.newX = self.width()            
        self.update()

    def setText(self, s):
        self.txt = s
        self.newX = 0
        self.update()

    def enterEvent(self, event):
        self.t.start(150)

    def leaveEvent(self, event):
        #鼠标离开则停止滚动并复位
        self.t.stop()
        self.newX = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(self.font)
        painter.setPen(QColor('transparent'));
        self.textRect = painter.drawText(QRect(0, -7, self.width(), 25), Qt.AlignHCenter | Qt.AlignVCenter, self.txt)

        if self.textRect.width() > self.width():    
            painter.setPen(QColor(0, 0, 0, 255)); #黑色
            painter.drawText(QRect(self.newX, -7, self.textRect.width(), 25), Qt.AlignLeft | Qt.AlignVCenter, self.txt)         
        else:
            painter.setPen(QColor(0, 0, 0, 255));#黑色
            self.textRect = painter.drawText(QRect(0, -7, self.width(), 25), Qt.AlignLeft | Qt.AlignVCenter, self.txt)
            self.t.stop()

