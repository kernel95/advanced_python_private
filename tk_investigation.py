# tk_investigation.py

import tkinter as tk
from tkinter import messagebox

from member_dao import MemberDao


def main():
    
    root = tk.Tk()
    root.title("Sample TK Application")
    root.geometry("600x400")

    def on_click():
        messagebox.showinfo("Click", "you clicked the button")
        

    #widget are the controls
    #create a button
    button = tk.Button(root, text="Press Me", command=on_click)
    button.place(x=10, y=20)

    lst_members = tk.Listbox(root)
    lst_members.place(x=10, y=50)

    #lst_members.insert(tk.END, "item")
    dao = MemberDao()
    members = dao.get_all()

    for member in members:
        lst_members.insert(tk.END, member.name)

    root.mainloop()



if __name__ == "__main__":

    main()