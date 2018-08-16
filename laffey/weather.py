#-*- coding:utf-8 -*-
import requests


def get_weather(city):
    url = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
    appcode = '6835620d8bf447a18707b741bd43b132'
    headers = {'Authorization': 'APPCODE ' + appcode}
    try:
        content = requests.get(url=url, params={'city': city}, headers=headers)
    except requests.exceptions.Timeout:
        return 'TimeoutError'
    except requests.exceptions.ConnectionError:
        return 'ConnectionError'
    except requests.exceptions.HTTPError:
        return 'HTTPError'
    except requests.exceptions.TooManyRedirects:
        return 'TooManyRedirects'
    except:
        return 'OtherError'
    else:
        if content.status_code == 200 and content.json():
            return content.json()
        elif content.status_code == 201:
            return {'result': '城市为空'}
        elif content.status_code == 202:
            return {'result': '城市不存在'}
        elif content.status_code == 203:
            return {'result': '此城市没有天气信息'}
        elif content.status_code == 204:
            return {'result': '没有信息'}
        else:
            return {'result': ''}


ErrorList = [
    'TimeoutError', 'ConnectionError', 'HTTPError', 'TooManyRedirects',
    'OtherError'
]


def request_weather(city):
    try:
        result = get_weather(city).get('result')
        weather = result.get('weather')
        templow = result.get('templow')
        temphigh = result.get('temphigh')
        humid = result.get('humidity')
        return (city + '的天气为:' + weather + ',温度:' + templow + '-' + temphigh +
                '°C,湿度:' + humid + '%')
    except AttributeError:
        return ('未获取到天气信息，可能城市不存在或者输入有误!')
