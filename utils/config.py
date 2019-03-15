import threading
from xml.etree import ElementTree as ET
import re
import os
import file_operate
import sqlite3
import platform
import pdb
import codecs
import utils.http_manager
# from utils.http_manager import httpManager

class ConfigParse(object):
    """The class can parse project config file of xml """

    def __init__(self):
        """disable the __init__ method"""
        pass
    
    
    __configParse = None
    __lock = threading.Lock()
    __SDKLs = {}
    _channelName = ''
    _outputDir = ''
    _outApkDir = ''
    __dictTemp_new={}
    __dictTemp_old={}
       
    @staticmethod
    def shareInstance():
        ConfigParse.__lock.acquire()
        if not ConfigParse.__configParse:
            ConfigParse.__configParse = object.__new__(ConfigParse)
            object.__init__(ConfigParse.__configParse)
            #ConfigParse.__configParse.projectConfigRead()
        ConfigParse.__lock.release()
        return ConfigParse.__configParse
        
#     def projectConfigRead(self):
#         """Read funcellconfig.xml file and save to a dictionary"""
#         try:
#             configfile = file_operate.getCommonXmlPath()
#             
#             config = ET.parse(configfile)
#             root = config.getroot()
#             apk = root.find("apk")
#             self._apkPath = apk.get("path")
# #             keystore = root.find("keystore")
# #             self._keystoreFile = keystore.get("path")
# #             self._keystorepassword = keystore.get("password")
# #             self._alias = keystore.get("alias")
# #             self._aliasPassword = keystore.get("aliaspassword")
#             
#             logFile = codecs.open('Log/SignFile.log', 'a+', 'utf-8')
#             for line in logFile.readlines():
#                 line = line.rstrip("\r\n")
#                 idx = line.find('|Default')
#                 if idx > 0:
#                     Info = line.split('|')
#                     self._keystoreFile = Info[0]
#                     self._keystorepassword = Info[1]
#                     self._alias = Info[2]
#                     self._aliasPassword = Info[3]
#                     break
#             logFile.close()
#             
#             configfile = file_operate.getConfigXmlPath()
#             config = ET.parse(configfile)
#             root = config.getroot()
#             app = root.find("app")
#             self._packageName = app.get("packageName")
#             platform = root.find("platform")
#             self._appVersion = platform.get("appVersion")
#             self._gameId = platform.get("gameId")
#             self._platformId = platform.get("platformId")
#             self._platformType = platform.get("platformType")
#             channel = root.find("channel")
#             self._resVersion = channel.get("resVersion")
#         
#         except Exception,e:
#             print e
#             print "Error: cannot parse file: funcellconfig.xml."
#             return -1
    
    def ConfigRead(self,idchannel):
        """Read funcellconfig.xml file and save to a dictionary"""
        try:
            dictTemp = {}
            
            ConfigParse.__lock.acquire()
            configfile = file_operate.getCommonXmlPath()
            config = ET.parse(configfile)
            root = config.getroot()
            apk = root.find("apk")
            self._apkPath = apk.get("path")
            self._outApkDir = apk.get("outDir")
#             keystore = root.find("keystore")
#             self._keystoreFile = keystore.get("path")
#             self._keystorepassword = keystore.get("password")
#             self._alias = keystore.get("alias")
#             self._aliasPassword = keystore.get("aliaspassword")
            
            productcode = self.getProductCode()
            logFile = codecs.open('Log/'+productcode+'/SignFile.log', 'a+', 'utf-8')
            for line in logFile.readlines():
                line = line.rstrip("\r\n")
                idx = line.find('|Default')
                if idx > 0:
                    Info = line.split('|')
                    self._keystoreFile = Info[0]
                    self._keystorepassword = Info[1]
                    self._alias = Info[2]
                    self._aliasPassword = Info[3]
                    break
            logFile.close()
            
            ConfigParse.__lock.release()
            
            configfile = file_operate.getchannelFuncellConfigXmlPath(idchannel)
            config = ET.parse(configfile)
            root = config.getroot()
            
#             app = root.find("otherKey")
#             dictTemp['packageName'] = app.get("packageName")
#             platform = root.find("platform")
#             dictTemp['appVersion'] = platform.get("appVersion")
#             dictTemp['gameId'] = platform.get("gameId")
#             dictTemp['platformId'] = platform.get("platformId")
#             dictTemp['platformType'] = platform.get("platformType")
#             dictTemp['resVersion'] = platform.get("resVersion")
            
            otherKeyLsNode = root.findall("otherKey")
            if otherKeyLsNode is not None:
                for otherKeyNode in otherKeyLsNode:
                    packageNameLsNode = otherKeyNode.findall('packageName')
                    for packageNameNode in packageNameLsNode:
                        dictTemp['packageName'] = packageNameNode.text
            
            platformLsNode = root.findall("platform")
            if platformLsNode is not None:
                for platformNode in platformLsNode:
                    appVersionLsNode = platformNode.findall('appVersion')
                    for appVersionNode in appVersionLsNode:
                        dictTemp['appVersion'] = appVersionNode.text
                    gameIdLsNode = platformNode.findall('gameId')
                    for gameIdNode in gameIdLsNode:
                        dictTemp['gameId'] = gameIdNode.text
                    platformIdLsNode = platformNode.findall('platformId')
                    for platformIdNode in platformIdLsNode:
                        dictTemp['platformId'] = platformIdNode.text
                    platformTypeLsNode = platformNode.findall('platformType')
                    for platformTypeNode in platformTypeLsNode:
                        dictTemp['platformType'] = platformTypeNode.text
                    resVersionLsNode = platformNode.findall('resVersion')
                    for resVersionNode in resVersionLsNode:
                        dictTemp['resVersion'] = resVersionNode.text
            
            return dictTemp
        except Exception,e:
            print e
            print "Error: cannot parse file: funcellconfig.xml."
            return -1
    
    def getOutApkDir(self):
        return self._outApkDir
    
    def getOutputDir(self):
        return self._outputDir
    
    def getApkPath(self):
        return self._apkPath
    
    def setChannelName(self, channelName):
        self._channelName = channelName
    
    def getChannelName(self):
        return self._channelName
    
    def getKeystoreFile(self):
        return self._keystoreFile
    
    def getPackageName(self):
        return self._packageName
    
    def getKeystorePassword(self):
        return self._keystorepassword
    
    def getKeystoreAlias(self):
        return self._alias
    
    def getKeystoreAliasPassword(self):
        return self._aliasPassword
    
    def getAppVersion(self):
        return self._appVersion
    
    def getGameId(self):
        return self._gameId
    
    def getPlatformId(self):
        return self._platformId
    
    def getplatformType(self):
        return self._platformType
    
    def getResVersion(self):
        return self._resVersion
    
    def getnew_updateFile_config(self):
        return self.__dictTemp_new
    
    def getold_updateFile_config(self):
        return self.__dictTemp_old
    
    def getProductCode(self):
        productcode = ""
        GameFile = file_operate.getFullPath("Log/GameFile.log")
        if os.path.exists(GameFile):
            f = open(GameFile, 'a+')
            data = str(f.read())
            f.close()
            if len(data) > 0 and data.find('|') != -1:
                logFile = codecs.open(GameFile, 'a+', 'utf-8')
                for line in logFile.readlines():
                    line = line.rstrip("\r\n")
                    Info = line.split('|')
                    productcode = Info[0]
                    
        return productcode
    
    def initDatabase(self):
        """get the data from database."""
        dbPath = os.path.join(file_operate.getCurDir(), '/config/config.db')
        cx = sqlite3.connect(dbPath)
        cx.row_factory = sqlite3.Row
        self.readSDKLs(cx)
        cx.close()
    
    def readSDKLs(self, cx):
        """get the data about tpl_sdk from database"""
        self.__SDKLs.clear()
        c = cx.cursor()
        c.execute('select * from sdk')
        rows = c.fetchall()
        for r in rows:
            dictTemp = {}
            dictTemp['idSDK'] = r['idSDK']
            dictTemp['SDKName'] = r['SDKName']
            dictTemp['SDKShowName'] = r['SDKShowName']
            dictTemp['bHasIcon'] = r['bHasIcon']
            dictTemp['sdk_developer_url'] = r['sdk_developer_url']
            self.__SDKLs[dictTemp['idSDK']] = dictTemp

        c.close()
    
    def updateExeFlag(self):
        dictTemp = {}
        result = utils.http_manager.httpManager.shareInstance().downloadUpdateFile()
        if result == False:
            return False
        UpdateDir = file_operate.getFullPath("Update/")
        new_updateFile = file_operate.getFullPath(UpdateDir+'UpdateFile/update.xml')
        old_updateFile = file_operate.getFullPath('update.xml')
        
        config = ET.parse(new_updateFile)
        root = config.getroot()
        self.__dictTemp_new['version'] = root.find('version').text
        self.__dictTemp_new['force'] = root.find('force').text
        self.__dictTemp_new['url'] = root.find('url').text
        self.__dictTemp_new['md5'] = root.find('md5').text
        self.__dictTemp_new['date'] = root.find('date').text
        self.__dictTemp_new['descript'] = root.find('descript').text
        
        config = ET.parse(old_updateFile)
        root = config.getroot()
        self.__dictTemp_old['version'] = root.find('version').text
        self.__dictTemp_old['force'] = root.find('force').text
        self.__dictTemp_old['url'] = root.find('url').text
        self.__dictTemp_old['md5'] = root.find('md5').text
        self.__dictTemp_old['date'] = root.find('date').text
        self.__dictTemp_old['descript'] = root.find('descript').text
        
        
        if self.__dictTemp_new.get('version') == self.__dictTemp_old.get('version'):
            dictTemp['updateflag'] = False
        else:
            dictTemp['updateflag'] = True
        dictTemp['force'] = self.__dictTemp_new.get('force')
        
        return dictTemp
