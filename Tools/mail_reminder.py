import yagmail
import time
import traceback
import os

sender_mail = 'zzs45622660@qq.com'
sender_password = 'rboieudsrpjhddga'
# 获取当前脚本的文件名
script_name = os.path.basename(__file__)

# 得保证服务器能联网
yag = yagmail.SMTP(user = sender_mail, password = sender_password, host = 'smtp.qq.com')
starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
yag.send(to = [sender_mail], subject = f'【{script_name }开始运行】', contents = [f'python程序程序开始运行\n时间:\n{starttime}\n此条消息确保程序能够发邮件提醒'])

if __name__ == '__main__':
    try:
        a= [5,6]
        b=int(a)
        # 登录邮箱提醒程序完成
        endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        yag.send(to = [sender_mail], subject = f'【{script_name }运行完成】', contents = [f'python程序运行完成啦!\n时间:\n{endtime}'])
    except Exception as ex:
        print(traceback.format_exc())
        endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        error_name=repr(ex)
        error_detail=traceback.format_exc()
        yag.send(to = [sender_mail], subject = f'【{script_name }异常中断】', contents = [f'错误名称：\n{error_name}\n\n详细错误:\n{error_detail}\n时间:\n{endtime}'])
                                  