#__author__ = 'tooweakchen'
#coding=utf-8
#第 010 题：使用 Python 生成类似于下图中的字母验证码图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#这里是随机选择一个字母
def rndchar():
    return chr(random.randint(65,122))
#这里是随机颜色
def rndcolor1():
    return (random.randint(0,127),random.randint(0,127),random.randint(0,127))

def rndcolor2():
    return (random.randint(128,255),random.randint(128,255),random.randint(128,255))
def yanzhengma():
    #这里创建一张白色的图片
    img=Image.new('RGB',(240,60),(255,255,255))
    myfont=ImageFont.truetype("/home/tooweakchen/文档/代码/Futura.ttf",40)
    draw=ImageDraw.Draw(img)
    #这里就是把这张白色的图片上的每个点上色
    for x in range(240):
        for y in range(60):
            draw.point((x,y),fill=rndcolor1())
    #这里就是4个验证码
    for i in range(4):
        draw.text((60*i+8,0),rndchar(),font=myfont,fill=rndcolor2())

    del draw
    #这里是滤镜模糊作用
    img=img.filter(ImageFilter.BLUR)
    img.show()
    img.save("/home/tooweakchen/文档/代码/010.jpg")

if __name__=='__main__':
    yanzhengma()
