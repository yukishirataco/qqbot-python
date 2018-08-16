# -*- coding:utf-8 -*-
#加密类调用API
import hashlib
import base64


def md5(source):
    #MD5加密
    encoded = hashlib.md5()
    encoded.update(source.encode("utf8"))
    return str(encoded.hexdigest())


def md5_addsalt(source, salt):
    #MD5加盐加密
    encoded = hashlib.md5()
    encoded.update(source.encode("utf8") + salt.encode("utf8"))
    return str(encoded.hexdigest())


def base64_en(source):
    #Base64加密
    return base64.b64encode(source.encode(encoding='utf-8')).decode()


def base64_de(source):
    #Base64解密
    return base64.b64decode(source)
