import tkinter as tk
import random
import string

def genrator_password(length):
    if length < 4:
        return "Password length should be at least 4 for better security."
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    all_charecters = upper + lower + digits + special

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_charecters, k = length - 4)
    random.shuffle(password)
    return ''.join(password)

def on_generator():
    try:
        user_choice = int(length_entry.get())
        result = genrator_password(user_choice)
        result_label.config(text = result)
    except ValueError:
        result_label.config(text = "Please enter a valid number.")

window = tk.Tk()
window.title("Password generator")
window.geometry('400x400')

tk.Label(window, text = "Enter Password length:").pack(pady = 10)
length_entry = tk.Entry(window)
length_entry.pack()

generator_button = tk.Button(window, text = "Password Generator", command = on_generator)
generator_button.pack(pady = 10)

result_label = tk.Label(window, text = "", fg = "blue", font = ("Helvetice", 12))
result_label.pack(pady = 10)

window.mainloop()
