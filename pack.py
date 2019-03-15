# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pack.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from utils.taskManagerModule import taskManager
import utils.start
from PyQt4.Qt import QString
import sys
from kestoreListUI import *
from utils import file_operate
from utils import constant
from packLog import *
from QudaoItem import MyItem
from xml.etree import ElementTree as ET
from utils.xml_manager import XmlManager
from ChannelItem import MyChannelItem
from sip import delete
from utils.http_manager import httpManager
from PIL import Image
import thread
from ChannelVersionUI import *
from ChannelVersionItem import ChannelVersionItem
from ChannelParameterUI import ChannelParameterUI
from ChannelSplashUI import ChannelSplashUI
from ItemDelegate import MyItemDelegate
from pluginListUI import pluginListUI
from pluginListItem import pluginListItem 
from ChannelPluginVersionUI import ChannelPluginVersionListUI
from ChannelPluginVersionItem import ChannelPluginVersionItem
from xml.etree.ElementTree import SubElement
from ChannelSettingUI import ChannelSettingUI
import xml.dom.minidom
import utils.startIcon
from utils.config import ConfigParse
import time
from loading import loadingUI


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


class Ui_MainWindow(QObject):
    __taskProgressBar = {}
    __chanelList = {}
    __jsonChannelList = {}
    __NodeList = {}
    __ChannelItemList={}
    __ChannelIconUrlList = {}
    __jsonChannelRemarkList = {}
    __SuccessPackageNum = 0
    __FailPackageNum = 0
    __TotalPackageNum = 0
#     __loading = None
#     __PackageCompleteMap = {}
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1070, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/funcell.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
"}\n"
"QLineEdit[objectName=\"lineEdit\"],QLineEdit[objectName=\"lineEdit_2\"],QLineEdit[objectName=\"lineEdit_3\"],QLineEdit[objectName=\"lineEdit_4\"],QLineEdit[objectName=\"lineEdit_5\"]{\n"
"    color:black;\n"
"}\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(262, 152, 806, 450))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
#         self.label_4 = QtGui.QLabel(self.page)
#         self.label_4.setGeometry(QtCore.QRect(120, 40, 54, 12))
#         self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_4.setObjectName(_fromUtf8("label_4"))
#         self.label_5 = QtGui.QLabel(self.page)
#         self.label_5.setGeometry(QtCore.QRect(280, 40, 54, 12))
#         self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_5.setObjectName(_fromUtf8("label_5"))
#         self.label_6 = QtGui.QLabel(self.page)
#         self.label_6.setGeometry(QtCore.QRect(120, 80, 54, 12))
#         self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_6.setObjectName(_fromUtf8("label_6"))
#         self.label_7 = QtGui.QLabel(self.page)
#         self.label_7.setGeometry(QtCore.QRect(280, 80, 54, 12))
#         self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_7.setObjectName(_fromUtf8("label_7"))
#         self.label_8 = QtGui.QLabel(self.page)
#         self.label_8.setGeometry(QtCore.QRect(120, 130, 54, 16))
#         self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_8.setObjectName(_fromUtf8("label_8"))
#         self.label_9 = QtGui.QLabel(self.page)
#         self.label_9.setGeometry(QtCore.QRect(280, 130, 54, 12))
#         self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_9.setObjectName(_fromUtf8("label_9"))
#         self.label_10 = QtGui.QLabel(self.page)
#         self.label_10.setGeometry(QtCore.QRect(120, 180, 54, 12))
#         self.label_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_10.setObjectName(_fromUtf8("label_10"))
#         self.label_11 = QtGui.QLabel(self.page)
#         self.label_11.setGeometry(QtCore.QRect(280, 180, 161, 16))
#         self.label_11.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
#         self.label_11.setObjectName(_fromUtf8("label_11"))
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
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.pushButton.setStyleSheet("QPushButton{text-align : left;}")
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
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.label_15.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(120, 20, 54, 12))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(180, 20, 54, 12))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.listWidget = QtGui.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 48, 239, 349))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
#         self.listWidget.setStyleSheet("QToolTip {background-color:white;color:black}")
        self.listWidget.setStyleSheet("""
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:8px;
            margin: 0px 0px 0px 0px;
        }
        QToolTip {
            background-color:white;color:black
        }
    """)
        
        
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
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.listWidget_3.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget_3.setItemDelegate(MyItemDelegate())
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.listWidget_3.setStyleSheet("""
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:5px;
            margin: 0px 0px 0px 0px;
        }
         
    """)

        
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
        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget_2.setItemDelegate(MyItemDelegate())
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_2.setStyleSheet("""
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:5px;
            margin: 0px 0px 0px 0px;
        }
         
    """)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.toolButton_9.clicked.connect(self.on_toolButton_9_clicked)
        self.toolButton_7.clicked.connect(self.selectAll)
        self.toolButton_8.clicked.connect(self.deSelectAll)
        self.connect(taskManager.shareInstance(), SIGNAL("UpdateChanelState"), self.UpdateChanelState)
        self.connect(taskManager.shareInstance(), SIGNAL("UpdatetoolButton_9"), self.UpdatetoolButton_9)
        self.pushButton.clicked.connect(self.selectApkClicked)
        self.pushButton_3.clicked.connect(self.OpenKeyStoreListUI)
        self.toolButton_12.clicked.connect(self.on_toolButton_12_clicked)
        self.connect(taskManager.shareInstance(), SIGNAL("updateTextLog"), self.UpdateFailedChannelState)
        self.connect(taskManager.shareInstance(), SIGNAL("updateKeystore"), self.updateKeystore)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemChanged(QListWidgetItem*)")), self.ListWidgetItemChanged)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.ListWidgetClicked)
        self.pushButton_4.clicked.connect(self.saveAppVersion)
        self.pushButton_5.clicked.connect(self.savaResVersion)
        self.toolButton_5.clicked.connect(self.saveParametersConfig)
        self.pushButton_2.clicked.connect(self.selectOutDir)
        self.connect(self, SIGNAL("updateSplashImage"), self.updateChannelSplashImage)
        self.connect(taskManager.shareInstance(), SIGNAL("UpdateChanelListWidget_icon"), self.UpdateChanelListWidget_icon)
        self.connect(self.toolButton_13, SIGNAL("clicked()"), self, SIGNAL("showSettingMenu()"))
        self.connect(taskManager.shareInstance(), SIGNAL("refreshPackUi"), self.refreshPackUi)
#         self.connect(taskManager.shareInstance(), SIGNAL("callbackListWidget"), self.callbackListWidget)
#         self.connect(taskManager.shareInstance(), SIGNAL("startIconTask"), self.startIconTask)

#         self.showLoading()
        
        self.updateChannelList()
        self.initUI()
        
    
    def refreshPackUi(self):
        print '数据更新中...'
        #清除当前的数据
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        taskManager.shareInstance().clearRecordChannelItemList()
        self.__ChannelIconUrlList.clear()
        self.__jsonChannelList.clear()
        self.__jsonChannelRemarkList.clear()
        
        #刷新最新数据
        self.updateChannelList()
        self.initUI()
        QtGui.QMessageBox.information(None,u"提示", u"数据刷新成功！")
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Funcell快速打包工具", None))
#         self.label_4.setText(_translate("MainWindow", "产品状态", None))
#         self.label_5.setText(_translate("MainWindow", "已上线", None))
#         self.label_6.setText(_translate("MainWindow", "AppId", None))
#         self.label_7.setText(_translate("MainWindow", "100", None))
#         self.label_8.setText(_translate("MainWindow", "AppKey", None))
#         self.label_9.setText(_translate("MainWindow", "1000", None))
#         self.label_10.setText(_translate("MainWindow", "回调地址", None))
#         self.label_11.setText(_translate("MainWindow", "www.haowan123.com", None))
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
    
    
    
    def savaResVersion(self):
        if len(self.lineEdit_5.text()):
            try:
                config = ET.parse(file_operate.getCommonXmlPath())
                root = config.getroot()
                apk = root.find("apk")
                apk.set("resVersion", unicode(self.lineEdit_5.text()))
                config.write(file_operate.getCommonXmlPath(), "utf-8")
                QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
            except Exception,e:
                print e
                print "Error: cannot parse file: commonconfig.xml."
                return -1
    
    def saveAppVersion(self):
        if len(self.lineEdit_4.text()):
            try:
                config = ET.parse(file_operate.getCommonXmlPath())
                root = config.getroot()
                apk = root.find("apk")
                apk.set("appVersion", unicode(self.lineEdit_4.text()))
                config.write(file_operate.getCommonXmlPath(), "utf-8")
                QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
            except Exception,e:
                print e
                print "Error: cannot parse file: commonconfig.xml."
                return -1
            
    def InitfinalsdkDir(self):
        if not os.path.exists(constant.sdkRelatePath):
            os.makedirs(constant.sdkRelatePath)
    
    def OpenKeyStoreListUI(self):
        dialog = keystoreUI()
#         dialog.setFixedSize(QSize(498, 406))
        
        dialog.setParent(self.centralwidget)
        size=self.centralwidget.geometry()
        dialog.move((size.width()-488)/2, (size.height()-402)/2)
        
        dialog.exec_()
    
    def selectOutDir(self):
        s=QtGui.QFileDialog.getExistingDirectory(None,u"选择输出路径")
        if s.length() > 0:
            self.lineEdit_2.setText(file_operate.getFullPath(unicode(s)))
            
    def selectApkClicked(self):
        s=QtGui.QFileDialog.getOpenFileName(None,u"选择APK","/","apk files(*.apk)")  
        if s.length() > 0:
            self.lineEdit.setText(unicode(s))
    
    
    def selectAll(self):
        self.__ChannelIconUrlList.clear()
        for i in range(self.listWidget.count()):
            if  self.listWidget.item(i).checkState() == QtCore.Qt.Unchecked:
                self.listWidget.item(i).setCheckState(QtCore.Qt.Checked)
                self.selectAllListWidgetFunction(self.listWidget.item(i))
                qApp.processEvents() #非常重要的一句，事件循环，避免主线程卡顿，立即分发事件
         
        #将icon地址加入子线程进行下载
        utils.startIcon.stopAllTask()
        utils.startIcon.start(self.__ChannelIconUrlList)
                
    
    def deSelectAll(self):
        for i in range(self.listWidget.count()):
            if  self.listWidget.item(i).checkState() == QtCore.Qt.Checked:
                self.listWidget.item(i).setCheckState(QtCore.Qt.Unchecked)
                
    
    
    def selectAllListWidgetFunction(self,item):
        channelItemList = taskManager.shareInstance().getChannelItemList()
        for key in channelItemList.keys():
            if key == item.text():
                channelitem = channelItemList[key]
                self.listWidget_3.removeItemWidget(channelitem)
                delete(channelitem)
                taskManager.shareInstance().getChannelItemListLock().acquire()
                taskManager.shareInstance().getChannelItemList().pop(key)
                taskManager.shareInstance().getChannelItemListLock().release()
#                 return
        
        chanel_item = MyChannelItem()
        version = '0'
        productcode = ConfigParse.shareInstance().getProductCode()
        for key in self.__jsonChannelList.keys():
            if item.text() == self.__jsonChannelList[key]:
                  
                channelListData = taskManager.shareInstance().getChannelListData()
                chanelData = channelListData[key]
#                 print 'chanelData:',chanelData
                if len(chanelData['description']) > 0:
                    chanel_item.label_4.setText(chanelData['channel_name']+'_'+chanelData['description'])
                else:
                    chanel_item.label_4.setText(chanelData['channel_name'])
                chanel_item.label_6.setText(chanelData['channel_type'])
#                 chanel_item.label_6.setAlignment(QtCore.Qt.AlignLeft)
                markText = chanelData.get('description')
                if (markText is None) or (markText == ''):
                    markText = u'— —'
                chanel_item.label_12.setText(markText)
                
                #显示渠道对应的icon图片，根据配置文件查询 使用client/server/default下的文件
                logDir = 'Log/'
                useServerIconFlag = True
                if os.path.exists(logDir + productcode+'/ChannelSettingSplashAndIconFile.log'):
                    config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
                    root = config.getroot()
                    channelNode = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
                    if channelNode is not None:
                        if channelNode.get("checkBoxflag") == "True":
                            if len(channelNode.get("icon").strip()) > 0: 
                                if os.path.exists(file_operate.getFullPath(channelNode.get("icon"))):
                                    DownloadDir = file_operate.getFullPath("Download/")
                                    img = Image.open(file_operate.getFullPath(channelNode.get("icon")))
                                    if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client')):
                                        os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'))
                                    img.save(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png'))
                                    if os.path.exists(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png')):
#                                         img = Image.open(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png'))
                                        icon = img.resize((60, 60), Image.ANTIALIAS)
                                        icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/channel.png'))
                                        chanel_item.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/channel.png')))
                                        print 'use client icon...'
                                        useServerIconFlag = False
                  
                if useServerIconFlag:
                    if len(chanelData['icon']) > 0:
                        print 'add icon list task...'
                        icondata = {}
                        icondata['obj']=chanel_item
                        icondata['icon']=chanelData['icon']
                        icondata['extend'] = item.text()
                        self.__ChannelIconUrlList[key] = icondata
                    else:
                        #使用默认图片
                        print '使用默认图片...默认不要使用本地图片，open会耗时'
#                         if os.path.exists(file_operate.getFullPath('config/icon/icon.png')):
#                             img = Image.open(file_operate.getFullPath('config/icon/icon.png'))
#                             DownloadDir = file_operate.getFullPath("Download/")
#                             if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default')):
#                                 os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'))
#                             img.save(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png'))
#                             if os.path.exists(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png')):
#                                 img = Image.open(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png'))
#                                 icon = img.resize((60, 60), Image.ANTIALIAS)
#                                 icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/channel.png'))
#                                 chanel_item.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/channel.png')))
                  
                #----------------显示渠道包名---------------------
                useServerPackageFlag = True
                if os.path.exists(logDir +productcode+ '/ChannelSettingApkFile.log'):
                    config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingApkFile.log'))
                    root = config.getroot()
                    channelNode = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
                    if channelNode is not None:
                        if channelNode.get("checkBoxflag") == "True":
                            if channelNode.get("packageName") != None:
                                if len(channelNode.get("packageName").strip()) > 0: 
                                    useServerPackageFlag = False
                                    chanel_item.lineEdit.setText(channelNode.get("packageName"))
                  
                if useServerPackageFlag:
                    chanel_item.lineEdit.setText(chanelData['config']['otherKey']['packageName'])
                #---------------------------------------------
                  
                channelSdkDir = file_operate.getFullPath(constant.sdkRelatePath+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi'])
                versionList = chanelData['version']
                
                #重新判断条件，若本地保存版本有效则显示保存版本，若无效则提示当前客户端版本为无效版本，若没有任何版本，则从json数据中提取最大版本
                flag = False
                logDir = 'Log/'
                logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
                for line in logFile.readlines():
                    line = line.rstrip("\r\n")
                    Info1 = line.split('|')
                    if Info1[0] == chanelData['channel_type'] and Info1[1] == chanelData['game'] +'.'+chanelData['fgi']:
                        flag = True
                logFile.close()
                if flag:
                    self.initChannelVersion(chanelData['channel_type']+':'+chanelData['game'] +'.'+chanelData['fgi'],chanel_item,chanelData['version'])
                else:
                    for key in versionList:
                        if cmp(key['version'],version) == 1:
                            version = key['version']
                               
                    chanel_item.pushButton.setText(str(version))
                #当不存在渠道sdk文件夹时候，先找到最大版本号，然后还需要考虑，当前用户本地没有渠道sdk文件夹，但是用户进行了版本选择，版本选择的也不是最大的版本号，这个时候需要以用户选择的版本号为准，不能使用最大的版本号
#                 if not os.path.exists(channelSdkDir): 
# #                 if not os.path.exists(channelSdkDir) or not os.path.exists('Log/'+productcode+'/ChannelVersionFile.log'): 
# #                     for key in versionList:
# #                         if cmp(key['version'],version) == 1: #key['version'] > version 返回1 相等返回0 小于返回-1
# #                             version = key['version']
#                     
#                     flag = False
#                     #判断是否用户进行了版本选择，如果版本配置文件中，当前渠道的版本号在json数据里面匹配到存在当前用户选择的版本号，那么将使用用户选择的为准
#                     if os.path.exists(logDir +productcode+ '/ChannelVersionFile.log'):
#                         logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'r', 'utf-8')
#                         for line in logFile.readlines():
#                             line = line.rstrip("\r\n")
#                             Info1 = line.split('|')
#                             if Info1[0] == chanelData['channel_type'] and Info1[1] == chanelData['game'] +'.'+chanelData['fgi']:
#                                 #找到用户本地的版本
#                                 flag = True
#                         logFile.close()
#                         if flag:
#                             self.initChannelVersion(chanelData['channel_type']+':'+chanelData['game'] +'.'+chanelData['fgi'],chanel_item,chanelData['version'])
#                         else:
#                             for key in versionList:
#                                 if cmp(key['version'],version) == 1:
#                                     version = key['version']
#                                     
#                             chanel_item.pushButton.setText(str(version))
#                     
# #                     print 'version:',version
# #                     chanel_item.pushButton.setText(str(version))
#                 else:
#                     flag = False
#                     logDir = 'Log/'
#                     logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
#                     for line in logFile.readlines():
#                         line = line.rstrip("\r\n")
#                         Info1 = line.split('|')
#                         if Info1[0] == chanelData['channel_type'] and Info1[1] == chanelData['game'] +'.'+chanelData['fgi']:
#                             flag = True
#                     logFile.close()
#                     if flag:
#                         self.initChannelVersion(chanelData['channel_type']+':'+chanelData['game'] +'.'+chanelData['fgi'],chanel_item,chanelData['version'])
#                     else:
#                         for key in versionList:
#                             if cmp(key['version'],version) == 1:
#                                 version = key['version']
#                                   
#                         chanel_item.pushButton.setText(str(version))
                  
#                 print 'chanelData:',chanelData['game']
                chanel_item.pushButton.clicked.connect(partial(self.openChannelVersionUI,versionList,chanel_item,chanelData))
                chanel_item.pushButton_2.clicked.connect(partial(self.openChannelSettingUI,chanelData,chanel_item))
                chanel_item.pushButton_3.clicked.connect(partial(self.openChannelSplashUI,chanelData,chanel_item))
                chanel_item.pushButton_4.clicked.connect(partial(self.openChannelPluginLsUI,chanelData,chanel_item))
                chanel_item.closetoolButton.clicked.connect(partial(self.closeChannelItem,item))
#                 chanel_item.pushButton_5.clicked.connect(partial(self.openChannelSettingUI,chanelData,chanel_item))
          
        item1 = QtGui.QListWidgetItem()
        item1.setSizeHint(QSize(0, 111))
          
        self.listWidget_3.addItem(item1)
        self.listWidget_3.setItemWidget(item1,chanel_item)
#         self.listWidget_3.update()
        taskManager.shareInstance().setChannelItemList(item.text(),item1)
        
    def ListWidgetItemChanged(self,item):
#         print 'ListWidgetItemChanged Changed'
        selected_num = 0
        unselected_num = 0
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                selected_num += 1
        unselected_num = self.listWidget.count() - selected_num
        self.label_16.setText(str(selected_num))
        self.label_18.setText(str(unselected_num))
        
    
    def ListWidgetClicked(self,item):
#         print 'ListWidgetClicked itemDoubleClicked'
        channelItemList = taskManager.shareInstance().getChannelItemList()
        for key in channelItemList.keys():
            if key == item.text():
                for i in self.__jsonChannelList.keys():
                    if item.text() == self.__jsonChannelList[i]:
                        channelitem = channelItemList[key]
                        self.listWidget_3.removeItemWidget(channelitem)
                        delete(channelitem)
                        taskManager.shareInstance().getChannelItemListLock().acquire()
                        taskManager.shareInstance().getChannelItemList().pop(key)
                        taskManager.shareInstance().getChannelItemListLock().release()
                        return
        
        chanel_item = MyChannelItem()
        version = '0'
        self.__ChannelIconUrlList.clear()
        productcode = ConfigParse.shareInstance().getProductCode()
        for key in self.__jsonChannelList.keys():
            if item.text() == self.__jsonChannelList[key]:
#                 print '---------------key:%s'%key
                channelListData = taskManager.shareInstance().getChannelListData()
                chanelData = channelListData[key]
#                 print 'chanelData:',chanelData
                if len(chanelData['description']) > 0:
                    chanel_item.label_4.setText(chanelData['channel_name']+'_'+chanelData['description'])
                else:
                    chanel_item.label_4.setText(chanelData['channel_name'])
                chanel_item.label_6.setText(chanelData['channel_type'])
#                 chanel_item.label_6.setAlignment(QtCore.Qt.AlignLeft)
                markText = chanelData.get('description')
                if (markText is None) or (markText == ''):
                    markText = u'— —'
                chanel_item.label_12.setText(markText)
#                 httpManager.shareInstance().GetImage(chanelData['icon'])#此处下载图片需要放到其他地方实现
                
                #显示下载的渠道对应的icon图片
#                 if os.path.exists(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/icon.png')):
#                     img = Image.open(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/icon.png'))
#                     icon = img.resize((60, 60), Image.ANTIALIAS)
#                     icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/channel.png'))
#                     chanel_item.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/channel.png')))
                
                #显示渠道对应的icon图片，根据配置文件查询 使用client/server/default下的文件
                logDir = 'Log/'
                useServerIconFlag = True
                if os.path.exists(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'):
                    config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
                    root = config.getroot()
                    channelNode = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
                    if channelNode is not None:
                        if channelNode.get("checkBoxflag") == "True":
                            if len(channelNode.get("icon").strip()) > 0: 
                                if os.path.exists(file_operate.getFullPath(channelNode.get("icon"))):
                                    DownloadDir = file_operate.getFullPath("Download/")
                                    img = Image.open(file_operate.getFullPath(channelNode.get("icon")))
                                    if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client')):
                                        os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'))
                                    img.save(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png'))
                                    if os.path.exists(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png')):
#                                         img = Image.open(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png'))
                                        icon = img.resize((60, 60), Image.ANTIALIAS)
                                        icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/channel.png'))
                                        chanel_item.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/channel.png')))
                                        print 'use client icon...'
                                        useServerIconFlag = False
                
                if useServerIconFlag:
                    if len(chanelData['icon']) > 0:
                        print 'add icon list task...'
                        icondata = {}
                        icondata['obj']=chanel_item
                        icondata['icon']=chanelData['icon']
                        icondata['extend'] = item.text()
                        self.__ChannelIconUrlList[key] = icondata
                        
                    else:
                        #使用默认图片
                        print '使用默认图片...默认不要使用本地图片，open会耗时'
#                         utils.taskManagerModule.taskManager.shareInstance().getIconLock().acquire()
#                         if os.path.exists(file_operate.getFullPath('config/icon/icon.png')):
#                             img = Image.open(file_operate.getFullPath('config/icon/icon.png'))
#                             DownloadDir = file_operate.getFullPath("Download/")
#                             if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default')):
#                                 os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'))
#                             img.save(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png'))
#                             if os.path.exists(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png')):
#                                 img = Image.open(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png'))
#                                 icon = img.resize((60, 60), Image.ANTIALIAS)
#                                 icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/channel.png'))
#                                 chanel_item.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/channel.png')))
#                         utils.taskManagerModule.taskManager.shareInstance().getIconLock().release()
                #----------------显示渠道包名---------------------
                useServerPackageFlag = True
                if os.path.exists(logDir +productcode+ '/ChannelSettingApkFile.log'):
                    config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingApkFile.log'))
                    root = config.getroot()
                    channelNode = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
                    if channelNode is not None:
                        if channelNode.get("checkBoxflag") == "True":
                            if channelNode.get("packageName") != None:
                                if len(channelNode.get("packageName").strip()) > 0: 
                                    useServerPackageFlag = False
                                    chanel_item.lineEdit.setText(channelNode.get("packageName"))
                
                if useServerPackageFlag:
                    chanel_item.lineEdit.setText(chanelData['config']['otherKey']['packageName'])
                #---------------------------------------------
                channelSdkDir = file_operate.getFullPath(constant.sdkRelatePath+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi'])
                versionList = chanelData['version']
                #重新判断条件，若本地保存版本有效则显示保存版本，若无效则提示当前客户端版本为无效版本，若没有任何版本，则从json数据中提取最大版本
                flag = False
                logDir = 'Log/'
                logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
                for line in logFile.readlines():
                    line = line.rstrip("\r\n")
                    Info1 = line.split('|')
                    if Info1[0] == chanelData['channel_type'] and Info1[1] == chanelData['game'] +'.'+chanelData['fgi']:
                        flag = True
                logFile.close()
                if flag:
                    self.initChannelVersion(chanelData['channel_type']+':'+chanelData['game'] +'.'+chanelData['fgi'],chanel_item,chanelData['version'])
                else:
                    for key in versionList:
                        if cmp(key['version'],version) == 1:
                            version = key['version']
                               
                    chanel_item.pushButton.setText(str(version))
                
                #当不存在渠道sdk文件夹时候，先找到最大版本号，然后还需要考虑，当前用户本地没有渠道sdk文件夹，但是用户进行了版本选择，版本选择的也不是最大的版本号，这个时候需要以用户选择的版本号为准，不能使用最大的版本号
#                 if not os.path.exists(channelSdkDir): 
# #                 if not os.path.exists(channelSdkDir) or not os.path.exists('Log/'+productcode+'/ChannelVersionFile.log'): 
# #                     for key in versionList:
# #                         if cmp(key['version'],version) == 1: #key['version'] > version 返回1 相等返回0 小于返回-1
# #                             version = key['version']
#                     
#                     flag = False
#                     #判断是否用户进行了版本选择，如果版本配置文件中，当前渠道的版本号在json数据里面匹配到存在当前用户选择的版本号，那么将使用用户选择的为准
#                     if os.path.exists(logDir +productcode+ '/ChannelVersionFile.log'):
#                         logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'r', 'utf-8')
#                         for line in logFile.readlines():
#                             line = line.rstrip("\r\n")
#                             Info1 = line.split('|')
#                             if Info1[0] == chanelData['channel_type'] and Info1[1] == chanelData['game'] +'.'+chanelData['fgi']:
#                                 #找到用户本地的版本
#                                 flag = True
#                         logFile.close()
#                         if flag:
#                             self.initChannelVersion(chanelData['channel_type']+':'+chanelData['game'] +'.'+chanelData['fgi'],chanel_item,chanelData['version'])
#                         else:
#                             for key in versionList:
#                                 if cmp(key['version'],version) == 1:
#                                     version = key['version']
#                                     
#                             chanel_item.pushButton.setText(str(version))
#                     
# #                     print 'version:',version
# #                     chanel_item.pushButton.setText(str(version))
#                 else:
#                     flag = False
#                     logDir = 'Log/'
#                     logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
#                     for line in logFile.readlines():
#                         line = line.rstrip("\r\n")
#                         Info1 = line.split('|')
#                         if Info1[0] == chanelData['channel_type'] and Info1[1] == chanelData['game'] +'.'+chanelData['fgi']:
#                             flag = True
#                     logFile.close()
#                     if flag:
#                         self.initChannelVersion(chanelData['channel_type']+':'+chanelData['game'] +'.'+chanelData['fgi'],chanel_item,chanelData['version'])
#                     else:
#                         for key in versionList:
#                             if cmp(key['version'],version) == 1:
#                                 version = key['version']
#                                 
#                         chanel_item.pushButton.setText(str(version))
                        
                    
                chanel_item.pushButton.clicked.connect(partial(self.openChannelVersionUI,versionList,chanel_item,chanelData))
                chanel_item.pushButton_2.clicked.connect(partial(self.openChannelSettingUI,chanelData,chanel_item))
                chanel_item.pushButton_3.clicked.connect(partial(self.openChannelSplashUI,chanelData,chanel_item))
                chanel_item.pushButton_4.clicked.connect(partial(self.openChannelPluginLsUI,chanelData,chanel_item))
                chanel_item.closetoolButton.clicked.connect(partial(self.closeChannelItem,item))
#                 chanel_item.pushButton_5.clicked.connect(partial(self.openChannelSettingUI,chanelData,chanel_item))
        
        item1 = QtGui.QListWidgetItem()
        item1.setSizeHint(QSize(0, 111))
        
        self.listWidget_3.addItem(item1)
        self.listWidget_3.setItemWidget(item1,chanel_item)
        taskManager.shareInstance().setChannelItemList(item.text(),item1)
        #将icon地址加入子线程进行下载
        utils.startIcon.stopAllTask()
        utils.startIcon.start(self.__ChannelIconUrlList)
    
    
    def closeChannelItem(self,item):
        channelItemList = taskManager.shareInstance().getChannelItemList()
        for key in channelItemList.keys():
            if key == item.text():
                for i in self.__jsonChannelList.keys():
                    if item.text() == self.__jsonChannelList[i]:
                        channelitem = channelItemList[key]
                        itemRow = self.listWidget_3.row(channelitem)
                        remove_item = self.listWidget_3.takeItem(itemRow)
                        self.listWidget_3.removeItemWidget(remove_item)
                        delete(remove_item)
                        taskManager.shareInstance().getChannelItemList().pop(key)
    
    def modifyChannelSplashImage(self,chanel_item,horizontal):
        channel = str(chanel_item.label_6.text())
        channelDir = file_operate.getFullPath(constant.sdkRelatePath+channel)
        if os.path.exists(channelDir) and os.path.exists(file_operate.getFullPath("Download/Splash/fun_plugin_splash.png")):
            ForSplashDir = channelDir+'/ForSplash'
            if horizontal:
                dir = ForSplashDir+'/landscape'
                hasSplashvalue = 'landscape'
            else:
                dir = ForSplashDir+'/portrait'
                hasSplashvalue = 'portrait'
            drawable = dir+'/drawable'
            drawablehdpi = dir+'/drawable-hdpi'
            drawableldpi= dir+'/drawable-ldpi'
            drawablemdpi= dir+'/drawable-mdpi'
            drawablexhdpi= dir+'/drawable-xhdpi'
            
            if os.path.exists(drawable):
                file_operate.delete_file_folder(drawable)
            if os.path.exists(drawablehdpi):
                file_operate.delete_file_folder(drawablehdpi)
            if os.path.exists(drawableldpi):
                file_operate.delete_file_folder(drawableldpi)
            if os.path.exists(drawablemdpi):
                file_operate.delete_file_folder(drawablemdpi)
            if os.path.exists(drawablexhdpi):
                file_operate.delete_file_folder(drawablexhdpi)
            
            if not os.path.exists(drawable):
                os.makedirs(drawable)
            if not os.path.exists(drawablehdpi):
                os.makedirs(drawablehdpi)
            if not os.path.exists(drawableldpi):
                os.makedirs(drawableldpi)
            if not os.path.exists(drawablemdpi):
                os.makedirs(drawablemdpi)
            if not os.path.exists(drawablexhdpi):
                os.makedirs(drawablexhdpi)
            
            drawableSize = (480, 320)
            hdpiSize = (800, 480)
            ldpiSize = (320, 240)
            mdpiSize = (480, 320)
            xhdpiSize = (1280,720)
            
            img = Image.open(file_operate.getFullPath("Download/Splash/fun_plugin_splash.png"))
            
            drawableIcon = img.resize(drawableSize, Image.ANTIALIAS)
            hdpiIcon = img.resize(hdpiSize, Image.ANTIALIAS)
            ldpiIcon = img.resize(ldpiSize, Image.ANTIALIAS)
            mdpiIcon = img.resize(mdpiSize, Image.ANTIALIAS)
            xhdpiIcon = img.resize(xhdpiSize, Image.ANTIALIAS)
            
            splashIconName = 'fun_plugin_splash.png'
        
            drawableIcon.save(os.path.join(drawable, splashIconName), 'PNG')
            hdpiIcon.save(os.path.join(drawablehdpi, splashIconName), 'PNG')
            ldpiIcon.save(os.path.join(drawableldpi, splashIconName), 'PNG')
            mdpiIcon.save(os.path.join(drawablemdpi, splashIconName), 'PNG')
            xhdpiIcon.save(os.path.join(drawablexhdpi, splashIconName), 'PNG')
            
            try:
                configfile = file_operate.getchannelFuncellConfigXmlPath(channel)
                config = ET.parse(configfile)
                root = config.getroot()
                splashLsNode = root.find('splash')
                if splashLsNode is not None:
                    hasSplashLsNode = splashLsNode.find('hasSplash')
                    hasSplash = hasSplashLsNode.text
                    if hasSplash != hasSplashvalue:
                        hasSplashLsNode.text = hasSplashvalue
                        config.write(file_operate.getchannelFuncellConfigXmlPath(channel), "utf-8")
                        
                else:
                    splash = SubElement(root, 'splash')
                    splash.set('type', 'dict')
                    splash_hasSplash = SubElement(splash, 'hasSplash')
                    splash_hasSplash.set('type', 'str')
                    splash_hasSplash.text = hasSplashvalue
                    config.write(file_operate.getchannelFuncellConfigXmlPath(channel), "utf-8")
                    
            except Exception,e:
                print e
                print "Error: modify FuncellConfig by splash"
                return -1
            
    
    def updateChannelSplashImage(self,dialog,chanel_item,channel):
        #替换最新的闪屏文件到指定的渠道目录
#         self.modifyChannelSplashImage(chanel_item,horizontal)
        
        dialog.label_2.setPixmap(QPixmap(file_operate.getFullPath('Download/Splash/'+channel+'/fun_plugin_splash.png')))
        widget = dialog.stackedWidget.widget(1)
        dialog.stackedWidget.setCurrentWidget(widget)
        dialog.stopAnimation()
    
    def getChannelSplash(self,splashUrl,dialog,chanel_item,channel):
        if len(splashUrl) > 0:
            httpManager.shareInstance().GetSplashImage(splashUrl,channel)
            self.emit(SIGNAL("updateSplashImage"), dialog,chanel_item,channel)
        thread.exit_thread()
    
    def openChannelPluginLsUI(self,chanelData,chanel_item):
        channel = chanel_item.label_6.text()
        PluginlListData = taskManager.shareInstance().getPluginlListData()
        dialog = pluginListUI()
        dialog.setFixedSize(QSize(498, 406))
        productcode = ConfigParse.shareInstance().getProductCode()
        
        if chanelData.has_key('config'):
            configData = chanelData['config']
            if configData.has_key('pluginLs'):
                channelPluginListData = configData['pluginLs']
                for key_data in  channelPluginListData:
                    plugintype = key_data['typePlugin']
                    pluginchannel = key_data['channel']
                    game_fgi = chanelData['game']+'.'+chanelData['fgi']
#                     status = key_data['status']
#                     version = key_data['version']
                    
#                     if 'enable' == status:
                    version = '0'
                    item = pluginListItem()
                    for key_pluginData in PluginlListData:
                        _pluginType = key_pluginData['type']
                        _pluginChannel = key_pluginData['channel']
                        if plugintype == _pluginType and pluginchannel == _pluginChannel:
#                                 pluginSdkDir = file_operate.getFullPath(constant.sdkRelatePath+plugintype+'/'+str(channel)+'/'+pluginchannel)
                            pluginSdkDir = file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/'+game_fgi+'/'+plugintype+'/'+pluginchannel)
                            
                            #重新判断条件，根据ChannelPluginListVersionFile中配置的版本进行查找，若保存的版本有效则显示本地保存版本，若无效则提示显示当前客户端保存版本为 无效版本,若没有任何版本，则从json数据中提取最大版本
                            flag = False
                            logDir = 'Log/'
                            logFile = codecs.open(logDir +productcode+ '/ChannelPluginListVersionFile.log', 'a+', 'utf-8')
                            for line in logFile.readlines():
                                line = line.rstrip("\r\n")
                                Info1 = line.split('|')
                                if Info1[0] == plugintype and Info1[1] == chanelData['channel_type'] and Info1[2] == game_fgi and Info1[3] == pluginchannel:
                                    flag = True
                                    version = Info1[4]
                            logFile.close()
                            if flag:
                                #判断当前版本是否有效
                                versionflag = False
                                pluginVersionListData = key_pluginData['version']
                                for key_pluginVersion in pluginVersionListData:
                                    if cmp(key_pluginVersion['version'],version) == 0:
                                        versionflag = True
                                if versionflag:
                                    item.pushButton.setText(str(version))
                                else:
                                    item.pushButton.setText(u'无效版本,请重新选择可用版本')
                            else:
                                pluginVersionListData = key_pluginData['version']
                                for key_pluginVersion in pluginVersionListData:
                                    if cmp(key_pluginVersion['version'],version) == 1:
                                        version = key_pluginVersion['version']
                                item.pushButton.setText(str(version))
                            
#                             if not os.path.exists(pluginSdkDir) or not os.path.exists('Log/'+productcode+'/ChannelPluginListVersionFile.log'):
# #                                 if not os.path.exists('Log/ChannelPluginListVersionFile.log'):
#                                 pluginVersionListData = key_pluginData['version']
#                                 for key_pluginVersion in pluginVersionListData:
#                                     if cmp(key_pluginVersion['version'],version) == 1:
#                                         version = key_pluginVersion['version']
# #                                             print '-------plugin version:',version
#                                 item.pushButton.setText(str(version))
#                             else:
#                                 flag = False
#                                 logDir = 'Log/'
#                                 logFile = codecs.open(logDir +productcode+ '/ChannelPluginListVersionFile.log', 'a+', 'utf-8')
#                                 for line in logFile.readlines():
#                                     line = line.rstrip("\r\n")
#                                     Info1 = line.split('|')
#                                     if Info1[0] == plugintype and Info1[1] == chanelData['channel_type'] and Info1[2] == game_fgi and Info1[3] == pluginchannel:
#                                         flag = True
#                                         version = Info1[4]
#                                 logFile.close()
#                                 if flag:
#                                     #判断当前版本是否有效
#                                     versionflag = False
#                                     pluginVersionListData = key_pluginData['version']
#                                     for key_pluginVersion in pluginVersionListData:
#                                         if cmp(key_pluginVersion['version'],version) == 0:
#                                             versionflag = True
#                                     if versionflag:
#                                         item.pushButton.setText(str(version))
#                                     else:
#                                         item.pushButton.setText(u'无效版本,请重新选择可用版本')
#                                 else:
#                                     
#                                     pluginVersionListData = key_pluginData['version']
#                                     for key_pluginVersion in pluginVersionListData:
#                                         if cmp(key_pluginVersion['version'],version) == 1:
#                                             version = key_pluginVersion['version']
#                                     item.pushButton.setText(str(version))

                    print 'plugintype:%s | pluginchannel:%s | version:%s'%(plugintype,pluginchannel,str(version))
                    
                    item1 = QtGui.QListWidgetItem()
                    item1.setSizeHint(QSize(0, 42))
                     
#                     item = pluginListItem()
#                     item.pushButton.setText(str(version))
                    item.label.setText(plugintype)
                    item.label_2.setText(pluginchannel)

                    dialog.listWidget.addItem(item1)
                    dialog.listWidget.setItemWidget(item1,item)
                     
                    item.pushButton.clicked.connect(partial(self.openChannelPluginUI,key_data,chanel_item,dialog,chanelData))
                    
        dialog.exec_()
    
    
    def openChannelPluginUI(self,channelPluginData,chanel_item,pluginListUIdialog,chanelData):
        channel = chanel_item.label_6.text()
        PluginlListData = taskManager.shareInstance().getPluginlListData()
#         print 'channel',channel
        dialog = ChannelPluginVersionListUI()
        dialog.setFixedSize(QSize(498, 406))
        
        pluginType = channelPluginData['typePlugin']
        pluginChannel = channelPluginData['channel']
#         pluginVersion = channelPluginData['version']
        
#         print 'pluginType:%s | pluginChannel:%s'%(pluginType,pluginChannel)
        for key_data in PluginlListData:
#             print 'key_data',key_data
            _pluginType = key_data['type']
            _pluginChannel = key_data['channel']
            if _pluginType == pluginType and _pluginChannel == pluginChannel:
#                 print '插件类型&插件渠道一致'
                _versionListData = key_data['version']
#                 _pluginDescript = key_data['descript']
                for key_versionData in _versionListData:
                    pluginVersionItem = ChannelPluginVersionItem()
                    _pluginVersion = key_versionData['version']
                    _pluginDate = key_versionData['date']
                    pluginVersionItem.label.setText(_pluginDate)
                    pluginVersionItem.label_2.setText(_pluginVersion)
                    if key_versionData.has_key('des'):
                        _pluginDescript = key_versionData['des']
                        pluginVersionItem.label_3.setText(_pluginDescript)
                    
                    item1 = QtGui.QListWidgetItem()
                    item1.setSizeHint(QSize(0, 42))
                    
                    dialog.listWidget.addItem(item1)
                    dialog.listWidget.setItemWidget(item1,pluginVersionItem)
        
        dialog.pushButton_2.clicked.connect(partial(self.ChannelPluginVersionListUI_pushButton_2_function,dialog,channelPluginData,chanel_item,pluginListUIdialog,chanelData))
        
        dialog.exec_()
    
    def ChannelPluginVersionListUI_pushButton_2_function(self,dialog,channelPluginData,chanel_item,pluginListUIdialog,chanelData):
        channel = chanel_item.label_6.text()
        item = dialog.listWidget.currentItem()
        if item != None:
            pluginVersion = dialog.listWidget.itemWidget(item).label_2.text()
            print 'pluginVersion:',pluginVersion
#             dialog.listWidget.itemWidget(item).pushButton.setText(pluginVersion)
            pluginType = channelPluginData['typePlugin']
            pluginChannel = channelPluginData['channel']
            for i in range(pluginListUIdialog.listWidget.count()):
                itempluginListUI = pluginListUIdialog.listWidget.item(i)
                itempluginListUI = pluginListUIdialog.listWidget.itemWidget(itempluginListUI)
                if pluginType == itempluginListUI.label.text() and pluginChannel == itempluginListUI.label_2.text():
                    print 'modify current item pluginVersion'
                    itempluginListUI.pushButton.setText(pluginVersion)
            
            #-------------保存当前配置
            self.SaveChannelPluginVersionConfig(pluginType+'|'+channel+'|'+chanelData['game']+'.'+chanelData['fgi']+'|'+pluginChannel+'|'+pluginVersion)
            
        dialog.close()
    
    def SaveChannelPluginVersionConfig(self,info):
#         print 'info',info
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
        
        oldstr=''
        newstr=''
        flag = False
        if os.path.exists(logDir +productcode+ '/ChannelPluginListVersionFile.log'):
            logFile = codecs.open(logDir +productcode+ '/ChannelPluginListVersionFile.log', 'a+', 'utf-8')
            for line in logFile.readlines():
                line = line.rstrip("\r\n")
                Info1 = line.split('|')
                Info2 = info.split('|')
                if Info1[0] == Info2[0] and Info1[1] == Info2[1] and Info1[2] == Info2[2] and Info1[3] == Info2[3]:
                    flag = True
                    oldstr = line
                    newstr = info
                    
            logFile.close()
            if flag:
                self.modifyFileContent(logDir +productcode+ '/ChannelPluginListVersionFile.log', str(oldstr), str(newstr))
                return
        
        
        logFile = codecs.open(logDir +productcode+ '/ChannelPluginListVersionFile.log', 'a+', 'utf-8')
        content = info + '\n'
        logFile.write(unicode(content, 'gbk'))
        logFile.close()
        
    def showLoading(self):
        taskManager.shareInstance().getLoadingUI().setWindowModality(Qt.ApplicationModal)
        taskManager.shareInstance().getLoadingUI().show()
    
    def dismissLoading(self):
        taskManager.shareInstance().getLoadingUI().stopAnimation()
        taskManager.shareInstance().getLoadingUI().close()
    
    def openChannelSplashUI(self,chanelData,chanel_item):
        splashUrl = chanelData['screen']
        channel = chanelData['channel_type']
        
        dialog = ChannelSplashUI()
        dialog.setFixedSize(QSize(498, 370))
        #判断闪屏显示是否使用客户端配置的闪屏图片
        downloadFlag = True
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if os.path.exists(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'):
            config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
            root = config.getroot()
            channelNode = root.find('channel_'+channel+'_'+chanelData['game']+'.'+chanelData['fgi'])
            if channelNode is not None:
                if channelNode.get("checkBoxflag") == "True":
                    if len(channelNode.get("splash").strip()) > 0:
                        if os.path.exists(file_operate.getFullPath(channelNode.get("splash"))):
                            downloadFlag = False
                            #--------------读取本地显示------------------
                            DownloadDir = file_operate.getFullPath("Download/")
                            img = Image.open(file_operate.getFullPath(channelNode.get("splash")))
                            if not os.path.exists(DownloadDir+'Splash/'+channel+'/'+chanelData['game']+'.'+chanelData['fgi']):
                                os.makedirs(DownloadDir+'Splash/'+channel+'/'+chanelData['game']+'.'+chanelData['fgi'])
                            icon = img.resize((495,280), Image.ANTIALIAS)
                            icon.save(file_operate.getFullPath(DownloadDir+'Splash/'+channel+'/'+chanelData['game']+'.'+chanelData['fgi']+'/fun_plugin_splash.png'))
                            print '使用客户端配置闪屏文件...'
                            self.emit(SIGNAL("updateSplashImage"), dialog,chanel_item,channel+'/'+chanelData['game']+'.'+chanelData['fgi'])
                            
                    else:
                        QtGui.QMessageBox.information(None,u"提示", u"客户端设置项未配置闪屏文件！")
                        return
            
        if downloadFlag:
            if len(splashUrl) > 0:
#                 dialog = ChannelSplashUI()
#                 dialog.setFixedSize(QSize(498, 370))
                print '下载闪屏文件...'
                thread.start_new_thread(self.getChannelSplash, (splashUrl,dialog,chanel_item,channel+'/'+chanelData['game']+'.'+chanelData['fgi']))
#                 dialog.exec_()
            else:
                QtGui.QMessageBox.information(None,u"提示", u"后台未配置闪屏文件！")
                return
        
        dialog.exec_()
    
    def openChannelSettingUI(self,chanelData,chanel_item):
        
        dialog = ChannelSettingUI()
        dialog.setFixedSize(QSize(498, 370))
        
        dialog.label.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">"+chanelData['channel_name']+"</span></p><p><span style=\" font-weight:600; color:#ffffff;\"><br/></span></p></body></html>")
        #----------------init parameter tab
        ConfigNodeList = chanelData['config']
        YPoint = 0
        for NodeKey in ConfigNodeList.keys():
            if isinstance(ConfigNodeList[NodeKey],list):
                pass
            else:
                for attributeKey in ConfigNodeList[NodeKey]:
                    if len(ConfigNodeList[NodeKey][attributeKey]) > 0:
                        lineEdit = QtGui.QLineEdit(dialog.parameter)
                        lineEdit.setGeometry(QtCore.QRect(40, 23+YPoint, 131, 20))
                        lineEdit.setText(attributeKey)
                        lineEdit.setStyleSheet("border:0px;background-color:transparent;")
                        lineEdit.setReadOnly(True)
                        label = QtGui.QLabel(dialog.parameter)
                        label.setGeometry(QtCore.QRect(210, 23+YPoint, 16, 16))
                        label.setText(':')
                        lineEdit2 = QtGui.QLineEdit(dialog.parameter)
                        lineEdit2.setGeometry(QtCore.QRect(250, 23+YPoint, 221, 20))
                        lineEdit2.setStyleSheet("border:0px;background-color:transparent;")
                        lineEdit2.setReadOnly(True)
                        lineEdit2.setText(ConfigNodeList[NodeKey][attributeKey])
                        YPoint += 22
        
        #--------------init multidex tab
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
#         if os.path.exists(logDir +productcode+ '/ChannelSettingMultidexFile.log'):
#             logFile = codecs.open(logDir +productcode+ '/ChannelSettingMultidexFile.log', 'a+', 'utf-8')
#             for line in logFile.readlines():
#                 line = line.rstrip("\r\n")
#                 Info1 = line.split('|')
#                 if Info1[0] == chanelData['channel_type'] and Info1[1] == chanelData['game']+'.'+chanelData['fgi']:
#                     dexNum = Info1[2]
#                     checkBoxflag = False
#                     if Info1[3] == "True":
#                         checkBoxflag = True
#                     if len(Info1) >= 5:
#                         if Info1[4] == "False":
#                             dialog.comboBox_2.setCurrentIndex(0)
#                         else:
#                             dialog.comboBox_2.setCurrentIndex(1)
#                     dialog.lineEdit_2.setText(dexNum)
#                     dialog.checkBox.setChecked(checkBoxflag)
#         dialog.pushButton_2.clicked.connect(partial(self.saveChannelSetting_multidex,chanelData,dialog))
        
        
        if os.path.exists(logDir +productcode+ '/ChannelSettingMultidexFile.xml'):
            config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingMultidexFile.xml'))
            root = config.getroot()
            channel = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
            if channel is not None:
                dialog.lineEdit_2.setText(channel.get("dexNum"))
                checkBoxflag = False
                if channel.get("checkBoxflag") == "True":
                    checkBoxflag = True
                dialog.checkBox.setChecked(checkBoxflag)
                dialog.lineEdit_14.setText(channel.get("multidexPath"))
                if channel.get("useFuncellApplicationJarFlag") == "False":
                    dialog.comboBox_2.setCurrentIndex(0)
                else:
                    dialog.comboBox_2.setCurrentIndex(1)
        
        dialog.pushButton_2.clicked.connect(partial(self.saveChannelSetting_multidex,chanelData,dialog))
        dialog.pushButton_7.clicked.connect(partial(self.openChannelSetting_multidexPath,chanelData,dialog))
        
        #---------------init apk tab
        if os.path.exists(logDir +productcode+ '/ChannelSettingApkFile.log'):
            config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingApkFile.log'))
            root = config.getroot()
            channel = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
            if channel is not None:
                dialog.lineEdit_3.setText(channel.get("appName"))
                dialog.lineEdit_6.setText(channel.get("versionCode"))
                dialog.lineEdit_7.setText(channel.get("versionName"))
                dialog.lineEdit_8.setText(channel.get("minsdkVersion"))
                dialog.lineEdit_9.setText(channel.get("targetsdkVersion"))
                if channel.get("packageName") != None:
                    print 'get packagename'
                    dialog.lineEdit_13.setText(channel.get("packageName"))
                    
                checkBoxflag = False
                if channel.get("checkBoxflag") == "True":
                    checkBoxflag = True
                dialog.checkBox_3.setChecked(checkBoxflag)
        dialog.pushButton_4.clicked.connect(partial(self.saveChannelSetting_apk,chanelData,dialog,chanel_item))
        
        #-------------init other tab
        if os.path.exists(logDir +productcode+ '/ChannelSettingOtherFile.log'):
            config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingOtherFile.log'))
            root = config.getroot()
            channel = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
            if channel is not None:
                dialog.lineEdit_4.setText(channel.get("source"))
                dialog.lineEdit_10.setText(channel.get("target"))
                checkBoxflag = False
                if channel.get("checkBoxflag") == "True":
                    checkBoxflag = True
                dialog.checkBox_4.setChecked(checkBoxflag)
                     
        dialog.pushButton_5.clicked.connect(partial(self.saveChannelSetting_other,chanelData,dialog))
        
        #-------------init splash_icon tab
        if os.path.exists(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'):
            config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
            root = config.getroot()
            channel = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
            if channel is not None:
                dialog.lineEdit_5.setText(channel.get("splash"))
                dialog.lineEdit_11.setText(channel.get("icon"))
                if channel.get("splash_time") is not None:
                    dialog.lineEdit_12.setText(channel.get("splash_time"))
                if channel.get("splash_fromAlpha") is not None:
                    dialog.lineEdit_16.setText(channel.get("splash_fromAlpha"))
                checkBoxflag = False
                if channel.get("checkBoxflag") == "True":
                    checkBoxflag = True
                dialog.checkBox_5.setChecked(checkBoxflag)
                if channel.get("landscapeFlag") == "True":
                    dialog.comboBox.setCurrentIndex(0)
                else:
                    dialog.comboBox.setCurrentIndex(1)
        
        dialog.pushButton.clicked.connect(partial(self.openChannelSetting_splashicon_splash,chanelData,dialog))
        dialog.pushButton_3.clicked.connect(partial(self.openChannelSetting_splashicon_icon,chanelData,dialog))
        dialog.pushButton_6.clicked.connect(partial(self.saveChannelSetting_splash_icon,chanelData,dialog,chanel_item))
        
        dialog.exec_()
    
    def openChannelSetting_splashicon_splash(self,chanelData,dialog):
        s=QtGui.QFileDialog.getOpenFileName(None,u"选择闪屏图片","/","splash files(*.png)")
        if s.length() > 0:
            dialog.lineEdit_5.setText(unicode(s))
    
    def openChannelSetting_splashicon_icon(self,chanelData,dialog):
        s=QtGui.QFileDialog.getOpenFileName(None,u"选择ICON图片","/","icon files(*.png)")  
        if s.length() > 0:
            dialog.lineEdit_11.setText(unicode(s))
    
    def openChannelSetting_multidexPath(self,chanelData,dialog):
        s=QtGui.QFileDialog.getOpenFileName(None,u"选择Multidex文件","/","files(*.*)")  
        if s.length() > 0:
            dialog.lineEdit_14.setText(unicode(s))
    
    def saveChannelSetting_splash_icon(self,chanelData,dialog,chanel_item):
        channel = chanelData['channel_type']
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
        
        landscapeFlag = "True"
        if dialog.comboBox.currentText() != 'landscape':
            landscapeFlag = "False"
        
        #检查闪屏文件大小是否为1280*720或者是720*1280
        splash_dir = unicode(dialog.lineEdit_5.text()).strip()
        if len(splash_dir) > 0:
            if os.path.exists(file_operate.getFullPath(splash_dir)):
                splash = Image.open(file_operate.getFullPath(splash_dir))
                if landscapeFlag == "True":
                    if splash.size != (1280,720):
                        QtGui.QMessageBox.information(None,u"提示", u"横屏图片格式大小错误,格式要求为 宽:1280 高:720")
                        return
                else:
                    if splash.size != (720,1280):
                        QtGui.QMessageBox.information(None,u"提示", u"竖屏图片格式大小错误,格式要求为 宽:720 高:1280")
                        return
        
        icon_dir = unicode(dialog.lineEdit_11.text()).strip()
        if len(icon_dir) > 0:
            if os.path.exists(file_operate.getFullPath(icon_dir)):
                icon = Image.open(file_operate.getFullPath(icon_dir))
                if icon.size != (512,512):
                    QtGui.QMessageBox.information(None,u"提示", u"应用Icon图片格式大小错误,格式要求为 宽:512 高:512")
                    return
        
        checkBoxflag = "False"
        if dialog.checkBox_5.isChecked():
            checkBoxflag = "True"
        
        xmlpath = file_operate.getFullPath(logDir+productcode+'/ChannelSettingSplashAndIconFile.log')
        if not os.path.exists(xmlpath):
            xmldoc = xml.dom.minidom.getDOMImplementation()
            dom = xmldoc.createDocument(None, 'root', None)
            f = open(xmlpath, 'w')
            dom.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
            f.close()
        dom = xml.dom.minidom.parse(logDir+productcode+'/ChannelSettingSplashAndIconFile.log')
        root = dom.documentElement
        channelList = root.getElementsByTagName('channel_'+channel+'_'+chanelData['game']+'.'+chanelData['fgi'])
        if len(channelList) == 0:
            print 'createElement '
            channelNode = dom.createElement('channel_'+channel+'_'+chanelData['game']+'.'+chanelData['fgi'])
            root.appendChild(channelNode) 
        else:
            print 'modify '
            channelNode = channelList[0]
            
        channelNode.setAttribute('splash',unicode(dialog.lineEdit_5.text()).strip())
        channelNode.setAttribute('splash_time',unicode(dialog.lineEdit_12.text()).strip())
        channelNode.setAttribute('splash_fromAlpha',unicode(dialog.lineEdit_16.text()).strip())
        channelNode.setAttribute('landscapeFlag',landscapeFlag)
        channelNode.setAttribute('icon',unicode(dialog.lineEdit_11.text()).strip())
        channelNode.setAttribute('checkBoxflag',checkBoxflag)
        
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        f = open(xmlpath, 'w')
        dom.writexml(f, addindent=' ', newl='\n',encoding='utf-8')
        f.close()
        
        #为了美化xml数据格式
        f = open(xmlpath, "w")
        content = self.beautifulFormat(dom)
        f.write(content)
        f.close()
        
        #刷新Download目录下的渠道icon文件
        if checkBoxflag == "True":
            #icon
            if len(unicode(dialog.lineEdit_11.text()).strip()) > 0:
                self.saveChannelSetting_IconToDownloadDir(unicode(dialog.lineEdit_11.text()), channel+'/'+chanelData['game']+'.'+chanelData['fgi'],chanel_item)
            #splash
            if len(unicode(dialog.lineEdit_5.text()).strip()) > 0:
                self.saveChannelSetting_SplashToDownloadDir(unicode(dialog.lineEdit_5.text()), channel+'/'+chanelData['game']+'.'+chanelData['fgi'])
        else:
            print '#####################'
            
            
        QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
    
    def refreshChannelSplashAndIcon(self,channel,chanelData,chanel_item):
        print '刷新渠道Icon和闪屏数据...'
        #icon图片刷新，需要判断客户端，服务器，如果都没有，默认使用一张图片
        
        
        
        
    def saveChannelSetting_SplashToDownloadDir(self,splashpath,channel):
        DownloadDir = file_operate.getFullPath("Download/")
        img = Image.open(file_operate.getFullPath(splashpath))
        if not os.path.exists(file_operate.getFullPath(DownloadDir+'Splash/'+channel)):
            os.makedirs(file_operate.getFullPath(DownloadDir+'Splash/'+channel))
        splash = img.resize((495,280), Image.ANTIALIAS)
        splash.save(file_operate.getFullPath(DownloadDir+'Splash/'+channel+'/fun_plugin_splash.png'))
        
        
    def saveChannelSetting_IconToDownloadDir(self,iconpath,channel,chanel_item):
        DownloadDir = file_operate.getFullPath("Download/")
        img = Image.open(file_operate.getFullPath(iconpath))
        if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+channel +'/client')):
            os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/client'))
        img.save(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/client'+'/icon.png'))
        
        if os.path.exists(file_operate.getFullPath('Download/Icon/'+channel+'/client'+'/icon.png')):
            img = Image.open(file_operate.getFullPath('Download/Icon/'+channel+'/client'+'/icon.png'))
            icon = img.resize((60, 60), Image.ANTIALIAS)
            icon.save(file_operate.getFullPath('Download/Icon/'+channel+'/client'+'/channel.png'))
            chanel_item.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+channel+'/client'+'/channel.png')))
        
    
    def saveChannelSetting_other(self,chanelData,dialog):
        channel = chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi']
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
             
        xmlpath = file_operate.getFullPath(logDir+productcode+'/ChannelSettingOtherFile.log')
        if not os.path.exists(xmlpath):
            xmldoc = xml.dom.minidom.getDOMImplementation()
            dom = xmldoc.createDocument(None, 'root', None)
            f = open(xmlpath, 'w')
            dom.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
            f.close()
         
        dom = xml.dom.minidom.parse(logDir+productcode+'/ChannelSettingOtherFile.log')
        root = dom.documentElement
        channelList = root.getElementsByTagName('channel_'+channel)
        if len(channelList) == 0:
            print 'createElement '
            channelNode = dom.createElement('channel_'+channel)
            root.appendChild(channelNode) 
        else:
            print 'modify  '
            channelNode = channelList[0]
            
        checkBoxflag = "False"
        if dialog.checkBox_4.isChecked():
            checkBoxflag = "True"
        
        channelNode.setAttribute('source',unicode(dialog.lineEdit_4.text()))
        channelNode.setAttribute('target',unicode(dialog.lineEdit_10.text()))
        channelNode.setAttribute('checkBoxflag',checkBoxflag)
        
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        f = open(xmlpath, 'w')
        dom.writexml(f, addindent=' ', newl='\n',encoding='utf-8')
        f.close()
        
        #为了美化xml数据格式
        f = open(xmlpath, "w")
        content = self.beautifulFormat(dom)
        f.write(content)
        f.close()
        QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
        
    
    def beautifulFormat(self, xmlDomObject):
        if xmlDomObject:
            xmlStr = xmlDomObject.toprettyxml(indent = '', newl = '', encoding = 'utf-8')
            xmlStr = xmlStr.replace('\t', '').replace('\n', '')
            xmlDomObject = xml.dom.minidom.parseString(xmlStr)
            xmlStr = xmlDomObject.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8')
            return xmlStr
            
    
    def saveChannelSetting_apk(self,chanelData,dialog,chanel_item):
        channel = chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi']
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
             
        xmlpath = file_operate.getFullPath(logDir+productcode+'/ChannelSettingApkFile.log')
        if not os.path.exists(xmlpath):
            xmldoc = xml.dom.minidom.getDOMImplementation()
            dom = xmldoc.createDocument(None, 'root', None)
            f = open(xmlpath, 'w')
            dom.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
            f.close()
         
        dom = xml.dom.minidom.parse(logDir+productcode+'/ChannelSettingApkFile.log')
        root = dom.documentElement
        channelList = root.getElementsByTagName('channel_'+channel)
        if len(channelList) == 0:
            print 'createElement '
            channelNode = dom.createElement('channel_'+channel)
            root.appendChild(channelNode)
        else:
            print 'modify  '
            channelNode = channelList[0]
            
        checkBoxflag = "False"
        if dialog.checkBox_3.isChecked():
            checkBoxflag = "True"
        
        channelNode.setAttribute('appName',unicode(dialog.lineEdit_3.text()))
        channelNode.setAttribute('versionCode',unicode(dialog.lineEdit_6.text()))
        channelNode.setAttribute('versionName',unicode(dialog.lineEdit_7.text()))
        channelNode.setAttribute('minsdkVersion',unicode(dialog.lineEdit_8.text()))
        channelNode.setAttribute('targetsdkVersion',unicode(dialog.lineEdit_9.text()))
        channelNode.setAttribute('packageName',unicode(dialog.lineEdit_13.text()).replace(' ',''))
        channelNode.setAttribute('checkBoxflag',checkBoxflag)
        
        if checkBoxflag == "True" and len(unicode(dialog.lineEdit_13.text()).replace(' ','')) > 0:
            chanel_item.lineEdit.setText(unicode(dialog.lineEdit_13.text()).replace(' ',''))
        else:
            chanel_item.lineEdit.setText(chanelData['config']['otherKey']['packageName'])
        
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        f = open(xmlpath, 'w')
        dom.writexml(f, addindent=' ', newl='\n',encoding='utf-8')
        f.close()
        
        #为了美化xml数据格式
        f = open(xmlpath, "w")
        content = self.beautifulFormat(dom)
        f.write(content)
        f.close()
        QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
#         channel = chanelData['channel_type']
#         appName = dialog.lineEdit_3.text()
#         versionCode = dialog.lineEdit_6.text()+''
#         versionName = dialog.lineEdit_7.text()+''
#         minsdkVersion = dialog.lineEdit_8.text()+''
#         targetsdkVersion = dialog.lineEdit_9.text()+''
#         checkBoxflag = "False"
#         if dialog.checkBox_3.isChecked():
#             checkBoxflag = "True"
#          
#         logDir = 'Log/'
#         if not os.path.exists(logDir):
#             os.makedirs(logDir)
#         
#         
#         
#         info =channel+'|'+appName+'|'+versionCode+'|'+versionName+'|'+minsdkVersion+'|'+targetsdkVersion+'|'+checkBoxflag
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         
#         oldstr=''
#         newstr=''
#         flag = False
#         if os.path.exists(logDir + 'ChannelSettingApkFile.log'):
#             logFile = codecs.open(logDir + 'ChannelSettingApkFile.log', 'a+', 'utf-8')
#             for line in logFile.readlines():
#                 line = line.rstrip("\r\n")
#                 Info1 = line.split('|')
#                 Info2 = info.split('|')
#                 if Info1[0] == Info2[0]:
#                     flag = True
#                     oldstr = Info1[1] +'|'+ Info1[2]+'|'+Info1[3]+'|'+Info1[4]+'|'+Info1[5]+'|'+Info1[6]
#                     newstr = Info2[1] +'|'+ Info2[2]+'|'+Info2[3]+'|'+Info2[4]+'|'+Info2[5]+'|'+Info2[6]
#             logFile.close()
#             if flag:
#                 self.modifyFileContent(logDir + 'ChannelSettingApkFile.log', str(oldstr), str(newstr))
#                 QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
#                 return
#         
#         logFile = codecs.open(logDir + 'ChannelSettingApkFile.log', 'a+', 'utf-8')
#         content = info + '\n'
#         
#         logFile.write(unicode(content,'utf-8'))
#         logFile.close()
#         QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
#         
        
    def saveChannelSetting_multidex(self,chanelData,dialog):
#         channel = chanelData['channel_type']+'|'+chanelData['game']+'.'+chanelData['fgi']
#         dexNum = dialog.lineEdit_2.text()
#         checkBoxflag = "False"
#         if dialog.checkBox.isChecked():
#             checkBoxflag = "True"
#         useLocalFuncellApplicationJarFlag = dialog.comboBox_2.currentText()
#         info = channel+'|'+dexNum+'|'+checkBoxflag+'|'+useLocalFuncellApplicationJarFlag
#         logDir = 'Log/'
#         productcode = ConfigParse.shareInstance().getProductCode()
#         if not os.path.exists(logDir+productcode):
#             os.makedirs(logDir+productcode)
#         
#         oldstr=''
#         newstr=''
#         flag = False
#         if os.path.exists(logDir +productcode+ '/ChannelSettingMultidexFile.log'):
#             logFile = codecs.open(logDir +productcode+ '/ChannelSettingMultidexFile.log', 'a+', 'utf-8')
#             for line in logFile.readlines():
#                 line = line.rstrip("\r\n")
#                 Info1 = line.split('|')
#                 Info2 = info.split('|')
#                 if Info1[0] == Info2[0] and Info1[1] == Info2[1]:
#                     flag = True
#                     oldstr = line
#                     newstr = info
#             logFile.close()
#             if flag:
#                 self.modifyFileContent(logDir +productcode+ '/ChannelSettingMultidexFile.log', str(oldstr), str(newstr))
#                 QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
#                 return
#         
#         logFile = codecs.open(logDir +productcode+ '/ChannelSettingMultidexFile.log', 'a+', 'utf-8')
#         content = info + '\n'
#         logFile.write(unicode(content, 'gbk'))
#         logFile.close()
#         QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
        
        channel = chanelData['channel_type']
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
            
        checkBoxflag = "False"
        if dialog.checkBox.isChecked():
            checkBoxflag = "True"
        
        useFuncellApplicationJarFlag = "False"
        if dialog.comboBox_2.currentText() == 'True':
            useFuncellApplicationJarFlag = "True"
        
        xmlpath = file_operate.getFullPath(logDir+productcode+'/ChannelSettingMultidexFile.xml')
        if not os.path.exists(xmlpath):
            xmldoc = xml.dom.minidom.getDOMImplementation()
            dom = xmldoc.createDocument(None, 'root', None)
            f = open(xmlpath, 'w')
            dom.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
            f.close()
        dom = xml.dom.minidom.parse(logDir+productcode+'/ChannelSettingMultidexFile.xml')
        root = dom.documentElement
        channelList = root.getElementsByTagName('channel_'+channel+'_'+chanelData['game']+'.'+chanelData['fgi'])
        if len(channelList) == 0:
            print 'createElement '
            channelNode = dom.createElement('channel_'+channel+'_'+chanelData['game']+'.'+chanelData['fgi'])
            root.appendChild(channelNode) 
        else:
            print 'modify '
            channelNode = channelList[0]
            
        channelNode.setAttribute('dexNum',unicode(dialog.lineEdit_2.text()).strip())
        channelNode.setAttribute('multidexPath',unicode(dialog.lineEdit_14.text()).strip())
        channelNode.setAttribute('useFuncellApplicationJarFlag',useFuncellApplicationJarFlag)
        channelNode.setAttribute('checkBoxflag',checkBoxflag)
        
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        f = open(xmlpath, 'w')
        dom.writexml(f, addindent=' ', newl='\n',encoding='utf-8')
        f.close()
        
        #为了美化xml数据格式
        f = open(xmlpath, "w")
        content = self.beautifulFormat(dom)
        f.write(content)
        f.close()
        
        QtGui.QMessageBox.information(None,u"提示", u"保存成功！")
    
    def openChannelParameterUI(self,chanelData,chanel_item):
        dialog = ChannelParameterUI()
        dialog.setFixedSize(QSize(498, 370))
        
        #----------------遍历参数，将参数显示出来
        dialog.label.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">"+chanelData['channel_name']+"</span></p><p><span style=\" font-weight:600; color:#ffffff;\"><br/></span></p></body></html>")
        ConfigNodeList = chanelData['config']
        YPoint = 0
        for NodeKey in ConfigNodeList.keys():
            if isinstance(ConfigNodeList[NodeKey],list):
                pass
            else:
                for attributeKey in ConfigNodeList[NodeKey]:
                    if len(ConfigNodeList[NodeKey][attributeKey]) > 0:
                        lineEdit = QtGui.QLineEdit(dialog)
                        lineEdit.setGeometry(QtCore.QRect(40, 127+YPoint, 131, 20))
                        lineEdit.setText(attributeKey)
                        lineEdit.setStyleSheet("border:0px;background-color:transparent;")
                        lineEdit.setReadOnly(True)
                        label = QtGui.QLabel(dialog)
                        label.setGeometry(QtCore.QRect(210, 127+YPoint, 16, 16))
                        label.setText(':')
                        lineEdit2 = QtGui.QLineEdit(dialog)
                        lineEdit2.setGeometry(QtCore.QRect(250, 127+YPoint, 221, 20))
                        lineEdit2.setStyleSheet("border:0px;background-color:transparent;")
                        lineEdit2.setReadOnly(True)
                        lineEdit2.setText(ConfigNodeList[NodeKey][attributeKey])
                        YPoint += 25
        
        dialog.exec_()
    
    def openChannelVersionUI(self,versionList,chanel_item,chanelData):
#         print 'versionList:',versionList
        self.dialog = ChannelVersionListUI()
        for key in versionList:
            versionTime = key['date']
            sdkVersion = key['version']
#             dependency = key['dependency']
            desc = key.get('description')
            
            item1 = QtGui.QListWidgetItem()
            item1.setSizeHint(QSize(0, 42))
            
            item = ChannelVersionItem()
            item.label.setText(versionTime)
            item.label_2.setText(sdkVersion)
            
            if desc is not None:
                item.label_3.setText(desc)
            self.dialog.listWidget.addItem(item1)
            self.dialog.listWidget.setItemWidget(item1,item)
            
        
        self.dialog.pushButton_2.clicked.connect(partial(self.pushButton_2Click,self.dialog,chanel_item,chanelData))
        
        self.dialog.setFixedSize(QSize(498, 406))
        self.dialog.exec_()
    
    def initChannelVersion(self,channel_type,chanel_item,versionList):
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
        versionflag = False
        for line in logFile.readlines():
            line = line.rstrip("\r\n")
            Info1 = line.split('|')
            if Info1[0] == channel_type.split(':')[0] and Info1[1] == channel_type.split(':')[1]:
                for key in versionList:
                    if cmp(key['version'],Info1[2]) == 0:
                        versionflag = True
                if versionflag:
                    chanel_item.pushButton.setText(Info1[2])
                else:
                    chanel_item.pushButton.setText(u'无效版本,请重新选择可用版本')
                
                
        logFile.close()  
    
    def pushButton_2Click(self,dialog,chanel_item,chanelData):
        item = dialog.listWidget.currentItem()
        if item != None:
            versionCode = dialog.listWidget.itemWidget(item).label_2.text()
            chanel_item.pushButton.setText(versionCode)
            #保存当前的渠道的version
            channel_type = chanel_item.label_6.text()
            self.SaveChannelVersionConfig(channel_type+'|'+chanelData['game']+'.'+chanelData['fgi']+'|'+versionCode)
        dialog.close()
    
    def SaveChannelVersionConfig(self,info):
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
        
        oldstr=''
        newstr=''
        flag = False
        if os.path.exists(logDir +productcode+ '/ChannelVersionFile.log'):
            logFile = codecs.open(logDir +productcode +'/ChannelVersionFile.log', 'a+', 'utf-8')
            for line in logFile.readlines():
                line = line.rstrip("\r\n")
                Info1 = line.split('|')
                Info2 = info.split('|')
                if Info1[0] == Info2[0] and Info1[1] == Info2[1]:
                    flag = True
                    oldstr = line
                    newstr = info
                    
            logFile.close()
            if flag:
                self.modifyFileContent(logDir +productcode+ '/ChannelVersionFile.log', str(oldstr), str(newstr))
                return
        
        
        logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
        content = info + '\n'
        logFile.write(unicode(content, 'gbk'))
        logFile.close()
    
    def modifyFileContent(self,sourcefile, oldContent, newContent):
        if os.path.isdir(sourcefile):
            print("the source %s must be a file not a dir", sourcefile)
            return
    
        if not os.path.exists(sourcefile):
            print("the source is not exists.path:%s", sourcefile)
            return 
    
        f = open(sourcefile, 'r+')
        data = str(f.read())
        f.close()
        bRet = False
        idx = data.find(oldContent)
        while idx != -1:
            data = data[:idx] + newContent + data[idx + len(oldContent):]
            idx = data.find(oldContent, idx + len(oldContent))
            bRet = True
    
        if bRet:
            fw = open(sourcefile, 'w')
            fw.write(data)
            fw.close()
            print("modify file success.path:%s", sourcefile)
        else:
            print("there is no content matched in file:%s with content:%s", sourcefile, oldContent)
    
    
    def initUI(self):
#         self.__chanelList = {
#                       "uc":"UC",
#                       "360":"360",
#                       "duoku":u"百度",
#                       "oppo":"OPPO",
#                       "xiaomi":u"小米",
#                       "funcell":"Funcell",
#         }
        for value in self.__jsonChannelList.values():
            item = QtGui.QListWidgetItem(value)
            item.setSizeHint(QSize(0, 25))
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            tip = value
            remark = self.__jsonChannelRemarkList.get(value)
            if (remark is not None) and remark != '':
                tip = tip + ' ' + remark
            item.setToolTip(tip)
            self.listWidget.addItem(item)
        
        config = ET.parse(file_operate.getCommonXmlPath())
        root = config.getroot()
        apk = root.find("apk")
        self.lineEdit.setText(apk.get("path"))
        self.lineEdit_2.setText(apk.get("outDir"))
        
        logDir = 'Log/'
        productcode = ConfigParse.shareInstance().getProductCode()
        if not os.path.exists(logDir+productcode):
            os.makedirs(logDir+productcode)
        if os.path.exists(logDir +productcode+ '/SignFile.log'):
            logFile = codecs.open(logDir +productcode+ '/SignFile.log', 'a+', 'utf-8')
            for line in logFile.readlines():
                line = line.rstrip("\r\n")  #此处需要去掉隐藏的\r\n，才能匹配
                idx = line.find('|Default')
                if idx > 0:
                    Info = line.split('|')
#                     self.lineEdit_3.setText(utils.file_operate.getFullPath(str(Info[0])))
                    self.lineEdit_3.setText(utils.file_operate.getFullPath(unicode(Info[0])))
                    break
        try:
            configfile = file_operate.getCommonXmlPath()
            config = ET.parse(configfile)
            root = config.getroot()
            apk = root.find("apk")
            appVersion = apk.get("appVersion")
            self.lineEdit_4.setText(appVersion)
            self.lineEdit_5.setText(apk.get("resVersion"))
            
        except Exception,e:
            print e
            print "Error: cannot parse file: commonconfig.xml."
            return -1
        
    def saveParametersConfig(self):
        try:
            config = ET.parse(file_operate.getCommonXmlPath())
            root = config.getroot()
            apk = root.find("apk")
            apk.set("path", unicode(self.lineEdit.text()))
            apk.set("outDir", unicode(self.lineEdit_2.text()))
            config.write(file_operate.getCommonXmlPath(), "utf-8")
        except Exception,e:
            print e
            print "Error: cannot parse file: commonconfig.xml."
            return -1
        
    def initListWidget_2(self,channeName):
        myitem = MyItem()
        
        myitem.label_2.setText(channeName)
        self.__taskProgressBar[channeName] = myitem
        
#         channel=''
#         for key in self.__jsonChannelList.keys():
#             if channeName == self.__jsonChannelList[key]:
#                 channel ='/'+key
#         
#         if os.path.exists(file_operate.getFullPath('Download/Icon'+channel+'/channel.png')):
#             myitem.label.setPixmap(QPixmap(file_operate.getFullPath(file_operate.getFullPath('Download/Icon'+channel+'/channel.png'))))
        
        #判断使用icon路径  server/client/default
        productcode = ConfigParse.shareInstance().getProductCode()
        for key in self.__jsonChannelList.keys():
            if channeName == self.__jsonChannelList[key]:
                channelListData = taskManager.shareInstance().getChannelListData()
                chanelData = channelListData[key]
                logDir = 'Log/'
                useServerIconFlag = True
                if os.path.exists(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'):
                    config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
                    root = config.getroot()
                    channelNode = root.find('channel_'+chanelData['channel_type']+'_'+chanelData['game']+'.'+chanelData['fgi'])
                    if channelNode is not None:
                        if channelNode.get("checkBoxflag") == "True":
                            if len(channelNode.get("icon").strip()) > 0: 
                                if os.path.exists(file_operate.getFullPath(channelNode.get("icon"))):
                                    DownloadDir = file_operate.getFullPath("Download/")
                                    img = Image.open(file_operate.getFullPath(channelNode.get("icon")))
                                    if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client')):
                                        os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'))
                                    img.save(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png'))
                                    if os.path.exists(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png')):
#                                         img = Image.open(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/icon.png'))
                                        icon = img.resize((60, 60), Image.ANTIALIAS)
                                        icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/channel.png'))
                                        myitem.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/client'+'/channel.png')))
                                        print 'use client icon...'
                                        useServerIconFlag = False
                
                if useServerIconFlag:
                    if len(chanelData['icon']) > 0:
                        print 'use server icon...'
                        DownloadDir = file_operate.getFullPath("Download/")
                        if os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/server'+'/icon.png')):
                            img = Image.open(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/server'+'/icon.png'))
                            icon = img.resize((60, 60), Image.ANTIALIAS)
                            icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/server'+'/channel.png'))
                            myitem.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/server'+'/channel.png')))
                    else:
                        #使用默认图片
                        print '使用默认图片...默认不要使用本地图片，open会耗时'
#                         if os.path.exists(file_operate.getFullPath('config/icon/icon.png')):
#                             img = Image.open(file_operate.getFullPath('config/icon/icon.png'))
#                             DownloadDir = file_operate.getFullPath("Download/")
#                             if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default')):
#                                 os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'))
#                             img.save(file_operate.getFullPath(DownloadDir+'Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png'))
#                             if os.path.exists(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png')):
#                                 img = Image.open(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/icon.png'))
#                                 icon = img.resize((60, 60), Image.ANTIALIAS)
#                                 icon.save(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/channel.png'))
#                                 myitem.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+chanelData['channel_type']+'/'+chanelData['game']+'.'+chanelData['fgi']+'/default'+'/channel.png')))
        
        item1 = QtGui.QListWidgetItem()
        item1.setSizeHint(QSize(0, 72))
        self.listWidget_2.addItem(item1)
        self.listWidget_2.setItemWidget(item1,myitem)
        
    
    def on_toolButton_12_clicked(self):
        dialog = packLogClass()
        dialog.setFixedSize(QSize(666, 460))
        dialog.exec_()
    
    
    def initpackagePage(self):
        self.__TotalPackageNum = 0
        self.__SuccessPackageNum = 0
        self.__FailPackageNum = 0
        self.label_22.setText(str(self.__SuccessPackageNum))
        self.label_24.setText(str(self.__FailPackageNum))
#         self.__PackageCompleteMap.clear()
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                self.__TotalPackageNum += 1
        self.label_20.setText(str(self.__TotalPackageNum))
        
    
    def on_toolButton_9_clicked(self):
        flag = True
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                flag = False
                
        if flag:
            QtGui.QMessageBox.information(None,u"提示", u"未选择渠道！")
            return
        
        if not os.path.exists(unicode(self.lineEdit_2.text())):
            QtGui.QMessageBox.information(None,u"提示", u"未配置输出目录！")
            return

        if not os.path.exists(unicode(self.lineEdit.text())):
            QtGui.QMessageBox.information(None,u"提示", u"未配置母包apk！")
            return
        
        if not os.path.exists(unicode(self.lineEdit_3.text())):
            QtGui.QMessageBox.information(None,u"提示", u"未配置签名文件！")
            return
        
        self.toolButton_9.setEnabled(False)
        self.listWidget_2.clear()
        self.__taskProgressBar.clear()
        #------------此步骤为 展示 Item 条目
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                channelName = item.text()
                self.initListWidget_2(channelName)
                qApp.processEvents()
                
        
        self.initpackagePage()
        #------------------------------
        #---------执行打包,先删除1.apk文件---------
        self.saveParametersConfig()
#         self.delete1Apk()
        self.deleteErrorLogFile()
        self.package()
        #------------------
    def updateChannelList(self):
        dataArray = taskManager.shareInstance().getChannelList()
        iconUrl=''
        channelJson = dataArray['channel']
        pluginJson = dataArray['plugin']
#         print 'channelJson:',channelJson
#         print 'pluginJson:',pluginJson
        taskManager.shareInstance().setPluginlListData(pluginJson)
        
        ChannelIconUrlList = {}
        for key_data in channelJson:
#             print 'key_data',key_data
            for key in key_data:
                #-------------------------将json数据按渠道号 保存到dict中，用于后面判断和使用-----------
#                 print 'key',key
#                 taskManager.shareInstance().setChannelListData(key_data['channel_type'],key_data)
                taskManager.shareInstance().setChannelListData(key_data['channel_type']+'_'+key_data['game']+'.'+key_data['fgi'],key_data)
                iconUrl = key_data['icon']
#                 #------------------------------此步骤是将查询到的渠道信息加入集合中--------------------
#                 self.__jsonChannelList[key_data['channel_type']] = key_data['channel_name']+'_'+key_data['channel_type']
                self.__jsonChannelList[key_data['channel_type']+'_'+key_data['game']+'.'+key_data['fgi']] = key_data['channel_name']+'_'+key_data['fgi']
                desc = key_data.get('description')
                if desc is not None:
                    self.__jsonChannelRemarkList[key_data['channel_name']+'_'+key_data['fgi']] = desc

#                 icondata = {}
#                 icondata['icon'] = iconUrl
#                 ChannelIconUrlList[key_data['channel_type']] = icondata
#                 ChannelIconUrlList[key_data['channel_type']+'_'+key_data['game']+'.'+key_data['fgi']] = icondata
        
#         print 'ChannelIconUrlList:%s \n'%ChannelIconUrlList
#         utils.startIcon.start(ChannelIconUrlList)
        
#         thread.start_new_thread(self.getChannelIconTask, (channelJson,))
    
#     def getChannelIconTask(self,channelJson=None):
#         for key_data in channelJson:
#             iconUrl = key_data['icon']
#             channel = key_data['channel_type']
#             
#             #读取配置文件，是否需要下载Icon图片
#             logDir = 'Log/'
#             productcode = ConfigParse.shareInstance().getProductCode()
#             if os.path.exists(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'):
#                 config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
#                 root = config.getroot()
#                 channelNode = root.find('channel_'+channel)
#                 if channelNode is not None:
#                     if channelNode.get("checkBoxflag") == "True":
#                         if len(channelNode.get("icon").strip()) > 0: 
#                             if os.path.exists(file_operate.getFullPath(channelNode.get("icon"))):
#                                 DownloadDir = file_operate.getFullPath("Download/")
#                                 img = Image.open(file_operate.getFullPath(channelNode.get("icon")))
#                                 if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/client')):
#                                     os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/client'))
#                                 img.save(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/client'+'/icon.png'))
#                                 print '使用客户端配置Icon图片...'
#                         else:
#                             #删除渠道icon文件夹
#                             if os.path.exists(file_operate.getFullPath("Download/"+'Icon/'+channel+'/client')):
#                                 file_operate.delete_file_folder(file_operate.getFullPath("Download/"+'Icon/'+channel+'/client'))
#             
#             if len(iconUrl) > 0:
#                 print '使用服务器配置Icon图片...'
#                 httpManager.shareInstance().GetChannelIcon(iconUrl,channel)
#             else:
#                 print '使用默认图片...'
#                 if os.path.exists(file_operate.getFullPath('config/icon/icon.png')):
#                     img = Image.open(file_operate.getFullPath('config/icon/icon.png'))
#                     DownloadDir = file_operate.getFullPath("Download/")
#                     if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/default')):
#                         os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/default'))
#                     img.save(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/default'+'/icon.png'))
#                         
#                 
#         thread.exit_thread()
    
    def updateKeystore(self,info,flag):
        if flag:
            info = info.decode('gb2312').encode('utf-8')
            print 'flag true info:',info
            Info = info.split('|')
            self.lineEdit_3.setText(unicode(Info[0]))
        else:
            print 'flag false info:',info
            Info = info.split('|')
            self.lineEdit_3.setText(unicode(Info[0]))
    
    def UpdateFailedChannelState(self,channel,log):
        for key in self.__jsonChannelList.keys():
            if channel == key:
                for taskProgressBar_key in self.__taskProgressBar.keys():
                    if  taskProgressBar_key == self.__jsonChannelList[key]:
                        self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"打包失败,请查看日志信息...")
                 
    
    def UpdatetoolButton_9(self):
        print '__TotalPackageNum:%s'%str(self.__TotalPackageNum)
        print '__SuccessPackageNum:%s'%str(self.__SuccessPackageNum)
        self.__FailPackageNum = self.__TotalPackageNum - self.__SuccessPackageNum
        print '__FailPackageNum:%s'%str(self.__FailPackageNum)
        self.label_24.setText(str(self.__FailPackageNum))
        self.toolButton_9.setEnabled(True)
    
    def UpdateChanelListWidget_icon(self,__taskCompletionByIcon):
        for taskCompletion_key in __taskCompletionByIcon.keys():
            for taskIcon_key in self.__ChannelIconUrlList.keys():
                if taskIcon_key == taskCompletion_key:
                    channel_item = self.__ChannelIconUrlList[taskIcon_key]['obj']
                    extend = self.__ChannelIconUrlList[taskIcon_key]['extend']
                    channel = taskIcon_key.split('_')[0]+'/'+taskIcon_key.split('_')[1]
                    if os.path.exists(file_operate.getFullPath('Download/Icon/'+channel+'/server'+'/channel.png')):
                        #需要判断当前listWidget_3 中是否有当前item，若存在，进行icon设置
                        taskManager.shareInstance().getChannelItemListLock().acquire()
                        channelItemList = taskManager.shareInstance().getChannelItemList()
                        if channelItemList.has_key(extend):
                            channel_item.label.setPixmap(QPixmap(file_operate.getFullPath('Download/Icon/'+channel+'/server'+'/channel.png')))
                        taskManager.shareInstance().getChannelItemListLock().release()
    
    
    def UpdateChanelState(self,__taskCompletion,channel,extData = None):
#         print 'channel:%s'%channel
        if self.__jsonChannelList.has_key(channel):
            channelName = self.__jsonChannelList[channel]
#         print 'channelName:%s'%channelName
        for taskProgressBar_key in self.__taskProgressBar.keys():
            if channelName == unicode(taskProgressBar_key):
                channelName = taskProgressBar_key
        if 100 == __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"完成")
            utils.taskManagerModule.taskManager.shareInstance().getPackNumLock().acquire()
            self.__SuccessPackageNum += 1
            self.label_22.setText(str(self.__SuccessPackageNum))
            utils.taskManagerModule.taskManager.shareInstance().getPackNumLock().release()
        elif 2 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在下载渠道包...请稍后")
        elif 3 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在下载渠道闪屏资源...请稍后")
        elif 4 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在下载渠道Icon...请稍后")
        elif 4.5 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在处理插件信息")
        elif 5 ==  __taskCompletion[channel]:
            tmpstr = '正在下载%s插件包...请稍后'%(extData)
            self.__taskProgressBar[channelName].label_3.setText(unicode(tmpstr))
        elif 6 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理游戏initialize脚本")
        elif 8 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在删除临时目录")
        elif 10 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在拷贝母包Apk")
        elif 13 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在拷贝渠道SDK")
        elif 15 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"正在拷贝插件SDK")
        elif 20 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"反编译Apk")
        elif 30 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理渠道Dex")
        elif 40 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并渠道Res资源")
        elif 50 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并渠道Assets资源")
        elif 55 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理游戏extra资源")
        elif 58 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理游戏otherScript脚本")
        elif 59 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并渠道Libs")
        elif 60 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并渠道Manifest")
        elif 62 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并用户自定义配置文件")
        elif 65 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"修改包名")
        elif 70 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"闪屏处理中")
        elif 71 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"拷贝自定义资源")
        elif 72 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理插件Dex")
        elif 73 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并插件Res资源")
        elif 74 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并插件Assets资源")
        elif 75 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并插件Libs")
        elif 76 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"合并插件Manifest")
        elif 77 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理插件script")
        elif 78 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"生成插件资源ID索引")
        elif 79 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理coverCustomSdk")
        elif 80 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理gameSdkScript")
        elif 81 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理渠道script")
        elif 82 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理Icon")
        elif 83 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理ChannelSettingApkFile")
        elif 84 ==  __taskCompletion[channel]:
            if extData != None:
                tmpstr = '处理%s资源ID索引' % (extData)
                self.__taskProgressBar[channelName].label_3.setText(unicode(tmpstr))
            else:
                self.__taskProgressBar[channelName].label_3.setText(u"生成包名资源ID索引")
        elif 85 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"计算dex方法数")
        elif 86 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"修改压缩配置文件")
        elif 87 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"生成未签名Apk")
        elif 88 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"处理unknow文件")
        elif 89 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"Apk签名")
        elif 95 ==  __taskCompletion[channel]:
            self.__taskProgressBar[channelName].label_3.setText(u"zipalign Apk")
        else:
            self.__taskProgressBar[channelName].label_3.setText(u"打包中...")
            
        self.__taskProgressBar[channelName].progressBar.setValue(__taskCompletion[channel])
            
                    
#     def UpdateChanelState(self,__taskCompletion):
#         for taskCompletion_key in __taskCompletion.keys():
#             for taskProgressBar_key in self.__taskProgressBar.keys():
#                 if self.__jsonChannelList[taskCompletion_key] == unicode(taskProgressBar_key):
#                     if 100 == __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"完成")
#                         utils.taskManagerModule.taskManager.shareInstance().getPackNumLock().acquire()
#                         if not self.__PackageCompleteMap.has_key(taskProgressBar_key):
#                             print 'add taskProgressBar_key to __PackageCompleteMap'
#                             self.__PackageCompleteMap[taskProgressBar_key] = taskProgressBar_key
#                             self.__SuccessPackageNum += 1
#                             self.label_22.setText(str(self.__SuccessPackageNum))
#                         utils.taskManagerModule.taskManager.shareInstance().getPackNumLock().release()
#                     elif 2 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"正在下载渠道包...请稍后")
#                     elif 3 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"正在下载渠道闪屏资源...请稍后")
#                     elif 4 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"正在下载渠道Icon...请稍后")
#                     elif 5 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理游戏initialize脚本")
#                     elif 10 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"正在拷贝母包Apk")
#                     elif 13 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"正在拷贝渠道SDK")
#                     elif 15 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"正在拷贝插件SDK")
#                     elif 20 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"反编译Apk")
#                     elif 30 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理渠道Dex")
#                     elif 40 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并渠道Res资源")
#                     elif 50 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并渠道Assets资源")
#                     elif 55 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理游戏extra资源")
#                     elif 58 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理游戏otherScript脚本")
#                     elif 59 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并渠道Libs")
#                     elif 60 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并渠道Manifest")
#                     elif 65 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"修改包名")
#                     elif 70 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"闪屏处理中")
#                     elif 71 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"拷贝自定义资源")
#                     elif 72 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理插件Dex")
#                     elif 73 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并插件Res资源")
#                     elif 74 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并插件Assets资源")
#                     elif 75 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并插件Libs")
#                     elif 76 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"合并插件Manifest")
#                     elif 77 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理插件script")
#                     elif 78 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"生成插件资源ID索引")
#                     elif 79 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理gameSdkScript")
#                     elif 80 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理渠道script")
#                     elif 81 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理Icon")
#                     elif 82 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"处理ChannelSettingApkFile")
#                     elif 83 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"生成包名资源ID索引")
#                     elif 84 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"计算dex方法数")
#                     elif 85 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"修改压缩配置文件")
#                     elif 86 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"生成未签名Apk")
#                     elif 87 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"Apk签名")
#                     elif 95 ==  __taskCompletion[taskCompletion_key]:
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"zipalign Apk")
#                     else:  
#                         self.__taskProgressBar[taskProgressBar_key].label_3.setText(u"打包中...")
#                          
#                     self.__taskProgressBar[taskProgressBar_key].progressBar.setValue(__taskCompletion[taskCompletion_key])
    
    
    def deleteErrorLogFile(self):
        logDir = 'Log/'
        errorLogFile = file_operate.getFullPath(logDir+'error.log')
        file_operate.delete_file_folder(errorLogFile)
    
    def delete1Apk(self):
        apkFile = file_operate.getFullPath(constant.apktoolframeworkApkFile)
        file_operate.delete_file_folder(apkFile)
    
    def package(self):
        arrayList = []
        channelList = {}
        for key in self.__jsonChannelList.keys():
            for i in range(self.listWidget.count()):
                item = self.listWidget.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    channelName = item.text()
                    if channelName == self.__jsonChannelList[key]:
                        channelListData = taskManager.shareInstance().getChannelListData()
                        for channelKey in channelListData.keys():
                            if key == channelKey:
#                                 print 'channelKey:',channelKey
#                                 channelData[key] = channelListData[channelKey]
                                channelList[key] = channelListData[channelKey]
#                         arrayList.append(key)
        
#         utils.start.start(arrayList)
        utils.start.start(channelList)
        
        
import res
