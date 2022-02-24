from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers)for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols)for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    get_website = website_entry.get()
    get_email = email_entry.get()
    get_password = password_entry.get()

    if get_website == "":
        messagebox.showinfo(title="not_get_website", message="You Please don't leave website fields empty")
    elif get_email == "":
        messagebox.showinfo(title="not_get_email", message="You Please don't leave email fields empty")
    elif get_password == "":
        messagebox.showinfo(title="not_get_password", message="You Please don't leave password fields empty")
    else:
        answer = messagebox.askokcancel(title="add data",
                                        message=f"These are the detail entered: \n Email: {get_email} "
                                                f"\nPassword: {get_password} \nIs it ok to save?")
        if answer:
            with open("password_manager.txt", mode="a") as file:
                file.write(f"{get_website}  |  {get_email}  |  {get_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password_Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:", fg="black")
website_text.grid(column=0, row=1)
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_text = Label(text="Email/Username:", fg="black")
email_text.grid(column=0, row=2)
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "siyea@testmail.com")

password_text = Label(text="Password:", fg="black")
password_text.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=13, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
