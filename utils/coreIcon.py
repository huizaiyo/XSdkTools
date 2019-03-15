# -*- coding: utf-8 -*-
from http_manager import httpManager
from taskManagerModule import taskManager

def main(channel,channelIconData):
#     print 'channel:%s \n'%channel
#     print 'channelIconData:%s \n'%channelIconData
    iconUrl = channelIconData['icon']
    if len(iconUrl) > 0:
        httpManager.shareInstance().GetChannelIcon(iconUrl,channel)
    taskManager.shareInstance().notifyByIcon(channel, 100)



