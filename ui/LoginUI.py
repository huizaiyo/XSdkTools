# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1083, 604)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/funcell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("QToolButton[objectName=\"closetoolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:hover {\n"
"image:url(:/images/close_hover.png);\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:pressed {\n"
"image:url(:/images/close_pressed.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"closetoolButton_2\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closetoolButton_2\"]:hover {\n"
"image:url(:/images/min_hover.png);\n"
"}\n"
"QToolButton[objectName=\"closetoolButton_2\"]:pressed {\n"
"image:url(:/images/min_pressed.png);\n"
"}\n"
"\n"
"QWidget[objectName=\"Form\"]{\n"
"border-image:url(\":/images/funcell_bg.png\");\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QToolButton[objectName=\"toolButton\"]{\n"
"background-color: rgb(85, 255, 127);\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"]{\n"
"border:0px;\n"
"background-color:transparent;\n"
"}\n"
"QCheckBox[objectName=\"checkBox\"],QLabel[objectName=\"label_3\"],QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"]{\n"
"font-family:\'微软雅黑\';\n"
"color:white;\n"
"}\n"
"\n"
"QLabel[objectName=\"label_4\"],QLabel[objectName=\"label_5\"]{\n"
"font-family:\'微软雅黑\';\n"
"color:red;\n"
"}\n"
"\n"
""))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 1081, 601))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(320, 225, 420, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 182, 30, 30))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/use.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_3 = QtGui.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(320, 295, 420, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(670, 365, 71, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(320, 425, 420, 61))
        self.toolButton.setAutoRepeat(False)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 185, 321, 25))
        font = QtGui.QFont()
