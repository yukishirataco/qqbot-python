#-*- coding:utf-8 -*-
#帮助文档查看
import os, json


def Help_for_Single_Command(command):
    '''
    Help_for_Single_Command 函数：
    使用方法:help.Help_for_Single_Command(指令名)
    参数:command,string 类型，要查询的指令。
    返回值:string 类型，要查询指令的帮助信息。
    '''

    if command == 'version':
        help_of_cmd = ('命令帮助:英文格式:!laffey version\n中文格式:\n说明:显示这个bot的内部版本号.')
    elif command == 'baidu':
        help_of_cmd = ('命令:!laffey baidu <内容>\n说明:百度搜索，返回搜索链接和结果数量。')
    elif command == 'google':
        help_of_cmd = ('命令:!laffey google <内容>\n说明:Google搜索，返回搜索链接和结果数量。')
    elif command == 'pixiv':
        help_of_cmd = ('命令:!laffey pixiv <内容>\n说明:Pixiv，返回图片链接（需登录）。')
    elif command == 'booru':
        help_of_cmd = ('命令:!laffey booru <tags>\n说明:Gelbooru,返回随机一张图的链接。')
    elif command == '女装':
        help_of_cmd = ('命令:!laffey 女装 <QQ号>\n说明:女装的作用是相互的哦。')
    elif command == 'info':
        help_of_cmd = ('命令:!laffey info\n说明:查看您当前信息。（仅用于调试。）')
    elif command == 'time':
        help_of_cmd = ('命令:!laffey time\n说明:春雨语音报时')
    elif command == 'blacklist':
        help_of_cmd = ('命令:!laffey blacklist\n说明:查询黑名单内容')
    elif command == 'repeat':
        help_of_cmd = ('命令:!laffey repeat\n说明:查询复读机频率')
    elif command == 'weather':
        help_of_cmd = (
            '命令:!laffey weather <地区>\n说明:查询指定地区(目前只支持中国大陆以及港澳台地区)的天气')
    elif command == 'ping':
        help_of_cmd = (
            '命令:!laffey ping <IP/域名>\n说明:从服务器端(DGC香港)到指定 IP/域名的 ICMP Ping 结果')
    elif command == 'encode':
        help_of_cmd = (
            '命令:!laffey encode <加密方式> <明文>\n说明:加密方式:md5/base64,根据MD5/Base64方式进行加密。'
        )
    elif command == 'mtr':
        help_of_cmd = (
            '命令:!laffey mtr <IP/域名>\n说明:从服务器端(DGC香港)到指定 IP/域名的 Mytraceroute 结果'
        )
    else:
        help_of_cmd = ('你要查询的命令不存在。')
    return help_of_cmd
