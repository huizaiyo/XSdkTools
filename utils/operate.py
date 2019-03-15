# -*- coding: utf-8 -*-
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
import smali_utils
from PIL import Image
import shutil
from taskManagerModule import taskManager
import trimFileTool

sys.path.append('module')
androidNS = 'http://schemas.android.com/apk/res/android'

def dexTrans2Smali(dexFile, targetDir, step, baksmali = 'baksmali.jar'):
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
    if os.path.exists(dexFile):
        dexFile = file_operate.getFullPath(dexFile)
        smaliFile = file_operate.getToolPath(baksmali)
        targetDir = file_operate.getFullPath(targetDir)
#         taskManager.shareInstance().getLock().acquire()
        cmd = '"%s" -jar -Xms512m -Xmx1024m "%s" -o "%s" "%s"' % (file_operate.getJava(),
         smaliFile,
         targetDir,
         dexFile)
        ret = file_operate.execFormatCmd(cmd)
#         taskManager.shareInstance().getLock().release()
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
        
def pushIconIntoApk(iconPath, decompileDir,channel):
    
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
    
    appendChannelIconMark(iconName,decompileDir,channel)


def appendIconMark(imgIcon, imgMark, position):

    """
        将两张同样大小的图片叠加在一起
    """

    if imgIcon.mode != 'RGBA':
        imgIcon = imgIcon.convert('RGBA')

    markLayer = Image.new('RGBA', imgIcon.size, (0,0,0,0))
    markLayer.paste(imgMark, position)

    return Image.composite(markLayer, imgIcon, markLayer)

def appendChannelIconMark(iconName, decompileDir,channel):

    """
        自动给游戏图标加上渠道SDK的角标
    """
    gameIconPath = file_operate.getFullPath(constant.sdkRelatePath+channel) + '/icon/icon.png'
#     gameIconPath = file_operate.getFullPath(constant.sdkRelatePath) + '/icon/icon.png'
    if not os.path.exists(gameIconPath):
        return 1
    
#     useMark = True
#     try:
# #         config = ET.parse(file_operate.getConfigXmlPath())
#         config = ET.parse(file_operate.getchannelFuncellConfigXmlPath(channel))
#         root = config.getroot()
#         icon = root.find("icon")
#         markType = icon.get("markType")
#     except Exception,e:
#         print e
#         useMark = False
    
    rlImg = Image.open(gameIconPath)
    
#     if useMark:
#         markName = 'right-bottom'
#         if markType == 'rb':
#             markName = 'right-bottom'
#         elif markType == 'rt':
#             markName = 'right-top'
#         elif markType == 'lt':
#             markName = 'left-top'
#         elif markType == 'lb':
#             markName = 'left-bottom'
# 
#         if channel==None:
#             markPath = file_operate.getFullPath(constant.sdkRelatePath+ConfigParse.shareInstance().getChannelName()) + '/icon_marks/'+markName+'.png'
#         else:
#             markPath = file_operate.getFullPath(constant.sdkRelatePath+channel) + '/icon_marks/'+markName+'.png'
#         if not os.path.exists(markPath):
#             return 1
#         else:
#             markIcon = Image.open(markPath)
#             rlImg = appendIconMark(rlImg, markIcon, (0, 0))
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
    
    drawable_hdpi_v4 = file_operate.getFullPath(decompileDir + '/res/drawable-hdpi-v4')
    drawable_ldpi_v4 = file_operate.getFullPath(decompileDir + '/res/drawable-ldpi-v4')
    drawable_mdpi_v4 = file_operate.getFullPath(decompileDir + '/res/drawable-mdpi-v4')
    drawable_xhdpi_v4 = file_operate.getFullPath(decompileDir + '/res/drawable-xhdpi-v4')
    drawable_xxhdpi_v4 = file_operate.getFullPath(decompileDir + '/res/drawable-xxhdpi-v4')
    drawable_xxxhdpi_v4 = file_operate.getFullPath(decompileDir + '/res/drawable-xxxhdpi-v4')
    
    gameIconName = iconName + '.png'
    
    #apktool版本为2.1.1后，反编译的资源文件夹默认带有v4,和以前2.0版本apktool反编译文件夹资源不一样，2.0版本不带v4标志
    #有奇葩引擎解包后不包含v4后缀，将icon保存到不带后缀的目录
    if os.path.exists(drawablePath):
        drawableIcon.save(os.path.join(drawablePath, gameIconName), 'PNG')
        
    if os.path.exists(drawable_hdpi_v4) and os.path.exists(drawable_hdpi_v4+'/'+gameIconName):
        hdpiIcon.save(os.path.join(drawable_hdpi_v4, gameIconName), 'PNG')
    else:
        if os.path.exists(hdpiPath) and os.path.exists(hdpiPath+'/'+gameIconName):
            hdpiIcon.save(os.path.join(hdpiPath, gameIconName), 'PNG')
            
    if os.path.exists(drawable_ldpi_v4) and os.path.exists(drawable_ldpi_v4+'/'+gameIconName):
        ldpiIcon.save(os.path.join(drawable_ldpi_v4, gameIconName), 'PNG' )
    else:
        if os.path.exists(ldpiPath) and os.path.exists(ldpiPath+'/'+gameIconName):
            ldpiIcon.save(os.path.join(ldpiPath, gameIconName), 'PNG' )
            
    if os.path.exists(drawable_mdpi_v4) and os.path.exists(drawable_mdpi_v4+'/'+gameIconName):
        mdpiIcon.save(os.path.join(drawable_mdpi_v4, gameIconName), 'PNG')
    else:
        if os.path.exists(mdpiPath) and os.path.exists(mdpiPath+'/'+gameIconName):
            mdpiIcon.save(os.path.join(mdpiPath, gameIconName), 'PNG')
    
    if os.path.exists(drawable_xhdpi_v4) and os.path.exists(drawable_xhdpi_v4+'/'+gameIconName):
        xhdpiIcon.save(os.path.join(drawable_xhdpi_v4, gameIconName), 'PNG')
    else:
        if os.path.exists(xhdpiPath) and os.path.exists(xhdpiPath+'/'+gameIconName):
            xhdpiIcon.save(os.path.join(xhdpiPath, gameIconName), 'PNG')
    
    if os.path.exists(drawable_xxhdpi_v4) and os.path.exists(drawable_xxhdpi_v4+'/'+gameIconName):
        xxhdpiIcon.save(os.path.join(drawable_xxhdpi_v4, gameIconName), 'PNG')
    else:
        if os.path.exists(xxhdpiPath) and os.path.exists(xxhdpiPath+'/'+gameIconName):
            xxhdpiIcon.save(os.path.join(xxhdpiPath, gameIconName), 'PNG')
    
    if os.path.exists(drawable_xxxhdpi_v4) and os.path.exists(drawable_xxxhdpi_v4+'/'+gameIconName):
        xxxhdpiIcon.save(os.path.join(drawable_xxxhdpi_v4, gameIconName), 'PNG')
    else:
        if os.path.exists(xxxhdpiPath) and os.path.exists(xxxhdpiPath+'/'+gameIconName):
            xxxhdpiIcon.save(os.path.join(xxxhdpiPath, gameIconName), 'PNG')
        
    return 0

def smaliTrans2dex(smaliDir, targetFile):
    smaliDir = file_operate.getFullPath(smaliDir)
    targetFile = file_operate.getFullPath(targetFile)
    smaliFile = file_operate.getToolPath('smali.jar')
    cmd = '"%s" -jar -Xms512m -Xmx1024m "%s" "%s" -o "%s"' % (file_operate.getJava(),
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
#     taskManager.shareInstance().getLock().acquire()
    cmd = '"%s" -jar -Xms512m -Xmx1024m "%s" -q d -b -f "%s" -o "%s"' % (file_operate.getJava(),
     apkTool,
     apkFile,
     targetDir)
    ret = file_operate.execFormatCmd(cmd)
#     taskManager.shareInstance().getLock().release()
    if ret:
        error_operate.error(80)
        return 1
    else:
        return 0


def modifyV4dir():
    pass


def decompileApk_android(apkFile, targetDir, lock, apkTool = 'apktool2.jar'):
    """
        Decompile apk
    """
    apkFile = file_operate.getFullPath(apkFile)
    targetDir = file_operate.getFullPath(targetDir)
    apkTool = file_operate.getToolPath(apkTool)
    frameworkDir = file_operate.getFullPath(constant.frameworkDir)
    if os.path.exists(targetDir):
        file_operate.delete_file_folder(targetDir)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
#     taskManager.shareInstance().getLock().acquire()
    cmd = '"%s" -jar -Xms512m -Xmx1024m "%s" -q d -b -f "%s" -o "%s" -p "%s"' % (file_operate.getJava(),
     apkTool,
     apkFile,
     targetDir,
     frameworkDir)
    ret = file_operate.execFormatCmd(cmd)
#     taskManager.shareInstance().getLock().release()
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
    frameworkDir = file_operate.getFullPath(constant.frameworkDir)
    print "apkTool" + apkTool
    print "java" + file_operate.getJava()
    if os.path.exists(srcFolder):
#         taskManager.shareInstance().getLock().acquire()ids.xml
        cmd = '"%s" -jar -Xms512m -Xmx1024m "%s" -q b -f "%s" -o "%s" -p "%s"' % (file_operate.getJava(),
         apkTool,
         srcFolder,
         apkFile,
         frameworkDir)
        ret = file_operate.execFormatCmd(cmd)
#         taskManager.shareInstance().getLock().release()
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


def produceNewRFileByAapt2(workDir, genPath, resPath, manifestPath):
    """
        generate R.java with aapt2
    """
    androidPath = file_operate.getToolPath('android.jar')

    if platform.system() == 'Windows':
        aapt2Path = file_operate.getToolPath("aapt2.exe")
    else:
        aapt2Path = file_operate.file_operate("aapt2")

    if not os.path.exists(aapt2Path):
        return False

    #compile res first...
    resFlatPath = workDir + "/res_flat.zip"
    cmd = '"%s" compile -o "%s" --dir "%s" -v' % (aapt2Path, resFlatPath, resPath)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        return False

    #link res to generate R.java
    resTempPath = workDir + "/res.apk"
    cmd = '"%s" link -o "%s" --manifest "%s" -I "%s" --java "%s" "%s" -v' % (aapt2Path, resTempPath, manifestPath, androidPath, genPath, resFlatPath)
    ret = file_operate.execFormatCmd(cmd)

    return ret

def produceNewRFile(channel, packName, decompileFullDir, androidManiFest = 'AndroidManifest.xml'):
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
#     aaptPath = file_operate.getToolPath('aapt2')
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
    if os.path.exists(file_operate.getchannelRConfigXmlPath(channel)):
        try:
            config = ET.parse(file_operate.getchannelRConfigXmlPath(channel))
            root = config.getroot()
            Manifest = root.find("Manifest")
            num = int(Manifest.get('num'))
            for i in range(0,num):
                srcManifest_i = os.path.join(file_operate.getFullPath(constant.tmpPath+'/'+channel), 'Manifest/'+str(i)+'/AndroidManifest.xml')
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
            print "Error: cannot parse file: ForRconfig.xml."
        
    ###################以上方式生成的R文件是每个包名下的R都包含了所有资源文件的引用索引，会生成太多静态字段变量，导致很有可能出现字段65535问题#################
    ###################最好的方式应该是对应包名下R文件中只包含对应的那部分的资源索引值###################
    ###################以下方式生成R文件，每个包名下面只有对应的资源索引值############################
    trimFileTool.trim_file(RFile)
    generateExtendRFile(os.path.dirname(decompileFullDir)+"/ExtendR",RFile,genPath,channel)
    #############################################

    dexPath = os.path.join(tempPath, 'class.dex')
    if platform.system() == 'Windows':
#         dxTool = file_operate.getToolPath('dx.bat')
        dxTool = file_operate.getFullPath('tool/win/lib/dx.jar')
    else:
        dxTool = file_operate.getToolPath('dx')
#     cmd = '"%s" --dex --output="%s" "%s"' % (dxTool, dexPath, genPath)
#     taskManager.shareInstance().getLock().acquire()
    cmd = '"%s" -jar -Xms512m -Xmx1024m "%s" --dex --output="%s" "%s"' % (file_operate.getJava(),dxTool, dexPath, genPath)
    ret = file_operate.execFormatCmd(cmd)
#     taskManager.shareInstance().getLock().release()
    if ret:
        error_operate.error(104)
        return 1
    smaliPath = os.path.join(fullPath, 'smali')
    ret = dexTrans2Smali(dexPath, smaliPath, 10)
    if ret:
        return 1
    else:
        return 0

def generateExtendRFile(ExtendRDir,RFile,genPath,channel):
    if os.path.exists(file_operate.getFullPath(ExtendRDir)):
        RFileds = codecs.open(file_operate.getFullPath(RFile), 'r', 'utf-8')
        RFiledsLines = RFileds.readlines()
        for parent, dirnames, filenames in os.walk(file_operate.getFullPath(ExtendRDir)):
            for filename in filenames:
                srcFilePath = file_operate.getFullPath(os.path.join(parent, filename))
                srcExtendRDirPath = file_operate.getFullPath(ExtendRDir)
                tmpPath = srcFilePath.replace(srcExtendRDirPath,"")
                if "\\" in tmpPath:
                    tmpPath = tmpPath.replace("\\", ".")
                elif "/" in tmpPath:
                    tmpPath = tmpPath.replace("/", ".")
                taskManager.shareInstance().notify(channel.split('/')[0] + '_' + channel.split('/')[1], 84,tmpPath)
                trimFileTool.trim_file(os.path.join(parent, filename))
                bak_file = os.path.join(parent, filename + ".bak")
                file_operate.copyFile(os.path.join(parent, filename), bak_file)
                fp_src = codecs.open(bak_file, 'r', 'utf-8')
                fp_dst = codecs.open(os.path.join(parent, filename), 'w', 'utf-8')
                extend_class_name = ""
                for extend_line in fp_src.readlines():
                    if "public static final class" in extend_line:
                        extend_class_name = extend_line
                        fp_dst.write(extend_line)
                    elif "public static final int" in extend_line:
                        extend_line_dict = extend_line.split('=')
                        if len(extend_line_dict) > 1:
                            if "{" in extend_line_dict[1]:
                                # 当前行为int[] 此逻辑部分为，多行为一个字段，需要判断行开始起点，行结束点
                                _class_name = ""
                                info = ""
                                info_start = "{"
                                info_end = "}"
                                info_end_flag = False
                                info_continue_flag = False
                                info_filed = ""
                                for line in RFiledsLines:
                                    if "public static final class" in line:
                                        _class_name = line
                                    if info_continue_flag == True and info_end in line:
                                        info += line
                                        info_continue_flag = False
                                        fp_dst.write(info)
                                    if info_continue_flag == True and info_end not in line:
                                        info += line
                                        info_continue_flag = True
                                    info_line = line.split('=')
                                    if len(info_line) > 1 and info_start in info_line[1]:
                                        info_filed = info_line[0]
                                        if extend_class_name != "" and _class_name != "" and extend_class_name == _class_name and info_filed.strip() == extend_line_dict[0].strip():
                                            info += line
                                            info_continue_flag = True
                            else:
                                # 当前行为int
                                class_name = ""
                                for line in RFiledsLines:
                                    if "public static final class" in line:
                                        class_name = line
                                    elif "public static final int" in line and len(line.split('=')) > 1 and "{" not in line.split("=")[1]:
                                        if extend_class_name != "" and class_name != "" and extend_class_name == class_name and line.split("=")[0].strip() == extend_line_dict[0].strip():
                                            fp_dst.write(line)
                    else:
                        fp_dst.write(extend_line)
                fp_src.close()
                fp_dst.close()
                file_operate.delete_file_folder(bak_file)
                #编译R.java文件
                cmd = '"%sjavac" -source 1.7 -target 1.7 -encoding UTF-8 "%s"' % (file_operate.getJavaBinDir(), os.path.join(parent, filename))
                ret = file_operate.execFormatCmd(cmd)
                if ret:
                    error_operate.error(103)
                    return 1
        RFileds.close()
        #拷贝当前目录到gen目录下
        file_operate.copyFiles(file_operate.getFullPath(ExtendRDir),genPath)

def jar2dex(sourceDir, targetDir):
    if platform.system() == 'Windows':
        dxTool = file_operate.getToolPath('dx.bat')
    else:
        dxTool = file_operate.getToolPath('dx')
    cmd = '"%s" --dex --output="%s" "%s"' % (dxTool, targetDir+'/classes.dex', sourceDir)
    ret = file_operate.execFormatCmd(cmd)
    if ret:
        error_operate.error(104)
        return 1

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

def addSplashScreen(channel, decompileDir):
    """ add splash screen
        channel hasn't Splash if channel["bHasSplash"] = 0
        otherwise channel["bHasSplash"] express orientation and color
    """
    channelHasSplash ="0";
    try:         
        #read has splash to funcellconfig.xml
        config = ET.parse(file_operate.getchannelFuncellConfigXmlPath(channel))
        root = config.getroot()
#         splash = root.find("splash")
#         channelHasSplash = splash.get('hasSplash');
        
        splashLsNode = root.findall("splash")
        if splashLsNode is not None:
            for splashNode in splashLsNode:
                hasSplashLsNode = splashNode.findall('hasSplash')
                for hasSplashNode in hasSplashLsNode:
                    channelHasSplash = hasSplashNode.text
            
    except Exception,e:
        print e
        print "Error: addSplashScreen."
        
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
    print "add splash activity name : "+activityName
    file_operate.modifyFileContent(newSplashCodePath, '.smali', '###FuncellSdk_Start_Activity###', activityName)
    
    #-------
    copyResToApk(file_operate.getFullPath('channel/ForRes'), resDir)
    productcode = ConfigParse.shareInstance().getProductCode()
    logDir = 'Log/'
    if os.path.exists(logDir + productcode+'/ChannelSettingSplashAndIconFile.log'):
        config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingSplashAndIconFile.log'))
        root = config.getroot()
        channelNode = root.find('channel_'+channel.split('/')[0]+'_'+channel.split('/')[1])
        if channelNode is not None:
            if channelNode.get("checkBoxflag") == "True":
                if len(channelNode.get("splash_time").strip()) > 0: 
                    splash_time = channelNode.get("splash_time")
                    funcellStringConfig = ET.parse(file_operate.getFullPath(resDir+"/values/funcell_splash_strings.xml"))
                    funcellStringConfigRoot = funcellStringConfig.getroot()
                    for funcellStringConfigNode in funcellStringConfigRoot:
                        if funcellStringConfigNode.attrib['name']=="funcell_splash_time" :
                            funcellStringConfigNode.text=splash_time
                    
                    funcellStringConfig.write(file_operate.getFullPath(resDir+"/values/funcell_splash_strings.xml"), "utf-8")
                if len(channelNode.get("splash_fromAlpha").strip()) > 0: 
                    splash_fromAlpha = channelNode.get("splash_fromAlpha")
                    funcellStringConfig = ET.parse(file_operate.getFullPath(resDir+"/values/funcell_splash_strings.xml"))
                    funcellStringConfigRoot = funcellStringConfig.getroot()
                    for funcellStringConfigNode in funcellStringConfigRoot:
                        if funcellStringConfigNode.attrib['name']=="funcell_splash_fromAlpha" :
                            funcellStringConfigNode.text=splash_fromAlpha
                    
                    funcellStringConfig.write(file_operate.getFullPath(resDir+"/values/funcell_splash_strings.xml"), "utf-8")
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
#     if strSplashType[:1] == '1':
    if strSplashType == 'landscape':
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

def rewriteYml(decompileDir):
    needDel = False
    lineNum = []
    old_yml = open(decompileDir +'/apktool.yml','r').readlines()
    for line in old_yml:
        if line == "isFrameworkApk: false\n":
            needDel = False
        if needDel:
            lineNum.append(old_yml.index(line))
        if line == "doNotCompress:\n":
            needDel = True
    
    new_yml = open(decompileDir +'/apktool.yml','w')
    for line in old_yml:
        if old_yml.index(line) not in lineNum:
            new_yml.write(line)
    new_yml.close()


def modifyGameName(channel, decompileDir):
    logDir = 'Log/'
    productcode = ConfigParse.shareInstance().getProductCode()
    apktoolYmlPath=decompileDir+'/apktool.yml'
    newapktoolYmlPath=decompileDir+'/apktool.yml.new'
    if os.path.exists(logDir +productcode+ '/ChannelSettingApkFile.log'):
        config = ET.parse(file_operate.getFullPath(logDir +productcode+ '/ChannelSettingApkFile.log'))
        root = config.getroot()
        channelNode = root.find('channel_'+channel.split('/')[0]+'_'+channel.split('/')[1])
        if channelNode is not None:
            if channelNode.get("checkBoxflag") is not None and channelNode.get("checkBoxflag") == "True":
                if channelNode.get("appName") is not None and len(channelNode.get("appName")) > 0:
                    for parent,dirnames,filenames in os.walk(decompileDir+'/res'):
                        for filename in filenames: 
                            if filename == "strings.xml":
                                print 'modify app_name by %s'%(os.path.join(parent,filename))
                                StringConfig = ET.parse(os.path.join(parent,filename))
                                StringConfigRoot = StringConfig.getroot()
                                for StringConfigNode in StringConfigRoot:
                                    if StringConfigNode.attrib['name']=="app_name" :
                                        StringConfigNode.text=unicode(channelNode.get("appName"))
                                        StringConfig.write(os.path.join(parent,filename), "utf-8")
#                     StringConfig = ET.parse(decompileDir+'/res/values/strings.xml')
#                     StringConfigRoot = StringConfig.getroot()
#                     for StringConfigNode in StringConfigRoot:
#                         if StringConfigNode.attrib['name']=="app_name" :
#                             StringConfigNode.text=unicode(channelNode.get("appName"))
#                     StringConfig.write(decompileDir+'/res/values/strings.xml', "utf-8")
            
                if channelNode.get("versionCode") is not None and len(channelNode.get("versionCode")) > 0:
                    with open(apktoolYmlPath, 'r') as f:
                        with open(newapktoolYmlPath, 'w') as g:
                            for line in f.readlines():
                                if 'versionCode' in line:
                                    line = "  versionCode: '%s'\n" %channelNode.get("versionCode")
                                g.write(line)
                    shutil.move(newapktoolYmlPath, apktoolYmlPath)
                
                if channelNode.get("versionName") is not None and len(channelNode.get("versionName")) > 0:
                    with open(apktoolYmlPath, 'r') as f:
                        with open(newapktoolYmlPath, 'w') as g:
                            for line in f.readlines():
                                if 'versionName' in line:
                                    line = "  versionName: '%s'\n" %channelNode.get("versionName")
                                g.write(line)
                    shutil.move(newapktoolYmlPath, apktoolYmlPath)
                    
                if channelNode.get("minsdkVersion") is not None and len(channelNode.get("minsdkVersion")) > 0:
                    with open(apktoolYmlPath, 'r') as f:
                        with open(newapktoolYmlPath, 'w') as g:
                            for line in f.readlines():
                                if 'minSdkVersion' in line:
                                    line = "  minSdkVersion: '%s'\n"%channelNode.get("minsdkVersion")
                                g.write(line)
                    shutil.move(newapktoolYmlPath, apktoolYmlPath)
                
                if channelNode.get("targetsdkVersion") is not None and len(channelNode.get("targetsdkVersion")) > 0:
                    with open(apktoolYmlPath, 'r') as f:
                        with open(newapktoolYmlPath, 'w') as g:
                            for line in f.readlines():
                                if 'targetSdkVersion' in line:
                                    line = "  targetSdkVersion: '%s'\n"%channelNode.get("targetsdkVersion")
                                g.write(line)
                    shutil.move(newapktoolYmlPath, apktoolYmlPath)
                    
def splitDexByMethod(workDir, decompileDir,dexMaxNum,useFuncellApplicationJarFlag,existsChannelMultidexFile = False,channelMultidexFile = None):
    """
        如果函数上限超过限制，自动拆分smali，以便生成多个dex文件
    """
    
    splitDexFlag=False
    smaliPath = decompileDir + "/smali"
    multidexFilePath = file_operate.getFullPath(smaliPath + "/android/support/multidex/MultiDex.smali")
    targetPath = file_operate.getFullPath(workDir + "/local")
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    if not os.path.exists(multidexFilePath):
        #android-support-multidex.jar不存在，从local下面拷贝，并编译
        dexJar = file_operate.getFullPath('config/local/android-support-multidex.jar')
        if not os.path.exists(dexJar):
            print("android-support-multidex.jar not exists")
            return
        file_operate.copyFiles(dexJar, targetPath+"/android-support-multidex.jar")
        splitDexFlag = True
        
    if useFuncellApplicationJarFlag:
        funcellApplicationFilePath = file_operate.getFullPath('config/local/FuncellApplication.jar')
        if os.path.exists(funcellApplicationFilePath):
            file_operate.copyFiles(funcellApplicationFilePath, targetPath+"/FuncellApplication.jar")
            splitDexFlag = True
    if splitDexFlag:
        jar2dex(targetPath, targetPath)
        smaliPath = file_operate.getFullPath(decompileDir + "/smali")
        ret = dexTrans2Smali(targetPath + '/classes.dex', smaliPath,3)
    
    allFiles = []
    allFiles = file_operate.list_files(smaliPath, allFiles, [])
    
#     maxFuncNum = 65535 #方法数最大值
    maxFuncNum = int(dexMaxNum) #方法数最大值
    currFucNum = 0
    totalFucNum = 0
 
    currDexIndex = 1
    allRefs = []
    
    #保证Application等类在第一个classex.dex文件中
    pattern  = re.compile(".+com/funcell/platform/android/game/proxy/FuncellApplication*")
    for f in allFiles:
        f = f.replace("\\", "/")
#         if "/com/haowan" in f or "/com/haowan123" in f or "/com/funcell123" in f or "/android/support/multidex" in f or "com/android/vending" in f or "com/funcell/platform/android/game/proxy" in f:
        if "/android/support/multidex" in f or "com/android/vending" in f or pattern.match(f):
#             currFucNum = currFucNum + file_operate.get_smali_func_num(f)
            currFucNum = currFucNum + smali_utils.get_smali_method_count(f, allRefs)
        elif existsChannelMultidexFile:
            for rule in channelMultidexFile:
                _pattern = re.compile(rule)
                if _pattern.match(f):
#                     print 'rule:',rule
                    currFucNum = currFucNum + smali_utils.get_smali_method_count(f, allRefs)
    
    for f in allFiles:
        
        f = f.replace("\\", "/")
        if not f.endswith(".smali"):
            continue
 
#         if "/com/haowan" in f or "/com/haowan123" in f or "/com/funcell123" in f or "/android/support/multidex" in f or "com/android/vending" in f or "com/funcell/platform/android/game/proxy" in f:
        if "/android/support/multidex" in f or "com/android/vending" in f or pattern.match(f):
            continue
        elif existsChannelMultidexFile:
            continueFlag = False
            for rule in channelMultidexFile:
                _pattern = re.compile(rule)
                if _pattern.match(f):
#                     print 'rule:',rule
                    continueFlag = True
                    break
            if continueFlag:
                continue
        
        thisFucNum = smali_utils.get_smali_method_count(f, allRefs)
        totalFucNum = totalFucNum + thisFucNum
        if currFucNum + thisFucNum >= maxFuncNum:
            currFucNum = thisFucNum
            currDexIndex = currDexIndex + 1
            newDexPath = os.path.join(decompileDir, "smali_classes"+str(currDexIndex))
            os.makedirs(newDexPath)
        else:
            currFucNum = currFucNum + thisFucNum
 
        if currDexIndex > 1:
            targetPath = f[0:len(decompileDir)] + "/smali_classes"+str(currDexIndex) + f[len(smaliPath):]
            file_operate.copyFiles(f, targetPath)
            file_operate.delete_file_folder(f)
 
    print 'the total func num:%s' %str(totalFucNum)
    print("split dex success. the classes.dex num:"+str(currDexIndex))
    return totalFucNum
# addSplashScreen('360', 'F:/funcellsdk/ReleaseSDK/android_pack_talkingdata/packpythonprj/packpythonprj/tmp/oldApkDir')

def splitDexByField(workDir, decompileDir,dexMaxNum,useFuncellApplicationJarFlag,existsChannelMultidexFile = False,channelMultidexFile = None):
    """
           如果字段上限超过限制，自动拆分smali，以便生成多个dex文件
    """
    splitDexFlag = False
    smaliPath = decompileDir + "/smali"
    multidexFilePath = file_operate.getFullPath(smaliPath + "/android/support/multidex/MultiDex.smali")
    targetPath = file_operate.getFullPath(workDir + "/local")
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    if not os.path.exists(multidexFilePath):
        # android-support-multidex.jar不存在，从local下面拷贝，并编译
        dexJar = file_operate.getFullPath('config/local/android-support-multidex.jar')
        if not os.path.exists(dexJar):
            print("android-support-multidex.jar not exists")
            return
        file_operate.copyFiles(dexJar, targetPath + "/android-support-multidex.jar")
        splitDexFlag = True

    if useFuncellApplicationJarFlag:
        funcellApplicationFilePath = file_operate.getFullPath('config/local/FuncellApplication.jar')
        if os.path.exists(funcellApplicationFilePath):
            file_operate.copyFiles(funcellApplicationFilePath, targetPath + "/FuncellApplication.jar")
            splitDexFlag = True
    if splitDexFlag:
        jar2dex(targetPath, targetPath)
        smaliPath = file_operate.getFullPath(decompileDir + "/smali")
        ret = dexTrans2Smali(targetPath + '/classes.dex', smaliPath, 3)

    allFiles = []
    allFiles = file_operate.list_files(smaliPath, allFiles, [])

    #     maxFuncNum = 65535 #方法数最大值
    maxFuncNum = int(dexMaxNum)  # 方法数最大值
    currFucNum = 0
    totalFucNum = 0

    currDexIndex = 1
    allRefs = []

    #保证Application等类在第一个classex.dex文件中
    pattern  = re.compile(".+com/funcell/platform/android/game/proxy/FuncellApplication*")




def saveChannelSetting_splashToChannelDir(splash,horizontal,channel):
    channelDir = file_operate.getFullPath(constant.sdkRelatePath+channel)
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
    
    img = Image.open(file_operate.getFullPath(splash))
    
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
    
def saveChannelSetting_iconToChannelDir(icon,channel):
    img = Image.open(file_operate.getFullPath(icon))
    if not os.path.exists(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon')):
        os.makedirs(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon'))
    img.save(file_operate.getFullPath(constant.sdkRelatePath+channel+'/icon/icon.png'))
    

def coverCustomSdk(workDir,decompileDir):
    smaliPath = decompileDir + "/smali"
    funcellsdkdexFilePath = file_operate.getFullPath('config/covercustomsdk')
    if os.path.exists(funcellsdkdexFilePath):
        dexJar = file_operate.getFullPath('config/covercustomsdk')
        targetPath = file_operate.getFullPath(workDir + "/covercustomsdk")
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        file_operate.copyFiles(dexJar, targetPath) 
        jar2dex(targetPath, targetPath)
        smaliPath = file_operate.getFullPath(decompileDir + "/smali")
        ret = dexTrans2Smali(targetPath + '/classes.dex', smaliPath,3)
