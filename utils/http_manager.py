# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import urllib2
import json
import threading
from StringIO import StringIO
from PIL import Image
import urllib
# from utils import constant, file_operate
import constant
import file_operate
import os
import utils.taskManagerModule
from xml.etree import ElementTree as ET

class httpManager(QObject):
    __instance = None
    __Lock = threading.Lock()
    __ChannelDownLoadNum = {}
    
    
    def __init__(self):
        pass
    
    @staticmethod
    def shareInstance():
        httpManager.__Lock.acquire()
        if httpManager.__instance == None:
            httpManager.__instance = QObject.__new__(httpManager)
            QObject.__init__(httpManager.__instance)
        httpManager.__Lock.release()
        return httpManager.__instance
    
    def http_get(self,url):
        response = urllib2.urlopen(url,timeout = 60)
        return response.read()
    
    def http_post(self,url,parameters):
        req = urllib2.Request(url, parameters)
        response = urllib2.urlopen(req,timeout = 60)
        return response.read()
    
    def http_postByJson(self,url,parameters):
        jdata = json.dumps(parameters)
        req = urllib2.Request(url, jdata)
        response = urllib2.urlopen(req,timeout = 60)
        return response.read()
    
    def GetChannelIcon(self,url,channel):
#         img_buff = urllib.urlopen(url).read()
#         urllib.urlretrieve(img_buff[0],file_operate.getFullPath(constant.sdkRelatePath+'/icon/icon.png'))
        channel = channel.split('_')[0] +'/' + channel.split('_')[1]
#         print 'channel:%s \r' %channel
        DownloadDir = file_operate.getFullPath("Download/")
        response = urllib2.urlopen(url,timeout = 60)
        img_buff = StringIO(response.read())
        img = Image.open(img_buff)
        
#         utils.taskManagerModule.taskManager.shareInstance().getIconLock().acquire()
        if not os.path.exists(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/server')):
            os.makedirs(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/server'))
        img.save(file_operate.getFullPath(DownloadDir+'Icon/'+channel+'/server'+'/icon.png'))
        if os.path.exists(file_operate.getFullPath('Download/Icon/'+channel+'/server'+'/icon.png')):
            img = Image.open(file_operate.getFullPath('Download/Icon/'+channel+'/server'+'/icon.png'))
            icon = img.resize((60, 60), Image.ANTIALIAS)
            icon.save(file_operate.getFullPath('Download/Icon/'+channel+'/server'+'/channel.png'))
#         utils.taskManagerModule.taskManager.shareInstance().getIconLock().release()
    
#     def downloadZip(self,url):
#         DownloadDir = file_operate.getFullPath("Download/")
#         print 'DownloadDir:',DownloadDir
# #         f = urllib2.urlopen(url)
# #         data = f.read()
#         
#         opener = urllib2.build_opener()
#         req = opener.open(url)
#         meta = req.info()
#         file_size = int(meta.getheaders("Content-Length")[0])
#         content_type = meta.getheaders('Content-Type')[0].split(';')[0]
#         print file_size, content_type
#         
#         if not os.path.exists(DownloadDir):
#             os.makedirs(DownloadDir)
#             
#         zipName = os.path.basename(file_operate.getFullPath(url))
#         print 'zipName:',zipName
#         with open(DownloadDir+zipName, "wb") as code:
# #             code.write(data)
#             code.write(req.read())
    
    
     
    def downloadZip(self,channel,url,md5value):
        DownloadDir = file_operate.getFullPath("Download/")
        print 'DownloadDir:',DownloadDir
        if not os.path.exists(DownloadDir):
            os.makedirs(DownloadDir)
        
        #此步骤为判断当前请求链接是否有效
        try:
            res = urllib2.urlopen(urllib2.Request(url),timeout = 60)  
            code = res.getcode()  
            res.close()
            print 'code:',code
            if code != 200:
                str_error = 'download url:%s download failed.Please check the current network. Network status code:%s'%(url,str(code))
                file_operate.reportError("", "", str_error)
                return False
        except Exception,e:
            print 'e:',e
            str_error = "download url:%s download failed.Please check the current network Exception:%s"%(url,str(e.message))
            file_operate.reportError("", "", str_error)
            return False
        
        try:
            zipName = os.path.basename(file_operate.getFullPath(url))
            urllib.urlretrieve(url,DownloadDir+zipName)
            zipmd5value = file_operate.md5sum(DownloadDir+zipName)
            if zipmd5value != md5value:
                for key in self.__ChannelDownLoadNum:
                    if key == channel and self.__ChannelDownLoadNum[channel] == 3:
                        print 'url:%s download fail'%(url)
                        str_error = 'download url:%s download failed.Download File MD5 value check does not pass'%(url)
                        file_operate.reportError("", "", str_error)
                        self.__ChannelDownLoadNum[channel] = 0
                        return False
                
                if channel not in self.__ChannelDownLoadNum:
                    self.__ChannelDownLoadNum[channel] = 0
                self.__ChannelDownLoadNum[channel] += 1
                self.downloadZip(channel,url,md5value)
            else:
                self.__ChannelDownLoadNum[channel] = 0
                return True
        except Exception,e:
            print 'e:',e
            str_error ="download url:%s download failed.Please check the current network Exception:%s"%(url,str(e.message))
            file_operate.reportError("", "", str_error)
            return False
        
#         zipName = os.path.basename(file_operate.getFullPath(url))
#         urllib.urlretrieve(url,DownloadDir+zipName)
#         zipmd5value = file_operate.md5sum(DownloadDir+zipName)
#         if zipmd5value != md5value:
#             for key in self.__ChannelDownLoadNum:
#                 if key == channel and self.__ChannelDownLoadNum[channel] == 3:
#                     print 'url:%s 下载失败'%(url)
#                     self.__ChannelDownLoadNum[channel] = 0
#                     file_operate.reportError("", "", 'url:%s 下载失败,请检查当前网络...'%(url))
#                     return False
#             
#             if channel not in self.__ChannelDownLoadNum:
#                 self.__ChannelDownLoadNum[channel] = 0
#             self.__ChannelDownLoadNum[channel] += 1
#             self.downloadZip(channel,url,md5value)
#         else:
#             self.__ChannelDownLoadNum[channel] = 0
#             return True
        
            
    def GetSplashImage(self,url,channel):
        DownloadDir = file_operate.getFullPath("Download/")
        response = urllib2.urlopen(url,timeout = 60)
        img_buff = StringIO(response.read())
        img = Image.open(img_buff)
        if not os.path.exists(DownloadDir+'Splash/'+channel):
            os.makedirs(DownloadDir+'Splash/'+channel)
        icon = img.resize((495,280), Image.ANTIALIAS)
        icon.save(file_operate.getFullPath(DownloadDir+'Splash/'+channel+'/fun_plugin_splash.png'))
#         img.save(file_operate.getFullPath(DownloadDir+'Splash/fun_plugin_splash.png'))
    
    def DownloadChannelIcon2ChannelDir(self,url,channel):
        try:
            req = urllib2.Request(url)
            response=urllib2.urlopen(req,timeout = 60)
            code=response.getcode()
            if code != 200:
                str_error = 'download url:%s download failed.Please check the current network. Network status code:%s'%(url,str(code))
                file_operate.reportError("", "", str_error)
                return False
            
        except urllib2.URLError,e:
            print e.reason
            
            
#         response = urllib2.urlopen(url)
        img_buff = StringIO(response.read())
        img = Image.open(img_buff)
        if not os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon')):
            os.makedirs(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon'))
        img.save(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon/icon.png'))
    
    
    def DownloadChannelSplash2ChannelDir(self,url,horizontal,channel_type):
        channelDir = file_operate.getFullPath(constant.sdkRelatePath+channel_type)
        ForSplashDir = channelDir+'/ForSplash'
        if horizontal:
            dir = ForSplashDir+'/landscape'
            drawableSize = (480, 320)
            hdpiSize = (800, 480)
            ldpiSize = (320, 240)
            mdpiSize = (480, 320)
            xhdpiSize = (1280,720)
        else:
            dir = ForSplashDir+'/portrait'
            drawableSize = (320, 480)
            hdpiSize = (480, 800)
            ldpiSize = (240, 320)
            mdpiSize = (320, 480)
            xhdpiSize = (720,1280)
            
        drawable = dir+'/drawable'
        drawablehdpi = dir+'/drawable-hdpi'
        drawableldpi= dir+'/drawable-ldpi'
        drawablemdpi= dir+'/drawable-mdpi'
        drawablexhdpi= dir+'/drawable-xhdpi'
        
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
        
        
        
        response = urllib2.urlopen(url,timeout = 60)
        img_buff = StringIO(response.read())
        img = Image.open(img_buff)
        
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
        
    
    def getUpdateAddress(self):
        address =''
        try:
            config = ET.parse(file_operate.getCommonXmlPath())
            root = config.getroot()
            host = root.find("update")
            address = host.get("address")
        except Exception,e:
            print e
            print "Error: cannot parse file: commonconfig.xml."
            return -1
        return address 
    
    def downloadUpdateFile(self):
#         url = "http://sdk.funcell123.com/upload/tool/update.xml"
#         url = "http://553.cdn.553.com/federation/tool/update.xml"
#         url = "http://553-cdn.haowan123.com/federation/tool/update.xml"
        url = self.getUpdateAddress()
        UpdateDir = file_operate.getFullPath("Update/")
        if not os.path.exists(UpdateDir+'UpdateFile'):
            os.makedirs(UpdateDir+'UpdateFile')
            
        try:
            res = urllib2.urlopen(urllib2.Request(url),timeout = 60)
            code = res.getcode()
            res.close()
            print 'downloadUpdateFile code:',code
            if code != 200:
                file_operate.reportError("", "", 'url:%s 下载失败,请检查当前网络... Exception:%s'%(url))
                return False
        except Exception,e:
            print 'e:',e
            file_operate.reportError("", "", 'url:%s 下载失败,请检查当前网络... Exception:%s'%(url,e))
            return False
        
        try:
            f = urllib2.urlopen(url,timeout = 60)
            data = f.read() 
            with open(UpdateDir+'UpdateFile/'+'update.xml', "wb") as code:
                code.write(data)
        except Exception,e:
            file_operate.reportError("", "", 'url:%s 下载失败,请检查当前网络... Exception:%s'%(url,e))
            return False
    
    
    def Schedule(self,a,b,c):
        #a:已经下载的数据块
        #b:数据块的大小
        #c:远程文件的大小
        
        per =100.0*a *b /c
        if per > 100:
            per =100
#         print'%.2f%%'%per
        utils.taskManagerModule.taskManager.shareInstance().updateDownloadProgress('%.2f%%'%per)
    
    def downloadExe(self,url,md5):
        UpdateDir = file_operate.getFullPath("Update/")
        if not os.path.exists(UpdateDir):
            os.makedirs(UpdateDir)
            
#         f = urllib2.urlopen(url) 
#         data = f.read()
#         with open(UpdateDir+'FuncellSDKTool.exe', "wb") as code:
#             code.write(data)
        
        #此步骤为判断当前请求链接是否有效
        try:
            res = urllib2.urlopen(urllib2.Request(url),timeout = 60)
            code = res.getcode()
            res.close()
            print 'code:',code
            if code != 200:
                file_operate.reportError("", "", 'url:%s 下载失败,请检查当前网络... Exception:%s'%(url))
                return False
        except Exception,e:
            print 'e:',e
            file_operate.reportError("", "", 'url:%s 下载失败,请检查当前网络... Exception:%s'%(url,e))
            return False
        
        urllib.urlretrieve(url,UpdateDir+'FuncellSDKTool.exe',self.Schedule)
        #进行md5检验
        newExeMd5value = file_operate.md5sum(UpdateDir+'FuncellSDKTool.exe')
        if md5 != newExeMd5value:
            print 'md5 value not equal'
            self.downloadExe(url, md5)
        else:
            return True
        
        
    