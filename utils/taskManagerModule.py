# -*- coding: utf-8 -*-
import threading
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class taskManager(QObject):
    __instance = None
    __Lock = threading.Lock()
    __TaskLock = threading.Lock()
    __packNumTaskLock = threading.Lock()
    __ChannelItemListLock = threading.Lock()
    __taskCompletion = {}
    __taskLog = []
    __ChannelList = []
    __ChannelImageList = {}
    __ChannelListData = {}
    __ChannelItemList = {}
    __PluginlListData = {} #公共的插件部分
    __ChannelPluginListData = {} #渠道目录下使用的插件部分
    __taskCompletionByIcon = {}
    __loadingUI = None
    def __init__(self):
        pass

    @staticmethod
    def shareInstance():
        taskManager.__Lock.acquire()
        if taskManager.__instance == None:
            taskManager.__instance = QObject.__new__(taskManager)
            QObject.__init__(taskManager.__instance)
        taskManager.__Lock.release()
        return taskManager.__instance

    def notify(self, platformname, percent,extData = None):
        self.__taskCompletion[platformname] = percent
        self.emit(SIGNAL("UpdateChanelState"), self.__taskCompletion,platformname,extData)
        

    def log(self, platformname, log):
        self.__taskLog[platformname].append(log)

    def getCompletionDict(self):
        return self.__taskCompletion

    def getLog(self, platformname):
        return self.__taskLog[platformname]

    def clearRecord(self):
        self.__taskCompletion.clear()

    def missionComplete(self):
        keys = self.__taskCompletion.keys()
        for key in keys:
            self.__taskCompletion[key] = -1
        self.emit(SIGNAL("UpdatetoolButton_9"))
    
    def getChannelList(self):
        return self.__ChannelList
    
    def getLock(self):
        return self.__TaskLock
    
    def getChannelItemListLock(self):
        return self.__ChannelItemListLock
    
    def getPackNumLock(self):
        return self.__packNumTaskLock
    
    def addKeyStore(self,keystoreInfo):
        self.emit(SIGNAL("addKeyStoreFile"),keystoreInfo)
        
    def updateLog(self,channel,log):
        self.emit(SIGNAL("updateTextLog"),channel,log)
        
    def updateKeystore(self,info,flag):
        self.emit(SIGNAL("updateKeystore"),info,flag)
        
    def updateChanelList(self,list):
        self.__ChannelList = list
        
    def addImage2List(self,channelName,image):
        self.__ChannelImageList[channelName] = image
    
    def getChannelListData(self):
        return self.__ChannelListData
    
    def setChannelListData(self,channel_type,data):
        self.__ChannelListData[channel_type] = data
    
    def getChannelItemList(self):
        return self.__ChannelItemList
    
    def setChannelItemList(self,channel_name,data):
        self.__ChannelItemList[channel_name] = data
    
    def clearRecordChannelItemList(self):
        self.__ChannelItemList.clear()
        
    def updateChannelVersionLabel(self,versionCode):
        self.emit(SIGNAL("updateChannelVersionLabel"),versionCode)
        
    def updateThreadFinish(self):
        self.emit(SIGNAL("updateThreadFinish"))
        
    def setPluginlListData(self,data):
        self.__PluginlListData = data
        
    def getPluginlListData(self):
        return self.__PluginlListData
    
    def setChannelPluginListData(self,data):
        self.__ChannelPluginListData = data
    
    def getChannelPluginListData(self):
        return self.__ChannelPluginListData
    
    def updateDownloadProgress(self,progressNum):
        self.emit(SIGNAL("updateDownloadProgress"),progressNum)
    
    def clearRecordByIcon(self):
        self.__taskCompletionByIcon.clear()
    
    def notifyByIcon(self, platformname, percent):
        self.__taskCompletionByIcon[platformname] = percent
        self.emit(SIGNAL("UpdateChanelListWidget_icon"), self.__taskCompletionByIcon)
    
    def refreshPackUi(self):
        self.emit(SIGNAL("refreshPackUi"))
    
    def callbackListWidget(self,item):
        self.emit(SIGNAL("callbackListWidget"),item)
    def startIconTask(self):
        self.emit(SIGNAL("startIconTask"))
    
    def setLoadingUI(self,loading):
        self.__loadingUI = loading
    def getLoadingUI(self):
        return self.__loadingUI
        