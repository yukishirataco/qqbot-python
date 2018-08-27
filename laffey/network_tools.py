import shlex
import subprocess
import time
import socket


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


