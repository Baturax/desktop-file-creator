from fileinput import filename
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os
from pathlib import Path



def name_of_file():
    name = simpledialog.askstring('Name of file', 'Enter the name of the file')
    if name:
        print("Name of App: ", name)

def comment_of_file():
    comment = simpledialog.askstring('Comment', 'Enter a comment for the file(can be empty)')
    if comment:
        print("Comment of App: ", comment)
    else:
        print("No comment for the app")

def exec_of_file():
    exec_path = filedialog.askopenfilename(title='Select Executable')
    if exec_path:
        print("The app will be ran: ", exec_path)

def icon_of_file():
    icon_path = filedialog.askopenfilename(title='Select Icon', filetypes=[('Icon Files', '*.png',), ('Icon Files', '*.ico'), ('Icon Files', '*.svg'), ('Icon Files', '*.jpg')])
    if icon_path:
        print("The app will have this icon: ", icon_path)
    else:
        print("The app will not have an icon")

def categories_of_file():
    categories = simpledialog.askstring('Categories', 'Enter the categories for the file')
    if categories:
        print("Categories of App: ", categories)

def terminal_of_file():
    terminal = simpledialog.askstring('Terminal', 'T or F')
    if terminal == 'T':
        print("The app will run in the terminal")
    elif terminal == 'F':
        print("The app will not run in the terminal")
    elif terminal == 't':
        print("The app will run in the terminal")
    elif terminal == 'f':
        print("The app will not run in the terminal")

filefolder = "~.local/share/applications"
filename = name

def create_the_file():
    pathlib.Path(f"{filefolder}/{filename}.desktop").touch()

#here

root = tk.Tk()
root.title('Create Desktop File')
root.geometry('300x300')
root.resizable(False, False)

install_button = tk.Button(root, text='Name of App', command=name_of_file)
install_button.pack()

comment_button = tk.Button(root, text='Comment of App', command=comment_of_file)
comment_button.pack()

exec_button = tk.Button(root, text='Executable', command=exec_of_file)
exec_button.pack()

icon_button = tk.Button(root, text='Icon', command=icon_of_file)
icon_button.pack()

categories_button = tk.Button(root, text='Categories', command=categories_of_file)
categories_button.pack()

terminal_button = tk.Button(root, text='Terminal', command=terminal_of_file)
terminal_button.pack()

create_button = tk.Button(root, text='Create Desktop File', command=create_the_file)
create_button.pack()

root.mainloop()