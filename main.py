# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
from pathlib import Path
import csv

import pandas as pd
from tkinter import messagebox

HEADER = ['Website', 'UserName', 'Password']
PATH = "./static/data.csv"

data = None
path = Path(PATH)

def create_data_file():
    with path.open(mode="w") as csvfile:
        # Create a csv.writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(HEADER)

        #log
        print(f"CSV file '{PATH}' created successfully using the csv module.")

def load_data():
    global data
    if not path.exists():
        create_data_file()

    data = pd.read_csv(PATH)

def check_if_exists():
    if data is None:
        return False

    website_data = website.get().lower()
    username_data = username.get().lower()

    return not data[
        (data["Website"].str.lower() == website_data) &
        (data["UserName"].str.lower() == username_data)
    ].empty


def save_data():
    website_data =  website.get()
    username_data = username.get()
    password_data = password.get()

    user_data = [website_data, username_data, password_data]
    data.loc[len(data)] = user_data

    data.to_csv(path, index=False, header=True)

def update_data():
    website_data = website.get().lower()
    username_data = username.get().lower()
    password_data = password.get()

    data.loc[
        (
            (data['Website'].str.lower() == website_data) &
            (data['UserName'].str.lower() == username_data)
        ),
        'Password'
    ] = password_data

    data.to_csv(path, index=False, header=True)

def find_data(value, column) -> list[dict]:
    value = value.lower()
    filtered  = data[(data[column].str.lower() == value)]
    return filtered.to_dict(orient='records')

def add_action():
    if not check_if_exists():
        save_data()
        website.delete(0, END)
        password.delete(0, END)
    else:
        messagebox.showwarning(
            message="Your website already has a user and a password",
            icon='warning', title='Save password'
        )

def update_action():
    if check_if_exists():
        update_data()
    else:
        messagebox.showwarning(
            message="Your website hasn't a user and a password",
            icon='warning', title='Update password'
        )

def find_action():
    website_data = website.get().lower()
    filter_data = find_data(value=website_data, column="Website")
    message = ""
    if len(filter_data):
        for value in filter_data:
            message += f"Website {value['Website']}: user name is {value['UserName']}, password is {value['Password']}\n"

        messagebox.showinfo(
            message=message,
            icon='info', title='User information'
        )

    else:
        messagebox.showinfo(
            message="Can't find user information",
            icon='info', title='User information'
        )

load_data()




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
website = ttk.Entry(
    mainframe,
    font=('Helvetica', 11, 'normal')
)
username_label = ttk.Label(mainframe, text="Email/User name:", font=('Helvetica', 11, 'bold'))
username = ttk.Entry(mainframe, font=('Helvetica', 11, 'normal'))
password_label = ttk.Label(mainframe, text="Password:", font=('Helvetica', 11, 'bold'))
password = ttk.Entry(mainframe, font=('Helvetica', 11, 'normal'))
generate_password_bt = ttk.Button(mainframe, text="Generate Password")
add_password_bt = ttk.Button(
    mainframe,
    text="Add",
    command=add_action
)

update_password_bt = ttk.Button(
    mainframe,
    text="Update",
    command=update_action
)

find_bt = ttk.Button(
    mainframe,
    text="Find",
    command=find_action
)

canvas.grid(row=0, column=1, columnspan=2)
website_label.grid(column=0, row=1, sticky=(W))
website.grid(column=1, row=1, columnspan=1, sticky=(W,E))
find_bt.grid(column=2, row=1, columnspan=1, sticky=(W,E))
username_label.grid(column=0, row=2, sticky=(W))
username.grid(column=1, row=2, columnspan=2, sticky=(W,E))
password_label.grid(column=0, row=3, sticky=(W))
password.grid(column=1, row=3, sticky=(W,E))
generate_password_bt.grid(column=2, row=3, sticky=(W,E))
add_password_bt.grid(column=1, row=4, columnspan=2, sticky=(W,E))
update_password_bt.grid(column=1, row=5, columnspan=2, sticky=(W,E))

website.focus()

root.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
root.mainloop()