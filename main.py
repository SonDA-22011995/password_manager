# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(700, 400)
root.title("Password Manager")

mainframe = ttk.Frame(root, padding=(60, 10, 60, 10))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

canvas = Canvas(mainframe, width=200, height=189)
logo = PhotoImage(file='./static/logo.png')
canvas.create_image(80, 100, image=logo)

website_label = ttk.Label(mainframe, text="Website:", font=('Helvetica', 11, 'bold'))
website = ttk.Entry(mainframe)
username_label = ttk.Label(mainframe, text="Website/User name:", font=('Helvetica', 11, 'bold'))
username = ttk.Entry(mainframe)
password_label = ttk.Label(mainframe, text="Password:", font=('Helvetica', 11, 'bold'))
password = ttk.Entry(mainframe)
generate_password_bt = ttk.Button(mainframe, text="Generate Password")
add_password_bt = ttk.Button(mainframe, text="Add")

canvas.grid(row=0, column=1, columnspan=2)
website_label.grid(column=0, row=1, sticky=(W))
website.grid(column=1, row=1, columnspan=2, sticky=(W,E))
username_label.grid(column=0, row=2, sticky=(W))
username.grid(column=1, row=2, columnspan=2, sticky=(W,E))
password_label.grid(column=0, row=3, sticky=(W))
password.grid(column=1, row=3, sticky=(W,E))
generate_password_bt.grid(column=2, row=3, sticky=(W,E))
add_password_bt.grid(column=1, row=4, columnspan=2, sticky=(W,E))

website.focus()

root.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
root.mainloop()