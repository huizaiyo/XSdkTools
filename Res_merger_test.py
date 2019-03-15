import sys
from ResourceMerger import *
from utils import file_operate
# from xml.dom import minidom

def test():
    resPath = file_operate.getFullPath("I:/WorkSpace/android_pack_talkingdata/tmptools/apk_funcell_korea_185.10646(2018-10-17-19-57-08)/res")
    channelPath = file_operate.getFullPath("I:/WorkSpace/WorkSpace_python/finalsdk/test/ForRes")
    ResourceMerger.merge(resPath, channelPath, None)

test()