#Embedded file name: D:/AnySDK_Package/Env/debug/../script\modifyManifest.py
import sys, string, os
from xml.etree import ElementTree as ET
import re
import file_operate
from xml.dom import minidom
import codecs
androidNS = 'http://schemas.android.com/apk/res/android'

def doModify(manifestFile, sourceFile, root):
    """
        modify AndroidManifest.xml by ForManifest.xml
    """
    if not os.path.exists(manifestFile):
        return False
    if not os.path.exists(sourceFile):
        return False
    
    print "exist"
    bRet = False
    sourceTree = ET.parse(sourceFile)
    sourceRoot = sourceTree.getroot()
    f = open(manifestFile)
    targetContent = f.read()
    f.close()
    
    appCfgNode = sourceRoot.find('applicationCfg')
    if appCfgNode is not None:
        key = '{' + androidNS + '}name'
        appName = appCfgNode.get(key)
        if appName != None and len(appName) > 0:
            targetAppNode = root.find("application")
            targetAppNode.set(key, appName)
        if len(appCfgNode) > 0:
            appKeyWord = appCfgNode.get('keyword')
            if appKeyWord != None and len(appKeyWord) > 0:
                keyIndex = targetContent.find(appKeyWord)
                print 'keyIndex:',keyIndex
                if -1 == keyIndex:
                    bRet = True
                    for node in list(appCfgNode):
                        root.find('application').append(node)
                 
    perCfgNode = sourceRoot.find('permissionCfg')
    if perCfgNode is not None and len(perCfgNode) > 0:
        for oneNode in list(perCfgNode):
            key = '{' + androidNS + '}name'
            perAttr = oneNode.get(key)
            if perAttr != None and len(perAttr) > 0:
                attrIndex = targetContent.find(perAttr)
                if -1 == attrIndex:
                    bRet = True
                    root.append(oneNode)

    return bRet


def modify(manifestFile, sourceCfgFile, pluginName, usrSDKConfig):
    manifestFile = file_operate.getFullPath(manifestFile)
    sourceXml = sourceCfgFile
    sourceXml = file_operate.getFullPath(sourceXml)
    if not os.path.exists(sourceXml):
        ForManifestDir = os.path.dirname(sourceXml)
        screenOrientation = getOrientation(manifestFile, usrSDKConfig)
        if screenOrientation == 'landscape' or screenOrientation == 'auto':
            sourceXml = ForManifestDir + '/ForManifestLandscape.xml'
        else:
            sourceXml = ForManifestDir + '/ForManifestPortrait.xml'
    if not os.path.exists(sourceXml):
        return
    ET.register_namespace('android', androidNS)
    targetTree = ET.parse(manifestFile)
    targetRoot = targetTree.getroot()
    haveChanged = doModify(manifestFile, sourceXml, targetRoot)
    if haveChanged:
        file_operate.printf('Modify AndroidManifest.xml for plugin ' + pluginName)
        targetTree.write(manifestFile, 'UTF-8')
        
def doModifyForManifest(manifestFile, sourceFile, root):
    """
    Merge ForManifest.xml e.g. talkingdata and sdk ForManifest.xml merge together
    """ 
    if not os.path.exists(manifestFile):
        return False
    if not os.path.exists(sourceFile):
        return False
    
    print "exist"
    bRet = False
    sourceTree = ET.parse(sourceFile)
    sourceRoot = sourceTree.getroot()
    f = open(manifestFile)
    targetContent = f.read()
    f.close()
    
    appCfgNode = sourceRoot.find('applicationCfg')
    if appCfgNode is not None:
        if len(appCfgNode) > 0:
            appKeyWord = appCfgNode.get('keyword')
            if appKeyWord != None and len(appKeyWord) > 0:
                keyIndex = targetContent.find(appKeyWord)
                if -1 == keyIndex:
                    bRet = True
                    appRootCfg = root.find('applicationCfg')
                    for node in list(appCfgNode):
                        appRootCfg.append(node)
                 
    perCfgNode = sourceRoot.find('permissionCfg')
    if perCfgNode is not None and len(perCfgNode) > 0:
        perRootCfg = root.find('permissionCfg')
        for oneNode in list(perCfgNode):
            key = '{' + androidNS + '}name'
            perAttr = oneNode.get(key)
            if perAttr != None and len(perAttr) > 0:
                attrIndex = targetContent.find(perAttr)
                if -1 == attrIndex:
                    bRet = True
                    perRootCfg.append(oneNode)
    return bRet


def getOrientation(manifestFile, usrSDKConfig):
    if os.path.exists(manifestFile):
        doc = minidom.parse(manifestFile)
        rootNode = doc.documentElement
        applicationList = rootNode.getElementsByTagName('application')
        for applicationNode in applicationList:
            activityList = rootNode.getElementsByTagName('activity')
            for activityNode in activityList:
                categoryList = activityNode.getElementsByTagName('category')
                for categoryNode in categoryList:
                    if categoryNode.getAttribute('android:name') == 'android.intent.category.LAUNCHER':
                        if activityNode.getAttribute('android:screenOrientation'):
                            return activityNode.getAttribute('android:screenOrientation')
                        if applicationNode.getAttribute('android:screenOrientation'):
                            return applicationNode.getAttribute('android:screenOrientation')

        for param in usrSDKConfig['param']:
            if param['name'].count('Orientation') > 0:
                return param['value']

    print 'default'
    return 'landscape'
