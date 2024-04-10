from tkinter import *
from time import *

fnameList = ["Jeju1.gif", "Jeju2.gif", "Jeju3.gif", "Jeju4.gif", "Jeju5.gif", "Jeju6.gif", "Jeju7.gif", "Jeju8.gif", "Jeju9.gif"]

num = 0

def clickNext():
    global num
    num += 1
    if num > len(fnameList) - 1:
        num = 0
    pLabel.configure(text=fnameList[num])

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = len(fnameList) - 1
    pLabel.configure(text=fnameList[num])

window = Tk()

pLabel = Label(window, text=fnameList[num])
pLabel.pack(side=TOP)

btnNext = Button(window, text="다음", command=clickNext)
btnPrev = Button(window, text="이전", command
