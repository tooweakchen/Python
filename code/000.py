#__author__ = 'tooweakchen'
#coding=utf-8
# 第 000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
# 类似于微信未读信息数量那种提示效果
from PIL import Image,ImageDraw,ImageFont

def add_num(filename,num):
    img=Image.open(filename)
    x,y=img.size
    myfont=ImageFont.truetype("/home/tooweakchen/文档/代码/Futura.ttf",30)
    draw=ImageDraw.Draw(img)
    draw.text((x-50,0),str(num),font=myfont,fill='red')
    del draw
    img.save("/home/tooweakchen/文档/代码/xiugai.jpg")
    img.show()


if __name__=='__main__':
    add_num("/home/tooweakchen/文档/代码/abc.jpg",6)
