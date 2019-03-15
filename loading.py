# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui  import *  
from PyQt4.QtCore import *   
import sys

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

class Ui_Dialog(object):
    __m_nIndex = 1;
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(483, 82)
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 45, 45))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/loading1.png")))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(179, 60, 110, 15))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.updatePixmap)
        self.startAnimation()
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.center()
    
    def startAnimation(self):
        self.timer.start()
    
    def stopAnimation(self):
        self.timer.stop()
    
    def updatePixmap(self):
        self.__m_nIndex += 1
        if self.__m_nIndex > 8 :
            self.__m_nIndex = 1
        pixmap = QtGui.QPixmap(QString(":/images/loading%1").arg(self.__m_nIndex))
        self.label_3.setPixmap(pixmap)
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "数据加载中...", None))
        
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0xD0, 0xD0, 0xD0, 0xD0));
        

    def center(self):  #主窗口居中显示函数
        screen=QtGui.QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2 - 15, (screen.height()-size.height())/2 -60)

import res  
        
class loadingUI(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(loadingUI,self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint |Qt.ToolTip)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setupUi(self)

  
if __name__ == '__main__':
    
    import sys
    app = QApplication(sys.argv)
    aboutus = loadingUI()
    aboutus.show()
    sys.exit(app.exec_())    