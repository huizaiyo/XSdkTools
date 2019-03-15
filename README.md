 XSdkTools
===============
*   QQ交流群： 722652515 
*   从零学Python，各种开发案例，不定期更新:https://gitee.com/52itstyle/Python
*   码云地址：https://gitee.com/huang465265897/XSdkTools
*   后端脚手架：https://github.com/huangjian888/jeeweb-mybatis-springboot

-----------------------------------
一款类似Anysdk、Quicksdk、棱镜sdk的打包工具（多线程）

技术选型
===============
* 框架：python2.7+pyQt4.8
* 开发环境：PyCharm
* 打包exe或者mac运行程序：PyInstaller
* 打包安装程序：Inno Setup 5

简单使用说明
-----------------------------------
* 快速安装环境：使用PyCharm开发工具中直接下载python版本，pyqt版本
* 启动frmmain.pyw
* ui目录为pyqt界面，后缀为ui，需要将ui转换为py文件，具体查看ui目录下的*.bat 文件中的命令
* pyrcc4 -o x.py x.qrc 将qrc文件输出为py文件，qrc文件为pyqt ui工具使用的文件，布局
* pyrcc4 -o x.py x.ui 将ui文件输出为py文件
* 该框架为PC客户端，后台服务器可以自行实现


框架流程
-----------------------------------
frmmain.pyw->UpdateUI.pyw（更新程序）->pack.py(主界面)->**

协议
-----------------------------------
* MIT License 
* 商业化请不要照搬UI布局，UI请换一套(要专业)




