from tkinter import *
window = Tk()

def rdo_change():
    if var.get() == 1:
        label1.configure(text="파일")
    else:
        label1.configure(text="폴더All")

var = IntVar()

rdo1 = Radiobutton(window, text="파일", variable=var, value=1, command=rdo_change)
rdo2 = Radiobutton(window, text="폴더All", variable=var, value=2, command=rdo_change)

label1 = Label(window, text="선택된 상태", fg="red")

rdo1.pack()
rdo2.pack()
label1.pack()

window.mainloop()
