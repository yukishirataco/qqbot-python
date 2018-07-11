# -*- coding:utf-8 -*- #
import time
import os
import urllib 
from random import choice,randint
from cqhttp_helper import CQHttp, Error
from bs4 import BeautifulSoup
import requests
import json
from laffey import one_para,no_para,two_paras,logging,helping,weather,network_tools,encrypt

admins = [675571268,2980503519]
#检查目录存在性
no_para.check_dir_existence()
bot = CQHttp(api_root='http://127.0.0.1:5700/',access_token='you9zh9chen991',)

@bot.on_message()
def handle_msg(context):
    global blacklist,repeat
    content=context['message']
    #如果发送的是群组消息
    if context['message_type']=='group':
        group_id = context['group_id']
        conf = r'./config/'+str(group_id)+'.json'
        group_cfg = one_para.read_config(group_id)
        #读取配置文件
        blacklist = group_cfg['blacklist']
        repeat = group_cfg['repeat']
        flag = group_cfg['flag']
        if content.split()[0] == '!laffey' or content.split()[0] == '！拉菲':
        #非管理指令
            logging.logging_command(context)
            if context['user_id'] in admins:
            #管理指令。
                if content.split(' ',1)[1] == 'touch' or content.split(' ',1)[1] == '摸摸':
                    bot.send(context,'唔……嗯……糟了，站着睡着了')

                elif content.split(' ',1)[1]=='speak' or content.split(' ',1)[1] == '说话':
                    #管理员指令，拉菲语言库（语音需要Cool Q Pro)
                    return_data = no_para.laffey_speaks()
                    bot.send(context,return_data['string'])
                    bot.send(context,[{"type": "record","data": {"file": return_data['voice_link']}}])

                elif content.split(' ',3)[1] == 'blacklist' or content.split(' ',3)[1] == '黑名单':
                    #管理黑名单。
                    if content.split(' ',3)[2] == 'add' or content.split(' ',3)[2] == '添加':
                        number = content.split(' ',3)[3]
                        if number.isdigit():
                            if number in blacklist:
                                bot.send(context,'你要添加到群组: ' + str(context['group_id']) + '复读黑名单的用户:'+number+'已存在')
                            else:
                                blacklist.append(number)
                                with open(conf,'w') as f_conf_w:
                                    dic_conf = json.dumps(dict(blacklist=blacklist,repeat=repeat,flag=flag))
                                    f_conf_w.write(dic_conf)
                                    f_conf_w.close()
                                bot.send(context,'用户:'+number+'已被添加至群组:'+str(group_id)+'的复读黑名单里，该用户将不会被机器人复读。')
                        else:
                            logging.logging_bad_type(context)
                            bot.send(context,'你输入的用户QQ号不是合法的数字。')

                    elif content.split(' ',3)[2] == 'del' or content.split(' ',3)[2] == '删除':
                        number = content.split(' ',3)[3]
                        if number.isdigit():
                            if number in blacklist:
                                loc = blacklist.index(number)
                                blacklist.pop(loc)
                                with open(conf,'w') as f_conf_w:
                                    dic_conf = json.dumps(dict(blacklist=blacklist,repeat=repeat,flag=flag))
                                    f_conf_w.write(dic_conf)
                                    f_conf_w.close()
                                bot.send(context,'用户'+number+'已从群组:'+str(group_id)+'的黑名单中移除。')
                            else:
                                bot.send(context,'用户不存在，请查看是否有输入错误。')
                        else:
                            logging.logging_bad_type(context)
                            bot.send(context,'你的输入有误，数据不是合法数字。')

                elif content.split(' ',3)[1] == 'repeat' or content.split(' ',3)[1] == '复读':
                    parameters = content.split(' ',3)[2]
                    if parameters == 'set' or parameters == '设定':
                        frequency = content.split(' ',3)[3]
                        if frequency.isdigit():
                            repeat = frequency
                            dic_conf = json.dumps(dict(blacklist=blacklist,repeat=int(repeat),flag=flag))
                            with open(conf,'w') as f_conf_w:
                                f_conf_w.write(dic_conf)
                                f_conf_w.close()
                            bot.send(context,'群组 '+str(context['group_id'])+' 的复读频率已成功修改，当前数值:'+str(repeat)+'%。')
                        
                elif content.split(' ',1)[1] == 'status' or content.split(' ',1)[1] == '状态':            
                    #管理员指令，查看服务器运行状态。
                    status = no_para.system_status()
                    bot.send(context,status)

                elif content.split(' ',3)[1] == '炸群' or content.split(' ',3)[1] == 'flow':
                    try:
                        times = int(content.split(' ',3)[2])
                        text = content.split(' ',3)[3]
                    except:
                        logging.logging_error_empty_parameter(context)
                        bot.send(context,'指令出错，您输入的参数有一项或者是两项为空\n正确用法:\n!laffey flow <重复次数> <重复消息（只支持文字）>')
                    else:
                        if times > 10:
                            times = 10
                        if times <=10:
                            for i in range(0,times):
                                bot.send(context,text)
                        if times <= 0:
                            bot.send(context,'您输入的次数参数有误！')

            if content.split(' ',1)[1] == 'info' or content.split(' ',1)[1] == '信息':
                bot.send(context,'您的信息:\n聊天类型:' + context['message_type'] + '群号:' + str(context['group_id']) + '\n消息ID:' + str(context['message_id']) + '\n发送者QQ:' + str(context['user_id']))
            elif content.split(' ',1)[1]=='version' or content.split(' ',1)[1]=='版本':
                #查询版本号
                bot.send(context,no_para.version())
            elif content.split(' ',1)[1] == 'time' or content.split(' ',1)[1] == '时间':
                #报时
                times = no_para.times_str()
                bot.send(context,times)
                voice = no_para.time_harusame()
                bot.send(context,[{"type": "record","data": {"file": voice }}])                              

            elif content.split(' ',2)[1] == 'repeat' or content.split(' ',2)[1] == '复读':
                if content.split(' ',3)[2].strip()=='show' or content.split(' ',3)[2].strip()=='显示':
                    bot.send(context,'群组 '+str(context['group_id'])+' 的复读频率: \n'+str(repeat)+' %')
                else:
                    pass
            elif content.split(' ',2)[1]=='blacklist' or content.split(' ',2)[1]=='黑名单':
                if content.split(' ',3)[2].strip()=='list' or content.split(' ',3)[2].strip()=='查询':
                    bot.send(context,'群组 '+str(group_id)+' 内的机器人黑名单查询完毕，共有 '+str(len(blacklist))+' 项\n内容如下:'+str('\n'.join(blacklist)))
                else:
                    pass
            elif content.split(' ',2)[1]=='baidu' or content.split(' ',2)[1]=='百度':
                try:
                    word = content.split(' ',2)[2] 
                except IndexError:
                    #没有提供指令的时候raise IndexError，被捕捉到了。
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'请提供百度搜索词')
                else:
                    result = one_para.baidu(word)
                    bot.send(context,result)

            elif content.split(' ',2)[1] == 'pixiv':
                    try:
                        pid = content.split(' ',2)[2] 
                    except IndexError:
                        #没有提供指令的时候raise IndexError，被捕捉到了。
                        logging.logging_error_empty_parameter(context)
                        bot.send(context,'请提供 Pixiv ID 号')
                    else:
                        if pid.isdigit():
                            link = one_para.pixiv(pid)
                            bot.send(context,link)
                        else:
                            logging.logging_bad_type(context)
                            bot.send(context,'你提供的 Pixiv ID 号不是一个合法的数字')

            elif content.split(' ',2)[1] == 'google':
                try:
                    word = content.split(' ',2)[2] 
                except IndexError:
                    #没有提供指令的时候raise IndexError，被捕捉到了。
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'请提供Google搜索词')
                else:
                    result = one_para.google(word)
                    bot.send(context,result)

            elif content.split(' ',2)[1] == 'booru':
                    #Gelbooru爬虫精简版，来自Ecchibot
                tags=content.split(' ',2)[2]
                return_data = one_para.booru(tags)
                bot.send(context,return_data['string'])
                bot.send(context,[{"type": "image","data": {"file": return_data['link']}}])

            elif content.split(' ',2)[1] == 'help' or content.split(' ',2)[1] == '帮助':
                try:
                    command = content.split(' ',2)[2] 
                except IndexError:
                    #没有提供指令的时候raise IndexError，被捕捉到了。
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'没有提供需要查询帮助的指令')
                else:
                    helps = helping.Help_for_Single_Command(command)
                    bot.send(context,helps)

            elif content.split(' ',3)[1] == '女装':
                #女装库
                try:
                    target=content.split(' ',3)[2]
                except IndexError:
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,[{"type": "at","data": {"qq": str(context['user_id'])}},{"type": "text","data": {"text": "，请开始你的女装表演"}}])
                else:
                    bot.send(context,[{"type": "at","data": {"qq": target}},{"type": "text","data": {"text": "女装了， "}},{"type": "at","data": {"qq": str(context['user_id'])}},{"type": "text","data": {"text": "也要女装哦"}}])
           
            elif content.split(' ',3)[1] == 'roll' or content.split(' ',3)[1] == '抽卡':
                try:
                    types = content.split(' ',3)[2]
                    times = content.split(' ',3)[3]
                except IndexError:
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'你提供的参数不完整，\n使用方法:\n!laffey roll <抽卡类型(l/h/s)> <抽卡次数(最大10次)>')
                else:
                    rollout = two_paras.roll(times,types)
                    bot.send(context,rollout)

            elif content.split(' ',2)[1] == 'weather' or content.split(' ',2)[1] == '天气':
                try:
                    citi = content.split(' ',2)[2]
                except IndexError:
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'请输入您要查询的城市')
                else:
                    bot.send(context,weather.request_weather(citi))

            elif content.split(' ',2)[1] == 'ping':
                try:
                    addr = content.split(' ',2)[2]
                except IndexError:
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'请输入您要检测连通性的IP/域名')
                else:
                    result = network_tools.ping_test(addr)
                    bot.send(context,result)

            elif content.split(' ',2)[1] == 'mtr':
                try:
                    addr = content.split(' ',2)[2]
                except IndexError:
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'请输入您要MyTraceRoute的IP/域名')
                else:
                    result = network_tools.mtr(addr)
                    bot.send(context,"MTR结果:\n"+result)

            elif content.split(' ',3)[1] == 'encode' or content.split(' ',3)[1] == '加密':
                try:
                    entype = content.split(' ',3)[2]
                    mingw = content.split(' ',3)[3]
                except IndexError:
                    logging.logging_error_empty_parameter(context)
                    bot.send(context,'指令不完整，完整的指令格式为:\n!laffey encode <加密方式> <明文>')
                else:
                    if entype == 'md5':
                        coded = encrypt.md5(mingw)
                        bot.send(context,coded)
                    elif entype == 'base64':
                        coded = encrypt.base64_en(mingw)
                        bot.send(context,coded)
                    else:
                        bot.send(context,'加密方式不存在!')
                    

            else:
                pass
        else:
        #非指令判定复读
            if randint(1,100)>100-repeat:
                if content[0] == '!' or "next time" in content:
                    pass
                else:
                    if str(context['user_id']) in blacklist:
                        logging.logging_repeat_failure(context)
                    else:
                        bot.send(context,context['message'].replace('我','你'))
                        logging.logging_repeat_success(context)
bot.run(host='127.0.0.1', port=8080)        
