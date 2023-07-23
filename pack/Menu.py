from pack.Regular import *
from pack.Shopping import *
# import tkinter as tk

def MENU(menu):
    menu.title("WEB.IO")
    menu.iconbitmap(R"WEB.ico")
    menu['background'] = '#363434'
    app_width = 540
    app_height = 540

    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()

    x = ((screen_width - app_width) / 2)
    y = ((screen_height - app_height) / 2)

    menu.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    global melo
    melo = PhotoImage(file=R"WebScrapper.png")
    label1 = Label(image=melo, width=430, height=200)
    label1.pack()

    global reg
    reg = PhotoImage(file=R"Regular.png")

    global shop
    shop = PhotoImage(file=R"Shopping.png")

    regular = tk.Button(menu, image=reg, highlightthickness=0, borderwidth=0, command=lambda: change2(menu))
    regular.pack(side=tk.TOP, pady=20)

    shopping = tk.Button(menu, image=shop, highlightthickness=0, borderwidth=0, command=lambda: change3(menu))
    shopping.pack(side=tk.TOP, pady=20)

def change2(menu):
    menu.destroy()
    regcall()

def change3(menu):
    menu.destroy()
    fun2()

def call2():
    menu = tk.Tk()
    MENU(menu)
    menu.mainloop()

call2