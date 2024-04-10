from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import PhotoImage

def func_open():
    global photo
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    convert_to_greyscale(photo)

def convert_to_greyscale(photo):
    width, height = photo.width(), photo.height()
    for y in range(height):
        for x in range(width):
            r, g, b = photo.get(x, y)
            grey = int((r + g + b) / 3)
            photo.put("#%02x%02x%02x" % (grey, grey, grey), (x, y))

def func_exit():
    window.quit()
    window.destroy()

window = Tk()
window.geometry("500x500")
window.title("이미지 처리기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
