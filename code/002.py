#__author__ = 'tooweakchen'
#coding=utf-8

#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import mysql.connector

def store_mysql(filepath):
    con=mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='test')
    cur=con.cursor()

    #判断表是否已经存在
    cur.execute('show tables in test;')
    tables=cur.fetchall()
    findtables=False
    for table in tables:
        if 'code' in table:
            findtables=True

    if not findtables:
        cur.execute("create table code(id int not null AUTO_INCREMENT,code varchar(30) not null,PRIMARY KEY (id))")

    f=open(filepath,'rb')
    #file1=open('/home/tooweakchen/文档/代码/mysql.txt','wb')
    for line in f.readlines():
        code=line.strip()
        cur.execute("insert into test.code(code) values(%s);",[code])

    #aa=cur.execute("select * from test.code")
    #print aa
    #info=cur.fetchmany(aa)
    #for ii in info:
    #    ch=str(ii)
    #    file1.write(ch+'\n')

    #file1.close()
    f.close()

    con.commit()
    cur.close()
    con.close()


if __name__=='__main__':
    store_mysql('/home/tooweakchen/文档/代码/随机数.txt')