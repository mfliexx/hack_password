import tkinter as tk
import string
import random


window = tk.Tk()
window.title("Password hack")
window.geometry("500x250")
window.configure(bg="black")


title = tk.Label(window, text="Enter password:", font=("Consolas", 14), fg="white", bg="#1d921b")
title.pack(pady=10)


entry = tk.Entry(window, font=("Consolas", 17), justify='center')
entry.pack(pady=5)


label = tk.Label(window, text="", font=("Consolas", 14), fg="lime", bg="black")
label.pack(pady=20)


guess = ""
index = 0
password = ""
chars = string.ascii_letters + string.digits + string.punctuation

def hack():
    global guess, index, password
    password = entry.get()
    guess = ""
    index = 0
    if password:
        entry.config(state="disabled")  
        hack_step()

def hack_step():
    global guess, index
    if index < len(password):
        random_char = random.choice(chars)
        label.config(text=f"Selection: {guess + random_char}")
        if random_char == password[index]:
            guess += random_char
            index += 1
        window.after(50, hack_step)
    else:
        label.config(text=f"Password hacked: {guess}")
        entry.config(state="normal")  


btn = tk.Button(window, text="Start hack", command=hack, font=("Consolas", 12), fg="white", bg="#1d921b" )
btn.pack()


window.mainloop()
