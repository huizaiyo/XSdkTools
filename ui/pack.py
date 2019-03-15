# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pack.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1068, 602)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/360logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("* {\n"
"font-family:\'微软雅黑\';\n"
"color:white;\n"
"}\n"
"\n"
"/*设置背景图片*/\n"
"QMainWindow{\n"
"border-image:url(\":/images/funcell_bg.png\");\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:hover {\n"
"image:url(:/images/open_over.png);\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:pressed {\n"
"image:url(:/images/open_over.png);\n"
"}\n"
"\n"
"QToolButton[objectName=\"toolButton_2\"],QToolButton[objectName=\"toolButton_13\"]  {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_2\"]:hover,QToolButton[objectName=\"toolButton_13\"]:hover {\n"
"image:url(:/images/open_over_02.png);\n"
"}\n"
"QToolButton[objectName=\"toolButton_2\"]:pressed,QToolButton[objectName=\"toolButton_13\"]:pressed {\n"
"image:url(:/images/open_over_02.png);\n"
"}\n"
"\n"
"QPushButton[objectName=\"toolButton\"],QPushButton[objectName=\"toolButton_3\"],QPushButton[objectName=\"toolButton_4\"]{\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_5\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_6\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_7\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_8\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_9\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_10\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"toolButton_11\"],QToolButton[objectName=\"toolButton_12\"] {\n"
"border:0px;\n"
"}\n"
"QListWidget[objectName=\"listWidget\"]{\n"
"    background-color:transparent;\n"
"border:0px;\n"
"}\n"
"QListWidget[objectName=\"listWidget_2\"],QListWidget[objectName=\"listWidget_3\"]{\n"
"    background-color:transparent;\n"
"border:0px;\n"
"QScrollBar{background:transparent; width:5px;}\n"
"}\n"
"QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"],QLineEdit[objectName=\"lineEdit_3\"],QLineEdit[objectName=\"lineEdit_4\"],QLineEdit[objectName=\"lineEdit_5\"]{\n"
"    color:black;\n"
"}\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(262, 152, 806, 450))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label_12 = QtGui.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(120, 40, 54, 12))
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit = QtGui.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(280, 30, 211, 20))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(500, 30, 75, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(180, 180, 180)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_13 = QtGui.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(120, 80, 54, 12))
        self.label_13.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_2 = QtGui.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 70, 211, 20))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 70, 75, 23))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(180, 180, 180)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_14 = QtGui.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(120, 120, 54, 12))
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_3 = QtGui.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 110, 211, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_3 = QtGui.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 110, 75, 23))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(180, 180, 180)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.toolButton_5 = QtGui.QToolButton(self.page)
        self.toolButton_5.setGeometry(QtCore.QRect(696, 398, 114, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sm_img_08.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.label_25 = QtGui.QLabel(self.page)
        self.label_25.setGeometry(QtCore.QRect(120, 155, 71, 16))
        self.label_25.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_4 = QtGui.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 150, 211, 20))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_4 = QtGui.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 148, 75, 23))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color:rgb(180, 180, 180)"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_26 = QtGui.QLabel(self.page)
        self.label_26.setGeometry(QtCore.QRect(120, 197, 71, 16))
        self.label_26.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.lineEdit_5 = QtGui.QLineEdit(self.page)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 192, 211, 20))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton_5 = QtGui.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 190, 75, 23))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color:rgb(180, 180, 180)"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolButton_6 = QtGui.QToolButton(self.page_2)
        self.toolButton_6.setGeometry(QtCore.QRect(696, 398, 114, 50))
        self.toolButton_6.setIcon(icon1)
        self.toolButton_6.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.line_3 = QtGui.QFrame(self.page_2)
        self.line_3.setGeometry(QtCore.QRect(0, 40, 801, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.toolButton_7 = QtGui.QToolButton(self.page_2)
        self.toolButton_7.setGeometry(QtCore.QRect(469, 398, 114, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/quanxuan_14.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon2)
        self.toolButton_7.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.toolButton_8 = QtGui.QToolButton(self.page_2)
        self.toolButton_8.setGeometry(QtCore.QRect(358, 398, 114, 50))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/fanxuan_14.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon3)
        self.toolButton_8.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.line_4 = QtGui.QFrame(self.page_2)
        self.line_4.setGeometry(QtCore.QRect(230, 0, 20, 401))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_15 = QtGui.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(70, 10, 54, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(70, 30, 54, 12))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.listWidget = QtGui.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 48, 239, 311))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.toolButton_10 = QtGui.QToolButton(self.page_2)
        self.toolButton_10.setGeometry(QtCore.QRect(582, 398, 114, 50))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sm_img_07.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon4)
        self.toolButton_10.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.listWidget_3 = QtGui.QListWidget(self.page_2)
        self.listWidget_3.setGeometry(QtCore.QRect(240, 48, 567, 349))
        self.listWidget_3.setAutoFillBackground(False)
        self.listWidget_3.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.line_5 = QtGui.QFrame(self.page_3)
        self.line_5.setGeometry(QtCore.QRect(0, 40, 806, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.page_3)
        self.line_6.setGeometry(QtCore.QRect(100, 0, 16, 49))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.page_3)
        self.line_7.setGeometry(QtCore.QRect(230, 0, 16, 49))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.page_3)
        self.line_8.setGeometry(QtCore.QRect(340, 0, 16, 49))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.label_19 = QtGui.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(10, 15, 31, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.page_3)
        self.label_20.setGeometry(QtCore.QRect(50, 17, 54, 12))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.page_3)
        self.label_21.setGeometry(QtCore.QRect(120, 15, 31, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.page_3)
        self.label_22.setGeometry(QtCore.QRect(170, 17, 54, 12))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.page_3)
        self.label_23.setGeometry(QtCore.QRect(250, 15, 31, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.page_3)
        self.label_24.setGeometry(QtCore.QRect(290, 17, 54, 12))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.listWidget_2 = QtGui.QListWidget(self.page_3)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 48, 806, 351))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.toolButton_9 = QtGui.QToolButton(self.page_3)
        self.toolButton_9.setGeometry(QtCore.QRect(696, 398, 114, 50))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/dabao_14.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon5)
        self.toolButton_9.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_9.setObjectName(_fromUtf8("toolButton_9"))
        self.toolButton_11 = QtGui.QToolButton(self.page_3)
        self.toolButton_11.setGeometry(QtCore.QRect(583, 398, 114, 50))
        self.toolButton_11.setIcon(icon4)
        self.toolButton_11.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_11.setObjectName(_fromUtf8("toolButton_11"))
        self.toolButton_12 = QtGui.QToolButton(self.page_3)
        self.toolButton_12.setGeometry(QtCore.QRect(471, 398, 114, 50))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/chakanrizhi_14.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon6)
        self.toolButton_12.setIconSize(QtCore.QSize(114, 50))
        self.toolButton_12.setObjectName(_fromUtf8("toolButton_12"))
        self.stackedWidget.addWidget(self.page_3)
        self.toolButton_2 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_2.setEnabled(True)
        self.toolButton_2.setGeometry(QtCore.QRect(950, 0, 55, 65))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/min_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon7)
        self.toolButton_2.setIconSize(QtCore.QSize(52, 62))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.closetoolButton = QtGui.QToolButton(self.centralwidget)
        self.closetoolButton.setGeometry(QtCore.QRect(1010, 0, 55, 65))
        self.closetoolButton.setToolTip(_fromUtf8(""))
        self.closetoolButton.setAutoFillBackground(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon8)
        self.closetoolButton.setIconSize(QtCore.QSize(52, 62))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))
        self.toolButton = QtGui.QPushButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(260, 62, 271, 87))
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setStyleSheet(_fromUtf8("QPushButton{background-image:url(:/images/sm_img_03.png);border:0px;}\n"
"QPushButton:hover{background-image:url(:/images/tar_03.png);border:0px}"))
        self.toolButton.setText(_fromUtf8(""))
        self.toolButton.setIconSize(QtCore.QSize(271, 87))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 550, 263, 51))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/version.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 262, 63))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/funcellimg_01.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 137, 63))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/funcellimg_02.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(257, 60, 8, 492))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(260, 545, 811, 10))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.toolButton_3 = QtGui.QPushButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(530, 61, 271, 87))
        self.toolButton_3.setAutoFillBackground(False)
        self.toolButton_3.setStyleSheet(_fromUtf8("QPushButton{background-image:url(:/images/btn_07.png);border:0px;}\n"
"QPushButton:hover{background-image:url(:/images/tar_qudao_03.png);border:0px}"))
        self.toolButton_3.setText(_fromUtf8(""))
        self.toolButton_3.setIconSize(QtCore.QSize(271, 87))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_4 = QtGui.QPushButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(800, 61, 271, 87))
        self.toolButton_4.setAutoFillBackground(False)
        self.toolButton_4.setStyleSheet(_fromUtf8("QPushButton{background-image:url(:/images/btn_08.png);border:0px;}\n"
"QPushButton:hover{background-image:url(:/images/tar_chubao_05.png);border:0px}"))
        self.toolButton_4.setText(_fromUtf8(""))
        self.toolButton_4.setIconSize(QtCore.QSize(271, 87))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.toolButton_13 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_13.setEnabled(True)
        self.toolButton_13.setGeometry(QtCore.QRect(900, 0, 50, 61))
        self.toolButton_13.setIconSize(QtCore.QSize(52, 62))
        self.toolButton_13.setObjectName(_fromUtf8("toolButton_13"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_12.setText(_translate("MainWindow", "母包路径", None))
        self.pushButton.setText(_translate("MainWindow", "选择", None))
        self.label_13.setText(_translate("MainWindow", "输出路径", None))
        self.pushButton_2.setText(_translate("MainWindow", "选择", None))
        self.label_14.setText(_translate("MainWindow", "签名文件", None))
        self.pushButton_3.setText(_translate("MainWindow", "配置", None))
        self.toolButton_5.setText(_translate("MainWindow", "...", None))
        self.label_25.setText(_translate("MainWindow", "appVersion", None))
        self.pushButton_4.setText(_translate("MainWindow", "保存", None))
        self.label_26.setText(_translate("MainWindow", "resVersion", None))
        self.pushButton_5.setText(_translate("MainWindow", "保存", None))
        self.toolButton_6.setText(_translate("MainWindow", "...", None))
        self.toolButton_7.setText(_translate("MainWindow", "全选", None))
        self.toolButton_8.setText(_translate("MainWindow", "反选", None))
        self.label_15.setText(_translate("MainWindow", "已选渠道：", None))
        self.label_16.setText(_translate("MainWindow", "Xx", None))
        self.label_17.setText(_translate("MainWindow", "未选渠道：", None))
        self.label_18.setText(_translate("MainWindow", "Xx", None))
        self.toolButton_10.setText(_translate("MainWindow", "...", None))
        self.label_19.setText(_translate("MainWindow", "出包：", None))
        self.label_20.setText(_translate("MainWindow", "Xx", None))
        self.label_21.setText(_translate("MainWindow", "成功：", None))
        self.label_22.setText(_translate("MainWindow", "Xx", None))
        self.label_23.setText(_translate("MainWindow", "失败：", None))
        self.label_24.setText(_translate("MainWindow", "Xx", None))
        self.toolButton_9.setText(_translate("MainWindow", "打包", None))
        self.toolButton_11.setText(_translate("MainWindow", "...", None))
        self.toolButton_12.setText(_translate("MainWindow", "...", None))
        self.toolButton_2.setText(_translate("MainWindow", "...", None))
        self.closetoolButton.setText(_translate("MainWindow", "...", None))
        self.toolButton_13.setText(_translate("MainWindow", "设置", None))

import res_rc
