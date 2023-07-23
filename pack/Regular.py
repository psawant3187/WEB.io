import tkinter as tk
from tkinter import scrolledtext, messagebox, PhotoImage, Label, END
import requests
from bs4 import BeautifulSoup
from goose3 import Goose
from datetime import datetime

import pack.Menu
from pack.Menu import *

def fun(a):
    def clear_output():
        output_area.delete(1.0, END)

    def scrape_website():
        url = url_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return

        # Scraping code
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            g = Goose()
            article = g.extract(url=url)

            title = article.title
            body = article.cleaned_text
            if not body:
                paragraphs = soup.find_all("p")
                body = "\n\n".join(p.text for p in paragraphs)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return

        # Displaying the output in the text widget
        output_area.configure(state="normal")
        output_area.delete(1.0, END)
        output_area.insert(tk.END, f"{title}\n\n{body}")
        # output_area.configure(state="disabled")

        # Saving the output to a file
        filename = f"{datetime.now().strftime('%HHrs-%MMin--%d-%m-%Y')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n{body}")

        messagebox.showinfo("Success", f"The output file has been saved to {filename}")

    # GUI code
    a.title("WEB.IO")
    a.iconbitmap(r"WEB.ico")
    a['background'] = '#383838'

    app_width = 720
    app_height = 640

    screen_width = a.winfo_screenwidth()
    screen_height = a.winfo_screenheight()

    x = ((screen_width - app_width) / 2)
    y = ((screen_height - app_height) / 2)

    a.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

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

    url_label = tk.Label(a, image=entry, borderwidth=0)
    url_label.pack(side=tk.TOP, pady=20)

    url_entry = tk.Entry(a, width=50, font=('Arial', 12), fg="Black", bg="#c9c7c7")
    url_entry.pack(side=tk.TOP)

    scrape_button = tk.Button(a, image=scrape, command=scrape_website, borderwidth=0, highlightthickness=0)
    scrape_button.pack(side=tk.TOP, pady=20)

    clear_button = tk.Button(a, image=clear, command=clear_output, borderwidth=0, highlightthickness=0)
    clear_button.pack(side=tk.BOTTOM, pady=20)

    back_button = tk.Button(a,image=main,command=lambda:back(a),borderwidth=0,highlightthickness=0)
    back_button.pack(side=tk.BOTTOM,pady=20)

    output_area = tk.Text(a, width=80, height=50, wrap=tk.WORD, bg='#c9c7c7', fg="Black", borderwidth=3)
    # output_area.configure(state="disabled")
    output_area.pack(side=tk.BOTTOM, pady=20)

    a.mainloop()

def back(a):
    a.destroy()
    pack.Menu.call2()

def regcall():
    a=tk.Tk()
    fun(a)
    a.mainloop()


regcall



