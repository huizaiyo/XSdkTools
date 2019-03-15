import thread
import time
from iconThreadManagerModule import packThreadManager
from taskManagerModule import taskManager
import os
import sys
import file_operate

def checkTaskThread(arrayList = None,dict = None):
    while 1:
        time.sleep(5)
        result = packThreadManager.shareInstance().isRunning()
        if result == 0:
            break
        packThreadManager.shareInstance().startTask(0,arrayList)

    file_operate.printf('Mission download Icon Complete!')
    thread.exit_thread()

def start(arrayList = None):
    dict = []
    reload(sys)
    sys.setdefaultencoding('utf8')
    taskManager.shareInstance().clearRecordByIcon()
    packThreadManager.shareInstance().clearRecord()
    packThreadManager.shareInstance().setCurWorkDir(os.getcwd())
    packThreadManager.shareInstance().startTask(0,arrayList)
    thread.start_new_thread(checkTaskThread, (arrayList,dict))


def stopAllTask():
    """Stop all of the tasks"""
    taskManager.shareInstance().clearRecordByIcon()
    packThreadManager.shareInstance().stopAllTask()


