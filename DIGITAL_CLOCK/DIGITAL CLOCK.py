from datetime import datetime
from tkinter import * 
from tkinter.ttk import * 
from time import strftime

root=Tk()
root.minsize(width=700,height=300)
root.title('clock')
def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000,time)


lbl = Label(root,font=('calibri',50,'bold',),foreground='white',background="black")

pri = Label(root,text="DIGITAL CLOCK",font=('verdana',50,),background="red",foreground="brown").place(relx=0.5,rely=0,anchor="n")

Label(root,text="CREATED BY ABHAY KUMAR",font=('verdana',15,),background="cyan",foreground="green").place(relx=1.0,rely=1.0,anchor="se")

#lbl.place(x=220,y=200)
lbl.place(relx=0.5,rely=0.5,anchor="center")
time()

#root.resizable(0,0)
mainloop()
