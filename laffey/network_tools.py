import shlex
import subprocess
import time
import socket
import requests

def ping_test(addr):
    past_time = time.time()
    newaddr = addr.split(' ')
    #为了防止滥用指令，强行去掉参数，只留下域名或者是IP地址。
    cmd = shlex.split("ping -c 5 " + newaddr[-1])
    addr.split(' ')
    try:
        output = subprocess.check_output(cmd)
        output_s = str(output, 'gbk')
    except subprocess.CalledProcessError:
        return ('用时:' + str(round(time.time() - past_time)) +
                's\n域名/IP {0} 无法连接'.format(cmd[-1]))
    else:
        return (output_s.splitlines()[-1].replace(
            'rtt min/avg/max/mdev', 'ICMP Ping结果:最小/平均/最大/极差') + '\n用时:' + str(
                round(time.time() - past_time)) + 's\n域名/IP {0} 连接正常'.format(
                    cmd[-1]))


def mtr(addr):
    past_time = time.time()
    newaddr = addr.split(' ')
    cmd = shlex.split("mtr -c 4 -r -4 " + newaddr[-1])
    #将MTR强行走IPv4
    output = subprocess.check_output(cmd)
    output_s = str(output, 'gbk')
    return ('mtr完成，用时:' + str(round(time.time() - past_time)) + 's' + '\n' + output_s )

def query_dns(address):
    return socket.gethostbyname(address)
    #查询DNS解析，获得域名对应的IP地址

def ip_check_gfwed(host):
    ipaddr = socket.gethostbyname(host)
    #先从本地解析域名到DNS记录
    query_url = 'https://ipcheck.need.sh/api_v2.php?ip='
    content = requests.get(url=query_url+ipaddr)
    result = content.json()
    #从 ipcheck.need.sh 的API获取数据
    icmp_outside_gfw = str(result.get('data')['outside_gfw']['icmp']['alive']).replace('True','回应').replace('False','无回应')
    tcp_outside_gfw = str(result.get('data')['outside_gfw']['tcp']['alive']).replace('True','回应').replace('False','无回应')
    icmp_inside_gfw = str(result.get('data')['inside_gfw']['icmp']['alive']).replace('True','回应').replace('False','无回应')
    tcp_inside_gfw = str(result.get('data')['inside_gfw']['tcp']['alive']).replace('True','回应').replace('False','无回应')
    #处理数据
    return ('目标的IP地址:'+ipaddr+'\n'+'墙外连通性测试原始结果如下:\nICMP:'+ icmp_outside_gfw + ' TCP:' + tcp_outside_gfw +'\n'+ '墙内连通性测试原始结果如下:\nICMP:'+ icmp_inside_gfw + ' TCP:' + tcp_inside_gfw)



