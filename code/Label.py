#__author__ = 'tooweakchen'
#coding:utf-8

from Tkinter import *
'''
#Python - Tkinter Label :
# 这个小工具，实现了显示框，
# 在那里你可以把文本或图像。

def get_title(root,title):
    if title is not None or title!='':
        root.title(title)
    else:
        root.title("卧槽")

root = Tk()
root.geometry('670x600')
title="python初学者"
get_title(root,title)
label = Label(root, text='Hello WOrld', relief=RAISED,font='Helvetica 20 bold' )
label.pack()
root.mainloop()
from Tkinter import *

def onclick():
   pass

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello....afssa.")
text.insert(END, "Bye Bye...savv..")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
root.mainloop()

from Tkinter import *

root = Tk()

var = StringVar()
label = Message( root, text="Hey!? How are you doing?" )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()

from Tkinter import *

master = Tk()
master.geometry('600x700')
w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()
from Tkinter import *

root = Tk()
root.geometry('600x700')
scrollbar = Scrollbar(root)
scrollbar.pack( side =RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH)
scrollbar.config( command = mylist.yview )
mainloop()
from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
top.mainloop()
'''

from Tkinter import *
root=Tk()
CheckVar1=IntVar()
CheckVar2=IntVar()
c1=Checkbutton(root,text="Music",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
c2=Checkbutton(root,text="Video",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
c1.pack(fill=Y,expand=1)
c2.pack(fill=Y,expand=1)
root.mainloop()