from tkinter import *
import random

btnList = [None] * 9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif",
             "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
photoList = [None] * 9
i, k, x = 0, 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("210x210")

def shuffle_images():
    random.shuffle(fnameList) 
    for i in range(len(btnList)):
        photoList[i] = PhotoImage(file=fnameList[i])
        btnList[i].configure(image=photoList[i])
        btnList[i].image = photoList[i]

shuffle_button = Button(window, text="섞기", command=shuffle_images)
shuffle_button.pack()

for i in range(0, 9):
    photoList[i] = PhotoImage(file=fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
