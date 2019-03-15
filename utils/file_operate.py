# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET
import os
import os.path
import zipfile
import re
import subprocess
import platform
from config import ConfigParse
import inspect
import sys
import codecs
import threading
import time
import error_operate
import constant
from taskManagerModule import taskManager
import hashlib
from os import listdir
from os.path import isfile,isdir,join
import shutil

bPrint = False
curDir = os.getcwd()

def md5hex(word):  
    """ MD5加密算法，返回32位小写16进制符号 
    """   
    if isinstance(word, unicode):  
        word = word.encode("utf-8")  
    elif not isinstance(word, str):  
        word = str(word)
    m = hashlib.md5()  
    m.update(word)  
    return m.hexdigest()  

def md5sum(fname):
    """ 计算文件的MD5值
    """
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else: #最后要将游标放回文件开头
            fh.seek(0)
    m = hashlib.md5()
    if isinstance(fname, basestring) \
        and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    #上传的文件缓存 或 已打开的文件流
    elif fname.__class__.__name__ in ["StringIO", "StringO"] \
        or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()



def list_files(src, resFiles, igoreFiles):

    if os.path.exists(src):

        if os.path.isfile(src) and src not in igoreFiles:
            resFiles.append(src)
        elif os.path.isdir(src):
            for f in os.listdir(src):
                if src not in igoreFiles:
                    list_files(os.path.join(src, f), resFiles, igoreFiles)

    return resFiles

def delete_file_folder(src):
    if os.path.exists(src):
        if os.path.isfile(src):
            try:
                src = src.replace('\\', '/')
                os.remove(src)
            except:
                pass

        elif os.path.isdir(src):
            for item in os.listdir(src):
                itemsrc = os.path.join(src, item)
                delete_file_folder(itemsrc)

            try:
                os.rmdir(src)
            except:
                pass


def copyFiles(sourceDir, targetDir):
    if not os.path.exists(sourceDir) and not os.path.exists(targetDir):
        printf('copy Files from %s to %s Fail:file not found' % (sourceDir, targetDir))
        return
    if os.path.isfile(sourceDir):
        copyFile(sourceDir, targetDir)
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, file)
        targetFile = os.path.join(targetDir, file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            targetFileHandle = open(targetFile, 'wb')
            sourceFileHandle = open(sourceFile, 'rb')
            targetFileHandle.write(sourceFileHandle.read())
            targetFileHandle.close()
            sourceFileHandle.close()
        if os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)


def copyFile(sourceFile, targetFile):
    
    sourceFile = getFullPath(sourceFile)
    targetFile = getFullPath(targetFile)
    if not os.path.exists(sourceFile):
        return
    
    targetDir = os.path.dirname(targetFile)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    targetFileHandle = open(targetFile, 'wb')
    sourceFileHandle = open(sourceFile, 'rb')
    targetFileHandle.write(sourceFileHandle.read())
    targetFileHandle.close()
    sourceFileHandle.close()

def copyBaseApk(sourceFile,targetFile):
    sourceFile = getFullPath(sourceFile)
    targetFile = getFullPath(targetFile)
    if not os.path.exists(sourceFile):
        return
    
    targetDir = os.path.dirname(targetFile)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
    shutil.copyfile(sourceFile,targetFile)
    

def copyApkToZip(filename):
    dotIndex = filename.find('.')
    newfilename = filename
    if dotIndex >= 0 and os.path.exists(filename):
        name = filename[:dotIndex]
        ext = filename[dotIndex:]
        newext = '.zip'
        newfilename = name + newext 
        targetFileHandle = open(newfilename, 'wb')
        sourceFileHandle = open(filename, 'rb')
        targetFileHandle.write(sourceFileHandle.read())
        targetFileHandle.close()
        sourceFileHandle.close()
        printf('copy success')

def unZip(src, dest, apkFile):
    reload(sys)
    sys.setdefaultencoding('gbk')
    src = str(src).decode('utf8')
    dest = str(dest).decode('utf8')
    delete_file_folder(dest)
    if not os.path.exists(dest):
        os.makedirs(dest)
    f = zipfile.ZipFile(src)
    f.extractall(dest)
    f.close()

def decompression(filename,channeldir, unziptodir):
#     delete_file_folder(unziptodir)
    if os.path.exists(channeldir):
        delete_file_folder(channeldir)
    if not os.path.exists(unziptodir):
#         os.mkdir(unziptodir, 511)
        os.makedirs(unziptodir)
    f = zipfile.ZipFile(filename)
    f.extractall(unziptodir)
    print 'decompression success!'
    f.close()
    delete_file_folder(filename)


def getCurDir():
    global curDir
    retPath = curDir
    if platform.system() == 'Windows':
        retPath = retPath.decode('gbk')
    return retPath
    caller_file = inspect.stack()[0][1]
    retPath = os.path.abspath(os.path.dirname(caller_file))
    if platform.system() == 'Windows':
        retPath = retPath.decode('gbk')
    return retPath


def getFullPath(filename):
    if os.path.isabs(filename):
        return filename
    dirname = sys.path[0]
    filename = os.path.join(dirname, filename)
    filename = filename.replace('\\', '/')
    filename = re.sub('/+', '/', filename)
    print filename
    return filename


def getToolPath(filename):
    toolPath = ''
    if platform.system() == 'Darwin':
        toolPath = getFullPath('tool/mac/' + filename)
    else:
        toolPath = getFullPath('tool/win/' + filename)
    return toolPath


def modifyFileContent(source, fileType, oldContent, newContent):
    if os.path.isdir(source):
        for file in os.listdir(source):
            sourceFile = os.path.join(source, file)
            modifyFileContent(sourceFile, fileType, oldContent, newContent)

    elif os.path.isfile(source) and os.path.splitext(source)[1] == fileType:
        f = open(source, 'r+')
        data = str(f.read())
        f.close()
        bRet = False
        idx = data.find(oldContent)
        while idx != -1:
            data = data[:idx] + newContent + data[idx + len(oldContent):]
            idx = data.find(oldContent, idx + len(oldContent))
            bRet = True

        if bRet:
            fhandle = open(source, 'w')
            fhandle.write(data)
            fhandle.close()
            printf('modify file:%s' % source)
        else:
            error_operate.error(108)


def execFormatCmd(cmd):
    cmd = cmd.replace('\\', '/')
    cmd = re.sub('/+', '/', cmd)
    ret = 0
    if platform.system() == 'Windows':
        st = subprocess.STARTUPINFO
        st.dwFlags = subprocess.STARTF_USESHOWWINDOW
        st.wShowWindow = subprocess.SW_HIDE
        cmd = str(cmd).encode('gbk')
    s = subprocess.Popen(cmd, shell=True)
    ret = s.wait()
    if ret:
        s = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdoutput, erroutput = s.communicate()
        reportError(cmd, stdoutput, erroutput)
        cmd = 'ERROR:' + cmd + ' ===>>> exec Fail <<<=== '
    else:
        cmd += ' ===>>> exec success <<<=== '
    printf(cmd)
    return ret


def getApkVersion(apkFile):
    """get the version about apk"""
    cmd = '"' + getToolPath('aapt') + '" d badging "' + apkFile + '"'
    cmd = cmd.replace('\\', '/')
    cmd = re.sub('/+', '/', cmd)
    ret = 0
    if platform.system() == 'Windows':
        st = subprocess.STARTUPINFO
        st.dwFlags = subprocess.STARTF_USESHOWWINDOW
        st.wShowWindow = subprocess.SW_HIDE
        cmd = str(cmd).encode('gbk')
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    info = s.communicate()[0]
    nPos = info.find('versionName')
    nEnd = info.find("'", nPos + 13)
    versionName = info[nPos + 13:nEnd]
    if versionName == '':
        versionName = 'Unknown Version'
    return versionName


def getTargetSdkVersion(deDir):
    xmlPath = deDir + "/AndroidManifest.xml"
    ET.register_namespace('android', constant.androidNS)
    configTree = ET.parse(xmlPath)
    configRoot = configTree.getroot()
    usesSdkNode = configRoot.find("uses-sdk")
    if usesSdkNode != None:
        targetSdkVersion = usesSdkNode.get('{' + constant.androidNS + '}targetSdkVersion')
        if targetSdkVersion != None and len(targetSdkVersion) != 0:
            return int(targetSdkVersion)
        
    return 17 


def backupApk(source):
    outputDir = constant.tmpPath
    backupName = '%s/common.apk' % outputDir
    backupName = getFullPath(backupName)
    print "backupname" + backupName
    
    if os.path.exists(backupName):
        os.remove(backupName)
    
    print "source " +source
    copyFile(source, backupName)


def getJavaBinDir():
    if platform.system() == 'Darwin':
        javaBinDir = ''
        if os.path.exists(os.path.join(curDir, '../tool/mac/jre/bin/')):
            libPath = ':' + os.path.join(curDir, '../tool/mac/jre/bin/')
            print libPath
            os.environ['PATH'] += libPath
        elif os.path.exists('/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Commands/'):
            libPath = ':' + '/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Commands/'
            os.environ['PATH'] += libPath
    else:
        javaBinDir = getFullPath('tool/win/jre/bin/')
        
    print javaBinDir
    
    return javaBinDir

def get_smali_func_num(smaliFile):
 
    if not os.path.exists(smaliFile):
        return 0
 
    f = open(smaliFile)
    lines = f.readlines()
    f.close()
 
    num = 0
    for line in lines:
        if line.startswith(".method"):
            num = num + 1
 
    return num


def getJava():
    return getJavaBinDir() + 'java'

def getConfigXmlPath():
    return getFullPath(constant.sdkRelatePath + ConfigParse.shareInstance().getChannelName()+"/funcellconfig.xml")

def getchannelFuncellConfigXmlPath(channel):
    return getFullPath(constant.sdkRelatePath + channel+"/funcellconfig.xml")

def getchannelRConfigXmlPath(channel):
    return getFullPath(constant.sdkRelatePath + channel+"/ForRconfig.xml")

def getUIConfigXmlPath():
    return getFullPath(constant.sdkRelatePath + ConfigParse.shareInstance().getChannelName()+"/uiconfig.xml")

def getTalkingDataPath():
    return getFullPath(constant.sdkRelatePath + "talkingdata")

def getGooglePlayServicesPath():
    return getFullPath(constant.sdkRelatePath + "google-play-services")

def getCrashPath():
    return getFullPath(constant.sdkRelatePath + "crash")

def getStatisticsPath():
    return getFullPath(constant.sdkRelatePath + "statistics")

def getAdvertisingPath():
    return getFullPath(constant.sdkRelatePath + "advertising")

def getPushPath():
    return getFullPath(constant.sdkRelatePath + "push")

def getForManifestXmlPath():
    return getFullPath(constant.sdkRelatePath + ConfigParse.shareInstance().getChannelName()+"/ForManifest.xml")

def getCommonXmlPath():
    return getFullPath("commonconfig.xml");

def getGameCommonScriptPath():
    return getFullPath("gameCommonScript")

def getGameSdkScriptPath():
    return getFullPath(constant.sdkRelatePath + ConfigParse.shareInstance().getChannelName() + "/gameSdkScript")
    
def printf(str):
    """
    print info in debug mode
    or
    write info into pythonLog.txt in release mode
    """
    global bPrint
    if bPrint:
        print str


def reportError(cmd, stdoutput, erroutput):
    """
    """
    idChannel = threading.currentThread().getName()
    errorOuput = '===================>>>> ERROR <<<<===================\r\n'
    errorOuput += '[FuncellSDK_Channel]: ' + threading.currentThread().getName() + '\r\n'
#     errorOuput += '[FuncellSDK_ChannelName]: ' + channelName + '\r\n'
#     errorOuput += '[FuncellSDK_Package]: ' + packageName + '\r\n'
    errorOuput += '[FuncellSDK_Time]: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '\r\n'
    errorOuput += '[FuncellSDK_Error]:\r\n'
    errorOuput += stdoutput + '\r\n'
    errorOuput += erroutput + '\r\n'
    errorOuput += '=====================================================\r\n'
    
    taskManager.shareInstance().updateLog(idChannel,errorOuput)
    log(errorOuput)


def log(str):
    outputDir = ConfigParse.shareInstance().getOutputDir()
    logDir = outputDir + 'Log/'
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    logFile = codecs.open(logDir + 'error.log', 'a+', 'utf-8')
    content = str + '\r\n'
    logFile.write(unicode(content, 'gbk'))
    logFile.close()


def setPrintEnable(bEnable):
    global bPrint
    global curDir
    bPrint = bEnable
    curDir = sys.path[0]
