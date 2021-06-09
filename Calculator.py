from tkinter import *
#defining function
def calculate(event):
    var=event.widget.cget("text")
    if var=="=":
        if val.get().isdigit():
            value=int(val.get())
        else:
            value=eval(screen.get())
        val.set(value)
        screen.update()
    elif var=="C":
        val.set("")
        screen.update()
    
    else:
        val.set(val.get()+var)
        screen.update()
#defining GUI
root=Tk()
root.geometry("600x700")
root.title("Rohit's Calculator")
val=StringVar()
val.set("")
#Calculator screen
screen=Entry(root,textvariable=val,font=("lucida",20,"bold"))
screen.pack(fill=X,ipady=20)
#defining frames and buttons for our calculator
#binding it into calculate 
f1=Frame(root,bg="grey")

for i in range(3):
    b=Button(f1,text=f"{9-i}",font=("lucida",30,"bold"))
    b.pack(side=LEFT,ipadx=6)
    b.bind("<Button-1>",calculate)
b=Button(f1,text="+",font=("lucida",30,"bold"))
b.pack(side=LEFT,ipadx=6)
b.bind("<Button-1>",calculate)
f1.pack(side=TOP,anchor="w")

f2=Frame(root,bg="grey")
for i in range(3):
    b=Button(f2,text=f"{6-i}",font=("lucida",30,"bold"))
    b.pack(side=LEFT,ipadx=6)
    b.bind("<Button-1>",calculate)
b=Button(f2,text="-",font=("lucida",30,"bold"))
b.pack(side=LEFT,ipadx=10)
b.bind("<Button-1>",calculate)
f2.pack(side=TOP,anchor="w")

f3=Frame(root,bg="grey")
for i in range(3):
    b=Button(f3,text=f"{3-i}",font=("lucida",30,"bold"))
    b.pack(side=LEFT,ipadx=7)
    b.bind("<Button-1>",calculate)
b=Button(f3,text="*",font=("lucida",30,"bold"))
b.pack(side=LEFT,ipadx=6)
b.bind("<Button-1>",calculate)
f3.pack(side=TOP,anchor="w")

f4=Frame(root,bg="grey")
b=Button(f4,text="C",font=("lucida",30,"bold"))
b.pack(side=LEFT,ipadx=3)
b.bind("<Button-1>",calculate)

b=Button(f4,text="0",font=("lucida",30,"bold"))
b.pack(side=LEFT,ipadx=6)
b.bind("<Button-1>",calculate)

b=Button(f4,text="/",font=("lucida",30,"bold"))
b.pack(side=LEFT,ipadx=10)
b.bind("<Button-1>",calculate)

b=Button(f4,text="=",font=("lucida",30,"bold"))
b.pack(side=LEFT,ipadx=6)
b.bind("<Button-1>",calculate)
f4.pack(side=TOP,anchor="w")


root.mainloop()
