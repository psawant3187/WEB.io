import tkinter as tk

import pack.Menu
from pack import Menu
from tkinter import scrolledtext, messagebox, PhotoImage, Label, END
import requests
from bs4 import BeautifulSoup
from goose3 import Goose
from datetime import datetime

def fun2():
    shop = tk.Tk()
    shop.title("WEB.IO")
    shop.iconbitmap(r"WEB.ico")
    shop['background'] = '#383838'

    app_width = 720
    app_height = 720

    screen_width = shop.winfo_screenwidth()
    screen_height = shop.winfo_screenheight()

    x = ((screen_width - app_width) / 2)
    y = ((screen_height - app_height) / 2)

    shop.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    global scrape
    scrape = PhotoImage(file=r"Scrape.png")
    # image1 = Label(image=scrape,borderwidth=0)
    # image1.pack(pady=20)

    global clear
    clear = PhotoImage(file=r"Clear.png")
    # image1 = Label(image=clear, width=500, height=40)

    global entry
    entry = PhotoImage(file=r"Entry.png")

    global main
    main = PhotoImage(file=R"Back.png")

    url_label = tk.Label(shop, image=entry, borderwidth=0,highlightthickness=0)
    url_label.pack(side=tk.TOP, pady=20)

    url_entry = tk.Entry(shop, width=50, font=('Arial', 12), fg="Black", bg="#c9c7c7")
    url_entry.pack(side=tk.TOP)

    scrape_button = tk.Button(shop, image=scrape,borderwidth=0, highlightthickness=0)
    scrape_button.pack(side=tk.TOP, pady=20)

    clear_button = tk.Button(shop, image=clear, borderwidth=0, highlightthickness=0)
    clear_button.pack(side=tk.BOTTOM, pady=20)

    back_button = tk.Button(shop, image=main,highlightthickness=0,borderwidth=0,command=lambda:back2(shop))
    back_button.pack(side=tk.BOTTOM, pady=20)

    output_area = tk.Text(shop, width=80, height=50, wrap=tk.WORD, bg='#c9c7c7', fg="Black", borderwidth=3)
    # output_area.configure(state="disabled")
    output_area.pack(side=tk.BOTTOM, pady=20)

def back2(shop):
    shop.destroy()
    pack.Menu.call2()

def call4():
    shop = tk.Tk()
    fun2(shop)
    shop.mainloop()
fun2