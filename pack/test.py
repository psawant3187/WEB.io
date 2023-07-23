from tkinter import *

root =Tk()
root.geometry("400x400")

global button
button = PhotoImage(file=r"start.png")

button1 = Button(root,image=button,borderwidth=0,highlightthickness=0)
button1.pack(pady=20)

root.mainloop()
