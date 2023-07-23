import tkinter
from tkinter import *

import pack.Main


def about():
    root = Tk()
    root.title("WEB.IO")
    root.iconbitmap(R"WEB.ico")
    root['background'] = '#383838'
    app_width = 540
    app_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = ((screen_width - app_width) / 2)
    y = ((screen_height - app_height) / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    global section
    section = PhotoImage(file=R"About.png")

    global back
    back = PhotoImage(file=R"Back.png")

    ab = Label(root,image=section,highlightthickness=0,borderwidth=0)
    ab.pack(side=tkinter.TOP)

    b = Button(root,image=back,highlightthickness=0,borderwidth=0,command=lambda:b2m(root))
    b.pack(side=tkinter.BOTTOM,pady=10)

    root.mainloop()

def b2m(root):
    root.destroy()
    pack.Main.call()

about