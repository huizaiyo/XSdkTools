# -*- coding: utf-8 -*-
#Embedded file name: D:/AnySDK_Package/Env/debug/../script\apk_operate.py
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree
import file_operate
import os
import os.path
import zipfile
import re
import modifyManifest
import subprocess
import platform
import error_operate
from xml.dom import minidom
import codecs
import sys
import constant
from _ast import Num
from config import ConfigParse
from PIL import Image
import shutil
sys.path.append('module')
androidNS = 'http://schemas.android.com/apk/res/android'

def dexTrans2Smali(dexFile, targetDir, step, baksmali = 'baksmali.jar'):
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
    if os.path.exists(dexFile):
        dexFile = file_operate.getFullPath(dexFile)
        smaliFile = file_operate.getToolPath(baksmali)
        targetDir = file_operate.getFullPath(targetDir)
        cmd = '"%s" -jar -Xms512m -Xmx512m "%s" -o "%s" "%s"' % (file_operate.getJava(),
         smaliFile,
         targetDir,
         dexFile)
        ret = file_operate.execFormatCmd(cmd)
        if ret:
            if step == 3:
                error_operate.error(30)
                return 1
            elif step == 4:
                error_operate.error(40)
                return 1
            else:
                error_operate.error(105)
                return 1
        else:
            return 0
        
def iconCopytoDrawable(drawableDir, needIconName, iconName):
    if not os.path.exists(needIconName):
        return
    
    if not os.path.exists(drawableDir):
        os.mkdir(drawableDir)
        
    file_operate.copyFile(needIconName, drawableDir + '/' + iconName + '.png')
        
def pushIconIntoApk(iconPath, decompileDir):
    
    manifestFile = decompileDir + '/AndroidManifest.xml'
    ET.register_namespace('android', androidNS)
    targetTree = ET.parse(manifestFile)
    targetRoot = targetTree.getroot()
    namekey = '{' + androidNS + '}name'
    key = '{' + androidNS + '}icon'
    icon = None
    applicationNode = targetRoot.find('application')
    if applicationNode is None:
        error_operate.error(121)
        return 1
    activityLsNode = applicationNode.findall('activity')
    if activityLsNode is not None:
        for activityNode in activityLsNode:
            intentLsNode = activityNode.findall('intent-filter')
            if intentLsNode is None:
                continue
            for intentNode in intentLsNode:
                bFindAction = False
                bFindCategory = False
                actionLsNode = intentNode.findall('action')
                for actionNode in actionLsNode:
                    if actionNode.attrib[namekey] == 'android.intent.action.MAIN':
                        bFindAction = True
                        break

                if not bFindAction:
                    continue
                categoryLsNode = intentNode.findall('category')
                for categoryNode in categoryLsNode:
                    if categoryNode.attrib[namekey] == 'android.intent.category.LAUNCHER':
                        bFindCategory = True
                        break

                if bFindAction and bFindCategory:
                    icon = activityNode.attrib.get(key)
                    break

    if icon is None:
        icon = applicationNode.attrib.get(key)
    if icon is None:
        icon = '@drawable/ic_launcher'
        applicationNode.attrib[key] = icon
        targetTree.write(manifestFile, 'UTF-8')
    iconName = 'ic_launcher'
    idxDrawable = icon.find('@drawable')
    if idxDrawable != -1:
        iconName = icon[idxDrawable + 10:]
#     resDir = decompileDir + '/res'
#     iconCopytoDrawable(os.path.join(resDir, 'drawable'), os.path.join(iconPath, 'icon48x48.png'), iconName)
#     iconCopytoDrawable(os.path.join(resDir, 'drawable-ldpi'), os.path.join(iconPath, 'icon36x36.png'), iconName)
#     iconCopytoDrawable(os.path.join(resDir, 'drawable-mdpi'), os.path.join(iconPath, 'icon48x48.png'), iconName)
#     iconCopytoDrawable(os.path.join(resDir, 'drawable-hdpi'), os.path.join(iconPath, 'icon72x72.png'), iconName)
#     iconCopytoDrawable(os.path.join(resDir, 'drawable-xhdpi'), os.path.join(iconPath, 'icon96x96.png'), iconName)
#     iconCopytoDrawable(os.path.join(resDir, 'drawable-xxhdpi'), os.path.join(iconPath, 'icon144x144.png'), iconName)
#     if os.path.exists(os.path.join(resDir, 'drawable-xxxhdpi')):
#         iconCopytoDrawable(os.path.join(resDir, 'drawable-xxxhdpi'), os.path.join(iconPath, 'icon192x192.png'), iconName)
    
    appendChannelIconMark(iconName,decompileDir)


def appendIconMark(imgIcon, imgMark, position):

    """
        将两张同样大小的图片叠加在一起
    """

    if imgIcon.mode != 'RGBA':
        imgIcon = imgIcon.convert('RGBA')

    markLayer = Image.new('RGBA', imgIcon.size, (0,0,0,0))
    markLayer.paste(imgMark, position)

    return Image.composite(markLayer, imgIcon, markLayer)

def appendChannelIconMark(iconName, decompileDir):

    """
        自动给游戏图标加上渠道SDK的角标
    """
#     gameIconPath = file_operate.getFullPath(constant.sdkRelatePath+ConfigParse.shareInstance().getChannelName()) + '/icon/icon.png'
    gameIconPath = file_operate.getFullPath(constant.sdkRelatePath) + '/game_icon/icon.png'
    if not os.path.exists(gameIconPath):
        return 1
    
    useMark = True
    try:
        config = ET.parse(file_operate.getConfigXmlPath())
        root = config.getroot()
        icon = root.find("icon")
        markType = icon.get("markType")
    except Exception,e:
        print e
        useMark = False
    
    rlImg = Image.open(gameIconPath)
    
    if useMark:
        markName = 'right-bottom'
        if markType == 'rb':
            markName = 'right-bottom'
        elif markType == 'rt':
            markName = 'right-top'
        elif markType == 'lt':
            markName = 'left-top'
        elif markType == 'lb':
            markName = 'left-bottom'

        markPath = file_operate.getFullPath(constant.sdkRelatePath+ConfigParse.shareInstance().getChannelName()) + '/icon_marks/'+markName+'.png'
        if not os.path.exists(markPath):
            return 1
        else:
            markIcon = Image.open(markPath)
            rlImg = appendIconMark(rlImg, markIcon, (0, 0))
#             rlImg.show()

    ldpiSize = (36, 36)
    mdpiSize = (48, 48)
    hdpiSize = (72, 72)
    xhdpiSize = (96, 96)
    xxhdpiSize = (144,144)
    xxxhdpiSize = (512,512)
    
    drawableIcon = rlImg.resize(mdpiSize, Image.ANTIALIAS)
    ldpiIcon = rlImg.resize(ldpiSize, Image.ANTIALIAS)
    mdpiIcon = rlImg.resize(mdpiSize, Image.ANTIALIAS)
    hdpiIcon = rlImg.resize(hdpiSize, Image.ANTIALIAS)
    xhdpiIcon = rlImg.resize(xhdpiSize, Image.ANTIALIAS)
    xxhdpiIcon = rlImg.resize(xxhdpiSize, Image.ANTIALIAS)
    xxxhdpiIcon = rlImg.resize(xxxhdpiSize, Image.ANTIALIAS)
    
    drawablePath = file_operate.getFullPath(decompileDir + '/res/drawable')
    ldpiPath = file_operate.getFullPath(decompileDir + '/res/drawable-ldpi')
    mdpiPath = file_operate.getFullPath(decompileDir + '/res/drawable-mdpi')
    hdpiPath = file_operate.getFullPath(decompileDir + '/res/drawable-hdpi')
    xhdpiPath = file_operate.getFullPath(decompileDir + '/res/drawable-xhdpi')
    xxhdpiPath = file_operate.getFullPath(decompileDir + '/res/drawable-xxhdpi')
    xxxhdpiPath = file_operate.getFullPath(decompileDir + '/res/drawable-xxxhdpi')
    
    if not os.path.exists(drawablePath):
        os.makedirs(drawablePath)
    
    if not os.path.exists(ldpiPath):
        os.makedirs(ldpiPath)

    if not os.path.exists(mdpiPath):
        os.makedirs(mdpiPath)

    if not os.path.exists(hdpiPath):
        os.makedirs(hdpiPath)       

    if not os.path.exists(xhdpiPath):
        os.makedirs(xhdpiPath)  

    if not os.path.exists(xxhdpiPath):
        os.makedirs(xxhdpiPath)
            
    
    gameIconName = iconName + '.png'
    
    drawableIcon.save(os.path.join(drawablePath, gameIconName), 'PNG')
    ldpiIcon.save(os.path.join(ldpiPath, gameIconName), 'PNG' )
    mdpiIcon.save(os.path.join(mdpiPath, gameIconName), 'PNG')
    hdpiIcon.save(os.path.join(hdpiPath, gameIconName), 'PNG')
    xhdpiIcon.save(os.path.join(xhdpiPath, gameIconName), 'PNG')
    xxhdpiIcon.save(os.path.join(xxhdpiPath, gameIconName), 'PNG')
    if os.path.exists(xxxhdpiPath):
        xxxhdpiIcon.save(os.path.join(xxxhdpiPath, gameIconName), 'PNG')
    return 0

def smaliTrans2dex(smaliDir, targetFile):
    smaliDir = file_operate.getFullPath(smaliDir)
    targetFile = file_operate.getFullPath(targetFile)
    smaliFile = file_operate.getToolPath('smali.jar')
    cmd = '"%s" -jar -Xms512m -Xmx512m "%s" "%s" -o "%s"' % (file_operate.getJava(),
     smaliFile,
     smaliDir,
     targetFile)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        error_operate.error(50)
        return 1
    else:
        file_operate.delete_file_folder('file/smali')
        return 0


def addFileToApk(srcfile, apkFile):
    if os.path.exists(srcfile) and os.path.exists(apkFile):
        apkFile = file_operate.getFullPath(apkFile)
        aapt = file_operate.getToolPath('aapt')
        rmcmd = '"%s" remove "%s" "%s"' % (aapt, apkFile, 'classes.dex')
        bReturn = file_operate.execFormatCmd(rmcmd)
        if bReturn:
            error_operate.error(70)
            return 1
        f = zipfile.ZipFile(apkFile, 'a')
        f.write(srcfile, 'classes.dex')
        f.close()
        file_operate.printf('add file:' + srcfile)
        return 0


def addForRootDir(tempApkName, SDKSrcDir):
    f = zipfile.ZipFile(tempApkName, 'a')
    for parent, dirnames, filenames in os.walk(SDKSrcDir + '/ForRootDir'):
        for file in filenames:
            sourceFile = parent + '/' + file
            targetFile = (parent + '/' + file)[len(SDKSrcDir + '/ForRootDir'):]
            f.write(sourceFile, targetFile)

    f.close()


def signApk(apkFile, keyStore, storepassword, keyalias, aliaspassword):
    if not os.path.exists(keyStore):
        print keyStore
        return 0
    apkFile = file_operate.getFullPath(apkFile)
    keyStore = file_operate.getFullPath(keyStore)
    aapt = file_operate.getToolPath('aapt')
    listcmd = '%s list %s' % (aapt, apkFile)
    listcmd = listcmd.encode('gb2312')
    output = os.popen(listcmd).read()
    for filename in output.split('\n'):
        if filename.find('META-INF') == 0:
            rmcmd = '"%s" remove "%s" "%s"' % (aapt, apkFile, filename)
            bReturn = file_operate.execFormatCmd(rmcmd)

    jarsingnCmd = '"%sjarsigner" -keystore "%s" -storepass "%s" -keypass "%s" "%s" "%s" -sigalg SHA1withRSA -digestalg SHA1' % (file_operate.getJavaBinDir(),
     keyStore,
     storepassword,
     aliaspassword,
     apkFile,
     keyalias)
    
    print jarsingnCmd
    ret = file_operate.execFormatCmd(jarsingnCmd)
    if ret:
        error_operate.error(140)
        return 1
    return 0


def alignAPK(tempApkFile, apkFile, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    align = file_operate.getToolPath('zipalign')
    aligncmd = '"%s" -f 4 "%s" "%s"' % (align, tempApkFile, apkFile)
    ret = file_operate.execFormatCmd(aligncmd)
    if ret:
        error_operate.error(250)
        return 1
    return 0


def decompileApk(apkFile, targetDir, apkTool = 'apktool2.jar'):
    """
        Decompile apk
    """
    apkFile = file_operate.getFullPath(apkFile)
    targetDir = file_operate.getFullPath(targetDir)
    apkTool = file_operate.getToolPath(apkTool)
    if os.path.exists(targetDir):
        file_operate.delete_file_folder(targetDir)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    
    cmd = '"%s" -jar -Xms512m -Xmx512m "%s" -q d -b -f "%s" -o "%s"' % (file_operate.getJava(),
     apkTool,
     apkFile,
     targetDir)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        error_operate.error(80)
        return 1
    else:
        return 0


def recompileApk(srcFolder, apkFile, apkTool = 'apktool2.jar'):
    """
        recompile Apk after decompile apk.
    """
    os.chdir(file_operate.curDir)
    apkFile = file_operate.getFullPath(apkFile)
    srcFolder = file_operate.getFullPath(srcFolder)
    apkTool = file_operate.getToolPath(apkTool)
    print "apkTool" + apkTool
    print "java" + file_operate.getJava()
    if os.path.exists(srcFolder):
        cmd = '"%s" -jar -Xms512m -Xmx512m "%s" -q b -f "%s" -o "%s"' % (file_operate.getJava(),
         apkTool,
         srcFolder,
         apkFile)
        ret = file_operate.execFormatCmd(cmd)
        if ret:
            error_operate.error(130)
            return 1
        else:
            return 0

def renameApkPackage(smaliFolder = 'file/decompile/smali', manifest = 'file/decompile/AndroidManifest.xml', newPackageName="com.zzw.noName"):
    """
        rename apk package name.
    """
    manifest = file_operate.getFullPath(manifest)
    ET.register_namespace('android', androidNS)
    targetTree = ET.parse(manifest)
    root = targetTree.getroot()
    bRet = False
    package = root.attrib.get('package')
    old_package = package
    applicationNode = root.find('application')
    if applicationNode != None:
        activityLs = applicationNode.findall('activity')
        key = '{' + androidNS + '}name'
        if activityLs != None and len(activityLs) > 0:
            for node in activityLs:
                activityName = node.attrib[key]
                if activityName[0:1] == '.':
                    activityName = old_package + activityName
                elif activityName.find('.') == -1:
                    activityName = old_package + '.' + activityName
                node.attrib[key] = activityName

        serviceLs = applicationNode.findall('service')
        key = '{' + androidNS + '}name'
        if serviceLs != None and len(serviceLs) > 0:
            for node in serviceLs:
                serviceName = node.attrib[key]
                if serviceName[0:1] == '.':
                    serviceName = old_package + serviceName
                elif serviceName.find('.') == -1:
                    serviceName = old_package + '.' + serviceName
                node.attrib[key] = serviceName

    root.attrib['package'] = newPackageName
    targetTree.write(manifest, 'UTF-8')
    return newPackageName


def packResIntoApk(SDKWorkDir, SDK, decompileDir, packageName, usrSDKConfig):
    SDKDir = SDKWorkDir + SDK['SDKName']
    for child in SDK['operateLs']:
        if child['name'] == 'modifyManifest':
            modifyFrom = child['from']
            modifyTo = child['to']
            if modifyFrom == None and modifyTo == None:
                file_operate.printf('Operate error, Please check your config in funcellconfig.xml')
                error_operate.error(100)
                return 1
            modifyFrom = None.path.join(SDKDir, modifyFrom)
            modifyTo = os.path.join(decompileDir, modifyTo)
            modifyFrom = file_operate.getFullPath(modifyFrom)
            modifyTo = file_operate.getFullPath(modifyTo)
            modifyManifest.modify(modifyTo, modifyFrom, SDK['SDKName'], usrSDKConfig)
            continue
        if child['name'] == 'copy':
            copyFrom = child['from']
            copyTo = child['to']
            if copyFrom == None and copyTo == None:
                file_operate.printf('Operate error, Please check your config in funcellconfig.xml')
                error_operate.error(101)
                return 1
            copyFrom = None.path.join(SDKDir, copyFrom)
            copyFrom = file_operate.getFullPath(copyFrom)
            copyTo = os.path.join(decompileDir, copyTo)
            copyTo = file_operate.getFullPath(copyTo)
            copyResToApk(copyFrom, copyTo)
            if child['to'] == 'lib':
                armPath = os.path.join(copyFrom, 'armeabi')
                armv7To = os.path.join(copyTo, 'armeabi-v7a')
                if os.path.exists(armPath) and os.path.exists(armv7To):
                    copyResToApk(armPath, armv7To)
                
            
        if child['name'] == 'script':
            scriptPath = SDKDir + '/script.pyc'
            if os.path.exists(scriptPath):
                sys.path.append(SDKDir)
                import script
                script.script(SDK, decompileDir, packageName, usrSDKConfig)
                del sys.modules['script']
                sys.path.remove(SDKDir)
            
    return 0


def copyResToApk(copyFrom, copyTo):
    if not os.path.exists(copyFrom) and not os.path.exists(copyTo):
        file_operate.printf('copy Files from %s to %s Fail:file not found' % (copyFrom, copyTo))
        return
    if os.path.isfile(copyFrom):
        if not appendResXml(copyFrom, copyTo):
            file_operate.copyFile(copyFrom, copyTo)
        return
    for file in os.listdir(copyFrom):
        sourceFile = os.path.join(copyFrom, file)
        targetFile = os.path.join(copyTo, file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(copyTo):
                os.makedirs(copyTo)
            if appendResXml(sourceFile, targetFile):
                continue
            if not os.path.exists(targetFile) or os.path.exists(targetFile) and os.path.getsize(targetFile) != os.path.getsize(sourceFile):
                targetFileHandle = open(targetFile, 'wb')
                sourceFileHandle = open(sourceFile, 'rb')
                targetFileHandle.write(sourceFileHandle.read())
                targetFileHandle.close()
                sourceFileHandle.close()
        if os.path.isdir(sourceFile):
            copyResToApk(sourceFile, targetFile)


def appendResXml(copyFrom, copyTo):
    """
        1.strings.xml
        2.styles.xml
        3.colors.xml
        4.dimens.xml
        5.ids.xml
        6.attrs.xml
        7.integers.xml
        8.arrays.xml
        9.bools.xml
        10.drawables.xml
    """
    basename = os.path.basename(copyFrom)
    if not os.path.exists(copyTo):
        return False
    aryXml = ['strings.xml',
     'styles.xml',
     'colors.xml',
     'dimens.xml',
     'ids.xml',
     'attrs.xml',
     'integers.xml',
     'arrays.xml',
     'bools.xml',
     'drawables.xml']
    if basename == 'strings.xml' or basename == 'styles.xml' or basename == 'colors.xml' or basename == 'dimens.xml' or basename == 'ids.xml' or basename == 'attrs.xml' or basename == 'integers.xml' or basename == 'arrays.xml':
        copyToTree = ET.parse(copyTo)
        copyToRoot = copyToTree.getroot()
        copyFromTree = ET.parse(copyFrom)
        copyFromRoot = copyFromTree.getroot()
        for node in list(copyFromRoot):
            copyToRoot.append(node)

        copyToTree.write(copyTo, 'UTF-8')
        return True
    return False


def produceNewRFile(packName, decompileFullDir, androidManiFest = 'AndroidManifest.xml'):
    """
        According to the merger of resources to create new R file
    """
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
    srcManifest = os.path.join(fullPath, androidManiFest)
    aaptPath = file_operate.getToolPath('aapt')
    cmd = '"%s" p -f -m -J "%s" -S "%s" -I "%s" -M "%s"' % (aaptPath,
     genPath,
     targetResPath,
     androidPath,
     srcManifest)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        error_operate.error(102)
        return 1
    RPath = packName.replace('.', '/')
    RPath = os.path.join(genPath, RPath)
    RFile = os.path.join(RPath, 'R.java')
    cmd = '"%sjavac" -source 1.7 -target 1.7 -encoding UTF-8 "%s"' % (file_operate.getJavaBinDir(), RFile)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        error_operate.error(103)
        return 1
    
    #针对某系渠道通过R。xx来获取资源，在指定包名下添加R文件
    try:         
        config = ET.parse(file_operate.getConfigXmlPath())
        root = config.getroot()
        Manifest = root.find("Manifest")
        num = int(Manifest.get('num'))
        for i in range(0,num):
            srcManifest_i = os.path.join(file_operate.getFullPath(constant.tmpPath), 'Manifest/'+str(i)+'/AndroidManifest.xml')
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
        print "Error: cannot parse file: funcellconfig.xml."
        
    ################################
    
    dexPath = os.path.join(tempPath, 'class.dex')
    if platform.system() == 'Windows':
        dxTool = file_operate.getToolPath('dx.bat')
    else:
        dxTool = file_operate.getToolPath('dx')
    cmd = '"%s" --dex --output="%s" "%s"' % (dxTool, dexPath, genPath)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        error_operate.error(104)
        return 1
    smaliPath = os.path.join(fullPath, 'smali')
    ret = dexTrans2Smali(dexPath, smaliPath, 10)
    if ret:
        return 1
    else:
        return 0


def configDeveloperInfo(channel, SDK, usrSDKConfig, decompileDir, privateKey):
    ret = generateDeveloperInfo(channel, SDK, usrSDKConfig, decompileDir, privateKey)
    if ret:
        return 1
    ret = generatePluginInfo(SDK, usrSDKConfig, decompileDir)
    if ret:
        return 1
    writeDeveloperIntoManifest(SDK, usrSDKConfig, decompileDir)
    return 0


def writeChannelInfoIntoDevelopInfo(decompileDir, channel, privateKey):
    """
        the infomation about channel would configure here
    """
    assetsDir = decompileDir + '/assets'
    developerFile = assetsDir + '/developerInfo.xml'
    if not os.path.exists(assetsDir):
        os.makedirs(assetsDir)
    targetTree = None
    targetRoot = None
    if not os.path.exists(developerFile):
        targetTree = ElementTree()
        targetRoot = Element('developer')
        targetTree._setroot(targetRoot)
    else:
        targetTree = ET.parse(developerFile)
        targetRoot = targetTree.getroot()
    infoNode = targetRoot.find('channel')
    if infoNode is None:
        infoNode = SubElement(targetRoot, 'channel')
    if infoNode.get('idChannel') is None:
        infoNode.set('idChannel', str(channel['channelNum']))
        infoNode.set('uApiKey', channel['uapiKey'])
        infoNode.set('uApiSecret', channel['uapiSecret'])
        infoNode.set('oauthLoginServer', channel['oauthLoginServer'])
        if channel['extChannel'] is not None:
            infoNode.set('extChannel', channel['extChannel'])
        infoNode.set('privateKey', privateKey)
    targetTree.write(developerFile, 'UTF-8')
    file_operate.printf("Save channel's information to developerInfo.xml success")


def generateDeveloperInfo(channel, SDK, usrSDKConfig, decompileDir, privateKey):
    """the infomation about developer would configure here
       the value of element's attribute cann't be int
    """
    assetsDir = decompileDir + '/assets'
    developerFile = assetsDir + '/developerInfo.xml'
    if not os.path.exists(assetsDir):
        os.makedirs(assetsDir)
    targetTree = None
    targetRoot = None
    if not os.path.exists(developerFile):
        targetTree = ElementTree()
        targetRoot = Element('developer')
        targetTree._setroot(targetRoot)
    else:
        targetTree = ET.parse(developerFile)
        targetRoot = targetTree.getroot()
    infoNode = targetRoot.find('channel')
    if infoNode is None:
        infoNode = SubElement(targetRoot, 'channel')
    if infoNode.get('idChannel') is None:
        infoNode.set('idChannel', str(channel['channelNum']))
        infoNode.set('uApiKey', channel['uapiKey'])
        infoNode.set('uApiSecret', channel['uapiSecret'])
        infoNode.set('oauthLoginServer', channel['oauthLoginServer'])
        if channel['extChannel'] is not None:
            infoNode.set('extChannel', channel['extChannel'])
        infoNode.set('privateKey', privateKey)
    if SDK.get('showVersion') is not None:
        attrName = SDK['SDKName'] + '_Version'
        infoNode.set(attrName, SDK['showVersion'])
    for param in usrSDKConfig['param']:
        if param['bWriteIntoClient'] and not param['bWriteIntoManifest']:
            paramName = param['name']
            pos = paramName.find('##')
            if pos != -1:
                paramName = paramName[pos + 2:]
            if paramName.count('Orientation') > 0:
                infoNode.set(paramName, modifyManifest.getOrientation(decompileDir + '/AndroidManifest.xml', usrSDKConfig))
            else:
                infoNode.set(paramName, param['value'])

    targetTree.write(developerFile, 'UTF-8')
    file_operate.printf('generate developerInfo.xml success')


def generatePluginInfo(SDK, usrSDKConfig, decompileDir):
    """the infomation about Plugin would configure here"""
    assetsDir = decompileDir + '/assets'
    if not os.path.exists(assetsDir):
        os.makedirs(assetsDir)
    PluginFile = assetsDir + '/supportPlugin.xml'
    targetTree = None
    targetRoot = None
    pluginLsNode = None
    if not os.path.exists(PluginFile):
        targetTree = ElementTree()
        targetRoot = Element('support')
        targetTree._setroot(targetRoot)
    else:
        targetTree = ET.parse(PluginFile)
        targetRoot = targetTree.getroot()
    for plugin in SDK['pluginLs']:
        type = plugin['typePlugin']
        typeTag = '<plugin>'
        if type == 0:
            typeTag = 'user_plugin'
            if not usrSDKConfig['type'] & 32:
                continue
        elif type == 1:
            typeTag = 'ads_plugin'
            if not usrSDKConfig['type'] & 16:
                continue
        elif type == 2:
            typeTag = 'iap_plugin'
            if not usrSDKConfig['type'] & 8:
                continue
        elif type == 3:
            typeTag = 'social_plugin'
            if not usrSDKConfig['type'] & 4:
                continue
        elif type == 4:
            typeTag = 'share_plugin'
            if not usrSDKConfig['type'] & 2:
                continue
        elif type == 5:
            typeTag = 'analytics_plugin'
            if not usrSDKConfig['type'] & 1:
                continue
        elif type == 6:
            typeTag = 'push_plugin'
            if not usrSDKConfig['type'] & 64:
                continue
        pluginName = plugin['name']
        if pluginName is None:
            file_operate.printf('pluginName error')
            error_operate.error(109)
            return 1
        pluginLsNode = targetRoot.find(typeTag)
        if pluginLsNode is not None:
            for plugin in pluginLsNode.getchildren():
                if plugin.text == pluginName:
                    pluginLsNode.remove(plugin)

        if pluginLsNode is None:
            pluginLsNode = SubElement(targetRoot, typeTag)
        paramNode = SubElement(pluginLsNode, 'param')
        paramNode.text = pluginName
        paramNode.set('name', SDK['SDKName'])

    targetTree.write(PluginFile, 'UTF-8')
    file_operate.printf('generate supportPlugin.xml success')
    return 0

def copyMetaDataToAndroidManifest(configFile, manifestFile):
    
    ET.register_namespace('android', androidNS)
    configTree = ET.parse(configFile)
    configRoot = configTree.getroot()
    metaConfig = configRoot.find("metaconfig")
    if metaConfig is None:
        return
    metaConfigList = metaConfig.findall("meta-data")
    
    targetTree = ET.parse(manifestFile)
    targetRoot = targetTree.getroot()
    key = '{' + androidNS + '}name'
    value = '{' + androidNS + '}value'
    applicationNode = targetRoot.find('application')
    if applicationNode is None:
        error_operate.error(110)
        return
    metaListNode = applicationNode.findall('meta-data')
    for metaNode in metaListNode:
        name = metaNode.attrib[key]
        for child in metaConfigList:
            if child.attrib[key] == name:
                metaListNode.remove(metaNode)

    for child in metaConfigList:
        metaNode = SubElement(applicationNode, "meta-data")
        metaNode.set(key, child.attrib[key])
        metaNode.set(value, child.attrib[value])

    targetTree.write(manifestFile, 'UTF-8')
    file_operate.printf('write funcellconfig.xml meta-data into AndroidManifest.xml success')

def writeDeveloperIntoManifest(SDK, usrSDKConfig, decompileDir):
    """"""
    manifestFile = decompileDir + '/AndroidManifest.xml'
    ET.register_namespace('android', androidNS)
    targetTree = ET.parse(manifestFile)
    targetRoot = targetTree.getroot()
    key = '{' + androidNS + '}name'
    value = '{' + androidNS + '}value'
    applicationNode = targetRoot.find('application')
    if applicationNode is None:
        error_operate.error(110)
        return
    metaListNode = applicationNode.findall('meta-data')
    for metaNode in metaListNode:
        name = metaNode.attrib[key]
        for child in usrSDKConfig['param']:
            if child['name'] == name and child['bWriteIntoManifest'] == 1:
                metaListNode.remove(metaNode)

    for child in usrSDKConfig['param']:
        if child['bWriteIntoClient']:
            if child['bWriteIntoManifest'] is not None and child['bWriteIntoManifest'] == 1:
                metaNode = SubElement(applicationNode, 'meta-data')
                metaNode.set(key, child['name'])
                metaNode.set(value, child['value'])

    targetTree.write(manifestFile, 'UTF-8')
    file_operate.printf('write Developer Infomation into AndroidManifest.xml success')

def addSplashScreen(splashSDKName, decompileDir):
    """ add splash screen
        channel hasn't Splash if channel["bHasSplash"] = 0
        otherwise channel["bHasSplash"] express orientation and color
    """
    channelHasSplash ="0";
    try:         
        #read has splash to funcellconfig.xml
        config = ET.parse(file_operate.getConfigXmlPath())
        root = config.getroot()
        splash = root.find("splash")
        channelHasSplash = splash.get('hasSplash');
            
    except Exception,e:
        print e
        print "Error: cannot parse file: funcellconfig.xml."
        
    print 'channelHasSplash = '+channelHasSplash
    if channelHasSplash == "0":
        return (0, False)
    SplashPath = decompileDir + '/ForSplash/' + channelHasSplash + '/'
    SplashPath = file_operate.getFullPath(SplashPath)
    print "SplashPath : "+SplashPath
    SplashCodePath = 'channel/SplashActivity.smali'
    SplashCodePath = file_operate.getFullPath(SplashCodePath)
    print "SplashCodePath : "+SplashCodePath
    SplashCode2Path = 'channel/SplashActivity$1.smali'
    SplashCode2Path = file_operate.getFullPath(SplashCode2Path)
    print "SplashCode2Path : "+SplashCode2Path
    xmlSplashSrc = 'channel/funcell_plugin_splash.xml'
    xmlSplashSrc = file_operate.getFullPath(xmlSplashSrc)
    print "xmlSplashSrc : "+xmlSplashSrc
    if not os.path.exists(SplashPath) or not os.path.exists(SplashCodePath) or not os.path.exists(SplashCode2Path) or not os.path.exists(xmlSplashSrc):
        error_operate.error(111)
        return (1, False)
    codeDir = decompileDir+'/oldApkDir/' + '/smali/com/haowan/funcell/sdk/api/splash'
    newSplashCodePath = codeDir + '/SplashActivity.smali'
    print "newSplashCodePath : "+newSplashCodePath
    file_operate.copyFile(SplashCodePath, newSplashCodePath)
    newSplashCode2Path = codeDir + '/SplashActivity$1.smali'
    file_operate.copyFile(SplashCode2Path, newSplashCode2Path)
    activityName = removeStartActivity(channelHasSplash, decompileDir+'/oldApkDir/')
    modifyManifestForSplash(channelHasSplash, decompileDir+'/oldApkDir/')
    xmlSplashTarget = decompileDir+'/oldApkDir/' + '/res/layout'
    if not os.path.exists(xmlSplashTarget):
        os.mkdir(xmlSplashTarget)
    xmlSplashTarget = xmlSplashTarget + '/funcell_plugin_splash.xml'
    file_operate.copyFile(xmlSplashSrc, xmlSplashTarget)
    resDir = decompileDir +'/oldApkDir/'+ '/res'
    file_operate.copyFiles(SplashPath, resDir)
#     assetsDir = decompileDir + '/assets'
#     developerFile = assetsDir + '/developerInfo.xml'
#     if not os.path.exists(assetsDir):
#         os.makedirs(assetsDir)
#     targetTree = None
#     targetRoot = None
#     if not os.path.exists(developerFile):
#         targetTree = ElementTree()
#         targetRoot = Element('developer')
#         targetTree._setroot(targetRoot)
#     else:
#         targetTree = ET.parse(developerFile)
#         targetRoot = targetTree.getroot()
#     infoNode = targetRoot.find('channel')
#     if infoNode is None:
#         infoNode = SubElement(targetRoot, 'channel')
#     infoNode.set('GameMainActivity', activityName)
#     targetTree.write(developerFile, 'UTF-8')
    print "add splash activity name : "+activityName
    file_operate.modifyFileContent(newSplashCodePath, '.smali', '###FuncellSdk_Start_Activity###', activityName)
    return (0, True)


def removeStartActivity(bHasSplash, decompileDir, bRemove = True):
    """
        if bRemove is True then remove start activity's action and category
        otherwise only return original activity's name
        @return original activity's name.
    """
    manifestFile = decompileDir + '/AndroidManifest.xml'
    ET.register_namespace('android', androidNS)
    key = '{' + androidNS + '}name'
    targetTree = ET.parse(manifestFile)
    targetRoot = targetTree.getroot()
    applicationNode = targetRoot.find('application')
    if applicationNode is None:
        return
    if applicationNode is not None:
        activityLsNode = applicationNode.findall('activity')
    if activityLsNode is None:
        return
    activityName = ''
    for activityNode in activityLsNode:
        bMainActivity = False
        intentLsNode = activityNode.findall('intent-filter')
        if intentLsNode is None:
            return
        for intentNode in intentLsNode:
            bFindAction = False
            bFindCategory = False
            actionLsNode = intentNode.findall('action')
            for actionNode in actionLsNode:
                if actionNode.attrib[key] == 'android.intent.action.MAIN':
                    bFindAction = True
                    break

            if not bFindAction:
                continue
            categoryLsNode = intentNode.findall('category')
            for categoryNode in categoryLsNode:
                if categoryNode.attrib[key] == 'android.intent.category.LAUNCHER':
                    bFindCategory = True
                    break

            if bFindAction and bFindCategory:
                if bRemove:
                    intentNode.remove(actionNode)
                    intentNode.remove(categoryNode)
                bMainActivity = True
                break

        if bMainActivity:
            activityName = activityNode.attrib[key]
            break

    targetTree.write(manifestFile, 'UTF-8')
    return activityName


def modifyManifestForSplash(bHasSplash, decompileDir):
    manifestFile = decompileDir + '/AndroidManifest.xml'
    ET.register_namespace('android', androidNS)
    key = '{' + androidNS + '}name'
    screenkey = '{' + androidNS + '}screenOrientation'
    theme = '{' + androidNS + '}theme'
    targetTree = ET.parse(manifestFile)
    targetRoot = targetTree.getroot()
    applicationNode = targetRoot.find('application')
    if applicationNode is None:
        return
    if applicationNode is not None:
        activityLsNode = applicationNode.findall('activity')
    if activityLsNode is None:
        return
    splashNode = None
    for actNode in activityLsNode:
        actName = actNode.attrib.get(key)
        if actName is None:
            continue
        if actName == 'com.haowan.funcell.sdk.api.splash.SplashActivity':
            splashNode = actNode
            break

    if splashNode == None:
        splashNode = SubElement(applicationNode, 'activity')
        splashNode.set(key, 'com.haowan.funcell.sdk.api.splash.SplashActivity')
    splashNode.set(theme, '@android:style/Theme.Black.NoTitleBar.Fullscreen')
    strSplashType = str(bHasSplash)
    if strSplashType[:1] == '1':
        splashNode.set(screenkey, 'landscape')
    else:
        splashNode.set(screenkey, 'portrait')
    intNode = splashNode.find('intent-filter')
    if intNode is None:
        intNode = SubElement(splashNode, 'intent-filter')
        actionNode = SubElement(intNode, 'action')
        actionNode.set(key, 'android.intent.action.MAIN')
        intentNode = SubElement(intNode, 'category')
        intentNode.set(key, 'android.intent.category.LAUNCHER')
    else:
        actionLsNode = intNode.findall('action')
        bFindAction = False
        for actionNode in actionLsNode:
            if actionNode.attrib[key] == 'android.intent.action.MAIN':
                bFindAction = True
                break

        if not bFindAction:
            actionNode = SubElement(intNode, 'action')
            actionNode.set(key, 'android.intent.action.MAIN')
        bFindCategory = False
        categoryLsNode = intNode.findall('category')
        for categoryNode in categoryLsNode:
            if categoryNode.attrib[key] == 'android.intent.category.LAUNCHER':
                bFindCategory = True
                break

        if not bFindCategory:
            intentNode = SubElement(intNode, 'category')
            intentNode.set(key, 'android.intent.category.LAUNCHER')
    targetTree.write(manifestFile, 'UTF-8')


def delUselessResource(decompileDir):
    if os.path.exists(decompileDir + '/res/values/public.xml'):
        os.remove(decompileDir + '/res/values/public.xml')
    if os.path.exists(decompileDir + '/res/drawable/btn_close.png'):
        os.remove(decompileDir + '/res/drawable/btn_close.png')
    if os.path.exists(decompileDir + '/res/drawable/ui_ad.png'):
        os.remove(decompileDir + '/res/drawable/ui_ad.png')
    if os.path.exists(decompileDir + '/res/layout/plugin_ads.xml'):
        os.remove(decompileDir + '/res/layout/plugin_ads.xml')
    if os.path.exists(decompileDir + '/res/layout/plugin_login.xml'):
        os.remove(decompileDir + '/res/layout/plugin_login.xml')
    if os.path.exists(decompileDir + '/res/values/plugin_string.xml'):
        os.remove(decompileDir + '/res/values/plugin_string.xml')


def deleteXmlResource(decompileFile):
    if os.path.exists(decompileFile):
        impl = minidom.getDOMImplementation()
        newDom = impl.createDocument(None, 'resources', None)
        newRoot = newDom.documentElement
        doc = minidom.parse(decompileFile)
        rootNode = doc.documentElement
        activityList = rootNode.getElementsByTagName('public')
        for node in activityList:
            if not (node.getAttribute('type') == 'drawable' and node.getAttribute('name') == 'btn_close' or node.getAttribute('type') == 'drawable' and node.getAttribute('name') == 'ui_ad' or node.getAttribute('type') == 'layout' and node.getAttribute('name') == 'plugin_ads' or node.getAttribute('type') == 'layout' and node.getAttribute('name') == 'plugin_login' or node.getAttribute('type') == 'values' and node.getAttribute('name') == 'plugin_string'):
                newPublic = newDom.createElement('public')
                newPublic.setAttribute('type', node.getAttribute('type'))
                newPublic.setAttribute('name', node.getAttribute('name'))
                newPublic.setAttribute('id', node.getAttribute('id'))
                newRoot.appendChild(newPublic)

        f = codecs.open(decompileFile, 'w', 'utf-8')
        newDom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
        f.close()


def modifyGameName(channel, decompileDir):
    config = ET.parse(file_operate.getConfigXmlPath())
    root = config.getroot()
    apktoolYmlPath=decompileDir+'/apktool.yml'
    newapktoolYmlPath=decompileDir+'/apktool.yml.new'
    try:
        game = root.find("game")
        appName = game.get("appName")
        if appName != None:
            StringConfig = ET.parse(decompileDir+'/res/values/strings.xml')
            StringConfigRoot = StringConfig.getroot()
            for StringConfigNode in StringConfigRoot:
                if StringConfigNode.attrib['name']=="app_name" :
                    StringConfigNode.text=unicode(appName)
            StringConfig.write(decompileDir+'/res/values/strings.xml', "utf-8")
    except Exception,e:
        print e
    try:
        game = root.find("game")
        versionCode = game.get("versionCode")
        if versionCode!=None:
            with open(apktoolYmlPath, 'r') as f:
                with open(newapktoolYmlPath, 'w') as g:
                    for line in f.readlines():
                        if 'versionCode' in line:
                            line = "  versionCode: '%s'\n" %versionCode
                        g.write(line)
            shutil.move(newapktoolYmlPath, apktoolYmlPath)
    except Exception,e:
        print e
    try:
        game = root.find("game")
        versionName = game.get("versionName")
        if versionName!=None:
            with open(apktoolYmlPath, 'r') as f:
                with open(newapktoolYmlPath, 'w') as g:
                    for line in f.readlines():
                        if 'versionName' in line:
                            line = "  versionName: '%s'\n" %versionName
                        g.write(line)
            shutil.move(newapktoolYmlPath, apktoolYmlPath)
    except Exception,e:
        print e
        
# addSplashScreen('360', 'F:/funcellsdk/ReleaseSDK/android_pack_talkingdata/packpythonprj/packpythonprj/tmp/oldApkDir')
