from tkinter import *
root = Tk()

def send():
    send = "You =>" + e.get()
    txt.insert(END,'\n' + send)
    if(e.get() == 'hello'):
        txt.insert(END,"\n" + "Bot => Hi")
    elif(e.get() == 'hi'):
        txt.insert(END,"\n" + "Bot => Hello")
    elif(e.get() == 'How are you'):
        txt.insert(END,"\n" + "Bot => I am fine and you?")
    elif(e.get() == 'fine'):
        txt.insert(END,"\n" + "Bot => Nice to hear!")
    elif(e.get() == 'What is your name'):
        txt.insert(END,"\n" + "Bot => !*Pybot*!")
    else:
        txt.insert(END,"\n" + "Bot => Sorry I didnt get it :(:(")
    e.delete(0,END)

txt = Text(root)
txt.grid(row=0,column=0)
e = Entry(root,width=100)
send = Button(root,text="Send",bg='black',fg='white',command=send).grid(row=1,column=1)
root.title('ChatBot')
root.mainloop()

if __name__ == "__main__":
    send

