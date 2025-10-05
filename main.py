# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_list = password_list + [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_list + [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    return "".join(password_list)
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

def check_not_empty_entry(value):
    return len(value)

def save_data():
    website_data =  website.get()
    username_data = username.get()
    password_data = password.get()

    if (check_not_empty_entry(website_data)
            and check_not_empty_entry(username_data)
            and check_not_empty_entry(password_data)
    ):
        user_data = [website_data, username_data, password_data]
        data.loc[len(data)] = user_data

        data.to_csv(path, index=False, header=True)

        website.delete(0, END)
        password.delete(0, END)

        messagebox.showinfo(
            message='Add new user information successfully',
            icon='info', title='Add'
        )
    else:
        messagebox.showwarning(
            message="Your user or website or password is empty",
            icon='warning', title='Save password'
        )

def update_data():
    website_data = website.get().lower()
    username_data = username.get().lower()
    password_data = password.get()

    if check_not_empty_entry(password_data):
        data.loc[
            (
                (data['Website'].str.lower() == website_data) &
                (data['UserName'].str.lower() == username_data)
            ),
            'Password'
        ] = password_data

        data.to_csv(path, index=False, header=True)

        messagebox.showinfo(
            message='Update user information successfully',
            icon='info', title='Update'
        )
    else:
        messagebox.showwarning(
            message="Your password is empty",
            icon='warning', title='Update password'
        )



def find_data(value, column) -> list[dict]:
    value = value.lower()
    filtered  = data[(data[column].str.lower() == value)]
    return filtered.to_dict(orient='records')

def add_action():
    if not check_if_exists():
        save_data()

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
    # message = ""
    if len(filter_data):
        open_child_window(filter_data)
        # for value in filter_data:
        #     message += f"Website {value['Website']}: user name is {value['UserName']}, password is {value['Password']}\n"
        #
        # messagebox.showinfo(
        #     message=message,
        #     icon='info', title='User information'
        # )

    else:
        messagebox.showinfo(
            message="Can't find user information",
            icon='info', title='User information'
        )

def generate_password_action():
    password.delete(0, END)
    password.insert(END, generate_password())

# ---------------------------- COPY USER NAME AND PASSWORD ------------------------------- #
import pyperclip

def copy_action():
    username_data = username.get()
    password_data = password.get()
    pyperclip.copy(username_data + "/" + password_data)

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
generate_password_bt = ttk.Button(
    mainframe,
    text="Generate Password",
    command=generate_password_action
)
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

copy_bt = ttk.Button(
    mainframe,
    text="Copy user name/password",
    command=copy_action
)

# ---------------------------- CHILD WINDOW ------------------------------- #
def open_child_window(user_data):
    child = Toplevel(root)

    child.title("Choose user information")
    child.geometry("400x250")

    columns = ("website", "user_name", "password")
    tree = ttk.Treeview(
        child,
        columns=columns,
        show="headings",
        selectmode="browse",
        height = len(user_data)
    )
    tree.heading("website", text="Website")
    tree.heading("user_name", text="User Name")
    tree.heading("password", text="Password")

    tree.column("website", width=150, anchor="w", stretch=True)
    tree.column("user_name", width=150, anchor="w", stretch=True)
    tree.column("password", width=150, anchor="w", stretch=True)

    for row in user_data:
        tree.insert("", END,
                    values=(row["Website"], row["UserName"], row["Password"])
                    )

    # tree.pack(fill="both", expand=True, padx=10, pady=10)
    tree.pack(fill="x", padx=10, pady=10)

    first_item = tree.get_children()[0]
    tree.selection_set(first_item)

    def confirm_selection():
        selected_item = tree.selection()

        if selected_item:
            values = tree.item(selected_item[0], "values")
            username.delete(0, END)
            password.delete(0, END)
            username.insert(END, values[1])
            password.insert(END, values[2])
        child.destroy()

    ttk.Button(child, text="Submit", command=confirm_selection).pack(pady=10)


# ---------------------------- GRID ------------------------------- #
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
copy_bt.grid(column=1, row=6, columnspan=2, sticky=(W,E))

website.focus()

root.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
root.mainloop()


