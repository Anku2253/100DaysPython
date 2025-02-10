from tkinter import *
import csv
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    passwdEntry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def addButton():
    
    if len(websiteEntry.get())==0 or len(passwdEntry.get())==0:
        messagebox.showinfo(title="Oops",message="Please make sure you have not left any field empty.")
    else:
        isOk = messagebox.askokcancel(title=websiteEntry.get(),message=f"These are the details entered: \nEmail: {mailEntry.get()} \nPassword: {passwdEntry.get()} \nIs it ok to save?")
    
        if isOk:
            with open(r"Day29\password-manager-start\data.csv","+a") as fh:
                data = [websiteEntry.get(),mailEntry.get(),passwdEntry.get()]
                writer = csv.writer(fh,delimiter="|")
                writer.writerow(data)
                websiteEntry.delete(0,END)
                mailEntry.delete(0,END)
                passwdEntry.delete(0,END)

    
# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

#Canvas
canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
lockImage = PhotoImage(file=r"Day29\password-manager-start\logo.png")
canvas.create_image(100,100,image=lockImage)
canvas.grid(row=0,column=1)

#Labels

websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1,column=0)

mailLabel = Label(text="Email/Username:")
mailLabel.grid(row=2,column=0)

passwdLabel = Label(text="Password:")
passwdLabel.grid(row=3,column=0)

#Widget
websiteEntry = Entry(width=35)
websiteEntry.grid(row=1,column=1,columnspan=2)
websiteEntry.focus()

mailEntry = Entry(width=35)
mailEntry.grid(row=2,column=1,columnspan=2)
mailEntry.insert(END,"@gmail.com")

passwdEntry = Entry(width=21)
passwdEntry.grid(row=3,column=1)

#Button
generate = Button(text="Generate Password",command=generate)
generate.grid(row=3,column=2)

add = Button(text="Add",width=36,command=addButton)
add.grid(row=4,column=1,columnspan=2)


window.mainloop()