#__author__ = 'tooweakchen'
#coding=utf-8
#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
#随便查了下为iphone5的分辨率为1136x640像素，因为自己也不用，所以不清楚，也懒得具体求证了
import glob
import Image
def get_list():
    file1=glob.glob(r'/home/tooweakchen/文档/图片/*.jpg')
    return file1

def xiugai(filepath,num):
    f=Image.open(filepath)
    f1=f.resize((1136,640))
    num=str(num)
    f1.save('./'+num+'.jpg','jpeg')

def kongzhi():
    file2=get_list()
    num=11
    for file in file2:
        xiugai(file,num)
        num+=1
if __name__=='__main__':
    kongzhi()