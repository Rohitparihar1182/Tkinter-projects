from tkinter import *
from tkinter.messagebox import showinfo,askyesnocancel
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def New():
    global file
    x=text.get(1.0,END).strip()
    if x=="":
        root.title("Untitled - Notepad")
        file = None
        text.delete(1.0, END)
    else:
        if file==None:
            var=askyesnocancel("File not saved","Do you want to save the file")
            if var==True:
                Save()
                root.title("Untitled - Notepad")
                file = None
                text.delete(1.0, END)
            elif var==False:
                root.title("Untitled - Notepad")
                file = None
                text.delete(1.0, END)
        else:
            with open(file,"r") as f:
                newtext=f.read()
                if newtext.strip()==x:
                    root.title("Untitled - Notepad")
                    file = None
                    text.delete(1.0, END)
                else:
                    var=askyesnocancel("File modified","Do you want to save the file")
                    if var==True:
                        f = open(file, "w")
                        f.write(text.get(1.0, END))
                        f.close()
                        root.title("Untitled - Notepad")
                        file = None
                        text.delete(1.0, END)
                    elif var==False:
                        root.title("Untitled - Notepad")
                        file = None
                        text.delete(1.0, END)



def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()



def Open():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()


def Save_as():
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file =="":
        file = None

    else:
        #Save as a new file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - Notepad")
        print("File Saved")


def Exit():
    root.destroy()

def func():
    pass

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def undo():
    showinfo("This feature is currently not available","We are currently working on this feature")

root=Tk()
root.geometry("799x877")
root.title("Untitled-Notepad")

def Menubars():
    mainmenu=Menu(root)
    filemenu=Menu(mainmenu,tearoff=0)
    editmenu=Menu(mainmenu,tearoff=0)
    formatmenu=Menu(mainmenu,tearoff=0)
    viewmenu=Menu(mainmenu,tearoff=0)
    helpmenu=Menu(mainmenu,tearoff=0)
    #for file menu

    filemenu.add_command(label="New       ",command=New)
    filemenu.add_command(label="Open      ",command=Open)
    filemenu.add_command(label="Save      ",command=Save)
    filemenu.add_command(label="Save as   ",command=Save_as)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=Exit)
    
    #for edit menu
    editmenu.add_command(label="Undo         ",command=undo)
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    
    #for format menu
    formatmenu.add_command(label="Word Wrap     ",command=func)
    formatmenu.add_command(label="font",command=func)

    #for view menu
    viewmenu.add_command(label="Zoom          ",command=func)
    viewmenu.add_command(label="Status bar",command=func)

    #for help menu
    helpmenu.add_command(label="View help     ",command=func)
    helpmenu.add_command(label="Send feedback",command=func)
    helpmenu.add_separator()
    helpmenu.add_command(label="About notepad",command=func)
    
    root.config(menu=mainmenu)
    
    #packing all submenus
    mainmenu.add_cascade(label="File",menu=filemenu)
    mainmenu.add_cascade(label="Edit",menu=editmenu)
    mainmenu.add_cascade(label="Format",menu=formatmenu)
    mainmenu.add_cascade(label="View",menu=viewmenu)
    mainmenu.add_cascade(label="Help",menu=helpmenu)
    
Menubars()
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
scroll1=Scrollbar(root,orient=HORIZONTAL)
scroll1.pack(side=BOTTOM,fill=X)
text=Text(root,font=("lucida" ,15),yscrollcommand=scroll.set,xscrollcommand=scroll1.set)
text.setvar("")
text.pack(fill=BOTH,expand=True)
file=None
scroll.config(command=text.yview)

scroll1.config(command=text.xview)
root.mainloop()
