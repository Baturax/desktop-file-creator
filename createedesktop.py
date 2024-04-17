import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os
from turtle import up, update

filefolder = os.path.expanduser("~/.local/share/applications")

filename = ""
comment = ""
exec_path = ""
icon_path = ""
categories = ""
terminal = False

# file's name
def name_of_file():
    global filename
    filename = simpledialog.askstring('Name of file', 'Enter the name of the file')
    if filename:
        update_filename_label()

def update_filename_label():
    label_offilename.config(text=f'Name of App: {filename}')

# file's comment
def comment_of_file():
    global comment
    comment = simpledialog.askstring('Comment', 'Enter a comment for the file (can be empty)')
    if comment:
        update_comment_label()

def update_comment_label():
    comment_ofcomment.config(text=f'Comment of App: {comment}')

# file's executable
def exec_of_file():
    global exec_path
    exec_path = filedialog.askopenfilename(title='Select Executable')
    if exec_path:
        update_exec_label()

def update_exec_label():
    executable_ofexec.config(text=f'Executable: {exec_path}')

# file's icon
def icon_of_file():
    global icon_path
    icon_path = filedialog.askopenfilename(title='Select Icon', filetypes=[('Icon Files', '*.png',), ('Icon Files', '*.ico'), ('Icon Files', '*.svg'), ('Icon Files', '*.jpg')])
    if icon_path:
        update_icon_label()

def update_icon_label():
    icon_oficon.config(text=f'Icon: {icon_path}')

# file's categories
def categories_of_file():
    global categories
    categories = simpledialog.askstring('Categories', 'Enter the categories for the file')
    if categories:
        update_categories_label()

def update_categories_label():
    categories_ofcategories.config(text=f'Categories: {categories}')

# file's terminal
def terminal_of_file():
    global terminal
    terminal_input = simpledialog.askstring('Terminal', 'T or F')
    if terminal_input is not None and (terminal_input.upper() == 'T' or terminal_input.lower() == 't'):
        terminal = True
        update_terminal_label()
    elif terminal_input is not None and (terminal_input.upper() == 'F' or terminal_input.lower() == 'f'):
        terminal = False
        update_terminal_label()

def update_terminal_label():
    terminal_ofterminal.config(text=f'Terminal: {terminal}')

# create the file
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

root = tk.Tk()
root.title('Create Desktop File')
root.geometry('500x400')
root.resizable(False, False)
root.configure(bg='black')

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

# Labels
label_offilename = tk.Label(root, text=f'Name of App: {filename}', fg='yellow', bg='black', font='monofont 12 bold')
label_offilename.pack()

comment_ofcomment = tk.Label(root, text=f'Comment of App: {comment}', fg='aqua', bg='black', font='monofont 12 bold')
comment_ofcomment.pack()

executable_ofexec = tk.Label(root, text=f'Executable: {exec_path}', fg='blue', bg='black', font='monofont 12 bold')
executable_ofexec.pack()

icon_oficon = tk.Label(root, text=f'Icon: {icon_path}', fg='pink', bg='black', font='monofont 12 bold')
icon_oficon.pack()

categories_ofcategories = tk.Label(root, text=f'Categories: {categories}', fg='#20272F', bg='black', font='monofont 12 bold')
categories_ofcategories.pack()

terminal_ofterminal = tk.Label(root, text=f'Terminal: {terminal}', fg='yellow', bg='black', font='monofont 12 bold')
terminal_ofterminal.pack()

root.mainloop()
