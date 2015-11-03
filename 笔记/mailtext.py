#__author__ = 'tooweakchen'
#coding:utf-8

######################################
#导入 smtplib 和 MIMEText             #
######################################
import smtplib
from email.mime.text import MIMEText

# 你要选择发送者的邮箱
mailto_list=["xxx@xxx.com"]

#设置服务器
mail_host="smtp.xxx.com"

#用户名
mail_user="xxxxx"

#密码
mail_pass="xxxxxx"

#发件箱的后缀
mail_postfix="xxx.com"

###################################
# 发 送 邮 箱                      #
###################################

def send_mail(to_list,sub,content):
    '''
    :param to_list: 要发送的人
    :param sub:     主题
    :param content:  正文内容
    :return:
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg=MIMEText(content)
    msg['Subject']=sub
    msg['From']=me
    msg['To']=";".join(to_list)

    try:
        s=smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.quit()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__=="__main__":

    if send_mail(mailto_list,"这是主题","这是正文"):
        print "发送成功"

    else:
        print "发送失败"


