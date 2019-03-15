# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SwitchAccoutUI.ui'
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
        Form.resize(502, 370)
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
"border-image:url(\":/images/setting_bg.jpg\");\n"
"}\n"
"\n"
"QToolButton[objectName=\"toolButton\"]{\n"
"background-color: gray;\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"]{\n"
"border:0px;\n"
"background-color:transparent;\n"
"}\n"
"QCheckBox[objectName=\"checkBox\"]{\n"
"color:white;\n"
"}\n"
"QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"]{\n"
"color:gray;\n"
"}\n"
"\n"
"QLabel[objectName=\"label_4\"],QLabel[objectName=\"label_5\"]{\n"
"color:red;\n"
"}\n"
""))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 370))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(70, 135, 310, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 92, 30, 30))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/use.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_3 = QtGui.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(70, 205, 310, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(315, 250, 71, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(85, 300, 310, 45))
        self.toolButton.setAutoRepeat(False)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 95, 231, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        self.lineEdit.setFont(font)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line_4 = QtGui.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(110, 165, 3, 25))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 165, 231, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.line = QtGui.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(110, 95, 3, 25))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 30, 30))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/suo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.closetoolButton = QtGui.QToolButton(self.widget)
        self.closetoolButton.setGeometry(QtCore.QRect(470, 5, 27, 22))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon1)
        self.closetoolButton.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))
        self.closetoolButton_2 = QtGui.QToolButton(self.widget)
        self.closetoolButton_2.setGeometry(QtCore.QRect(440, 5, 27, 22))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/min_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton_2.setIcon(icon2)
        self.closetoolButton_2.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton_2.setObjectName(_fromUtf8("closetoolButton_2"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(390, 120, 105, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(390, 190, 105, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "请登录", None))
        self.checkBox.setText(_translate("Form", "记住密码", None))
        self.toolButton.setText(_translate("Form", "登 录", None))
        self.closetoolButton.setText(_translate("Form", "...", None))
        self.closetoolButton_2.setText(_translate("Form", "...", None))
        self.label_4.setText(_translate("Form", "游戏ProductCode", None))
        self.label_5.setText(_translate("Form", "游戏ProductKey", None))

import res_rc
