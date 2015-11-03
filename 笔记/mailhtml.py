#__author__ = 'tooweakchen'
#coding:utf-8

############################
# 导入MIMEText 和 smtplib   #
############################
from email.mime.text import MIMEText
import smtplib

mailto_list=['1292095940@qq.com']
mail_host="smtp.xxx.com"
mail_user="xxxxxxxxx"
mail_pass="xxxxxxxxx"
mail_postfix="xxxx.com"

def send_mail(to_list,sub,content):
    '''
    :param to_list:
    :param sub:
    :param content:
    :return:
    '''
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg=MIMEText(content,_subtype='html',_charset='utf-8')
    msg['Subject']=sub   #设置主题
    msg['From']=me
    msg['To']=";".join(to_list)

    try:
        s=smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__=='__main__':
    if send_mail(mailto_list,"这是主题","<a href='http://www.baidu.com'>这是正文</a>"):
        print "发送成功"
    else:
        print "发送失败"