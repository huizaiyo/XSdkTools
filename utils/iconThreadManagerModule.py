# -*- coding: utf-8 -*-
import threading
from iconThreadModule import PackThread
import file_operate
from time import sleep

class packThreadManager(object):
    """
    
    """
    __instance = None
    __Lock = threading.Lock()
    __taskThreads = []
    __finishChannel = []
    __curworkDir = ''

    def __init__(self):
        pass

    @staticmethod
    def shareInstance():
        packThreadManager.__Lock.acquire()
        if packThreadManager.__instance == None:
            packThreadManager.__instance = object.__new__(packThreadManager)
            object.__init__(packThreadManager.__instance)
        packThreadManager.__Lock.release()
        return packThreadManager.__instance

    def getIdleThread(self):
        for thread in self.__taskThreads:
            if thread.getStatus() == 0:
                return thread

        if len(self.__taskThreads) < 3:
            pkThread = PackThread(len(self.__taskThreads), self.__curworkDir)
            self.__taskThreads.append(pkThread)
            return pkThread

    def startTask(self, platform,arrayList):
        iconLs = arrayList
        for package in iconLs.keys():
            idChannel = package
            
            if idChannel in self.__finishChannel:
                continue
            pkThread = self.getIdleThread()
            if pkThread is None:
                return
            pkThread.setPlatform(platform)
            pkThread.assignPackTask(idChannel,iconLs[idChannel])
            if not pkThread.isAlive():
                pkThread.start()
            self.__finishChannel.append(idChannel)

        bOver = True
        for thread in self.__taskThreads:
            if thread.getStatus() != 0:
                bOver = False
                break

        if bOver == True:
            for thread in self.__taskThreads:
                thread.stop()
                self.__taskThreads.remove(thread)

    def getFinishChannelLs(self):
        return self.__finishChannel

    def isRunning(self):
        return len(self.__taskThreads)

    def setCurWorkDir(self, workDir):
        self.__curworkDir = workDir
        file_operate.curDir = workDir

    def stopAllTask(self):
        for thread in self.__taskThreads:
            thread.stop()
            self.__taskThreads.remove(thread)

    def clearRecord(self):
        self.__finishChannel = []
