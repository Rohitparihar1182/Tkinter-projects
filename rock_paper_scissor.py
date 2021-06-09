from tkinter import *
import random
def game(event):
    var=event.widget.cget("text")
    global options
    var2=options[random.randint(0,2)]
    com.set(var2)
    if var==options[0]:
        if var2==options[0]:
            str1.set("TIE")
        elif var2==options[1]:
            str1.set("LOSE")
            x=s1.get()
            x+=1
            s1.set(x)
        elif var2==options[2]:
            str1.set("WIN")
            x=s2.get()
            x+=1
            s2.set(x)
    elif var==options[1]:
        if var2==options[0]:
            str1.set("WIN")
            x=s2.get()
            x+=1
            s2.set(x)
        elif var2==options[1]:
            str1.set("TIE")
        elif var2==options[2]:
            str1.set("LOSE")
            x=s1.get()
            x+=1
            s1.set(x)
    elif var==options[2]:
        if var2==options[0]:
            str1.set("LOSE")
            x=s1.get()
            x+=1
            s1.set(x)
        elif var2==options[1]:
            str1.set("WIN")
            x=s2.get()
            x+=1
            s2.set(x)
        elif var2==options[2]:
            str1.set("TIE")
root=Tk()
root.geometry("900x900")
root.minsize(900,900)
root.maxsize(900,900)
root.configure(bg="yellow")
root.title("Welcome to Rock Paper n Scissor game")
options=[" Rock  "," Paper ","Scissor"]
colours=["red","white","green"]
Label(root,text="Computer",font=("arial",20)).place(x=10,y=10)
com=StringVar()
com.set("")
Com_entry=Entry(root,textvariable=com,font=("arial",20)).place(x=10,y=50,height=30,width=100)
Label(root,text="Score",font=("arial",20)).place(x=700,y=10)
Label(root,text="Com|You",font=("arial",20)).place(x=700,y=50)
s1=IntVar()
s1.set(0)
s1_entry=Entry(root,textvariable=s1,font=("arial",20)).place(x=700,y=80,height=30,width=60)
s2=IntVar()
s2.set(0)
s2_entry=Entry(root,textvariable=s2,font=("arial",20)).place(x=760,y=80,height=30,width=60)




for i in range(3):
    B=Button(root,text=options[i],bg=colours[i],padx=60,pady=40,relief=SUNKEN)
    B.pack()
    B.bind("<Button-1>",game)
str1=StringVar()
str1.set("")
E=Entry(root,textvariable=str1,fg="yellow",bg="blue",font=("arial",40,"bold")).place(x=200,y=400,height=200,width=200)



root.mainloop()
