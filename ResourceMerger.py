# -*- coding: utf-8 -*-

# resouce merge priority：base apk resource > channel resource > plugin resources
#  
# ResourceSet -> res folder
# ResourceFolder -> sub folder in res folder. like values,drawables,etc
# ResourceBlock -> a resource item. for example, a single file in drawable folder or a resource item in a value file
# 
# both single file and resource item use full name (with type_name format) to check whether t'is duplicated.
# but styleable resources are more complex. styleable resources and global attr resources should be merged together.
#

import os
import os.path
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree
import os
import os.path
import zipfile
import re
import subprocess
import platform
#from xml.dom import minidom
import codecs
import sys
import shutil
import time
from utils import file_operate
import json

global_ignored = ['.git','.svn']

class ResourceBlock(object):
    """the block defined an resource item in a res file. this can be a single file or a block item in the valueable file."""

    OP_TYPE_STAY = 0                    #file to copy or item to stay in where it is.
    OP_TYPE_REMOVE = 1                  #file or item to remove from curr folder or file
    OP_TYPE_MERGE = 2                   #attrs in styleable to merge 

    B_TYPE_ADD = 0                      #新增
    B_TYPE_MERGE = 1                    #需要合并


    BLOCK_TYPE_SINGLE_FILE = 1          #single file 
    BLOCK_TYPE_VALUE_FILE = 2           #value file

    RES_VAL_STRING = "string"
    RES_VAL_COLOR = "color"
    RES_VAL_DIMENS = "dimen"
    RES_VAL_STYLE = "style"
    RES_VAL_STYLEABLE = "declare-styleable"
    RES_VAL_BOOL = "bool"
    RES_VAL_INTEGER = "integer"
    RES_VAL_ID = "id"
    RES_VAL_ITEM = "item"
    RES_VAL_ATTR = "attr"
    RES_VAL_PUBLIC = "public"



    def __init__(self):
        super(ResourceBlock, self).__init__()
        self.blockType = ResourceBlock.BLOCK_TYPE_SINGLE_FILE
        self.resType = ""
        self.filePath = ""
        self.name = ""
        self.opType = ResourceBlock.OP_TYPE_STAY
        self.bType = ResourceBlock.B_TYPE_ADD
        self.librayName = ""
        self.format = ""        #format in attr node
        self.children = dict()  #attrs in declare-styleable


    def fullname(self):
        """return the name with type of the block entry"""
        return self.resType+"_"+self.name

    def path(self):

        return self.filePath

    def get_name(self):

        return self.name

    def get_res_type(self):

        return self.resType


    def file_name(self):

        return os.path.basename(self.filePath)


    def mark_removed(self):

        self.opType = ResourceBlock.OP_TYPE_REMOVE

    def mark_merged(self):

        self.opType = ResourceBlock.OP_TYPE_MERGE

    def mark_file_merged(self):

        self.bType = ResourceBlock.B_TYPE_MERGE


    def is_removed(self):

        return self.opType == ResourceBlock.OP_TYPE_REMOVE

    def is_merged(self):

        return self.opType == ResourceBlock.OP_TYPE_MERGE

    def is_file_merged(self):

        return self.bType == ResourceBlock.B_TYPE_MERGE


    def is_single_file(self):

        return self.blockType == ResourceBlock.BLOCK_TYPE_SINGLE_FILE


    def is_styleable(self):

        return self.resType == ResourceBlock.RES_VAL_STYLEABLE

    def is_attr(self):

        return self.resType == ResourceBlock.RES_VAL_ATTR


    def add_child(self, block):

        if block.fullname() in self.children:
            print "attr in declare-styleable duplicated:%s; %s"%(block.path(), block.name)
            return

        # print "block.fullname():"+block.fullname()
        self.children[block.fullname()] = block


    def has_format(self):

        return self.format != None and len(self.format) > 0

    def get_format(self):

        return self.format


    def get_children(self):

        return self.children

    def exists_in_children(self, fullName, format):

        if fullName not in self.children:
            return False

        block = self.children[fullName]

        # if format == None or len(format) == 0:
        #     return False
        #
        # if block.format == None or len(block.format) == 0:
        #     return False

        return True



    @classmethod
    def create_single_block(cls, filePath, librayName):

        return ResourceBlock.create_single_block_with_type("", filePath, librayName)


    @classmethod
    def create_single_block_with_type(cls, resType, filePath, librayName):

        block = ResourceBlock()
        block.blockType = ResourceBlock.BLOCK_TYPE_SINGLE_FILE
        block.resType = resType
        block.filePath = filePath
        block.name = os.path.splitext(os.path.basename(filePath))[0]
        block.opType = ResourceBlock.OP_TYPE_STAY
        block.bType = ResourceBlock.B_TYPE_ADD
        block.librayName = librayName
        block.format = ""

        return block        


    @classmethod
    def create_value_block(cls, resType, filePath, name, librayName):

        block = ResourceBlock()
        block.blockType = ResourceBlock.BLOCK_TYPE_VALUE_FILE
        block.resType = resType
        block.filePath = filePath
        block.name = name
        block.opType = ResourceBlock.OP_TYPE_STAY
        block.bType = ResourceBlock.B_TYPE_ADD
        block.librayName = librayName
        block.format = ""

        return block      


    @classmethod
    def create_value_block_with_format(cls, resType, filePath, name, librayName, format):

        block = ResourceBlock()
        block.blockType = ResourceBlock.BLOCK_TYPE_VALUE_FILE
        block.resType = resType
        block.filePath = filePath
        block.name = name
        block.opType = ResourceBlock.OP_TYPE_STAY
        block.bType = ResourceBlock.B_TYPE_ADD
        block.librayName = librayName
        block.format = format

        return block    






class ResourceFolder(object):
    """the sub folder in the res folder"""
    def __init__(self):
        super(ResourceFolder, self).__init__()
        self.name = ""
        self.filePath = ""
        self.librayName = ""
        self.entries = dict()           #key is full name of block item. full name is  [type]_[name]
        self.fileNames = dict()         # key is file base name.  value is file full path.


    @classmethod
    def create(cls, name, folderPath, librayName):

        folder = ResourceFolder()
        folder.name = name
        folder.filePath = folderPath
        folder.librayName = librayName

        return folder


    def get_name(self):

        return self.name

    def path(self):

        return self.filePath



    def load_blocks(self):
        """load all block entries in the folder"""

        if self.name == "values" or self.name.startswith("values-"):
            self.load_value_blocks()
        else:
            self.load_single_blocks()
            


    def load_value_blocks(self):

        blocks = ValueResourceParser.parse(self.filePath, self.librayName)

        if blocks == None or len(blocks) == 0:
            return

        for block in blocks:
            self.add_block_with_check(block)
            #print "add a new value block:%s;path:%s"%(block.get_name(), block.path())


    def load_single_blocks(self):

        for f in os.listdir(self.filePath):
            fpath = os.path.join(self.filePath, f)

            if not os.path.isfile(fpath):
                # if folder in sub res folder will be ignored.
                continue

            block = ResourceBlock.create_single_block(fpath, self.librayName)
            self.add_block_with_check(block)
            # print "add a new single block:"+block.path()


    def internal_add_block(self, block):

        blockFileName = block.file_name()
        blockFilePath = block.path()


        if blockFileName in self.fileNames:

            if blockFilePath != self.fileNames[blockFileName]:
                print "mark_file_merged:"+blockFilePath+"; "+block.get_name()
                block.mark_file_merged()
        else:
            self.fileNames[blockFileName] = blockFilePath


        fullName = block.fullname()

        if fullName not in self.entries:
            self.entries[fullName] = list()

        self.entries[fullName].append(block)        


    def add_block_with_check(self, block):

        # print "add_block_with_check:"+block.get_name()+" into "+self.filePath
        print "add_block_with_check block.get_name():" + block.get_name() + " | block.fullname():"+block.fullname() + " | block.get_res_type():"+block.get_res_type() +" | block.path():"+block.path()

        fullName = block.fullname()

        #check global attr
        if block.get_res_type() == ResourceBlock.RES_VAL_ATTR:

            if fullName in self.entries:

                block.mark_removed()
                self.internal_add_block(block)
                return

            #check in children
            for k in self.entries:

                exists = self.entries[k]

                for b in exists:

                    if b.is_styleable() and b.exists_in_children(fullName, block.get_format()):
                        block.mark_removed()
                        self.internal_add_block(block)
                        return


        #check styleable attrs
        if block.get_res_type() == ResourceBlock.RES_VAL_STYLEABLE:
            children = block.get_children()

            for k in children:
                childFullName = children[k].fullname()
                # print  "childFullName:"+childFullName
                if childFullName in self.entries and block.has_format():
                    children[k].mark_removed()
                    continue

                if childFullName in self.entries:
                    children[k].mark_removed()
                    continue

                for m in self.entries:

                    exists = self.entries[m]

                    for b in exists:
                        # print "b.is_styleable():" +str(b.is_styleable()) + " |b.exists_in_children:"+str(b.exists_in_children(childFullName, children[k].get_format()))
                        if b.is_styleable() and b.exists_in_children(childFullName, children[k].get_format()):
                            children[k].mark_removed()
                            break




        if fullName in self.entries:

            if block.get_res_type() == ResourceBlock.RES_VAL_PUBLIC:
                #pre merge public.xml
                #ValueResourceParser.merge_val_files_with_check(block.path(), self.entries[fullName][0].path()) #public.xml文件不能直接合并，这里暂时采用新的目录下直接覆盖母包的public.xml文件。
                file_operate.copyFile(block.path(), self.entries[fullName][0].path())
                print "pre merge public.xml from %s to %s"%(block.path(), self.entries[fullName][0].path())
                return 

            if block.get_res_type() == ResourceBlock.RES_VAL_STYLEABLE:
                #styable attrs to merge
                print "check styable duplicated. name:%s;new_path:%s;exists_path:%s"%(block.get_name(), block.path(), self.entries[fullName][0].path())
                block.mark_merged()
                # block.mark_removed()
            else:
                print "check resource block duplicated. name:%s;new_path:%s;exists_path:%s;"%(block.get_name(), block.path(), self.entries[fullName][0].path())
                block.mark_removed()


        self.internal_add_block(block)


    def merge_to(self, target):
        """merge all entries in this folder to the target folder"""

        for k in self.entries:
            # print  "~~~:"+k
            for b in self.entries[k]:
                # print "~~~~:"+b.path()
                target.add_block_with_check(b)


    def flush(self):
        """flush all the blocks to files"""
        
        #remove all [remove marked] blocks from origin file
        removedBlocks = self.get_removed_blocks()

        for f in removedBlocks:
            removedLst = removedBlocks[f]
            if len(removedLst) == 1 and removedLst[0].is_single_file():
                print "remove duplicated file %s"%(f)
                file_operate.delete_file_folder(f)
            else:
                # print "--------------------f:"+f
                ValueResourceParser.remove_blocks(f, removedLst)


        #merge styleable attrs.
        styleableBlocks = self.get_styleable_merged_blocks()
        for f in styleableBlocks:
            mergedLst = styleableBlocks[f]
            ValueResourceParser.merge_styleable_blocks(mergedLst)

            for b in mergedLst:
                if b.is_merged():
                    b.mark_removed()
                    ValueResourceParser.remove_blocks(b.path(), [b])


        #copy added files
        addedBlocks = self.get_added_blocks()

        for f in addedBlocks:
            addedLst = addedBlocks[f]
            targetFile = os.path.join(self.filePath, os.path.basename(f))

            if os.path.exists(targetFile):
                print "resource flush error. file already exists:%s"%(targetFile)
                continue

            file_operate.copyFile(f, targetFile)
            print "copy a new file from %s to %s"%(f, targetFile)


        #merge blocks from files with same name.
        mergedBlocks = self.get_merged_blocks()

        for f in mergedBlocks:
            mergedLst = mergedBlocks[f]
            ValueResourceParser.merge_val_files(f, os.path.join(self.filePath, os.path.basename(f)))


    def get_removed_blocks(self):

        removed = dict()

        for k in self.entries:

            if len(self.entries[k]) >= 1:

                for b in self.entries[k]:

                    if b.is_removed():
                        filePath = b.path()
                        if filePath not in removed:
                            removed[filePath] = list()
                            
                        removed[filePath].append(b)
                        # print "------------filePath:"+filePath

                    elif b.is_styleable():
                        children = b.get_children()
                        for i in children:
                            if children[i].is_removed():

                                cpath = children[i].path()
                                if cpath not in removed:
                                    removed[cpath] = list()

                                removed[cpath].append(children[i])
                                # print "------------cpath:" + cpath



        return removed


    def get_merged_blocks(self):

        merged = dict()

        for k in self.entries:

            block = self.entries[k][0]

            if self.is_need_merge(block):

                filePath = block.path()
                if filePath not in merged:
                    merged[filePath] = list()

                merged[filePath].append(block)

        return merged


    def get_styleable_merged_blocks(self):

        merged = dict()

        for k in self.entries:

            block = self.entries[k][0]

            if self.entries[k] > 1 and block.is_styleable():
                merged[block.fullname()] = self.entries[k]

        return merged



    def get_added_blocks(self):

        added = dict()

        for k in self.entries:

            block = self.entries[k][0]

            if self.is_need_add(block):

                filePath = block.path()
                if filePath not in added:
                    added[filePath] = list()

                added[filePath].append(block)

        return added



    def is_local_block(self, block):

        return os.path.dirname(block.path()) == self.filePath


    def is_need_copy(self, block):

        return (not block.is_removed()) and (os.path.dirname(block.path()) != self.filePath)


    def is_need_merge(self, block):

        if not self.is_need_copy(block):
            return False

        if block.is_single_file():
            return False

        if block.is_file_merged():
            return True

        return False

        # fileName = block.file_name()
        # fullPath = os.path.join(self.filePath, fileName)

        # log_utils.debug("is_need_merge:"+fullPath)

        # return os.path.exists(fullPath)


    def is_need_add(self, block):

        if not self.is_need_copy(block):
            return False

        if block.is_single_file():
            return True        

        if block.is_file_merged():
            return False

        fileName = block.file_name()

        return not os.path.exists(os.path.join(self.filePath, fileName))



class ResourceSet(object):
    """the res folder"""
    def __init__(self):
        super(ResourceSet, self).__init__()
        self.librayName = ""
        self.filePath = ""
        self.folders = dict()       #key is the folder name.


    @classmethod
    def create(cls, librayName, path):

        print "create a new resource set. librayName:"+librayName+";path:"+path

        res = ResourceSet()
        res.librayName = librayName
        res.filePath = path
        return res


    def load_blocks(self):
        """load all block entries in the res folder"""

        if not os.path.exists(self.filePath):
            print "%s res folder not exists."%(self.filePath)
            return

        for f in os.listdir(self.filePath):

            if os.path.isfile(os.path.join(self.filePath, f)):
                #files in res folder will be ignored.
                continue

            if f in global_ignored:
                #files in global_ignored will be ignored.
                continue

            fpath = os.path.join(self.filePath, f)
            folder = ResourceFolder.create(f, fpath, self.librayName)
            folder.load_blocks()
            self.add_folder_with_check(folder)
    

    def add_folder_with_check(self, folder):

        name = folder.get_name()
        if name in self.folders:
            # print "----:"+name
            # print "----:"+folder.path()
            # print "----:"+self.folders[name].path()
            folder.merge_to(self.folders[name])
        else:
            self.folders[name] = folder


    def merge_to(self, target):
        """merge the resource set into the target resource set"""

        for k in self.folders:
            target.add_folder_with_check(self.folders[k])


    # def is_new_folder(self, folder):
    #     return (os.path.dirname(block.path()) != self.filePath)


    def flush(self):
        """flush all the blocks to files"""
        
        for k in self.folders:
            self.folders[k].flush()

        for k in self.folders:
            localFolder = os.path.join(self.filePath, self.folders[k].get_name())
            if not os.path.exists(localFolder):
                file_operate.copyFiles(self.folders[k].path(), localFolder)



class ValueResourceParser(object):
    """parser for resource in values folders"""
    def __init__(self, folder, librayName):
        super(ValueResourceParser, self).__init__()
        self.folder = folder
        self.librayName = librayName
        self.entries = dict()

    def load_blocks(self):

        for f in os.listdir(self.folder):

            if not os.path.isfile(os.path.join(self.folder, f)):
                # if folder in sub res folder will be ignored.
                continue            

            self.load_blocks_in_file(os.path.join(self.folder, f), f)


    def load_blocks_in_file(self, filePath, fileName):

        # print "begin load blocks in file:"+filePath

        if fileName == "public.xml":
            block = ResourceBlock.create_single_block_with_type(ResourceBlock.RES_VAL_PUBLIC, filePath, self.librayName)
            self.entries[block.fullname()] = block
            return

        tree = ET.parse(filePath)
        root = tree.getroot()
        for node in list(root):
            resType = node.tag
            resName = node.attrib.get('name')
            typeAlias = node.attrib.get('type')
            format = node.attrib.get('format')
            if typeAlias != None:
                resType = typeAlias


            if resName == None or len(resName) == 0:
                #maybe eat-comment
                continue

            block = ResourceBlock.create_value_block_with_format(resType, filePath, resName, self.librayName, format)

            fullName = block.fullname()

            # print "fullName:"+fullName
            # print "filePath:"+filePath
            if fullName in self.entries:
                print "value resource %s duplicated in same sub folder. in %s and %s"%(resName, filePath, self.entries[fullName].path())
                #raise RuntimeError("value resource duplicated in same res sub folder")  #aapt can ignore this if there are with same values. so just ignore here.
            else:    
                self.entries[fullName] = block

                #load all children of styleable
                if block.is_styleable():
                    children = node.findall('attr')
                    if children != None and len(children) > 0:
                        for attrNode in children:
                            attrName = attrNode.attrib.get('name')
                            # print "attrName:"+attrName
                            attrBlock = ResourceBlock.create_value_block_with_format(ResourceBlock.RES_VAL_ATTR, filePath, attrName, self.librayName, format)
                            block.add_child(attrBlock)




    @classmethod
    def remove_blocks(cls, filePath, blocks):

        if blocks == None or len(blocks) == 0:
            return

        tree = ET.parse(filePath)
        root = tree.getroot()

        for block in blocks:

            for node in list(root):
                resType = node.tag
                resName = node.attrib.get('name')
                typeAlias = node.attrib.get('type')

                if typeAlias != None:
                    resType = typeAlias


                if resType == ResourceBlock.RES_VAL_STYLEABLE:

                    children = node.findall('attr')
                    if children != None and len(children) > 0:

                        for child in list(children):
                            childResName = child.attrib.get('name')
                            if block.is_attr() and block.get_name() == childResName:
                                print "remove duplicated attr node %s in %s"%(childResName, filePath)
                                node.remove(child)
                                break


                if block.get_res_type() == resType and block.get_name() == resName:
                    print "remove duplicated node %s from file:%s"%(resName, filePath)
                    root.remove(node) 
                    break                   

        tree.write(filePath, "UTF-8")


    @classmethod
    def merge_styleable_blocks(cls, blocks):

        if blocks == None or len(blocks) <= 1:
            return

        mainBlock = blocks[0]

        tree = ET.parse(mainBlock.path())
        root = tree.getroot()

        mainNode = None
        for node in list(root):
            resType = node.tag
            resName = node.attrib.get('name')

            if resType == mainBlock.get_res_type() and resName == mainBlock.get_name():
                mainNode = node
                break

        if mainNode == None:
            print "merge styleable node failed. main node %s not exists in file:%s"%(mainBlock.get_name(), mainBlock.path())
            return

        for k in range(1, len(blocks)):

            mtree = ET.parse(blocks[k].path())
            mroot = mtree.getroot()

            mergeNode = None
            for mnode in list(mroot):
                mtype = mnode.tag
                mname = mnode.attrib.get('name')

                if mtype == mainBlock.get_res_type() and mname == mainBlock.get_name():
                    mergeNode = mnode
                    break

            if mergeNode != None:

                mergeChildren = mergeNode.findall('attr')
                if mergeChildren != None and len(mergeChildren) > 0:
                    for node in list(mergeChildren):
                        print "merge styleable attr %s from %s to %s"%(mainBlock.get_name(), blocks[k].path(), mainBlock.path())
                        mainNode.append(node)


        tree.write(mainBlock.path(), "UTF-8")



    @classmethod
    def merge_val_files(cls, filePath, targetFilePath):

        #log_utils.debug("merge val files:" + filePath + " and " + targetFilePath)

        oldTree = ET.parse(filePath)
        oldRoot = oldTree.getroot()

        tree = ET.parse(targetFilePath)
        root = tree.getroot()

        for node in list(oldRoot):
            print "merge res node %s from %s to %s"%(node.attrib.get('name'), filePath, targetFilePath)
            root.append(node)

        tree.write(targetFilePath, "UTF-8")

    @classmethod
    def merge_val_files_with_check(cls,filePath, targetFilePath):

        oldTree = ET.parse(filePath)
        oldRoot = oldTree.getroot()

        tree = ET.parse(targetFilePath)
        root = tree.getroot()

        exists = list()
        for node in list(root):
            mtype = node.tag
            mname = node.attrib.get('name')
            if mtype != None and mname != None:
                exists.append(mtype+"_"+mname)

        for node in list(oldRoot):
            mtype = node.tag
            mname = node.attrib.get('name')
            if mtype != None and mname != None:
                fullname = mtype+"_"+mname
                if fullname not in exists:
                    root.append(node)


        tree.write(targetFilePath, "UTF-8")



    @classmethod
    def parse(cls, folder, librayName):

        parser = ValueResourceParser(folder, librayName)

        parser.load_blocks()

        return list(parser.entries.values())

        

class ResourceMerger(object):

    """the merger for resource from base apk, channel resource folder and plugin resource folders"""
    def __init__(self):
        super(ResourceMerger, self).__init__()

        self.baseSet = None
        self.channelSet = None
        self.pluginSets = list()
    

    @classmethod
    def merge(cls, baseResPath, channelResPath, pluginResPaths):

        merger = ResourceMerger()

        merger.baseSet = ResourceSet.create("base", baseResPath)

        if channelResPath != None and os.path.exists(channelResPath):
            merger.channelSet = ResourceSet.create(merger.parse_name(channelResPath), channelResPath)

        if pluginResPaths != None and len(pluginResPaths) > 0:
            for plugin in pluginResPaths:
                if os.path.exists(plugin):
                    pluginSet = ResourceSet.create(merger.parse_name(plugin), plugin)
                    merger.pluginSets.append(pluginSet)


        merger.do_merge()


    def parse_name(self, resPath):

        return os.path.basename(os.path.dirname(resPath))


    def load_blocks(self):

        self.baseSet.load_blocks()

        if self.channelSet != None:
            # print "channelSet.load_blocks()"
            self.channelSet.load_blocks()

        if len(self.pluginSets) > 0:
            for p in self.pluginSets:
                p.load_blocks()


    def do_merge(self):

        self.load_blocks()

        if self.channelSet != None:
            self.channelSet.merge_to(self.baseSet)
        if len(self.pluginSets) > 0:
            for p in self.pluginSets:
                p.merge_to(self.baseSet)


        self.baseSet.flush()


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

if __name__ == "__main__":
    # file_operate.copyFile(file_operate.getFullPath("I:/WorkSpace/test/appcompat-v7-27.0.2_values-test.xml"),file_operate.getFullPath("I:/WorkSpace/test/base/values/appcompat-v7-27.0.2_values-test.xml"))
    # file_operate.copyFile(file_operate.getFullPath("I:/WorkSpace/test/appcompat-v7-27.0.2_values-test.xml"),file_operate.getFullPath("I:/WorkSpace/test/channel/values/appcompat-v7-27.0.2_values-test.xml"))
    #
    # resPath = file_operate.getFullPath("I:\\WorkSpace\\test\\base")
    # channelPath = file_operate.getFullPath("I:\\WorkSpace\\test\\channel")
    #
    # ResourceMerger.merge(resPath, channelPath, None)

    pass

