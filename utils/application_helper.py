# -*- coding: utf-8 -*-
#从smali文件中，定位父类
import os
import file_operate
from xml.etree import ElementTree as ET
androidNS = 'http://schemas.android.com/apk/res/android'

def getSuperClassNameInSmali(decompileDir, smaliPath):
 
    f = open(smaliPath, 'r')
    lines = f.readlines()
    f.close()
 
 
    for line in lines:
 
        if line.strip().startswith('.super'):
            line = line[6:].strip()
            return line[1:-1].replace('/', '.')
 
    return None
 
 
#查找指定类的smali文件路径
def findSmaliPathOfClass(decompileDir, className):
    
#     log_utils.debug("findSmaliPathOfClass:%s", className)
 
    className = className.replace(".", "/")
 
    for i in range(1,10):
        smaliPath = "smali"
        if i > 1:
            smaliPath = smaliPath + str(i)
 
        path = decompileDir + "/" + smaliPath + "/" + className + ".smali"
 
#         log_utils.debug(path)
 
        if os.path.exists(path):
            return path
 
 
    return None
 
 
#查找当前AndroidManifest.xml中的application类
def findApplicationClass(decompileDir):
 
    manifestFile = decompileDir + "/AndroidManifest.xml"
    manifestFile = file_operate.getFullPath(manifestFile)
    ET.register_namespace('android', androidNS)
    key = '{' + androidNS + '}name'
 
    tree = ET.parse(manifestFile)
    root = tree.getroot()
 
    applicationNode = root.find('application')
    if applicationNode is None:
        return None
 
    applicationClassName = applicationNode.get(key)   
    
    return applicationClassName
 
 
#查找AndroidManfiest.xml中application类的一级父类
def findRootApplicationSmali(decompileDir):
 
    applicationClassName = findApplicationClass(decompileDir)
 
    if applicationClassName is None:
#         log_utils.debug("findRootApplicationSmali: applicationClassName:%s", applicationClassName)
        return None
 
 
    return findRootApplicationRecursively(decompileDir, applicationClassName)
 
 
#循环定位
def findRootApplicationRecursively(decompileDir, applicationClassName):
 
    smaliPath = findSmaliPathOfClass(decompileDir, applicationClassName)
 
    if smaliPath is None or not os.path.exists(smaliPath):
#         log_utils.debug("smaliPath not exists or get failed.%s", smaliPath)
        return None
 
 
    superClass = getSuperClassNameInSmali(decompileDir, smaliPath)
    if superClass is None:
        return None
 
    if superClass == 'android.app.Application':
        return smaliPath
    else:
        return findRootApplicationRecursively(decompileDir, superClass)
 
 
#主调用接口， 设置一级Application继承指定的applicationClassName
def modifyRootApplicationExtends(decompileDir, applicationClassName):
 
    applicationSmali = findRootApplicationSmali(decompileDir)
    if applicationSmali is None:
#         log_utils.error("the applicationSmali get failed.")
        return 
 
#     log_utils.debug("modifyRootApplicationExtends: root application smali:%s", applicationSmali)
 
    modifyApplicationExtends(decompileDir, applicationSmali, applicationClassName)
 
 
 
#将一级Application的父类Application改为继承指定的applicationClassName
def modifyApplicationExtends(decompileDir, applicationSmaliPath, applicationClassName):
 
 
#     log_utils.debug("modify Application extends %s; %s", applicationSmaliPath, applicationClassName)
 
    applicationClassName = applicationClassName.replace(".", "/")
 
    f = open(applicationSmaliPath, 'r')
    lines = f.readlines()
    f.close()
 
    result = ""
    for line in lines:
 
        if line.strip().startswith('.super'):
            result = result + '\n' + '.super L'+applicationClassName+';\n' 
        elif line.strip().startswith('invoke-direct') and 'android/app/Application;-><init>' in line:
            result = result + '\n' + '      invoke-direct {p0}, L'+applicationClassName+';-><init>()V'
        elif line.strip().startswith('invoke-super'):
            if 'attachBaseContext' in line:
                result = result + '\n' + '      invoke-super {p0, p1}, L'+applicationClassName+';->attachBaseContext(Landroid/content/Context;)V'
            elif 'onConfigurationChanged' in line:
                result = result + '\n' + '      invoke-super {p0, p1}, L'+applicationClassName+';->onConfigurationChanged(Landroid/content/res/Configuration;)V'
            elif 'onCreate' in line:
                result = result + '\n' + '      invoke-super {p0}, L'+applicationClassName+';->onCreate()V'
            elif 'onTerminate' in line:
                result = result + '\n' + '      invoke-super {p0}, L'+applicationClassName+';->onTerminate()V'
            else:
                result = result + line
 
        else:
            result = result + line
 
 
    f = open(applicationSmaliPath, 'w')
    f.write(result)
    f.close()
 
    return 0