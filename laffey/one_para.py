#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import time
import os
import urllib 
from random import choice,randint
from bs4 import BeautifulSoup
import requests
import json

def baidu(words):
    #百度搜索指令
    words[14:].strip()
    #获得字符串，去除空格
    url=r'http://www.baidu.com/s?wd='
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    source = requests.get(url+words,headers=headers)
    source.encoding = 'utf-8'
    soup=BeautifulSoup(source.text,'lxml')
    tables = soup.find_all(name='div',attrs={"class":"nums"})
    str_return = '百度:'+url+words+'\n'+str(tables[0])[133:-13]
    return str_return

def pixiv(pid):
    pid.strip()
    if pid.isdigit():
        str_return = 'https://www.pixiv.net/i/'+pid
    else:
        str_return = '您的输入有误，请查看是否混入了非数字字符。'
    return str_return

def google(words):
    words.strip()
    r = requests.get('http://www.google.com/search',
            params={'q':'"'+words+'"',
                    "tbs":"li:1"}
        )
    soup = BeautifulSoup(r.text,'lxml')
    str_return = '谷歌:http://www.google.com/search?q='+words+'\n'+soup.find('div',{'id':'resultStats'}).text
    return str_return

def booru(tags):
    past = time.time()
    return_data = {'string':'','link':''}
    source=requests.get(r'http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags='+tags+' rating:safe -highres')
    soup = BeautifulSoup(source.text, "lxml")
    #如果API页面能正常打开
    num = int(soup.find('posts')['count'])
    #就用bs4解析网页
    maxpage = int(round(num/100))
    if maxpage <= 1:
        page=0
    else:
        page=randint(0,maxpage)
    source=requests.get(r'http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags='+tags+' rating:safe -highres'+'&pid='+str(page))
    soup = BeautifulSoup(source.text, "lxml")
    t=soup.find('posts')
    p=t.find_all('post')
    if num < 100:
        pic=p[randint(0,num-1)]
    elif page==maxpage:
        pic=p[randint(0,num%100-1)]
    else:
        pic=p[randint(0,99)]
    if num > 0:
        return_data['string'] = '用时'+str(round(time.time()-past))+'s\n对于tag：'+tags+'\n'+'Gelbooru上有'+str(num)+'张图\n这是随机一张图:'
        return_data['link'] = pic['sample_url']
    elif num ==0:
        return_data['string'] = '对于tag：'+tags+'\n'+'Gelbooru上没有找到图片'
    return return_data

def read_config(group_id):
    #读取当前群组内的配置文件
    group_id = group_id
    conf = r'./config/'+str(group_id)+'.json'
    if os.path.exists(conf):
        pass
    else:
        print('群组 '+str(group_id)+" 的配置文件不存在，建立中...")
        with open(conf,'w') as def_conf:
            default_conf = { "blacklist" : ['0'] , "repeat" : 20 ,"flag" : 0 }
            def_conf.write(json.dumps(default_conf))
            def_conf.close()
            print("写入配置文件成功")
    with open(conf,'r') as grp_con:
        group_cfg = json.load(grp_con)
    return group_cfg


