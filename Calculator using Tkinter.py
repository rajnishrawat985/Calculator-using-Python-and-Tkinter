# CALCULATOR USING TKINTER

from tkinter import *
windows = Tk()
windows.geometry("500x500")
windows.title("CALCULATOR")
windows.config(bg="light blue")
e = Entry(windows,width=50,borderwidth=5,font="bold")
e.place(x=0,y=0)
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str((result) + str(num)))
b = Button(windows,text="1",width=12,command= lambda:click(1),bg="orange",borderwidth=5,font="bold")
b.place(x=10,y=60)
b = Button(windows,text="2",width=12,command= lambda:click(2),bg="orange",borderwidth=5,font="bold")
b.place(x=80,y=60)
b = Button(windows,text="3",width=12,command=lambda:click(3),bg="orange",borderwidth=5,font="bold")
b.place(x=170,y=60)
b = Button(windows,text="4",width=12,command=lambda:click(4),bg="green",borderwidth=5,font="bold")
b.place(x=10,y=120)
b = Button(windows,text="5",width=12,command=lambda:click(5),bg="green",borderwidth=5,font="bold")
b.place(x=80,y=120)
b = Button(windows,text="6",width=12,command=lambda:click(6),bg="green",borderwidth=5,font="bold")
b.place(x=170,y=120)
b = Button(windows,text="7",width=12,command=lambda:click(7),bg="cyan",borderwidth=5,font="bold")
b.place(x=10,y=180)
b = Button(windows,text="8",width=12,command=lambda:click(8),bg="cyan",borderwidth=5,font="bold")
b.place(x=80,y=180)
b = Button(windows,text="9",width=12,command=lambda:click(9),bg="cyan",borderwidth=5,font="bold")
b.place(x=170,y=180)
b = Button(windows,text="0",width=12,command=lambda:click(0),bg="violet",borderwidth=5,font="bold")
b.place(x=10,y=240)
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(windows,text="+",width=12,command=add,bg="violet",borderwidth=5,font="bold")
b.place(x=80,y=240)
def sub():
    n1 = e.get()
    global math
    math = "substraction"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(windows,text="-",width=12,command=sub,bg="violet",borderwidth=5,font="bold")
b.place(x=170,y=240)
def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(windows,text="*",width=12,command=mul,bg="indigo",borderwidth=5,font="bold")
b.place(x=10,y=300)
def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(windows,text="/",width=12,command=div,bg="indigo",borderwidth=5,font="bold")
b.place(x=80,y=300)
def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "substraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))
b = Button(windows,text="=",width=12,command = equal,bg="indigo",borderwidth=5,font="bold")
b.place(x=170,y=300)
def clear():
    e.delete(0,END)
b = Button(windows,text="clear",width=12,command = clear,bg="red",borderwidth=5,font="bold")
b.place(x=10,y=350)

mainloop()