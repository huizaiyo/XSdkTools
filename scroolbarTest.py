# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scroolbarTest.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
        QudaoWidget.resize(700, 500)
#         QudaoWidget.resize(523, 404)
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
        self.contentsWidget = QtGui.QListWidget(QudaoWidget)
        self.contentsWidget.setGeometry(QtCore.QRect(0, 44, 141, 357))
        self.contentsWidget.setObjectName(_fromUtf8("listWidget"))
        self.scrollArea = QtGui.QScrollArea(QudaoWidget)
#         self.scrollArea.setGeometry(QtCore.QRect(140, 44, 381, 357))
#         self.scrollArea.setWidgetResizable(True)
#         self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
#         self.scrollAreaWidgetContents = QtGui.QWidget()
#         self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 355))
#         self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
#         self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(QudaoWidget)
        QtCore.QMetaObject.connectSlotsByName(QudaoWidget)
        
        #--------------------------
        self.rectMove = QRect(0, 0, self.width(), 35)
        self.signFlag= False
        self.tab_1.setStyleSheet("background:#FFFFFF")
        self.tab_2.setStyleSheet("background:#FFFFFF")
        self.tab_3.setStyleSheet("background:#FFFFFF")
        
        QudaoWidget.setStyleSheet(
                                  "QCheckBox{font-family:arial;font-size:13px;border-radius:2px;color:#000000;}"
                                  "QCheckBox::indicator:checked{color:#FF0000}"
                                  "QTabWidget::pane{border:none;}"
                                  "QTabWidget::tab-bar{alignment:left;}"
                                  "QTabBar::tab{background:transparent;color:#000000;min-width:100px;min-height:35px;}"
                                  "QTabBar::tab:hover{background:rgb(255, 255, 255, 255);}"
                                  "QTabBar::tab:selected{border-color: white;color:green;padding-left:5px}"
                                  "QListWidget{background:rgba(240,240,240,255);color:#000000;border:0px solid gray;padding:0px;}"
                                  "QListWidget::item{width:94px;height:38px;border:0px solid gray;padding-left:24px;}"
                                  "QListWidget::item:selected:active{background:#FFFFFF;color:#19649F;border-width:-1;}"
                                  "QListWidget::item:selected{background:#FFFFFF;color:#19649F;}"
                                  "QLabel,QRadioButton{background:transparent;color:#000000;font-family:arial;font-size:13px;}"
                
                                  "QComboBox{border:1px solid #d7d7d7; border-radius: 3px; padding: 1px 3px 1px 3px;}"
                                  "QComboBox:editable{background:transparent;}"
                                  "QComboBox:!editable{background: #fbfbfb;color:#666666}"
                                  "QComboBox::down-arrow:on {top: 1px;left: 1px;}"
                                  "QComboBox QAbstractItemView::item{max-width:30px;min-height:20px;}"
                                  )
        self.tabWidget.setCurrentIndex(0)
        self.contentsWidget.setFocusPolicy(Qt.NoFocus)
        self.connect(self.contentsWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.slotItemClicked)
        self.scrollArea.setStyleSheet(
                                      "QScrollArea{background:transparent;}"
                                      "QScrollBar::vertical{background:#35A739;border:-5px solid grey;margin:-2px 0px 0px 0px;width:8px;}"
                                      "QScrollBar::horizontal{background:#35A739;border:0px solid #126691;height:10px;}"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background:#D3D3D3;}"
                                      )
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.connect(self.scrollArea.verticalScrollBar(),QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),self.slotValueChanged)
        self.connect(self.tabWidget,QtCore.SIGNAL(_fromUtf8("currentChanged(int)")),self.slotCurrentChanged)
        self.slotCurrentChanged(0)
        
    
    def initTabOneWidget(self):
        #loginWidget
        self.loginWidget =  QtGui.QWidget(self.widgetScrollArea)
        self.loginWidget.show()
        self.label = QtGui.QLabel(self.loginWidget)
        self.label.setText(u"登录：")
        self.label.setGeometry(30, 10, 50, 30)
        self.label.show();
        self.first = QtGui.QCheckBox(self.loginWidget)
        self.first.setFocusPolicy(Qt.NoFocus)
        self.first.setText(u"开机时自动启动QQ")
        self.first.setGeometry(100, 10, 300, 30)
        self.first.show()
        self.second = QtGui.QCheckBox(self.loginWidget)
        self.second.setFocusPolicy(Qt.NoFocus)
        self.second.setText("login when starting QQ")
        self.second.setGeometry(100, 40, 300, 30)
        self.second.show()
        self.third = QtGui.QCheckBox(self.loginWidget)
        self.third.setFocusPolicy(Qt.NoFocus)
        self.third.setChecked(True)
        self.third.setText("open the tips always")
        self.third.setGeometry(100, 70, 300, 30)
        self.third.show()
        self.forth = QtGui.QCheckBox(self.loginWidget)
        self.forth.setFocusPolicy(Qt.NoFocus)
        self.forth.setText("open the previous session when logining")
        self.forth.setGeometry(100, 100, 300, 30)
        self.forth.show()
        self.five = QtGui.QCheckBox(self.loginWidget)
        self.five.setFocusPolicy(Qt.NoFocus)
        self.five.setText("open the tips always")
        self.five.setGeometry(100, 130, 300, 30)
        self.five.show()
        self.sixth = QtGui.QCheckBox(self.loginWidget)
        self.sixth.setFocusPolicy(Qt.NoFocus)
        self.sixth.setChecked(True)
        self.sixth.setText("start phone qq when leaving")
        self.sixth.setGeometry(100, 160, 300, 30)
        self.sixth.show()
        self.seventh = QtGui.QCheckBox(self.loginWidget)
        self.seventh.setFocusPolicy(Qt.NoFocus)
        self.seventh.setChecked(True)
        self.seventh.setText("diskplay the waiting tips when logining")
        self.seventh.setGeometry(100, 190, 300, 30)
        self.seventh.show()
        self.loginWidget.setGeometry(0, 0, 555, 220)
        #panelWidget
        self.panelWidget = QtGui.QWidget(self.widgetScrollArea)
        self.panelWidget.show()
        self.plabel = QtGui.QLabel(self.panelWidget)
        self.plabel.setText("mainpanel:")
        self.plabel.setGeometry(30, 10, 50, 30)
        self.plabel.show()
        self.pfirst = QtGui.QCheckBox(self.panelWidget)
        self.pfirst.setChecked(True)
        self.pfirst.setFocusPolicy(Qt.NoFocus)
        self.pfirst.setText("stays on top always")
        self.pfirst.setGeometry(100, 10, 300, 30)
        self.pfirst.show()
        self.psecond = QtGui.QCheckBox(self.panelWidget)
        self.psecond.setChecked(True)
        self.psecond.setFocusPolicy(Qt.NoFocus)
        self.psecond.setText("hide when  skiming the edge of desktop")
        self.psecond.setGeometry(100, 40, 300, 30)
        self.psecond.show()
        self.pthird = QtGui.QCheckBox(self.panelWidget)
        self.pthird.setFocusPolicy(Qt.NoFocus)
        self.pthird.setChecked(True)
        self.pthird.setText("display the icon of qq at the taskbar")
        self.pthird.setGeometry(100, 70, 300, 30)
        self.pthird.show()
        self.pforth = QtGui.QLabel(self.panelWidget)
        self.pforth.setText("when closing the mainpanel:")
        self.pforth.setGeometry(100, 100, 300, 30)
        self.pforth.show()
        self.hideRadio = QtGui.QRadioButton(self.panelWidget)
        self.hideRadio.setFocusPolicy(Qt.NoFocus)
        self.hideRadio.setText("hide at the taskbar and do not exit")
        self.hideRadio.setGeometry(120, 130, 300, 30)
        self.hideRadio.show()
        self.exitRadio = QtGui.QRadioButton(self.panelWidget)
        self.exitRadio.setFocusPolicy(Qt.NoFocus)
        self.exitRadio.setChecked(True)
        self.exitRadio.setText("exit the program")
        self.exitRadio.setGeometry(120, 160, 300, 30)
        self.exitRadio.show()
        self.panelWidget.setGeometry(0, 220, 555, 190)
        #statusWidget
        self.statusWidget = QtGui.QWidget(self.widgetScrollArea)
        self.statusWidget.show()
        self.slabel = QtGui.QLabel(self.statusWidget)
        self.slabel.setText(("status:"))
        self.slabel.setGeometry(30, 10, 50, 30)
        self.slabel.show()
        self.slabelsecond = QtGui.QLabel(self.statusWidget)
        self.slabelsecond.setText(("the status of logining:"))
        self.slabelsecond.setGeometry(100, 10, 150, 30)
        self.slabelsecond.show()
        self.combox = QtGui.QComboBox(self.statusWidget)
        self.combox.setFocusPolicy(Qt.NoFocus)
        self.combox.addItems(QStringList() << ("hide") << ("oneline") << ("busy") << ("leave"))
        self.combox.setGeometry(200, 12, 80, 24)
        self.combox.show()
        self.ssecond = QtGui.QCheckBox(self.statusWidget)
        self.ssecond.setChecked(True)
        self.ssecond.setFocusPolicy(Qt.NoFocus)
        self.ssecond.setText(("switch to busy when running the program of fullscreen"))
        self.ssecond.setGeometry(100, 40, 300, 30)
        self.ssecond.show()
        self.sthird = QtGui.QCheckBox(self.statusWidget)
        self.sthird.setFocusPolicy(Qt.NoFocus)
        self.sthird.setChecked(True)
        self.sthird.setText(("auto replay when leaving or busy"))
        self.sthird.setGeometry(100, 70, 300, 30)
        self.sthird.show()
        self.sforth = QtGui.QCheckBox(self.statusWidget)
        self.sforth.setFocusPolicy(Qt.NoFocus)
        self.sforth.setText(("lock the qq when do not moving"))
        self.sforth.setGeometry(100, 100, 300, 30)
        self.sforth.show()
        self.statusWidget.setGeometry(0, 410, 555, 130)
        #sessionWidget
        self.sessionWidget = QtGui.QWidget(self.widgetScrollArea)
        self.sessionWidget.show()
        self.elabel = QtGui.QLabel(self.sessionWidget)
        self.elabel.setText(("session:"))
        self.elabel.setGeometry(30, 10, 50, 30)
        self.elabel.show()
        self.efirst = QtGui.QCheckBox(self.sessionWidget)
        self.efirst.setChecked(True)
        self.efirst.setFocusPolicy(Qt.NoFocus)
        self.efirst.setText(("use colourful bubble to chat"))
        self.efirst.setGeometry(100, 10, 300, 30)
        self.efirst.show()
        self.esecond = QtGui.QCheckBox(self.sessionWidget)
        self.esecond.setChecked(True)
        self.esecond.setFocusPolicy(Qt.NoFocus)
        self.esecond.setText(("do not dispaly ad"))
        self.esecond.setGeometry(100, 40, 300, 30)
        self.esecond.show()
        self.ethird = QtGui.QCheckBox(self.sessionWidget)
        self.ethird.setFocusPolicy(Qt.NoFocus)
        self.ethird.setText(("auto pop the panel when having massage"))
        self.ethird.setGeometry(100, 70, 300, 30)
        self.ethird.show()
        self.eforth = QtGui.QCheckBox(self.sessionWidget)
        self.eforth.setChecked(True)
        self.eforth.setFocusPolicy(Qt.NoFocus)
        self.eforth.setText(("use autorun magic and supper expression"))
        self.eforth.setGeometry(100, 100, 300, 30)
        self.eforth.show()
        self.efive = QtGui.QCheckBox(self.sessionWidget)
        self.efive.setChecked(True)
        self.efive.setFocusPolicy(Qt.NoFocus)
        self.efive.setText(("use moving feeling to char"))
        self.efive.setGeometry(100, 130, 300, 30)
        self.efive.show()
        self.esixth = QtGui.QCheckBox(self.sessionWidget)
        self.esixth.setFocusPolicy(Qt.NoFocus)
        self.esixth.setChecked(True)
        self.esixth.setText(("display the window of char at the sidebar"))
        self.esixth.setGeometry(100, 160, 300, 30)
        self.esixth.show()
        self.eseventh = QtGui.QCheckBox(self.sessionWidget)
        self.eseventh.setFocusPolicy(Qt.NoFocus)
        self.eseventh.setChecked(True)
        self.eseventh.setText(("allow the moving window"))
        self.eseventh.setGeometry(100, 190, 300, 30)
        self.eseventh.show()
        self.eeighth = QtGui.QCheckBox(self.sessionWidget)
        self.eeighth.setFocusPolicy(Qt.NoFocus)
        self.eeighth.setChecked(True)
        self.eeighth.setText(("dispaly search tips"))
        self.eeighth.setGeometry(100, 210, 300, 30)
        self.eeighth.show()
        self.enineth = QtGui.QCheckBox(self.sessionWidget)
        self.enineth.setFocusPolicy(Qt.NoFocus)
        self.enineth.setChecked(True)
        self.enineth.setText(("dispaly the history information"))
        self.enineth.setGeometry(100, 240, 300, 30)
        self.enineth.show()
        self.etenth = QtGui.QCheckBox(self.sessionWidget)
        self.etenth.setFocusPolicy(Qt.NoFocus)
        self.etenth.setChecked(True)
        self.etenth.setText(("combine the session window"))
        self.etenth.setGeometry(100, 270, 300, 30)
        self.etenth.show()
        self.sessionWidget.setGeometry(0, 540, 555, 300 + 127)
        
        self.widgetScrollArea.resize(555, 840+127)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
#         painter.setBrush(QColor("#F0F0F0"))
#         painter.drawRect(self.rect())
        painter.setBrush(QColor("#069dd5"))
        painter.drawRect(self.rectMove)
        painter.setPen(QColor("#D7D7D7"))
        painter.drawLine(0, 70, self.width(), 70)
        self.paintEvent(event)
        
    
    def resizeEvent(self,event):
        self.tabWidget.setGeometry(0, 36, self.width(), self.height()-36)
        self.contentsWidget.setGeometry(0, 71, 130, self.height() - 71)
        self.scrollArea.setGeometry(131, 72, self.width() - 132, self.height() - 73)
#         self.tabWidget.setGeometry(0, 10, 521, 35)
#         self.contentsWidget.setGeometry(0, 44, 141, 357)
#         self.scrollArea.setGeometry(140, 44, 381, 357)
        
        self.resizeEvent(event)
    
    def slotCurrentChanged(self,index):
        self.contentsWidget.clear()
        self.scrollArea.takeWidget()
        self.loginWidget = None
        self.panelWidget = None
        self.statusWidget = None
        self.sessionWidget = None
        
        self.widgetScrollArea = QtGui.QWidget(self)
        self.widgetScrollArea.setStyleSheet("background:transparent")
        self.scrollArea.setWidget(self.widgetScrollArea)
        if index == 0:
            self.contentsWidget.addItem(u"登录")
            self.contentsWidget.addItem(u"主面板")
            self.contentsWidget.addItem(u"状态")
            self.contentsWidget.addItem(u"会话窗口")
            self.initTabOneWidget()
        elif index == 1:
            self.contentsWidget.addItem(u"密码")
            self.contentsWidget.addItem(u"QQ锁")
        elif index == 2:
            self.contentsWidget.addItem(u"空间权限")
        
        if self.contentsWidget.count() > 0:
            self.contentsWidget.setCurrentRow(0)
    
    def slotValueChanged(self,value):
        if self.tabWidget.currentIndex() == 0:
            loginItem = self.contentsWidget.item(0)
            panelItem = self.contentsWidget.item(1)
            statusItem = self.contentsWidget.item(2)
            sessionItem = self.contentsWidget.item(3)
            if not self.signFlag:
                if self.loginWidget != None and self.panelWidget != None and self.statusWidget!=None and self.sessionWidget!=None:
                    if not self.loginWidget.visibleRegion().isEmpty():
                        loginItem.setSelected(True)
                        return
                    else:
                        loginItem.setSelected(False)
                    if not self.panelWidget.visibleRegion().isEmpty():
                        panelItem.setSelected(True)
                        return
                    else:
                        panelItem.setSelected(False)
                    if not self.statusWidget.visibleRegion().isEmpty():
                        statusItem.setSelected(True)
                        return
                    else:
                        statusItem.setSelected(False)
                    if not self.sessionWidget.visibleRegion().isEmpty():
                        sessionItem.setSelected(True)
                        return
                    else:
                        sessionItem.setSelected(False)
        elif  self.tabWidget.currentIndex() == 1:
            pass
        self.signFlag= False
        
        
    def slotItemClicked(self,item):
        self.signFlag = True
        itemText = item.text()
        widgetPos=''
        if self.tabWidget.currentIndex() == 0:
            if itemText == u"主面板":
                widgetPos = self.panelWidget.pos()
                self.scrollArea.verticalScrollBar().setSliderPosition(widgetPos.y())
            elif itemText == u"状态":
                widgetPos = self.statusWidget.pos()
                self.scrollArea.verticalScrollBar().setValue(widgetPos.y())
            elif itemText == u"会话窗口":
                widgetPos = self.sessionWidget.pos()
                self.scrollArea.verticalScrollBar().setValue(widgetPos.y())
            elif itemText == u"登录":
                widgetPos = self.loginWidget.pos()
                self.scrollArea.verticalScrollBar().setValue(widgetPos.y())
                
        elif self.tabWidget.currentIndex() == 1:
            pass
        
        
    def retranslateUi(self, QudaoWidget):
        QudaoWidget.setWindowTitle(_translate("QudaoWidget", "Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("QudaoWidget", "基本设置", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("QudaoWidget", "安全设置", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("QudaoWidget", "权限设置", None))

import res

class scroolbarTest(QDialog,Ui_QudaoWidget):
    def __init__(self,parent=None):
        super(scroolbarTest,self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)

    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = scroolbarTest()
    myapp.show()
    sys.exit(app.exec_())
