from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_symbols)]
    password_symbols = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def find_password():
    search_query = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if search_query in data:
            details = data[search_query]
            messagebox.showinfo(title=search_query,
                                message=f"Email: {details['email']}\n Password: {details['password']}")
        else:
            messagebox.showinfo(title="Error",
                                message=f"There are no details for {search_query}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    username = username_input.get()
    website = website_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            username_input.insert(0, "jeshuwabradley@gmail.com")
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=32)
website_input.focus()
website_input.grid(column=1, row=1)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry(width=42)
username_input.insert(0, "jeshuwabradley@gmail.com")
username_input.grid(column=1, columnspan=2, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)
generate_button.config(padx=0, pady=0)

add_button = Button(text="Add", width=36, command=save_details)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
