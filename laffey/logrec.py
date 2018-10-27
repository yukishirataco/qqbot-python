import time
'''
bot 日志记录模块
'''
dates = time.strftime('%Y-%m-%d', time.localtime())
times = time.strftime("%H:%M:%S", time.localtime())
# 日志数据，时间戳
logfile = r'./logs/' + dates + '.log'


# 日志文件直接保存到 bot 所在的根目录里
def logging_repeat_success(context):
    #用户位于黑名单之外，不复读
    gid = str(context['group_id'])
    uid = str(context['user_id'])
    message = context['message']
    with open(logfile, 'a') as logout:
        logout.write('[信息][' + dates + ' ' + times + ']' + ' 群组:' + gid +
                     ' 内用户:' + uid + '发的消息' + message + '被复读了')
        logout.close()
    print('[信息][' + dates + ' ' + times + ']' + ' 群组:' + gid + ' 内用户:' + uid +
          '发的消息 ' + message + ' 被复读了')


def logging_repeat_failure(context):
    gid = str(context['group_id'])
    uid = str(context['user_id'])
    with open(logfile, 'a') as logout:
        logout.write('[信息][' + dates + ' ' + times + ']' + ' 群组:' + gid +
                     ' 内用户:' + uid + '由于位于黑名单内，复读失败')
        logout.close()
    print('[信息][' + dates + ' ' + times + ']' + ' 群组:' + gid + ' 内用户:' + uid +
          '由于位于黑名单内，复读失败')


def logging_command(context):
    gid = str(context['group_id'])
    uid = str(context['user_id'])
    message = context['message']
    with open(logfile, 'a') as logout:
        logout.write('[信息][' + dates + ' ' + times + ']' + ' 群组: ' + gid +
                     ' 内用户: ' + uid + '使用了指令: ' + message)
        logout.close()
    print('[信息][' + dates + ' ' + times + ']' + ' 群组: ' + gid + ' 内用户: ' +
          uid + '使用了指令: ' + message)


def logging_error_empty_parameter(context):
    gid = str(context['group_id'])
    uid = str(context['user_id'])
    message = context['message']
    with open(logfile, 'a') as logout:
        logout.write('[错误][' + dates + ' ' + times + ']' + ' 群组: ' + gid +
                     ' 内用户: ' + uid + '使用指令: ' + message + ' 时出现错误:未提供参数')
        logout.close()
    print('[错误][' + dates + ' ' + times + ']' + ' 群组: ' + gid + ' 内用户: ' +
          uid + '使用指令: ' + message + ' 时出现错误:未提供参数')


def logging_bad_type(context):
    gid = str(context['group_id'])
    uid = str(context['user_id'])
    message = context['message']
    with open(logfile, 'a') as logout:
        logout.write('[错误][' + dates + ' ' + times + ']' + ' 群组: ' + gid +
                     ' 内用户: ' + uid + '使用指令: ' + message + ' 时出现错误:错误的参数类型')
        logout.close()
    print('[错误][' + dates + ' ' + times + ']' + ' 群组: ' + gid + ' 内用户: ' +
          uid + '使用指令: ' + message + ' 时出现错误:错误的参数类型')

def logging_send_message_exception(gid,message):
    #用户位于黑名单之外，不复读
    with open(logfile, 'a') as logout:
        logout.write('[信息][' + dates + ' ' + times + ']' + ' 群组:' + gid +
                     ' 内推送的消息' + message + '发送失败!')
        logout.close()
    print('[信息][' + dates + ' ' + times + ']' + ' 群组:' + gid +
            ' 内推送的消息' + message + '发送失败!')


