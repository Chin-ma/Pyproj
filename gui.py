import tkinter as Tkinter
from tkinter import *

root = Tkinter.Tk()

def send():
    send = "Me - "+e.get()
    txt.insert(END,'\n'+send)
    if e.get() == 'hello' or 'Hello':
        txt.insert(END,"\n"+"BOT - Hi")
    elif e.get() == 'hi' or 'Hi':
        txt.insert(END,"\n"+"BOT - Hello")
    elif e.get() == 'how are you':
        txt.insert(END,"\n"+"BOT - fine and you")
    elif e.get() == 'fine':
        txt.insert(END,"\n"+"BOT - Nice to hear")
    elif e.get() == 'what is your name' or "what's your name":
        txt.insert(END,"\n"+"BOT - I don't have name for now but my master would soon give me a name or you may suggest him some name")
    else:
        txt.insert(END,"\n"+"BOT - Sorry!")
    e.delete(0,END)


txt = Tkinter.Text(root)
txt.grid(row=0,column=0)
e = Tkinter.Entry(root, width=100, bd=5)
send = Tkinter.Button(root, text="SEND",bg='black',fg='white',command=send).grid(row=1,column=1)
e.grid(row=1,column=0)

root.title("ChatBot")
root.mainloop()