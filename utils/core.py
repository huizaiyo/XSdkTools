# -*- coding: utf-8 -*-
import file_operate
import operate
import error_operate
from config import ConfigParse
from taskManagerModule import taskManager
import thread
import threading
import platform
from time import sleep
import os
import time
import constant
from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import SubElement
import modifyManifest
import sys
import re
from http_manager import httpManager
from xml_manager import XmlManager
import codecs
from importlib import import_module
import copy
import zipfile
import shutil
# import chardet
# from ResourceMerger import *

global splitDexFlag
splitDexFlag = False

def main(channel,channelJsonData):
    threading.currentThread().setName(channel)
    channel_old = channel
    taskManager.shareInstance().notify(channel_old, 1)
    print 'channel:',channel
    print 'channelJsonData:',channelJsonData
    
    tmpstr = channel
    flagNum = len(tmpstr.split('_'))
    game_fig = tmpstr.split('_')[flagNum - 1]
    tmpChannellen = len(tmpstr) - len(game_fig) - 1
    tmpChannel = tmpstr[0:tmpChannellen]
    channel = tmpChannel + '/' + game_fig
    
#     channel = channel.split('_')[0] +'/'+ channel.split('_')[1]
        
    print 'channel:',channel
    #-----------------------------如果当前渠道不存在，则下载--------------------------------------------
    channelDir = file_operate.getFullPath(constant.sdkRelatePath+channel)
    version = '0'
    if not os.path.exists(channelDir):
        #当不存在渠道sdk文件夹时候，先找到最大版本号的url，然后还需要考虑，当前用户本地没有渠道sdk文件夹，但是用户进行了版本选择，版本选择的也不是最大的版本号，这个时候需要以用户选择的版本号为准，不能使用最大的版本号对应的url地址
        #以下方式为遍历最大版本并进行下载
        versionList = channelJsonData['version']
        for key in versionList:
            if cmp(key['version'],version) == 1:
                version = key['version']
                url = key['url']
                md5 = key['md5']
        #判断是否用户进行了版本选择，如果版本配置文件中，当前渠道的版本号在json数据里面匹配到存在当前用户选择的版本号，那么将使用用户选择的为准
        local_version = '0'
        logDir = 'Log/'
#         versionCode = 0
        productcode = ConfigParse.shareInstance().getProductCode()
        if os.path.exists(logDir +productcode+ '/ChannelVersionFile.log'):
            logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'r', 'utf-8')
            for line in logFile.readlines():
                line = line.rstrip("\r\n")
                Info1 = line.split('|')
                if Info1[0] == channel.split('/')[0] and Info1[1] == channel.split('/')[1]:
                    #找到用户本地的版本
                    local_version = Info1[2]
        #判断用户本地版本是否有效，即是否在json数据中有当前本地版本
        for key in versionList:
            if cmp(local_version,key['version']) == 0:
                url = key['url']
                md5 = key['md5']
                version = local_version
        
        print '-----url:',url
        taskManager.shareInstance().notify(channel_old, 2)
        downloadFlag = httpManager.shareInstance().downloadZip(channel,url,md5)
        if downloadFlag == False:
            print 'download zip fail,url:%s'%(url)
            return
        zipName = os.path.basename(file_operate.getFullPath(url))
        DownloadDir = file_operate.getFullPath("Download/")
        file_operate.decompression(DownloadDir+zipName,channelDir,file_operate.getFullPath(constant.sdkRelatePath + channel))
        
        #---------------判断是否有渠道闪屏文件，
#         splashFlag = False
#         horizontal = False
#         splashUrl = str(channelJsonData['screen'])
#         if len(splashUrl) > 0:
#             splashFlag =True
#             if len(str(channelJsonData['horizontal'])) > 0:
#                 if True == channelJsonData['horizontal']:
#                     horizontal = True
#                 taskManager.shareInstance().notify(channel, 3)
#                 httpManager.shareInstance().DownloadChannelSplash2ChannelDir(splashUrl,horizontal,channel)
#         
#         
#         #--------------下载icon图片
#         iconUrl = str(channelJsonData['icon'])
#         if len(iconUrl) > 0:
#             taskManager.shareInstance().notify(channel, 4)
#             httpManager.shareInstance().DownloadChannelIcon2ChannelDir(iconUrl,channel)
        
    #---------------------此步骤是为了创建渠道xml文件，用于java中读取-------------------------------------
#         platformList = {}
#         platform = {}
#         
#         configfile = file_operate.getCommonXmlPath()
#         config = ET.parse(configfile)
#         root = config.getroot()
#         apk = root.find("apk")
#         appVersion = apk.get("appVersion")
#         
#         platform['appVersion'] = appVersion
#         platform['datacenter'] = 'szdc'
#         platform['gameId'] = channelJsonData['game']
#         platform['platformId'] = channelJsonData['fgi']
#         platform['platformType'] = channel
#         platform['eve'] = channelJsonData['eve']+'/config/'
#         platform['resVersion'] = '1.0.0'
#         platform['ChannelVersionCode'] = str(version)
#         platformList['platform'] = platform
#         
#         splashList={}
#         splash = {}
#         if splashFlag:
#             if horizontal:
#                 splash['hasSplash'] = 'landscape'
#             else:
#                 splash['hasSplash'] = 'portrait'
#             splashList['splash'] = splash
#         else:
#             splash['hasSplash'] = '0'
#             splashList['splash'] = splash
#         
#         channelXmlPath = file_operate.getFullPath(constant.sdkRelatePath+channel)
#         
#         # 深拷贝：拷贝后，对象的引用发生了变化，即对象不同，所以，即使对象再怎么变，也不会对其他对象产生影响
#         #copy.deepcopy(d)
#         #浅拷贝：拷贝后，对象的引用没有发生变化，而对象的行为发生变化，会反映到拷贝后的对象身上
#         #copy.copy(s)
#         channelJson = copy.deepcopy(channelJsonData['config'])
#         #=============
#         if channelJson.has_key('pluginLs'):
#             channelJson.pop('pluginLs')
#         #=============
#         channelJson['platform'] = platform
#         channelJson['splash'] = splash
#         
#         XmlManager.shareInstance().createFuncellconfigXml(channelXmlPath,channelJson)
        
        info = str(channel.split('/')[0])+'|'+str(channel.split('/')[1])+'|'+ str(version)
        SaveChannelVersionConfig(info)
    #---------如果存在当前渠道，则需要判断当前渠道的版本是否和配置文件ChannelVersionFile.log中相同，不相同，不相同则需要使用ChannelVersionFile.log中的配置版本信息-------
    else:
        ChannelVersionCode='0'
        if os.path.exists(constant.sdkRelatePath + channel + "/funcellconfig.xml"):
            configfile = file_operate.getchannelFuncellConfigXmlPath(channel)
            config = ET.parse(configfile)
            root = config.getroot()
            #platform = root.find("platform")
            #ChannelVersionCode = platform.get("ChannelVersionCode")
            
            platformLsNode = root.findall("platform")
            if platformLsNode is not None:
                for platformNode in platformLsNode:
                    ChannelVersionCodeLsNode = platformNode.findall('ChannelVersionCode')
                    for ChannelVersionCodeNode in ChannelVersionCodeLsNode:
                        ChannelVersionCode = ChannelVersionCodeNode.text
                        print '-----%s use version %s'%(channel,ChannelVersionCode)
        
        versionFlag = False #是否使用最新版本的version，如果为False，则代表ChannelVersionFile中没有当前渠道的配置，需要使用最大的版本号
        logDir = 'Log/'
#         versionCode = 0
        productcode = ConfigParse.shareInstance().getProductCode()
        if os.path.exists(logDir +productcode+ '/ChannelVersionFile.log'):
            logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
            for line in logFile.readlines():
                line = line.rstrip("\r\n")
                Info1 = line.split('|')
                if Info1[0] == channel.split('/')[0] and Info1[1] == channel.split('/')[1]:
    #                 versionCode = Info1[1]
                    version = Info1[2]
                    versionFlag = True
                    print '-----channel config:channel:%s  version:%s'%(channel,version)
            logFile.close()  
        
        if versionFlag == False:
            print '-----query max version-----'
            versionList = channelJsonData['version']
            for key in versionList:
                if cmp(key['version'],version) == 1:
                    version = key['version']
            
        
#         if float(versionCode) != float(ChannelVersionCode):
        if cmp(version,ChannelVersionCode) != 0:
#         if float(version) != float(ChannelVersionCode):
            versionList = channelJsonData['version']
            for key in versionList:
#                 if float(versionCode) == float(key['version']):
                if cmp(version,key['version']) == 0:
#                 if float(version) == float(key['version']):
                    url = key['url']
                    md5 = key['md5']
                    taskManager.shareInstance().notify(channel_old, 2)
                    downloadFlag = httpManager.shareInstance().downloadZip(channel,url,md5)
                    if downloadFlag == False:
                        print 'download fail,url:%s'%(url)
                        return
                    zipName = os.path.basename(file_operate.getFullPath(url))
                    DownloadDir = file_operate.getFullPath("Download/")
                    file_operate.decompression(DownloadDir+zipName,channelDir,file_operate.getFullPath(constant.sdkRelatePath + channel))
                    
                    #---------------判断是否有渠道闪屏文件，
#                     splashFlag = False
#                     horizontal = False
#                     splashUrl = str(channelJsonData['screen'])
#                     if len(splashUrl) > 0:
#                         splashFlag =True
#                         if len(str(channelJsonData['horizontal'])) > 0:
#                             if True == channelJsonData['horizontal']:
#                                 horizontal = True
#                             taskManager.shareInstance().notify(channel, 3)
#                             httpManager.shareInstance().DownloadChannelSplash2ChannelDir(splashUrl,horizontal,channel)
#                     
#                     #--------------下载icon图片
#                     iconUrl = str(channelJsonData['icon'])
#                     if len(iconUrl) > 0:
#                         taskManager.shareInstance().notify(channel, 4)
#                         httpManager.shareInstance().DownloadChannelIcon2ChannelDir(iconUrl,channel)
                    
#                     platformList = {}
#                     platform = {}
#                     configfile = file_operate.getCommonXmlPath()
#                     config = ET.parse(configfile)
#                     root = config.getroot()
#                     apk = root.find("apk")
#                     appVersion = apk.get("appVersion")
#                     
#                     platform['appVersion'] = appVersion
#                     platform['datacenter'] = 'szdc'
#                     platform['gameId'] = channelJsonData['game']
#                     platform['platformId'] = channelJsonData['fgi']
#                     platform['platformType'] = channel
#                     platform['eve'] = channelJsonData['eve']+'/config/'
#                     platform['resVersion'] = '1.0.0'
#                     platform['ChannelVersionCode'] = key['version']
#                     platformList['platform'] = platform
#                     
#                     splashList={}
#                     splash = {}
#                     if splashFlag:
#                         if horizontal:
#                             splash['hasSplash'] = 'landscape'
#                         else:
#                             splash['hasSplash'] = 'portrait'
#                         splashList['splash'] = splash
#                     else:
#                         splash['hasSplash'] = '0'
#                         splashList['splash'] = splash
#                     
#                     channelXmlPath = file_operate.getFullPath(constant.sdkRelatePath+channel)
#                     channelJson = copy.deepcopy(channelJsonData['config'])
#                     #=============
#                     if channelJson.has_key('pluginLs'):
#                         channelJson.pop('pluginLs')
#                     #=============
#                     channelJson['platform'] = platform
#                     channelJson['splash'] = splash
#                     
#                     XmlManager.shareInstance().createFuncellconfigXml(channelXmlPath,channelJson)
                    
        info = str(channel.split('/')[0])+'|'+str(channel.split('/')[1])+'|'+ str(version)
        SaveChannelVersionConfig(info)
        
    #-------------------------------创建渠道funcellconfig.xml文件-----------------------------------------------
    splashFlag = False
    horizontal = False
    useSplashFileFlag = False
    logDir = 'Log/'
    productcode = ConfigParse.shareInstance().getProductCode()
    if os.path.exists(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'):
        config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
        root = config.getroot()
        channelNode = root.find('channel_'+channel.split('/')[0]+'_'+channel.split('/')[1])
        if channelNode is not None:
            if channelNode.get("checkBoxflag") == "True":
                if len(channelNode.get("splash").strip()) > 0:
                    if os.path.exists(file_operate.getFullPath(channelNode.get("splash"))):
                        useSplashFileFlag = True
                        splashFlag = True
                        if channelNode.get("landscapeFlag") == "True":
                            horizontal = True
                        print 'use client splash...'
                        operate.saveChannelSetting_splashToChannelDir(channelNode.get("splash"),horizontal,channel)
                else:
                    #删除splash闪屏文件夹
                    if os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+channel+'/ForSplash')):
                        file_operate.delete_file_folder(constant.sdkRelatePath+channel+'/ForSplash')
    #---------------判断是否有渠道闪屏文件，
#     splashFlag = False
#     horizontal = False
    if useSplashFileFlag == False:
        splashUrl = str(channelJsonData['screen']).strip()
        if len(splashUrl) > 0:
            splashFlag =True
            if len(str(channelJsonData['horizontal']).strip()) > 0:
                if True == channelJsonData['horizontal']:
                    horizontal = True
                taskManager.shareInstance().notify(channel_old, 3)
                print 'download server splash...'
                httpManager.shareInstance().DownloadChannelSplash2ChannelDir(splashUrl,horizontal,channel)
        else:
            #删除splash闪屏文件夹
            if os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+channel+'/ForSplash')):
                file_operate.delete_file_folder(constant.sdkRelatePath+channel+'/ForSplash')
    
    useIconFileFlag = False
    if os.path.exists(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'):
        config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
        root = config.getroot()
        channelNode = root.find('channel_'+channel.split('/')[0]+'_'+channel.split('/')[1])
        if channelNode is not None:
            if channelNode.get("checkBoxflag") == "True":
                if len(channelNode.get("icon").strip()) > 0:
                    if os.path.exists(file_operate.getFullPath(channelNode.get("icon"))):
                        useIconFileFlag = True
                        print 'use client icon...'
                        operate.saveChannelSetting_iconToChannelDir(channelNode.get("icon"),channel)
                else:
                    #删除icon文件夹
                    if os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon')):
                        file_operate.delete_file_folder(constant.sdkRelatePath+channel+'/icon')
        
    #--------------下载icon图片
    if useIconFileFlag == False:
        iconUrl = str(channelJsonData['icon']).strip()
        print 'iconUrl:',iconUrl
        if len(iconUrl) > 0:
            taskManager.shareInstance().notify(channel_old, 4)
            print 'download server icon...'
            httpManager.shareInstance().DownloadChannelIcon2ChannelDir(iconUrl,channel)
        else:
            #删除icon文件夹
            if os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon')):
                file_operate.delete_file_folder(constant.sdkRelatePath+channel+'/icon')
    #-------------------------------------
    
    platformList = {}
    platform = {}
    
    configfile = file_operate.getCommonXmlPath()
    config = ET.parse(configfile)
    root = config.getroot()
    apk = root.find("apk")
    appVersion = apk.get("appVersion")
    resVersion = apk.get("resVersion")
    
    platform['appVersion'] = appVersion
    platform['datacenter'] = 'szdc'
    platform['gameId'] = channelJsonData['game']
    platform['platformId'] = channelJsonData['fgi']
    platform['platformType'] = channel.split('/')[0]
#     platform['eve'] = channelJsonData['eve']+'/config/'
    platform['eve'] = channelJsonData['initdata']['eve']
    platform['area'] = channelJsonData['initdata']['area']
    platform['report'] = channelJsonData['initdata']['report']
    platform['resVersion'] = resVersion
    platform['ChannelVersionCode'] = str(version)
    platformList['platform'] = platform
    
    splashList={}
    splash = {}
    if splashFlag:
        if horizontal:
            splash['hasSplash'] = 'landscape'
        else:
            splash['hasSplash'] = 'portrait'
        splashList['splash'] = splash
    else:
        splash['hasSplash'] = '0'
        splashList['splash'] = splash
    
    channelXmlPath = file_operate.getFullPath(constant.sdkRelatePath+channel)
    
    # 深拷贝：拷贝后，对象的引用发生了变化，即对象不同，所以，即使对象再怎么变，也不会对其他对象产生影响
    #copy.deepcopy(d)
    #浅拷贝：拷贝后，对象的引用没有发生变化，而对象的行为发生变化，会反映到拷贝后的对象身上
    #copy.copy(s)
    channelJson = copy.deepcopy(channelJsonData['config'])
    #=============
    if channelJson.has_key('pluginLs'):
        channelJson.pop('pluginLs')
    #=============
    channelJson['platform'] = platform
    channelJson['splash'] = splash
    
    XmlManager.shareInstance().createFuncellconfigXml(channelXmlPath,channelJson)
    
    
    #------------------判断三方插件SDK，若json数据中有插件使用，则需要判断当前插件是否已经存在本地-------------------------------------
    #查找插件列表哪些插件需要使用
    taskManager.shareInstance().notify(channel_old, 4.5)
    if channelJsonData['config'].has_key('pluginLs') and channelJsonData['config']['pluginLs']: #有键值并且数据不为空
        pluginLsJson = channelJsonData['config']['pluginLs']
        pluginPublicLsJson = taskManager.shareInstance().getPluginlListData()
        channelPluginJson = channelJsonData['config']['pluginLs']
        for key_data in  pluginLsJson:
#             for key in key_data:
#                 if 'status' == key and 'enable' == key_data[key]:
            print '---------plugin find----------'
            print '---------key_data:----------',key_data
            print '\r'
            pluginTypePlugin = key_data['typePlugin']
            pluginChannel = key_data['channel']
            
            if not os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/'+pluginTypePlugin)):
                os.makedirs(file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/'+pluginTypePlugin))
            
            #若插件不存在，则下载最新版本插件SDK，
            pluginDir = file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/'+pluginTypePlugin+'/'+pluginChannel)
            if not os.path.exists(pluginDir):
                print '---------pluginDir not exists----------',pluginDir
                print '\r'
                pluginversion = '0'
                for key_pluginData in pluginPublicLsJson:
                    _pluginType = key_pluginData['type']
                    _pluginChannel = key_pluginData['channel']
                    if pluginTypePlugin == _pluginType and pluginChannel == _pluginChannel:
                        #当不存在插件sdk文件夹，先找到最大版本号的url，然后还需要考虑，当前用户本地没有插件sdk文件夹，但是用户进行了版本选择，版本选择的也不是最大的版本号，这个时候需要以用户选择的版本号为准，不能使用最大的版本号对应的url地址
                        #以下方式为遍历最大版本并进行下载
                        pluginVersionListData = key_pluginData['version']
                        for key_pluginVersion in pluginVersionListData:
                            if cmp(key_pluginVersion['version'],pluginversion) == 1:
                                pluginversion = key_pluginVersion['version']
                                pluginurl = str(key_pluginVersion['url'])
                                pluginmd5 = str(key_pluginVersion['md5'])
                        #判断是否用户进行了版本选择，如果版本配置文件中，当前插件的版本号在json数据里面匹配到存在当前用户选择的版本号，那么将使用用户选择的为准
                        local_pluginversion = '0'
                        logDir = 'Log/'
                        productcode = ConfigParse.shareInstance().getProductCode()
                        if os.path.exists(logDir +productcode+ '/ChannelPluginListVersionFile.log'):
                            logFile = codecs.open(logDir +productcode+ '/ChannelPluginListVersionFile.log', 'r', 'utf-8')
                            for line in logFile.readlines():
                                line = line.rstrip("\r\n")
                                Info1 = line.split('|')
                                if Info1[0] == pluginTypePlugin and Info1[1] == channel.split('/')[0] and Info1[2] == channel.split('/')[1] and Info1[3] == pluginChannel:
                                    local_pluginversion = Info1[4]
                            logFile.close()
                        #判断用户本地版本是否有效，即是否在json数据中有当前本地版本
                        for key_pluginVersion in pluginVersionListData:
                            if cmp(key_pluginVersion['version'],local_pluginversion) == 0:
                                pluginversion = key_pluginVersion['version']
                                pluginurl = str(key_pluginVersion['url'])
                                pluginmd5 = str(key_pluginVersion['md5'])
                        
                print 'pluginTypePlugin:%s | pluginChannel:%s | pluginversion:%s | channel:%s | pluginurl:%s | pluginmd5:%s'%(pluginTypePlugin,pluginChannel,str(pluginversion),str(channel),pluginurl,pluginmd5)
                
                taskManager.shareInstance().notify(channel_old, 5,pluginTypePlugin+'_'+pluginChannel)
                downloadFlag = httpManager.shareInstance().downloadZip(channel,pluginurl,pluginmd5)
                if downloadFlag == False:
                    print 'download plugin zip fail,url:%s'%(pluginurl)
                    return
                pluginzipName = os.path.basename(file_operate.getFullPath(pluginurl))
                DownloadDir = file_operate.getFullPath("Download/")
                file_operate.decompression(DownloadDir+pluginzipName,pluginDir,file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/'+pluginTypePlugin+'/'+pluginChannel))
                
                for key_channelpluginJson in  channelPluginJson:
                    if pluginTypePlugin == key_channelpluginJson['typePlugin'] and pluginChannel == key_channelpluginJson['channel']:
                        key_channelpluginJson['version'] = str(pluginversion)
                
                SavaChannePluginlVersionConfig(pluginTypePlugin,channel,pluginChannel,str(pluginversion))
                
            else:   
                #若存在当前渠道,则需要判读当前版本是否和ChannelPluginListVersionFile.log中配置的相同
                print '---------pluginDir exists----------',pluginDir
                print '\r'
                channelPluginJson = judgeChannelPluginVersion(channel,pluginTypePlugin,pluginChannel,channelPluginJson)
                if channelPluginJson == '':
                    print 'download plugin zip fail'
                    return
        
        
        XmlManager.shareInstance().createFuncellPluginXml(file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)),channelPluginJson)
    #-----------------------------------------------------------------
    #---------判断当前cp配置的appversion是否和渠道目录下funcellconfig配置中的appversion一致，如果不一致，则需要使用cp配置的appversion--------------
#     try:
#         configfile = file_operate.getCommonXmlPath()
#         config = ET.parse(configfile)
#         root = config.getroot()
#         apk = root.find("apk")
#         appVersion_CommonXml = apk.get("appVersion")
#         
#         configfile = file_operate.getchannelFuncellConfigXmlPath(channel)
#         config = ET.parse(configfile)
#         root = config.getroot()
#         platformLsNode = root.findall("platform")
#         if platformLsNode is not None:
#             for platformNode in platformLsNode:
#                 appVersionLsNode = platformNode.findall('appVersion')
#                 for appVersionNode in appVersionLsNode:
#                     appVersion_FuncellConfig = appVersionNode.text
#                     print 'appVersion_FuncellConfig:',appVersion_FuncellConfig
#                     if appVersion_CommonXml != appVersion_FuncellConfig:
#                         appVersionNode.text = appVersion_CommonXml
#                         print 'appVersionNode.text:',appVersionNode.text
#                         config.write(file_operate.getchannelFuncellConfigXmlPath(channel), "utf-8")
#             
#     except Exception,e:
#         print e
#         print "Error: modify FuncellConfig by appVersion"
#         return -1
    #------------------------------------------------------------------------------
        
#     writeConfigToSdkConfigFile(channel,dict)
#     taskManager.shareInstance().notify(channel_old, 5)
    dictTemp = ConfigParse.shareInstance().ConfigRead(channel)
    platformId = dictTemp.get('platformId')
    appVersion = dictTemp.get('appVersion')
    resVersion = dictTemp.get('resVersion')
    platformType = dictTemp.get('platformType')
    #------包名默认使用Server端------
    packageName = dictTemp.get('packageName')
    if os.path.exists(logDir +productcode+ '/ChannelSettingApkFile.log'):
        config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingApkFile.log'))
        root = config.getroot()
        channelNode = root.find('channel_'+channelJsonData['channel_type']+'_'+channelJsonData['game']+'.'+channelJsonData['fgi'])
        if channelNode is not None:
            if channelNode.get("checkBoxflag") == "True":
                if channelNode.get("packageName") != None:
                    if len(channelNode.get("packageName").strip()) > 0: 
                        packageName = channelNode.get("packageName")
                        print 'use client packageName config'
    #----------------------------            
        
    
    taskLock = taskManager.shareInstance().getLock()
    
    ret = execGameCommonInitializeScript(channel,platformId,appVersion,resVersion,platformType,packageName)
    if ret:
        return
    CreateTmpFolder(channel)
    source = ConfigParse.shareInstance().getApkPath()
    taskManager.shareInstance().notify(channel_old, 10)
#     source = dict.get('ApkPath')
    backupApk(source,channel)
    sourceDir = file_operate.getFullPath(constant.sdkRelatePath+channel)
    targetDir = file_operate.getFullPath(constant.tmpPath + '/'+channel)
    #拷贝渠道SDK
    taskManager.shareInstance().notify(channel_old, 13)
    file_operate.copyFiles(sourceDir, targetDir)
    taskManager.shareInstance().notify(channel_old, 15)
    #拷贝插件SDK
    copyPluginSdk(channel,targetDir)
    taskManager.shareInstance().notify(channel_old, 20)

    apkFile = targetDir + "/common.apk"
    deDir = targetDir + "/oldApkDir"
    
#     taskLock.acquire()
    operate.decompileApk_android(apkFile, deDir, taskLock)
#     taskLock.release()
    #修改v4文件夹
    #暂时不实现...
    
    
    taskManager.shareInstance().notify(channel_old, 30)

    oldApkDir = targetDir + "/oldApkDir"
    SmaliDir = oldApkDir + "/smali"
    dexFile1 = targetDir + "/classes.dex"
#     taskLock.acquire()
    ret = operate.dexTrans2Smali(dexFile1, SmaliDir, 3)
#     taskLock.release()
    
    dexFile2 = targetDir + "/classes2.dex"
    if os.path.exists(dexFile2):
        global splitDexFlag
        splitDexFlag = True
#         taskLock.acquire()
        ret = operate.dexTrans2Smali(dexFile2, SmaliDir, 3)
#         taskLock.release()
    if ret:
        return
    
#     dexFileApk = oldApkDir + "/classes.dex"
#     ret = operate.dexTrans2Smali(dexFileApk, SmaliDir, 3)
#     if ret:
#         return
    #copy res
    taskManager.shareInstance().notify(channel_old, 40)
    if os.path.exists(targetDir+"/ForRes"):
        operate.copyResToApk(targetDir+"/ForRes", oldApkDir+"/res")
        #合并资源merger方式
        # ResourceMerger.merge(oldApkDir+"/res", targetDir+"/ForRes", None)
    #copy funcellconfig.xml
    file_operate.copyFile(file_operate.getchannelFuncellConfigXmlPath(channel), oldApkDir + "/assets/funcellconfig.xml")
    
    taskManager.shareInstance().notify(channel_old, 50)
    #copy Assets
#     armPath = targetDir+"/ForAssets/so/armeabi"
#     armv7Path = targetDir+"/ForAssets/so/armeabi-v7a"
#     if os.path.exists(armPath) and os.path.exists(armv7Path):
#         operate.copyResToApk(armPath, armv7Path)
        
    if os.path.exists(targetDir+"/ForAssets"):
        operate.copyResToApk(targetDir+"/ForAssets", oldApkDir+"/assets")
    #copy extra
    
    if os.path.exists(targetDir+"/extra"):
        taskManager.shareInstance().notify(channel_old, 55)
        #-----------------六扇门配置-----------------------
#         if os.path.exists(targetDir+"/extra/Assets/GameAssets/Resources/Config") :
#             execOtherScript(channel,targetDir)
        
        execOtherScript(channel,targetDir)
        #----------------------------------------
#         operate.copyResToApk(targetDir+"/extra", oldApkDir+"/assets")
        file_operate.copyFiles(targetDir+"/extra",oldApkDir+"/assets")
    
    #copy libs
    if os.path.exists(targetDir+"/ForLibs"):
        taskManager.shareInstance().notify(channel_old, 59)
        if os.path.exists(oldApkDir+"/lib/armeabi") and os.path.exists(targetDir+"/ForLibs/armeabi"):
            operate.copyResToApk(targetDir+"/ForLibs/armeabi", oldApkDir+"/lib/armeabi")
        if os.path.exists(oldApkDir+"/lib/armeabi-v7a") and os.path.exists(targetDir+"/ForLibs/armeabi-v7a"):
            operate.copyResToApk(targetDir+"/ForLibs/armeabi-v7a", oldApkDir+"/lib/armeabi-v7a")
        if os.path.exists(oldApkDir+"/lib/x86") and os.path.exists(targetDir+"/ForLibs/x86"):
            operate.copyResToApk(targetDir+"/ForLibs/x86", oldApkDir+"/lib/x86")
        if os.path.exists(oldApkDir+"/lib/mips") and os.path.exists(targetDir+"/ForLibs/mips"):
            operate.copyResToApk(targetDir+"/ForLibs/mips", oldApkDir+"/lib/mips")
            
    taskManager.shareInstance().notify(channel_old, 60)
    #�ϲ�AndroidManifest.xml
    manifestFile = oldApkDir + "/AndroidManifest.xml"
    ET.register_namespace('android', constant.androidNS)
    targetTree = ET.parse(manifestFile)
    targetRoot = targetTree.getroot()
    print 'targetDir+/ForManifest.xml:',targetDir+"/ForManifest.xml"
    
    haveChanged = modifyManifest.doModify(manifestFile, targetDir+"/ForManifest.xml", targetRoot)
    if haveChanged:
        targetTree.write(manifestFile, 'UTF-8')
    
    taskManager.shareInstance().notify(channel_old, 62)
    #添加用户自定义配置文件
    if os.path.exists(file_operate.getFullPath(file_operate.getCommonXmlPath())):
        config = ET.parse(file_operate.getFullPath(file_operate.getCommonXmlPath()))
        root = config.getroot()
        customfile = root.find('custom_file')
        if customfile is not None:
            if customfile.get("checkBoxflag") == "True" and len(customfile.get("path")) > 0:
                sourcefile = customfile.get("path")
                file_operate.copyFile(file_operate.getFullPath(sourcefile),targetDir+"/customFile/customFile.xml")
                if os.path.exists(file_operate.getFullPath(targetDir+"/customFile/customFile.xml")):
                    custom_haveChanged = modifyManifest.doModify(manifestFile, targetDir+"/customFile/customFile.xml", targetRoot)
                    if custom_haveChanged:
                        targetTree.write(manifestFile, 'UTF-8')
                        
    taskManager.shareInstance().notify(channel_old, 65)
    
    newPackagename = operate.renameApkPackage(SmaliDir, manifestFile, packageName)
    
    taskManager.shareInstance().notify(channel_old, 70)
    
    print channel , oldApkDir
    operate.addSplashScreen(channel, targetDir)
    
    #拷贝设置界面中的目录到指定目录
    copyCustomDir(channel, oldApkDir)
    
    #插件sdk加入母包中-------------------
    copyPluginToApk(channel,targetDir,oldApkDir,channelJsonData,packageName)
    
#     taskManager.shareInstance().notify(channel_old, 79)
    
    #覆盖某些jar
    taskManager.shareInstance().notify(channel_old, 79)
    operate.coverCustomSdk(targetDir, deDir)
    
    
    ret = execGameCommongameSdkScript(channel,oldApkDir,newPackagename,channelJsonData)
    if ret:
        return
    
    taskLock.acquire()
    tmp_module = 'script'
    scriptPath = targetDir + "/script.pyc"
    if os.path.exists(scriptPath):
        taskManager.shareInstance().notify(channel_old, 81)
        sys.path.append(targetDir)
        ret = import_module(tmp_module).script(oldApkDir, newPackagename,channelJsonData)
        del sys.modules[tmp_module]
        sys.path.remove(targetDir)
    taskLock.release()
    
    taskManager.shareInstance().notify(channel_old, 82)
    ret = operate.pushIconIntoApk('', oldApkDir,channel)
    
    taskManager.shareInstance().notify(channel_old, 83)
    
    operate.modifyGameName(channel, oldApkDir)
    
#     taskLock.acquire()
    taskManager.shareInstance().notify(channel_old, 84)
    ret = operate.produceNewRFile(channel,newPackagename, oldApkDir)
#     taskLock.release()
    if ret:
        return


    
    #smali to dex
#     classesDexFile = oldApkDir + "/classes.dex"
#     ret = operate.smaliTrans2dex(SmaliDir, classesDexFile)
#     if ret:
#         return 
    #         if os.path.exists(SmaliDir):
    #             file_operate.delete_file_folder(SmaliDir)
    
    
    maxFuncNum = 65000
    checkBoxflag = False
    useFuncellApplicationJarFlag = False
    logDir = 'Log/'
    allFiles = []
    if os.path.exists(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingMultidexFile.xml')):
        config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingMultidexFile.xml'))
        root = config.getroot()
        channelNode = root.find('channel_'+channel.split('/')[0]+'_'+channel.split('/')[1])
        if channelNode is not None:
            if channelNode.get("checkBoxflag") == "True":
                checkBoxflag = True
                maxFuncNum = channelNode.get("dexNum")
                if channelNode.get("useFuncellApplicationJarFlag") == "True":
                    useFuncellApplicationJarFlag = True
                if len(channelNode.get("multidexPath").strip()) > 0 and os.path.exists(file_operate.getFullPath(channelNode.get("multidexPath").strip())):
                    multidexFile = codecs.open(file_operate.getFullPath(channelNode.get("multidexPath").strip()), 'r', 'utf-8')
                    for line in multidexFile.readlines():
                        line = line.rstrip("\r\n")
                        allFiles.append(line)
        
    channelMultidexFile = targetDir + "/ForMultidex.xml"
    existsChannelMultidexFile = False
    if os.path.exists(channelMultidexFile):
        existsChannelMultidexFile = True
        multidexFile = codecs.open(channelMultidexFile, 'r', 'utf-8')
        for line in multidexFile.readlines():
            line = line.rstrip("\r\n")
            allFiles.append(line)
    
    if splitDexFlag == True or checkBoxflag == True or existsChannelMultidexFile == True:
        print '+++++++++++++++++++++++++++++++++++++'
        taskManager.shareInstance().notify(channel_old, 85)
        totalMethod = operate.splitDexByMethod(targetDir, oldApkDir,maxFuncNum,useFuncellApplicationJarFlag,existsChannelMultidexFile,allFiles)
        if totalMethod < int(maxFuncNum):
            #查询所有字段数量
            pass
            # totalField = operate.splitDexByField(targetDir, oldApkDir,maxFuncNum,useFuncellApplicationJarFlag,existsChannelMultidexFile,allFiles)
        print '+++++++++++++++++++++++++++++++++++++'
    
    taskManager.shareInstance().notify(channel_old, 86)
    operate.rewriteYml(oldApkDir)
    
#     taskLock.acquire()
    taskManager.shareInstance().notify(channel_old, 87)
    tempApkName = file_operate.getFullPath(ConfigParse.shareInstance().getOutApkDir()) + "/apk_"+channel.split('/')[0]+'_'+channel.split('/')[1]+"_unsigned.apk"
    ret = operate.recompileApk(oldApkDir, tempApkName)
#     taskLock.release()
    if ret:
        return
    #-------------------添加unkonw文件夹，可能为资源文件放入到代码目录中
    if os.path.exists(file_operate.getFullPath(targetDir+"/unknown")):
        taskManager.shareInstance().notify(channel_old, 88)
        # newZipName = file_operate.getFullPath(ConfigParse.shareInstance().getOutApkDir()) + "/apk_"+channel.split('/')[0]+'_'+channel.split('/')[1]+"_unsigned.zip"
        # os.rename(tempApkName, newZipName)
        # azip = zipfile.ZipFile(newZipName, 'a')
        azip = zipfile.ZipFile(tempApkName, 'a')
        for current_path, subfolders, filesname in os.walk(targetDir+"/unknown"):
            fpath = current_path.replace(targetDir+"/unknown",'')
            fpath = fpath and fpath + os.sep or ''#实现当前文件夹以及包含的所有文件的压缩
            for filename in filesname:
                azip.write(os.path.join(current_path, filename),fpath+filename)
        azip.close()
        # os.rename(newZipName, tempApkName)
    
    taskManager.shareInstance().notify(channel_old, 89)
    keystoreFile = ConfigParse.shareInstance().getKeystoreFile()
    storepassword = ConfigParse.shareInstance().getKeystorePassword()
    alias = ConfigParse.shareInstance().getKeystoreAlias()
    aliasPasswd = ConfigParse.shareInstance().getKeystoreAliasPassword()
    #def signApk(apkFile, keyStore, storepassword, keyalias, aliaspassword):
    ret = operate.signApk(tempApkName, keystoreFile, storepassword, alias, aliasPasswd)
    taskManager.shareInstance().notify(channel_old, 95)
#     print "sign"
    print ret
    if ret:
        return
    rule='%Y-%m-%d-%H-%M-%S'
    time_stamp = time.strftime(rule, time.localtime())
    apkName = (file_operate.getFullPath(ConfigParse.shareInstance().getOutApkDir()) + "/apk_"+channel.split('/')[0]+'_'+channel.split('/')[1]+'%s'+".apk") %("("+time_stamp+")")
    ret = operate.alignAPK(tempApkName, apkName, file_operate.getFullPath(ConfigParse.shareInstance().getOutApkDir()))
    
#     ret = execGameCommonFinalizeScript(channel,platformId,appVersion,resVersion,checkBox_isChecked,checkBox_4_isChecked,checkBox_5_isChecked)
#     if ret:
#         print 'execGameCommonFinalizeScript error:'
#         return
    taskManager.shareInstance().notify(channel_old, 100)
    print "----------------------------%s pack complete!------------------------" % channel

def copyCustomDir(channel, oldApkDir):
    logDir = 'Log/'
    productcode = ConfigParse.shareInstance().getProductCode()
    if os.path.exists(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingOtherFile.log')):
        config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingOtherFile.log'))
        root = config.getroot()
        channelNode = root.find('channel_'+channel.split('/')[0]+'_'+channel.split('/')[1])
        if channelNode is not None:
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 71)
            source = file_operate.getFullPath(channelNode.get("source"))
            target = channelNode.get("target")
            checkBoxflag = channelNode.get("checkBoxflag")
            if checkBoxflag == "True":
                file_operate.copyFiles(source, file_operate.getFullPath(oldApkDir+'/'+target))


def SavaChannePluginlVersionConfig(pluginType,channel,pluginChannel,pluginVersion):
    info = str(pluginType+'|'+channel.split('/')[0]+'|'+channel.split('/')[1]+'|'+pluginChannel+'|'+pluginVersion)
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
            modifyFileContent(logDir +productcode+ '/ChannelPluginListVersionFile.log', str(oldstr), str(newstr))
            return
    
    
    logFile = codecs.open(logDir +productcode+ '/ChannelPluginListVersionFile.log', 'a+', 'utf-8')
    content = info + '\n'
    logFile.write(unicode(content, 'gbk'))
    logFile.close()
       

def SaveChannelVersionConfig(info):
    logDir = 'Log/'
    productcode = ConfigParse.shareInstance().getProductCode()
    if not os.path.exists(logDir+productcode):
        os.makedirs(logDir+productcode)
    
    oldstr=''
    newstr=''
    flag = False
    if os.path.exists(logDir +productcode+ '/ChannelVersionFile.log'):
        logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
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
            modifyFileContent(logDir +productcode+ '/ChannelVersionFile.log', str(oldstr), str(newstr))
            return
    
    
    logFile = codecs.open(logDir +productcode+ '/ChannelVersionFile.log', 'a+', 'utf-8')
    content = info + '\n'
    logFile.write(unicode(content, 'gbk'))
    logFile.close()
    
def modifyFileContent(sourcefile, oldContent, newContent):
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


def CreateTmpFolder(channel):
        tmp = file_operate.getFullPath(constant.tmpPath)
        if not os.path.exists(tmp):
            os.makedirs(tmp)
        tmp_channel = file_operate.getFullPath(constant.tmpPath+'/'+channel)
        if os.path.exists(tmp_channel):
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 8)
            file_operate.delete_file_folder(tmp_channel)
        if not os.path.exists(tmp_channel):
            os.makedirs(tmp_channel)


def backupApk(source,channel):
    outputDir = constant.tmpPath
    backupName = '%s/%s/common.apk' % (outputDir,channel)
    backupName = file_operate.getFullPath(backupName)
    print "backupname" + backupName
    
    if os.path.exists(backupName):
        os.remove(backupName)
    
    print "source " +source
    file_operate.copyBaseApk(source, backupName)
#     file_operate.copyFile(source, backupName)

def writeConfigToSdkConfigFile(channel,dictTemp):
    try:
        #write talkingdata to funcellconfig.xml
        checkBox_isChecked = dictTemp.get('checkBox_isChecked')
        checkBox_2_isChecked = dictTemp.get('checkBox_2_isChecked')
        checkBox_4_isChecked = dictTemp.get('checkBox_4_isChecked')
        checkBox_5_isChecked = dictTemp.get('checkBox_5_isChecked')
        comboBox_3_currentText = dictTemp.get('comboBox_3_currentText')
        lineEdit_13_text = dictTemp.get('lineEdit_13_text')
        lineEdit_16_text = dictTemp.get('lineEdit_16_text')
        lineEdit_17_text = dictTemp.get('lineEdit_17_text')
        advertising_appid = dictTemp.get('advertising_appid')
        pushAppKey_text = dictTemp.get('pushAppKey_text')
        pushAppSecret_text = dictTemp.get('pushAppSecret_text')
        
        
        config = ET.parse(file_operate.getchannelFuncellConfigXmlPath(channel))
        root = config.getroot()
        talkingdata = root.find("talkingdata")
        if checkBox_isChecked:
            talkingdata.set("status", "enable")
        else:
            talkingdata.set("status", "disable")
        talkingdata.set("appId", unicode(lineEdit_13_text))
        
        crash = root.find("crash")
        if checkBox_4_isChecked:
            crash.set("status", "enable")
        else:
            crash.set("status", "disable")
        crash.set("appId", unicode(lineEdit_16_text))
        
        push = root.find("push")
        if checkBox_5_isChecked:
            push.set("status", "enable")
        else:
            push.set("status", "disable")
        push.set("appId", unicode(lineEdit_17_text))
        push.set("appKey", '')
        push.set("appSecret", '')
        if comboBox_3_currentText==u'个推':
            push.set("appKey", unicode(pushAppKey_text))
            push.set("appSecret", unicode(pushAppSecret_text))
        
        advertising = root.find("advertising")
        if advertising == None:
            if checkBox_2_isChecked:
                advertisingNode = SubElement(root, 'advertising')
                advertisingNode.set('appId', unicode(advertising_appid))
                advertisingNode.set('status', 'enable')
        else:
            advertising.set("appId",unicode(advertising_appid))
            if checkBox_2_isChecked:
                advertising.set('status', 'enable')
            else:
                advertising.set('status', 'disable')
                
        config.write(file_operate.getchannelFuncellConfigXmlPath(channel), "utf-8")
    
    except Exception,e:
        print e
        print "Error: cannot parse file: funcellconfig.xml."
        return -1

def execGameCommonInitializeScript(channelName,platformId,appVersion,resVersion,platformType,packageName):
    if (os.path.exists(file_operate.getGameCommonScriptPath())):
        
        gameCommonInitScriptBat = file_operate.getGameCommonScriptPath() + "/initialize.bat"
        if (os.path.exists(gameCommonInitScriptBat)):
            cmd = '"%s" "%s" "%s" "%s" "%s"' % (gameCommonInitScriptBat, platformId, channelName, appVersion, resVersion)
            ret = file_operate.execFormatCmd(cmd)
            if ret:
                print "execute initialize.bat error"
                return 1
        gameCommonInitScriptExe = file_operate.getGameCommonScriptPath() + "/initialize.exe"
        if (os.path.exists(gameCommonInitScriptExe)):
            cmd = '"%s" "%s" "%s" "%s" "%s"' % (gameCommonInitScriptExe, platformId, channelName, appVersion, resVersion)
            ret = file_operate.execFormatCmd(cmd)
            if ret:
                print "execute initialize.exe error"
                return 1
        gameCommonInitScriptPyc = file_operate.getGameCommonScriptPath() + "/initialize.pyc"
        if os.path.exists(gameCommonInitScriptPyc):
            taskManager.shareInstance().notify(channelName.split('/')[0]+'_'+channelName.split('/')[1], 6)
            tmp_module = 'initialize'
            sys.path.append(file_operate.getGameCommonScriptPath())
            ret = import_module(tmp_module).initialize(platformId, channelName,platformType, appVersion, resVersion,packageName)
            del sys.modules[tmp_module]
            sys.path.remove(file_operate.getGameCommonScriptPath())
#             import initialize
#             ret = initialize.initialize(platformId, channelName,platformType, appVersion, resVersion)



def execGameCommongameSdkScript(channelName,oldApkDir,newPackagename,channelJsonData):
    if (os.path.exists(file_operate.getGameCommonScriptPath())):
        gameCommongameSdkScriptPyc = file_operate.getGameCommonScriptPath() + "/gameSdkScript.pyc"
         
        if os.path.exists(gameCommongameSdkScriptPyc):
            taskManager.shareInstance().notify(channelName.split('/')[0]+'_'+channelName.split('/')[1], 80)
            tmp_module = 'gameSdkScript'
            sys.path.append(file_operate.getGameCommonScriptPath())
            ret = import_module(tmp_module).gameSdkScript(oldApkDir,channelName,newPackagename,channelJsonData)
            del sys.modules[tmp_module]
            sys.path.remove(file_operate.getGameCommonScriptPath())
            
#             import gameSdkScript
#             ret = gameSdkScript.gameSdkScript(oldApkDir,channelName)
#             del sys.modules['gameSdkScript']
#             sys.path.remove(file_operate.getGameCommonScriptPath())

def execGameCommonFinalizeScript(channelName,platformId,appVersion,resVersion,checkBox_isChecked,checkBox_4_isChecked,checkBox_5_isChecked):
    if (os.path.exists(file_operate.getGameCommonScriptPath())):
        
        gameCommonFinalizeScriptBat = file_operate.getGameCommonScriptPath() + "/finalize.bat"
        if (os.path.exists(gameCommonFinalizeScriptBat)):
            cmd = '"%s" "%s" "%s" "%s" "%s"' % (gameCommonFinalizeScriptBat, platformId, channelName, appVersion, resVersion)
            ret = file_operate.execFormatCmd(cmd)
            if ret:
                print "execute finalize.bat error"
                return 1
        gameCommonFinalizeScriptExe = file_operate.getGameCommonScriptPath() + "/finalize.exe"
        if (os.path.exists(gameCommonFinalizeScriptExe)):
            cmd = '"%s" "%s" "%s" "%s" "%s"' % (gameCommonFinalizeScriptExe, platformId, channelName, appVersion, resVersion)
            ret = file_operate.execFormatCmd(cmd)
            if ret:
                print "execute finalize.exe error"
                return 1
        gameCommonFinalizeScriptPyc = file_operate.getGameCommonScriptPath() + "/finalize.pyc"
        if os.path.exists(gameCommonFinalizeScriptPyc):
            print "gameCommonFinalize" + file_operate.getGameCommonScriptPath() + "/finalize.pyc"
            sys.path.append(file_operate.getGameCommonScriptPath())
            import finalize
            ret = finalize.finalize(platformId, channelName, appVersion, resVersion,checkBox_isChecked,checkBox_4_isChecked,checkBox_5_isChecked)
            
def execOtherScript(channel,oldApkDir):
        if (os.path.exists(file_operate.getGameCommonScriptPath())):
            otherScriptPyc = file_operate.getGameCommonScriptPath() + "/otherScript.pyc"
            if os.path.exists(otherScriptPyc):
                taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 58)
                tmp_module = 'otherScript'
                sys.path.append(file_operate.getGameCommonScriptPath())
                ret = import_module(tmp_module).otherScript(oldApkDir)
                del sys.modules[tmp_module]
                sys.path.remove(file_operate.getGameCommonScriptPath())
                
#                 import otherScript
#                 ret = otherScript.otherScript(oldApkDir)

def deleteWorkspace(channel):
    tmpstr = channel
    flagNum = len(tmpstr.split('_'))
    game_fig = tmpstr.split('_')[flagNum - 1]
    tmpChannellen = len(tmpstr) - len(game_fig) - 1
    tmpChannel = tmpstr[0:tmpChannellen]
    channel = tmpChannel + '/' + game_fig
    
#     targetDir = file_operate.getFullPath(constant.tmpPath + '/'+channel.split('_')[0]+'/'+channel.split('_')[1])
    targetDir = file_operate.getFullPath(constant.tmpPath + '/'+channel)
    if os.path.exists(targetDir):
        file_operate.delete_file_folder(targetDir)

def judgeChannelPluginVersion(channel,pluginTypePlugin,pluginChannel,channelPluginJson):
    pluginconfig_version = 0
    if os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/funcellplugin.xml')):
        pluginconfigfile = file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/funcellplugin.xml')
        pluginconfig = ET.parse(pluginconfigfile)
        root = pluginconfig.getroot()
        pluginLsNode = root.findall("pluginLs")
#         pluginconfig_version = 0
        if pluginLsNode is not None:
            for pluginNode in pluginLsNode:
                itemLsNode = pluginNode.findall("item")
                if itemLsNode is not None:
                    for itemNode in itemLsNode:
                        typePluginLsNode = itemNode.findall('typePlugin')
                        channelLsNode = itemNode.findall('channel')
                        versionLsNode = itemNode.findall('version')
                        for typePluginNode in typePluginLsNode:
                            for channelNode in channelLsNode:
                                for versionNode in versionLsNode:
                                    if pluginTypePlugin == typePluginNode.text and pluginChannel == channelNode.text:
                                        pluginconfig_version = versionNode.text
                            
    print 'pluginconfig_version:',pluginconfig_version
    
    logDir = 'Log/'
    productcode = ConfigParse.shareInstance().getProductCode()
    versionCode = pluginconfig_version
    versionFlag = False
    if os.path.exists(logDir +productcode+ '/ChannelPluginListVersionFile.log'):
        logFile = codecs.open(logDir +productcode+ '/ChannelPluginListVersionFile.log', 'r', 'utf-8')
        for line in logFile.readlines():
            line = line.rstrip("\r\n")
            Info1 = line.split('|')
            if Info1[0] == pluginTypePlugin and Info1[1] == channel.split('/')[0] and Info1[2] == channel.split('/')[1] and Info1[3] == pluginChannel:
                versionCode = Info1[4]
                versionFlag = True
        logFile.close()
    
    #查找最大版本号
    if versionFlag == False:
        pluginPublicLsJson = taskManager.shareInstance().getPluginlListData()
        for key_pluginData in pluginPublicLsJson:
            _pluginType = key_pluginData['type']
            _pluginChannel = key_pluginData['channel']
            if pluginTypePlugin == _pluginType and pluginChannel == _pluginChannel:
                pluginVersionListData = key_pluginData['version']
                for key_pluginVersion in pluginVersionListData:
                    if cmp(key_pluginVersion['version'],versionCode) == 1:
                        versionCode = key_pluginVersion['version']
            
    if cmp(versionCode,pluginconfig_version) != 0:
#     if float(versionCode) != float(pluginconfig_version):
        pluginPublicLsJson = taskManager.shareInstance().getPluginlListData()
        pluginDir = file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/'+pluginTypePlugin+'/'+pluginChannel)
        for key_pluginData in pluginPublicLsJson:
            _pluginType = key_pluginData['type']
            _pluginChannel = key_pluginData['channel']
            if pluginTypePlugin == _pluginType and pluginChannel == _pluginChannel:
                pluginVersionListData = key_pluginData['version']
                for key_pluginVersion in pluginVersionListData:
                    if versionCode == key_pluginVersion['version']:
                        pluginurl = key_pluginVersion['url']
                        pluginmd5 = key_pluginVersion['md5']
                        
                        taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 5,pluginTypePlugin+'_'+pluginChannel)
                        downloadFlag = httpManager.shareInstance().downloadZip(channel,pluginurl,pluginmd5)
                        if downloadFlag == False:
                            print 'download plugin zip fail,url:%s'%(pluginurl)
                            return ''
                        pluginzipName = os.path.basename(file_operate.getFullPath(pluginurl))
                        DownloadDir = file_operate.getFullPath("Download/")
                        file_operate.decompression(DownloadDir+pluginzipName,pluginDir,file_operate.getFullPath(constant.sdkRelatePath+'plugin'+'/'+str(channel)+'/'+pluginTypePlugin+'/'+pluginChannel))
        
#         for key_channelpluginJson in channelPluginJson:
#             if pluginTypePlugin == key_channelpluginJson['typePlugin'] and pluginChannel == key_channelpluginJson['channel']:
#                 key_channelpluginJson['version'] = str(versionCode)
    
    for key_channelpluginJson in channelPluginJson:
        if pluginTypePlugin == key_channelpluginJson['typePlugin'] and pluginChannel == key_channelpluginJson['channel']:
            key_channelpluginJson['version'] = str(versionCode)
         
    SavaChannePluginlVersionConfig(pluginTypePlugin,channel,pluginChannel,str(versionCode))
    
    return channelPluginJson

def copyPluginSdk(channel,targetDir):
    sourceDir = file_operate.getFullPath(constant.sdkRelatePath+'/plugin'+'/'+channel)
    if os.path.exists(sourceDir):
        file_operate.copyFiles(sourceDir, targetDir)
    
def copyPluginToApk(channel,targetDir,oldApkDir,channelJsonData,packageName):
    #copy funcellplugin.xml
    file_operate.copyFile(targetDir+'/funcellplugin.xml', oldApkDir + "/assets/funcellplugin.xml")
    if channelJsonData['config'].has_key('pluginLs'):
        pluginLsJson = channelJsonData['config']['pluginLs']
        #-----------排序------------------
#         print 'pluginLsJson source:',pluginLsJson
        pluginLsJson.sort(key = lambda x:x["channel"])
        pluginLsJson.sort(key = lambda x:x["typePlugin"])
#         print 'pluginLsJson sort:',pluginLsJson
        #-----------End-----------------
        
        for key_data in  pluginLsJson:
#             for key in key_data:
#                 if 'status' == key and 'enable' == key_data[key]:
            print '---------copy plugin----------'
            pluginTypePlugin = key_data['typePlugin']
            pluginChannel = key_data['channel']

            print "pluginTypePlugin:"+pluginTypePlugin+" pluginChannel:"+pluginChannel
            pluginDir = targetDir + '/'+pluginTypePlugin +'/' +pluginChannel
            
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 72)
            #copy dex
            SmaliDir = oldApkDir + "/smali"
            dexFile = pluginDir + "/classes.dex"
#             taskManager.shareInstance().getLock().acquire()
            ret = operate.dexTrans2Smali(dexFile, SmaliDir, 3)
#             taskManager.shareInstance().getLock().release()
            
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 73)
            #cpoy res
            if os.path.exists(pluginDir+"/ForRes"):
                operate.copyResToApk(pluginDir+"/ForRes", oldApkDir+"/res")
                #采用merger方式合并
                # ResourceMerger.merge(oldApkDir + "/res", pluginDir + "/ForRes", None)
            
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 74)
            #copy Assets
            if os.path.exists(pluginDir+"/ForAssets"):
                operate.copyResToApk(pluginDir+"/ForAssets", oldApkDir+"/assets")
            
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 75)
            #copy libs
            if os.path.exists(pluginDir+"/ForLibs"):
                if os.path.exists(oldApkDir+"/lib/armeabi") and os.path.exists(pluginDir+"/ForLibs/armeabi"):
                    operate.copyResToApk(pluginDir+"/ForLibs/armeabi", oldApkDir+"/lib/armeabi")
                if os.path.exists(oldApkDir+"/lib/armeabi-v7a") and os.path.exists(pluginDir+"/ForLibs/armeabi-v7a"):
                    operate.copyResToApk(pluginDir+"/ForLibs/armeabi-v7a", oldApkDir+"/lib/armeabi-v7a")
                if os.path.exists(oldApkDir+"/lib/x86") and os.path.exists(pluginDir+"/ForLibs/x86"):
                    operate.copyResToApk(pluginDir+"/ForLibs/x86", oldApkDir+"/lib/x86")
                if os.path.exists(oldApkDir+"/lib/mips") and os.path.exists(pluginDir+"/ForLibs/mips"):
                    operate.copyResToApk(pluginDir+"/ForLibs/mips", oldApkDir+"/lib/mips")
            
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 76)
            #modify AndroidManifest.xml
            manifestFile = oldApkDir + "/AndroidManifest.xml"
            ET.register_namespace('android', constant.androidNS)
            targetTree = ET.parse(manifestFile)
            targetRoot = targetTree.getroot()

            haveChanged = modifyManifest.doModify(manifestFile, pluginDir+"/ForManifest.xml", targetRoot)
            if haveChanged:
                targetTree.write(manifestFile, 'UTF-8')

            #exec script
            taskManager.shareInstance().getLock().acquire()
            tmp_module = 'script'
            scriptPath = pluginDir + "/script.pyc"
            if os.path.exists(scriptPath):
                taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 77)
                sys.path.append(pluginDir)
                ret = import_module(tmp_module).script(oldApkDir, packageName,channelJsonData)
                del sys.modules[tmp_module]
                sys.path.remove(pluginDir)
            taskManager.shareInstance().getLock().release()
            
            taskManager.shareInstance().notify(channel.split('/')[0]+'_'+channel.split('/')[1], 78)
            #插件中R.xx方式 ，生成指定包名下R文件
#             taskManager.shareInstance().getLock().acquire()
            generatePluginR(pluginDir,oldApkDir)
#             taskManager.shareInstance().getLock().release()

            #拷贝插件目录中的ExtendR 文件夹到tmp目录中进行合并
            if os.path.exists(pluginDir+"/ExtendR"):
                if not os.path.exists(targetDir+"/ExtendR"):
                    os.makedirs(targetDir + "/ExtendR")
                file_operate.copyFiles(pluginDir + "/ExtendR", targetDir + "/ExtendR")

            #----拷贝unknow目录资源
            if os.path.exists(pluginDir+"/unknown"):
                if not os.path.exists(targetDir+"/unknown"):
                    os.makedirs(targetDir+"/unknown")
                file_operate.copyFiles(pluginDir+"/unknown",targetDir+"/unknown")
                    

def generatePluginR(pluginDir,decompileFullDir):
    if not os.path.exists(pluginDir+"/ForRconfig.xml"):
        return
    fullPath = decompileFullDir
    tempPath = os.path.dirname(decompileFullDir)
    tempPath = tempPath + '/tempRFile'
    if os.path.exists(tempPath):
        file_operate.delete_file_folder(tempPath)
    if not os.path.exists(tempPath):
        os.makedirs(tempPath)
    resPath = os.path.join(decompileFullDir, 'res')
    targetResPath = os.path.join(tempPath, 'res')
    file_operate.copyFiles(resPath, targetResPath)
    genPath = os.path.join(tempPath, 'gen')
    if not os.path.exists(genPath):
        os.mkdir(genPath)
    androidPath = file_operate.getToolPath('android.jar')
    aaptPath = file_operate.getToolPath('aapt')
    try:
        config = ET.parse(pluginDir+"/ForRconfig.xml")
        root = config.getroot()
        Manifest = root.find("Manifest")
        num = int(Manifest.get('num'))
        for i in range(0,num):
            srcManifest_i = os.path.join(pluginDir, 'Manifest/'+str(i)+'/AndroidManifest.xml')
            cmd = '"%s" p -f -m -J "%s" -S "%s" -I "%s" -M "%s"' % (aaptPath,genPath,targetResPath,androidPath,srcManifest_i)
            ret = file_operate.execFormatCmd(cmd)
            if ret:
                error_operate.error(102)
                return 1
            packageNameArray = Manifest.get('packageNameArray')
            packageNameNode = packageNameArray.split(',')[i]
            RPath = packageNameNode.replace('.', '/')
            RPath = os.path.join(genPath, RPath)
            RFile = os.path.join(RPath, 'R.java')
            cmd = '"%sjavac" -source 1.7 -target 1.7 -encoding UTF-8 "%s"' % (file_operate.getJavaBinDir(), RFile)
            ret = file_operate.execFormatCmd(cmd)
            if ret:
                error_operate.error(103)
                return 1
    except Exception,e:
        print e
        print "Error: generatePluginR..."
    
    dexPath = os.path.join(tempPath, 'class.dex')
    if platform.system() == 'Windows':
#         dxTool = file_operate.getToolPath('dx.bat')
        dxTool = file_operate.getFullPath('tool/win/lib/dx.jar')
    else:
        dxTool = file_operate.getToolPath('dx')
#     cmd = '"%s" --dex --output="%s" "%s"' % (dxTool, dexPath, genPath)
    cmd = '"%s" -jar -Xms512m -Xmx1024m "%s" --dex --output="%s" "%s"' % (file_operate.getJava(),dxTool, dexPath, genPath)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        error_operate.error(104)
        return 1
    smaliPath = os.path.join(fullPath, 'smali')
    ret = operate.dexTrans2Smali(dexPath, smaliPath, 10)
    if ret:
        return 1
    else:
        return 0


