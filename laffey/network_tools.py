import shlex 
import subprocess 
import time 
# Tokenize the shell command # cmd will contain ["ping","-c1","google.com"]
def ping_test(addr):
        past_time = time.time()
        newaddr = addr.split(' ')
        cmd=shlex.split("ping -c 5 " + newaddr[-1])
        addr.split(' ')
        try:
            output = subprocess.check_output(cmd)
            output_s = str(output,'gbk')
        except subprocess.CalledProcessError:
        #Will print the command failed with its exit status
            return ('\n用时:'+ str(round ( time.time() - past_time )) + 's\n域名/IP {0} 无法连接'.format(cmd[-1]))
        else:
            return (output_s.splitlines()[-1].replace('rtt min/avg/max/mdev','ICMP Ping结果:最小/平均/最大/极差') + '\n用时:'+ str(round ( time.time() - past_time )) + 's\n域名/IP {0} 连接正常'.format(cmd[-1]))
def mtr(addr):
    past_time = time.time()
    newaddr = addr.split(' ')
    cmd=shlex.split("mtr -r " + newaddr[-1]) 
    output = subprocess.check_output(cmd)
    output_s = str(output,'gbk')
    return (output_s + '用时:'+ str(round ( time.time() - past_time )) + 's')