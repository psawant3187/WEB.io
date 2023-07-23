from pack.Main import *
import tkinter as tk
def start1(login):
	def loginButton():
		username = entry_username.get()
		password = entry_password.get()

		if username == "admin" and password == "3187@admin1336":
			login.destroy()
			Macall()
		else:
			messagebox.showerror("Error","Incorrect username or password")

	login.title("WEB.IO")
	login.iconbitmap(R"WEB.ico")
	login['background'] = '#363434'
	app_width = 540
	app_height = 540

	screen_width = login.winfo_screenwidth()
	screen_height = login.winfo_screenheight()

	x = ((screen_width - app_width) / 2)
	y = ((screen_height - app_height) / 2)

	login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

	global logo
	logo = PhotoImage(file=R"WebScrapper.png")
	welo = Label(image=logo, width=550, height=200)
	welo.pack()

	global gin
	gin = PhotoImage(file=R"Login.png")

	global user
	user = PhotoImage(file=R"Username.png")

	global pas
	pas= PhotoImage(file=R"Pasword.png")

	label_username = tk.Label(login,image=user,borderwidth=0,highlightthickness=0)
	label_username.pack(side=tk.TOP,pady=10)

	entry_username = tk.Entry(login,width=30,font=('Arial',14))
	entry_username.pack(side=tk.TOP,pady=10)

	label_password = tk.Label(login,image=pas,borderwidth=0,highlightthickness=0)
	label_password.pack(side=tk.TOP,pady=20)

	entry_password = tk.Entry(login, show="*",font=('Arial',14),width=30)
	entry_password.pack(side=tk.TOP,pady=20)

	button_login = tk.Button(login,image=gin,command=lambda:loginButton(),highlightthickness=0,borderwidth=0)
	button_login.pack(side=tk.BOTTOM,pady=20)

def Locall():
	login = tk.Tk()
	start1(login)
	login.mainloop()

Locall()