#-*- coding:utf-8 -*-

import time
import os
import urllib
from random import choice, randint
from bs4 import BeautifulSoup
import requests
import json


def times_str():
    time_hour = time.strftime("%H", time.localtime())
    time_hour = int(time_hour)
    if time_hour == 0:
        str_return = ('凌晨0点。那个，日期已经改变了呢。')
    elif time_hour == 1:
        str_return = ('〇一〇〇。司令官，已经是深夜了。嗯！')
    elif time_hour == 2:
        str_return = ('〇二〇〇。到了2点了呢。稍微有点..没..没什么！一点都没有觉得恐怖的说o(>﹏<)o')
    elif time_hour == 3:
        str_return = ('〇三〇〇。呼啊～呜呜，对不起。从现在开始会更加注意的。')
    elif time_hour == 4:
        str_return = ('〇四〇〇。呐…困Zzz没…没事！一点都没有想睡，嗯！')
    elif time_hour == 5:
        str_return = ('〇五〇〇。司令官，日出的时间到了。早上好～')
    elif time_hour == 6:
        str_return = ('〇六〇〇。就由春雨来替司令官准备早饭可以吗？嗯！那去准备啰～')
    elif time_hour == 7:
        str_return = ('〇七〇〇。早饭是麻婆春…开玩笑的。（欸嘿～）是正常的和风餐点哟～请用。')
    elif time_hour == 8:
        str_return = ('〇八〇〇。今日的输送作战会努力的！。输送和护卫都很重要的！')
    elif time_hour == 9:
        str_return = ('〇九〇〇。村雨姐姐大人的精神怎么样呢。嗯…')
    elif time_hour == 10:
        str_return = ('一〇〇〇。午饭...啊，距离午饭的时间还早呢。对不起。')
    elif time_hour == 11:
        str_return = ('一一〇〇。司令官。午饭要吃什么呢？出去吃也不错呢。那、那个…')
    elif time_hour == 12:
        str_return = ('一二〇〇。欸，可以和司令官一起出去买午餐吗？好高兴呢。')
    elif time_hour == 13:
        str_return = ('一三〇〇。能在西式餐厅用餐真愉快。很高兴呢！嗯！')
    elif time_hour == 14:
        str_return = ('一四〇〇。阿勒？夕立姐姐在那个地方。不危险吗？ ')
    elif time_hour == 15:
        str_return = ('一五〇〇。司令官。那、那个…需要春雨拿一些点心给您吗？ ')
    elif time_hour == 16:
        str_return = ('一六〇〇。天色有些变暗了呢。差不多该到了夕阳西下的时候了。嗯！ ')
    elif time_hour == 17:
        str_return = ('一七〇〇。司令官，夕阳真的很美丽呢。真希望能够一直看见这样的美景。 ')
    elif time_hour == 18:
        str_return = ('一八〇〇。要准备晚饭了呢。司令官，有什么想要的吗？ ')
    elif time_hour == 19:
        str_return = ('一九〇〇。完成了～春雨特制的麻婆春雨（冬粉）。试，试试看吧！ ')
    elif time_hour == 20:
        str_return = ('二〇〇〇。晚饭的味道怎么样呢？胡麻油和五香粉是其中的秘诀哟。 ')
    elif time_hour == 21:
        str_return = ('二一〇〇。司令官，春雨要准备收拾碗盘了，不好意思。 ')
    elif time_hour == 22:
        str_return = ('二二〇〇。司令官，差不多该准备明天输送作战的计划了。那个… ')
    elif time_hour == 23:
        str_return = ('二三〇〇。那，那个。司令官，今天真的辛苦了。 ')
    elif time_hour == 24:
        str_return = ('凌晨0点。那个，日期已经改变了呢。')
    return str_return


def check_dir_existence():
    #检测配置目录存在性
    if os.path.exists(r'./config'):
        pass
    else:
        print("数据文件夹不存在，建立中...")
        os.mkdir(r'./config')
        print("建立数据文件夹成功...")
    if os.path.exists(r'./logs'):
        pass
    else:
        print('日志存储目录不存在，建立中...')
        os.mkdir(r'./logs')
        print('建立日志存储目录成功。')


def laffey_speaks():
    #管理员指令，拉菲放置语音
    return_list = {'string': '', 'voice_link': ''}
    speak_lib = [
        '指挥官休息的还好吗，拉菲现在很有精神，大概', '唔……还算勉勉强强吧', '呣……指挥官，不要摇我……',
        '如果我的躯体不再是这个躯体，你还会看我吗？……', '嗯……我去睡个回笼觉', '指挥官，我们要不要种点花呢？',
        '指挥官不理拉菲，哈啊……都要睡着噜……', '嗯？这是拉菲心情好的表现喔', '拉菲并没有在让指挥官理她，嗯，并没有',
        '拉菲并没有在引诱指挥官跟她玩，嗯，大概', '指挥官指挥官，拉菲，可，怕，吗？', '状态良好……去吧', '指挥官，累了吗？',
        '指挥官……莫非是变态？！', '拉菲，现在，超有精神—— ', '标枪，绫波，Z23……都是好朋友，想和她们，还有大家一直在一起',
        '拉菲并没有在摆姿势引诱指挥官夸她，嗯，并没有', '唔，不过保持这个状态，好累……指挥官，大腿借我，我要睡会儿Zzzzzz',
        '被大家说虽然外表变帅了，本质却一点也没有变，这是在夸拉菲吗？'
    ]
    inde = randint(0, len(speak_lib) - 1)
    return_list['string'] = speak_lib[inde]
    if inde == 0:
        return_list['voice_link'] = "https://img.moegirl.org/common/5/53/%E6%8B%89%E8%8F%B2login.mp3"
    elif inde == 1:
        return_list['voice_link'] = "https://img.moegirl.org/common/9/97/%E6%8B%89%E8%8F%B2mvp.mp3"
    elif inde == 2:
        return_list['voice_link'] = "https://img.moegirl.org/common/a/af/%E6%8B%89%E8%8F%B2touch_head.mp3"
    elif inde == 3:
        return_list['voice_link'] = "https://img.moegirl.org/common/a/a4/%E6%8B%89%E8%8F%B2detail.mp3"
    elif inde == 4:
        return_list['voice_link'] = "https://img.moegirl.org/common/9/91/%E6%8B%89%E8%8F%B2upgrade.mp3"
    elif inde == 5:
        return_list['voice_link'] = "https://img.moegirl.org/common/f/fe/%E6%8B%89%E8%8F%B2main1.mp3"
    elif inde == 6:
        return_list['voice_link'] = "https://img.moegirl.org/common/c/c9/%E6%8B%89%E8%8F%B2main2.mp3"
    elif inde == 7:
        return_list['voice_link'] = "https://img.moegirl.org/common/7/7b/%E6%8B%89%E8%8F%B2main3.mp3"
    elif inde == 8:
        return_list['voice_link'] = "https://img.moegirl.org/common/d/db/%E6%8B%89%E8%8F%B2main4.mp3"
    elif inde == 9:
        return_list['voice_link'] = "https://img.moegirl.org/common/2/29/%E6%8B%89%E8%8F%B2main5.mp3"
    elif inde == 10:
        return_list['voice_link'] = "https://img.moegirl.org/common/0/07/%E6%8B%89%E8%8F%B2main6.mp3"
    elif inde == 11:
        return_list['voice_link'] = "https://img.moegirl.org/common/6/6a/%E6%8B%89%E8%8F%B2skill.mp3"
    elif inde == 12:
        return_list['voice_link'] = "https://img.moegirl.org/common/0/0a/%E6%8B%89%E8%8F%B2touch1.mp3"
    elif inde == 13:
        return_list['voice_link'] = "https://img.moegirl.org/common/e/e0/%E6%8B%89%E8%8F%B2touch2.mp3"
    return return_list


def system_status():
    mem = {}
    f = open("/proc/meminfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2: continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = int(var) * 1024.0
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1'] = con[0]
    loadavg['lavg_5'] = con[1]
    loadavg['lavg_15'] = con[2]
    loadavg['nr'] = con[3]
    loadavg['last_pid'] = con[4]
    hd = {}
    disk = os.statvfs("/")
    avahd = disk.f_bsize * disk.f_bavail / (1024 * 1024)
    caphd = disk.f_bsize * disk.f_blocks / (1024 * 1024)
    frehd = disk.f_bsize * disk.f_bfree / (1024 * 1024)
    usedRam = str(int((mem['MemUsed']) / (1024 * 1024)))
    topRam = str(int(mem['MemTotal'] / (1024 * 1024)))
    return ("内存占用:" + usedRam + 'M/' + topRam + 'M(' + str(
        round(float((mem['MemUsed']) / int(mem['MemTotal'])) * 100)) + '%)\n' +
            "负载:" + str(loadavg['lavg_1']) + ' ' + str(loadavg['lavg_5'])
            + ' ' + str(loadavg['lavg_15']) + "\n硬盘:" + str(
                int(caphd - avahd)) + 'M/' + str(int(caphd)) + 'M')


def time_harusame():
    time_hour = time.strftime("%H", time.localtime())
    time_hour = int(time_hour)
    if time_hour == 0:
        return "https://img.moegirl.org/common/a/a1/Harusame30.mp3"
    elif time_hour == 1:
        return "https://img.moegirl.org/common/5/52/Harusame31.mp3"
    elif time_hour == 2:
        return "https://img.moegirl.org/common/d/d2/Harusame32.mp3"
    elif time_hour == 3:
        return "https://img.moegirl.org/common/0/09/Harusame33.mp3"
    elif time_hour == 4:
        return "https://img.moegirl.org/common/c/c5/Harusame34.mp3"
    elif time_hour == 5:
        return "https://img.moegirl.org/common/f/f3/Harusame35.mp3"
    elif time_hour == 6:
        return "https://img.moegirl.org/common/6/6d/Harusame36.mp3"
    elif time_hour == 7:
        return "https://img.moegirl.org/common/d/df/Harusame37.mp3"
    elif time_hour == 8:
        return "https://img.moegirl.org/common/6/67/Harusame38.mp3"
    elif time_hour == 9:
        return "https://img.moegirl.org/common/6/66/Harusame39.mp3"
    elif time_hour == 10:
        return "https://img.moegirl.org/common/9/91/Harusame40.mp3"
    elif time_hour == 11:
        return "https://img.moegirl.org/common/4/46/Harusame41.mp3"
    elif time_hour == 12:
        return "https://img.moegirl.org/common/9/92/Harusame42.mp3"
    elif time_hour == 13:
        return "https://img.moegirl.org/common/8/89/Harusame43.mp3"
    elif time_hour == 14:
        return "https://img.moegirl.org/common/7/7f/Harusame44.mp3"
    elif time_hour == 15:
        return "https://img.moegirl.org/common/4/45/Harusame45.mp3"
    elif time_hour == 16:
        return "https://img.moegirl.org/common/3/32/Harusame46.mp3"
    elif time_hour == 17:
        return "https://img.moegirl.org/common/a/a2/Harusame47.mp3"
    elif time_hour == 18:
        return "https://img.moegirl.org/common/0/08/Harusame48.mp3"
    elif time_hour == 19:
        return "https://img.moegirl.org/common/4/49/Harusame49.mp3"
    elif time_hour == 20:
        return "https://img.moegirl.org/common/6/6a/Harusame50.mp3"
    elif time_hour == 21:
        return "https://img.moegirl.org/common/7/75/Harusame51.mp3"
    elif time_hour == 22:
        return "https://img.moegirl.org/common/8/8c/Harusame52.mp3"
    elif time_hour == 23:
        return "https://img.moegirl.org/common/8/83/Harusame53.mp3"
    elif time_hour == 24:
        return "https://img.moegirl.org/common/a/a1/Harusame30.mp3"
    else:
        pass


def version():
    info = [
        'Laffey & Shuvi Bot Engine Under Test',
        '这个 Bot 的当前版本号: 180817 内部代号:Poki',
        '更新日志:',
        '·服务器移至阿里云（深圳）服务器，今后的连接将会更加稳定',
        '·修正了几处文本字符串',
        '·移除了由于GFW原因而无法使用的几个功能',
    ]
    return '\n'.join(info)
