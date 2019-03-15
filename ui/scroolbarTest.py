# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scroolbarTest.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_QudaoWidget(object):
    def setupUi(self, QudaoWidget):
        QudaoWidget.setObjectName(_fromUtf8("QudaoWidget"))
        QudaoWidget.resize(523, 404)
        self.tabWidget = QtGui.QTabWidget(QudaoWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 521, 35))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/RefreshData.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_1, icon, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, icon, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, icon, _fromUtf8(""))
        self.listWidget = QtGui.QListWidget(QudaoWidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 44, 141, 357))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.scrollArea = QtGui.QScrollArea(QudaoWidget)
        self.scrollArea.setGeometry(QtCore.QRect(140, 44, 381, 357))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 355))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(QudaoWidget)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(QudaoWidget)

    def retranslateUi(self, QudaoWidget):
        QudaoWidget.setWindowTitle(_translate("QudaoWidget", "Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("QudaoWidget", "基本设置", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("QudaoWidget", "安全设置", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("QudaoWidget", "权限设置", None))

import res_rc
