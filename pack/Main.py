import pack.Login
from pack.Menu import *
from pack.About import *
def start(main):
    main.title("WEB.IO")
    main.iconbitmap(R"WEB.ico")
    main['background']='#383838'
    app_width = 540
    app_height=540

    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    x = ((screen_width-app_width)/2)
    y = ((screen_height-app_height)/2)

    main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    global button
    button = PhotoImage(file=r"start.png")
    # image = Label(image=button,borderwidth=0,background='#383838')

    global abu
    abu = PhotoImage(file=R"About1.png")

    global  logo
    logo = PhotoImage(file=R"WebScrapper.png")
    label1 = Label(image=logo,width=564,height=308)
    label1.pack()

    global log
    log =PhotoImage(file=R"Logout.png")

    label2=Label(main,text="Contact Us at:Datta Meghe College of Engineering,Plot 98,Sector 3",font=('Comic_Sans',10),bg='#363434')
    label2.pack(side=tk.BOTTOM)

    label3=Label(main,text="Phone No.7045272526",font=('Comic_Sans',10),bg='#363434')
    label3.pack(side=tk.BOTTOM)

    startsc = Button(main,image=button,borderwidth=0,command=lambda:startscr(main),highlightthickness=0)
    startsc.pack(side=tk.TOP,pady=20)

    about = Button(main,image=abu,borderwidth=0,highlightthickness=0,command=lambda:ab(main))
    about.pack(side=tk.TOP,pady=20)

    logout = Button(main,image=log,borderwidth=0,highlightthickness=0,command=lambda :lgo(main))
    logout.pack(side=tk.TOP,pady=20)

def ab(main):
    main.destroy()
    about()

def startscr(main):
    main.destroy()
    call2()

def Macall():
    main=Tk()
    start(main)
    main.mainloop()

def lgo(main):
    main.destroy()
    pack.Login.Locall()

Macall()