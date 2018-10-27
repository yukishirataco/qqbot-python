# -*- coding:utf-8 -*- #

import json
import urllib
import urllib.parse
from random import choice

import wsgiserver
from cqhttp import CQHttp

from laffey import one_para, no_para, two_paras, logrec, helping, weather, network_tools, encrypt

repeat_names = {
    870680559: 'BSY',
    1371855771: 'max',
    542154951: 'red',
    3487973010: 'red',
    1297976315: 'john',
    1213696841: '121',
    2510470532: 'ad',
    675571268: '指挥官',
    2980503519: '指挥官',
    624749918: '阿帕奇'
}

def abcgen():
    a_list = '吖醃醃厑錒呵吖ア啊A'
    b_list = '鉑僰蔢噃秡砵盋ボ伯B'
    c_list = '彳瓻卶灻杘伬瘛チ吃C'
    #阿伯吃姓名替换生成器，仅供娱乐系列
    return choice(a_list) + choice(b_list) + choice(c_list)

admins = [675571268, 2980503519]
# 可以直接使用bot管理指令的Admin名单

# 检查目录存在性（工作目录以及运行目录）
no_para.check_dir_existence()

bot = CQHttp(
    api_root='http://127.0.0.1:5700/',
    access_token='',
)

@bot.on_message()
def handle_msg(context):
    global blacklist, repeat
    content = context['message']
    # 单独提取消息
    # 如果发送的是群组消息
    if context['message_type'] == 'group':
        group_id = context['group_id']
        conf = r'./config/' + str(group_id) + '.json'
        group_cfg = one_para.read_config(group_id)
        # 读取配置文件
        blacklist = group_cfg['blacklist']
        repeat = group_cfg['repeat']
        flag = group_cfg['flag']
        if content.split()[0] == '!laffey' or content.split()[0] == '！拉菲':
            logrec.logging_command(context)
            if context['user_id'] in admins:
                # 管理指令
                # TODO:使用dict-function重构命令部分
                if content.split(' ', 1)[1] == 'touch' or content.split(
                        ' ', 1)[1] == '摸摸':
                    bot.send(context, '唔……嗯……糟了，站着睡着了')

                elif content.split(' ', 1)[1] == 'speak' or content.split(
                        ' ', 1)[1] == '说话':
                    # 管理员指令，拉菲语言库（语音需要Cool Q Pro)
                    return_data = no_para.laffey_speaks()
                    bot.send(context, return_data['string'])
                    bot.send(context, [{
                        "type": "record",
                        "data": {
                            "file": return_data['voice_link']
                        }
                    }])

                elif content.split(' ', 3)[1] == 'blacklist' or content.split(
                        ' ', 3)[1] == '黑名单':
                    # 管理黑名单。
                    if content.split(' ', 3)[2] == 'add' or content.split(
                            ' ', 3)[2] == '添加':
                        number = content.split(' ', 3)[3]
                        if number.isdigit():
                            if number in blacklist:
                                bot.send(
                                    context,
                                    '你要添加到群组: ' + str(context['group_id']) +
                                    '复读黑名单的用户:' + number + '已存在')
                            else:
                                blacklist.append(number)
                                with open(conf, 'w') as f_conf_w:
                                    dic_conf = json.dumps(
                                        dict(
                                            blacklist=blacklist,
                                            repeat=repeat,
                                            flag=flag))
                                    f_conf_w.write(dic_conf)
                                    f_conf_w.close()
                                bot.send(
                                    context, '用户:' + number + '已被添加至群组:' +
                                    str(group_id) + '的复读黑名单里，该用户将不会被机器人复读。')
                        else:
                            logrec.logging_bad_type(context)
                            bot.send(context, '你输入的用户QQ号不是合法的数字。')
                    # TODO:加入全局黑名单(gblacklist)功能，位于该名单中的用户将无法使用bot。
                    elif content.split(' ', 3)[2] == 'del' or content.split(
                            ' ', 3)[2] == '删除':
                        number = content.split(' ', 3)[3]
                        if number.isdigit():
                            if number in blacklist:
                                loc = blacklist.index(number)
                                blacklist.pop(loc)
                                with open(conf, 'w') as f_conf_w:
                                    dic_conf = json.dumps(
                                        dict(
                                            blacklist=blacklist,
                                            repeat=repeat,
                                            flag=flag))
                                    f_conf_w.write(dic_conf)
                                    f_conf_w.close()
                                bot.send(
                                    context, '用户' + number + '已从群组:' +
                                    str(group_id) + '的黑名单中移除。')
                            else:
                                bot.send(
                                    context,
                                    '用户不存在，请查看是否有输入错误。\n指令的格式为:!laffey blacklist del <QQ>'
                                )
                        else:
                            logrec.logging_bad_type(context)
                            bot.send(context, '你的输入有误，数据不是合法数字。')

                elif content.split(' ', 3)[1] == 'repeat' or content.split(
                        ' ', 3)[1] == '复读':
                    parameters = content.split(' ', 3)[2]
                    if parameters == 'set' or parameters == '设定':
                        frequency = content.split(' ', 3)[3]
                        if frequency.isdigit():
                            repeat = frequency
                            dic_conf = json.dumps(
                                dict(
                                    blacklist=blacklist,
                                    repeat=int(repeat),
                                    flag=flag))
                            with open(conf, 'w') as f_conf_w:
                                f_conf_w.write(dic_conf)
                                f_conf_w.close()
                            bot.send(
                                context, '群组 ' + str(context['group_id']) +
                                ' 的复读频率已成功修改，当前数值:' + str(repeat) + '%。')

                elif content.split(' ', 1)[1] == 'status' or content.split(
                        ' ', 1)[1] == '状态':
                    # 管理员指令，查看服务器运行状态。
                    status = no_para.system_status()
                    bot.send(context, status)

                elif content.split(' ', 3)[1] == '炸群' or content.split(
                        ' ', 3)[1] == 'flow':
                    try:
                        times = int(content.split(' ', 3)[2])
                        text = content.split(' ', 3)[3]
                    except IndexError:
                        logrec.logging_error_empty_parameter(context)
                        bot.send(
                            context,
                            '指令出错，您输入的参数有一项或者是两项为空\n正确用法:\n!laffey flow <重复次数> <重复消息（只支持文字）>'
                        )
                    else:
                        if times > 10:
                            times = 10
                        if times <= 10:
                            for i in range(0, times):
                                bot.send(context, text)
                        if times <= 0:
                            bot.send(context, '您输入的次数参数有误！')

            if content.split(' ', 1)[1] == 'info' or content.split(
                    ' ', 1)[1] == '信息':
                bot.send(
                    context, '您的信息:\n聊天类型:' + context['message_type'] + '群号:' +
                    str(context['group_id']) + '\n消息ID:' + str(
                        context['message_id']) + '\n发送者QQ:' + str(
                            context['user_id']))
            elif content.split(' ', 1)[1] == 'version' or content.split(
                    ' ', 1)[1] == '版本':
                #查询版本号
                bot.send(context, no_para.version())
            elif content.split(' ', 1)[1] == 'time' or content.split(
                    ' ', 1)[1] == '时间':
                #报时
                times = no_para.times_str()
                bot.send(context, times)
                voice = no_para.time_harusame()
                bot.send(context, [{
                    "type": "record",
                    "data": {
                        "file": voice
                    }
                }])

            elif content.split(' ', 2)[1] == 'repeat' or content.split(
                    ' ', 2)[1] == '复读':
                if content.split(' ', 3)[2].strip() == 'show' or content.split(
                        ' ', 3)[2].strip() == '显示':
                    bot.send(
                        context, '群组 ' + str(context['group_id']) +
                        ' 的复读频率: \n' + str(repeat) + ' %')
                else:
                    pass

            elif content.split(' ', 2)[1] == 'blacklist' or content.split(
                    ' ', 2)[1] == '黑名单':
                if content.split(' ', 3)[2].strip() == 'list' or content.split(
                        ' ', 3)[2].strip() == '查询':
                    bot.send(
                        context,
                        '群组 ' + str(group_id) + ' 内的机器人黑名单查询完毕，共有 ' + str(
                            len(blacklist)) + ' 项\n内容如下:' + str(
                                '\n'.join(blacklist)))
                else:
                    pass

            elif content.split(' ', 2)[1] == 'baidu' or content.split(
                    ' ', 2)[1] == '百度':
                try:
                    word = content.split(' ', 2)[2]
                except IndexError:
                    # 没有提供指令的时候raise IndexError，被捕捉到了。
                    logrec.logging_error_empty_parameter(context)
                    bot.send(context, '请提供百度搜索词\n指令格式:!laffey baidu <搜索关键词>')
                else:
                    word = urllib.parse.quote(word)
                    result = one_para.baidu(word)
                    #用 URLLib 处理 Baidu 搜索关键词，将其编码成 URL 编码
                    bot.send(context, result)

            elif content.split(' ', 2)[1] == 'check':
                #使用ipcheck.need.sh API查询域名的ICMP和TCP连通性
                try:
                    word = content.split(' ', 2)[2]
                except IndexError:
                    #没有提供指令的时候raise IndexError，被捕捉到了。
                    logrec.logging_error_empty_parameter(context)
                    bot.send(context,
                             '请提供要查询的域名!\n指令格式:!laffey check <待查询连通性域名/IP地址>')
                else:
                    result = network_tools.ip_check_gfwed(word)
                    bot.send(context, result)

            elif content.split(' ', 2)[1] == 'help' or content.split(
                    ' ', 2)[1] == '帮助':
                try:
                    command = content.split(' ', 2)[2]
                except IndexError:
                    # 没有提供指令的时候raise IndexError，被捕捉到了。
                    logrec.logging_error_empty_parameter(context)
                    bot.send(context,
                             '没有提供需要查询帮助的指令\n用法:!laffey help <需要查询帮助的指令名字>')
                else:
                    helps = helping.Help_for_Single_Command(command)
                    bot.send(context, helps)

            elif content.split(' ', 3)[1] == '女装':
                # 女装库
                try:
                    target = content.split(' ', 3)[2]
                except IndexError:
                    logrec.logging_error_empty_parameter(context)
                    bot.send(context, [{
                        "type": "at",
                        "data": {
                            "qq": str(context['user_id'])
                        }
                    }, {
                        "type": "text",
                        "data": {
                            "text": "，请开始你的女装表演"
                        }
                    }])
                else:
                    bot.send(context, [{
                        "type": "at",
                        "data": {
                            "qq": target
                        }
                    }, {
                        "type": "text",
                        "data": {
                            "text": "女装了， "
                        }
                    }, {
                        "type": "at",
                        "data": {
                            "qq": str(context['user_id'])
                        }
                    }, {
                        "type": "text",
                        "data": {
                            "text": "也要女装哦"
                        }
                    }])

            elif content.split(' ', 3)[1] == 'roll':
                try:
                    types = content.split(' ', 3)[2]
                    times = content.split(' ', 3)[3]
                except IndexError:
                    logrec.logging_error_empty_parameter(context)
                    bot.send(
                        context,
                        '你提供的参数不完整，\n抽奖卡池:碧蓝航线日常建造\n使用方法:\n!laffey roll <抽卡类型(l/h/s)> <抽卡次数(最大10次)>'
                    )
                else:
                    rollout = two_paras.roll(times, types)
                    bot.send(context, rollout)

            elif content.split(' ', 2)[1] == 'weather' or content.split(
                    ' ', 2)[1] == '天气':
                try:
                    citi = content.split(' ', 2)[2]
                except IndexError:
                    logrec.logging_error_empty_parameter(context)
                    bot.send(
                        context,
                        '请输入您要查询的城市(仅可以查询中国大陆以及港澳台地区)\n指令格式:!laffey weather <地区>'
                    )
                else:
                    bot.send(context, weather.request_weather(citi))

            elif content.split(' ', 2)[1] == 'ping':
                try:
                    addr = content.split(' ', 2)[2]
                except IndexError:
                    logrec.logging_error_empty_parameter(context)
                    bot.send(context,
                             '请输入您要检测墙内连通性的IP/域名\n指令格式:!laffey ping <IP/域名>')
                else:
                    result = network_tools.ping_test(addr)
                    bot.send(context, result)

            elif content.split(' ', 2)[1] == 'mtr':
                try:
                    addr = content.split(' ', 2)[2]
                except IndexError:
                    logrec.logging_error_empty_parameter(context)
                    bot.send(
                        context,
                        '请输入您要查询MyTraceRoute结果的IP/域名\n由于网络连接问题，这个指令可能需要比较久的时间才能返回\n指令格式:!laffey mtr <IP/域名>'
                    )
                else:
                    result = network_tools.mtr(addr)
                    bot.send(context, result)

            elif content.split(' ', 3)[1] == 'encode' or content.split(
                    ' ', 3)[1] == '加密':
                try:
                    entype = content.split(' ', 3)[2]
                    mingw = content.split(' ', 3)[3]
                except IndexError:
                    logrec.logging_error_empty_parameter(context)
                    bot.send(
                        context,
                        '指令不完整，完整的指令格式为:\n!laffey encode <加密方式>(可选:md5,base64) <明文>'
                    )
                else:
                    if entype == 'md5':
                        coded = encrypt.md5(mingw)
                        bot.send(context, coded)
                    elif entype == 'base64':
                        coded = encrypt.base64_en(mingw)
                        bot.send(context, coded)
                    else:
                        bot.send(context, '加密方式不存在!')

            else:
                pass
        else:
            # 非指令判定复读
            if repeat == 0:
                pass
            else:
                if context['user_id'] == 542154951:
                    repeat = 5
                if context['user_id'] == 1181948577:
                    repeat = 40
                if context['user_id'] == 675571268:
                    repeat = 10
            # 某些人专用
            if choice(range(0, 100)) > 100 - repeat:
                # 当概率大于复读频率时
                if content[0] == '!' or "next time" in content or '[CQ:image,' in content:
                    # 防止触发kjBot和自动禁言指令
                    pass
                elif '我考' in content or '我靠' in content or '我拷' in content:
                    if str(context['user_id']) in blacklist:
                        logrec.logging_repeat_failure(context)
                    else:
                        # 素质！素质！
                        if context['user_id'] == 1181948577 or context['user_id'] == 3563182687:
                            # ABCDE11819专用
                            bot.send(
                                context, context['message'].replace(
                                    '我考', '考' + abcgen()).replace(
                                        '我靠', '靠' + abcgen()).replace(
                                            '我拷', '拷' + abcgen()))
                        elif context['user_id'] in repeat_names:
                            # 其他在列表中的人
                            bot.send(
                                context, context['message'].replace(
                                    '我考', '考' +
                                    repeat_names[context['user_id']]).replace(
                                        '我靠',
                                        '靠' + repeat_names[context['user_id']])
                                .replace(
                                    '我拷',
                                    '拷' + repeat_names[context['user_id']]))
                        else:
                            # 一般群员
                            bot.send(
                                context, context['message'].replace(
                                    '我考', '考你').replace('我靠', '靠你').replace(
                                        '我拷', '拷你'))
                        logrec.logging_repeat_success(context)
                else:
                    if str(context['user_id']) in blacklist:
                        logrec.logging_repeat_failure(context)
                    else:
                        # 针对不同的人替换到不同的内容
                        if context['user_id'] == 1181948577 or context['user_id'] == 3563182687:
                            # 某人专用
                            bot.send(
                                context, context['message'].replace(
                                    '我们', '你们').replace('我', abcgen()))
                        elif context['user_id'] in repeat_names:
                            bot.send(
                                context, context['message'].replace(
                                    '我们', '你们').replace(
                                        '我', repeat_names[context['user_id']]))
                        else:
                            bot.send(context, context['message'].replace(
                                '我', '你'))
                        logrec.logging_repeat_success(context)
    elif context['message_type'] == 'private':
        # 如果接收到的是私聊消息
        if context['user_id'] in admins:
            if context['message'].split()[0] == '!laffey':
                if context['message'].split(' ',2)[1] == 'group':
                    bot.send(context,'当前加入群组\n'+str(bot.get_group_list()))
                    try:
                        message = context['message'].split(' ',2)[2]
                    except IndexError:
                        bot.send(context,"群发消息指令格式错误，可能缺少参数\n格式如下:!laffey group <待发送消息>")
                    else:
                        glist = bot.get_group_list()
                        # 获得 Bot 当前已经加入的群组
                        gblist = [317872133,632331383]
                        # 不启用群发功能的群组
                        for i in range(0,len(glist)):
                            gid = glist[i]['group_id']
                            if gid in gblist:
                                pass
                            else:
                                try:
                                    bot.send_group_msg(group_id=gid, message=message, auto_escape=False)
                                except Exception as e:
                                    print(str(e))
                                    logrec.logging_send_message_exception(gid,message)
                                else:
                                    bot.send(context, '群发:群组' + str(gid) + '的消息已发送成功！')
                                    print('群发:群组' + str(gid) + '的消息已发送成功！')
                elif context['message'].split()[1] == 'update':
                    # 向群组推送更新日志，请修改 laffey/no_para.py
                    glist = bot.get_group_list()
                    # 获得已加入的群组列表
                    for i in range(0, len(glist)):
                        gid = glist[i]['group_id']
                        if gid == 317872133 or gid == 632331383:
                            # in global banned list.
                            pass
                        else:
                            try:
                                bot.send_group_msg(group_id=gid, message=no_para.version(), auto_escape=False)
                            except Exception as e:
                                print(str(e))
                                # TODO:在logrec中记录下bot消息发送失败的异常。
                                logrec.logging_send_message_exception(gid,no_para.version())
                            else:
                                bot.send(context, '群组' + str(gid) + '的消息推送成功!')



# 测试环境:bot.run(host='127.0.0.1', port=8080)
# 启动Bot
app = bot.wsgi
server = wsgiserver.WSGIServer(app,host='127.0.0.1',port=8080)
if __name__ == '__main__':
    no_para.check_dir_existence()
    try:
        print("Bot已启动.")
        server.start()
    except KeyboardInterrupt:
        server.stop()