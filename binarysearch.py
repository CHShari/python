from tkinter import *
root = Tk()
root.title("Welcome to thonny")
root.geometry('350x200')
lbl = Label(root, text = "Are you a programmer?")
lbl.grid()
def clicked():
    lbl.configure(text = "I just got clicked")
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
btn.grid(column=1, row=0)
root.mainloop()
