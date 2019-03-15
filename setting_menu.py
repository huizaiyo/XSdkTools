#!/usr/bin/python  
#-*-coding:utf-8-*-



from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

class SettingMenu(QMenu):
	def __init__(self,parent = None):
		super(SettingMenu,self).__init__()
# 		self.setStyleSheet("background-image:url(\":/images/setting_bg.jpg\");")
		self.setStyleSheet("QMenu{background: rgb(255, 255, 255)}" 
#                             "QMenu::item{color:gray}" 
                            "QMenu::item:selected:enabled{background-color:gray;}"  
                
						)
		self.createActions()
		self.translateActions()

	def createActions(self):

		#创建菜单项
		self.action_refresh_data =  QAction(self)
		self.action_switch_account =  QAction(self)
		self.action_setcustom_config =  QAction(self)

		self.action_refresh_data.setIcon(QIcon(":/images/RefreshData.png"))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.action_refresh_data.setFont(font)
		
		self.action_switch_account.setIcon(QIcon(":/images/RefreshData.png"))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.action_switch_account.setFont(font)
		
		self.action_setcustom_config.setIcon(QIcon(":/images/RefreshData.png"))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.action_setcustom_config.setFont(font)
		
		#添加菜单项
		self.addAction(self.action_refresh_data)
		self.addSeparator()
		self.addAction(self.action_switch_account)
		self.addSeparator()
		self.addAction(self.action_setcustom_config)
		
		
# 		self.addSeparator()

		#设置信号连接
		self.connect(self.action_refresh_data, SIGNAL("triggered()"), SIGNAL("refreshData()"))
		self.connect(self.action_switch_account, SIGNAL("triggered()"), SIGNAL("switchAccount()"))
		self.connect(self.action_setcustom_config, SIGNAL("triggered()"), SIGNAL("setCustomConfig()"))

	def translateActions(self):
		self.action_refresh_data.setText(u" 数据刷新")
		self.action_switch_account.setText(u" 切换帐号")
		self.action_setcustom_config.setText(u" 自定义配置")

