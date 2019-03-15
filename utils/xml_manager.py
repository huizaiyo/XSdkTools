# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import threading
import xml.dom.minidom
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

class XmlManager(QObject):
    __instance = None
    __Lock = threading.Lock()
    
    def __init__(self):
        pass
    
    @staticmethod
    def shareInstance():
        XmlManager.__Lock.acquire()
        if XmlManager.__instance == None:
            XmlManager.__instance = QObject.__new__(XmlManager)
            QObject.__init__(XmlManager.__instance)
        XmlManager.__Lock.release()
        return XmlManager.__instance
    
    def createElement(self,xmlpath,ConfigNodeList = None,PlatformNodeList = None,SplashNodeList = None,pluginNodeList = None):
        xmlpath = xmlpath+'/funcellconfig.xml'
        xmldoc = xml.dom.minidom.getDOMImplementation()
        dom = xmldoc.createDocument(None, 'root', None)
        root = dom.documentElement
        
        for NodeKey in ConfigNodeList.keys():
            childNode = dom.createElement(NodeKey)
            for attributeKey in ConfigNodeList[NodeKey]:
                childNode.setAttribute(attributeKey, ConfigNodeList[NodeKey][attributeKey])
                
            root.appendChild(childNode)
        
        for NodeKey in PlatformNodeList.keys():
            childNode = dom.createElement(NodeKey)
            for attributeKey in PlatformNodeList[NodeKey]:
                childNode.setAttribute(attributeKey, PlatformNodeList[NodeKey][attributeKey])
                
            root.appendChild(childNode)
        
        for NodeKey in SplashNodeList.keys():
            childNode = dom.createElement(NodeKey)
            for attributeKey in SplashNodeList[NodeKey]:
                childNode.setAttribute(attributeKey, SplashNodeList[NodeKey][attributeKey])
                
            root.appendChild(childNode)
        
        for NodeKey in pluginNodeList.keys():
            childNode = dom.createElement(NodeKey)
            for attributeKey in SplashNodeList[NodeKey]:
                childNode.setAttribute(attributeKey, SplashNodeList[NodeKey][attributeKey])
                
            root.appendChild(childNode)
        
        f = open(xmlpath, 'w')
        dom.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
        f.close()
    
    def createFuncellconfigXml(self,xmlpath,ConfigNodeList = None):
        xml = dicttoxml(ConfigNodeList)
        dom = parseString(xml)
#         print(dom.toprettyxml())
        content = dom.toprettyxml()
        xmlpath = xmlpath+'/funcellconfig.xml'
        f = open(xmlpath, "w")
        f.write(content)
        f.close()
    
    def createFuncellPluginXml(self,xmlpath,ConfigNodeList = None):
        ConfigList={}
        ConfigList['pluginLs'] = ConfigNodeList
        xml = dicttoxml(ConfigList)
        dom = parseString(xml)
#         print(dom.toprettyxml())
        content = dom.toprettyxml()
        xmlpath = xmlpath+'/funcellplugin.xml'
        f = open(xmlpath, "w")
        f.write(content)
        f.close()
        