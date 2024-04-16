import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os
import pathlib 


filefolder = os.path.expanduser("~/.local/share/applications")


def name_of_file():
    global filename
    filename = simpledialog.askstring('Name of file', 'Enter the name of the file')
    if filename:
        print("Name of App: ", filename)


def comment_of_file():
    global comment
    comment = simpledialog.askstring('Comment', 'Enter a comment for the file(can be empty)')
    if comment:
        print("Comment of App: ", comment)
    else:
        print("No comment for the app")

def exec_of_file():
    global exec_path
    exec_path = filedialog.askopenfilename(title='Select Executable')
    if exec_path:
        print("The app will be ran: ", exec_path)

def icon_of_file():
    global icon_path
    icon_path = filedialog.askopenfilename(title='Select Icon', filetypes=[('Icon Files', '*.png',), ('Icon Files', '*.ico'), ('Icon Files', '*.svg'), ('Icon Files', '*.jpg')])
    if icon_path:
        print("The app will have this icon: ", icon_path)
    else:
        print("The app will not have an icon")

def categories_of_file():
    global categories
    categories = simpledialog.askstring('Categories', 'Enter the categories for the file')
    if categories:
        print("Categories of App: ", categories)


def terminal_of_file():
    global terminal
    terminal_input = simpledialog.askstring('Terminal', 'T or F')
    if terminal_input.upper() == 'T' or terminal_input.lower() == 't':
        terminal = True
        print("The app will run in the terminal")
    elif terminal_input.upper() == 'F' or terminal_input.lower() == 'f':
        terminal = False
        print("The app will not run in the terminal")



def create_the_file():
    file_path = f"{filefolder}/{filename}.desktop"
    with open(file_path, 'w') as file:
        file.write("[Desktop Entry]\n")
        file.write("Type=Application\n")
        file.write("Encoding=UTF-8\n")
        file.write(f"Name={filename}\n")
        file.write(f"Comment={comment}\n")
        file.write(f"Exec={exec_path}\n")
        file.write(f"Icon={icon_path}\n")
        file.write(f"Categories={categories}\n")
        file.write(f"Terminal={terminal}")




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