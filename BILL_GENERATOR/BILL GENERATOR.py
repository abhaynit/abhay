# Python3 program to get selected
# value(s) from tkinter listbox

# Import tkinter

from tkinter import *
from tkinter.font import BOLD 

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
	
	
] 

def bill():
    pdf = SimpleDocTemplate( "bill.pdf" , pagesize = A4 )
    styles = getSampleStyleSheet()
    title_style = styles[ "Heading1" ]
    title_style.alignment = 1
    title = Paragraph( "BILL GENERATOR" , title_style )
    style = TableStyle()
    table = Table( DATA , style = style )
    pdf.build([ title , table ])


# Create the root window
root = Tk()
root.geometry('940x550')
root.title('ABHAY BILL GENERATOR')

# Create a listbox
listbox = Listbox(root, width=40, height=20, selectmode=MULTIPLE)
selected_listbox = Listbox(root, width=40, height=20, selectmode=MULTIPLE)

f=open("book1.txt",'r')
s=f.read()

import json
book = json.loads(s)
item=[]
for i in book:
    lis=[]
    lis.append(i)
    lis.append(book[i])
    item.append(lis)

print(item)

item.sort()
selected=[]


def inser():
    item.sort()
    for i in range(len(item)):
        qw=item[i][0].ljust(40,"*") + str(item[i][1]) 
        listbox.insert(i+1,qw)

# Inserting the listbox items
for i in range(len(item)):
        qw=item[i][0].ljust(40,"*") + str(item[i][1]) 
        listbox.insert(i+1,qw)


# Function for printing the
# selected listbox value(s)
def selected_item():
    DATA.append([ "ITEMS","PRICE"])
    DATA.append(["-------","------"])
    for i in selected:
        lis=[]
        sd=i.split('*')
        lis.append(sd[0])
        lis.append(sd[-1])
        DATA.append(lis)
    if len(DATA)==1:
        DATA.clear()
    global total
    DATA.append(["-------","------"])
    DATA.append(['TOTAL',total])
    bill()
    DATA.clear()
    

def delete_item():
    global total
    listbox.delete(0,'end')
    inser()
    for i in  selected_listbox.curselection():
        qw=selected_listbox.get(i)
        selected.remove(qw)
        selected_listbox.delete(i)
        total -= int(qw.split('*')[-1])
    gt1.configure(text=str(total))

gt = Label(root,text="TOTAL : ",foreground='darkgreen', background='darkkhaki',font=('verdana',15,BOLD))
gt.place(x=400,y=500)

gt1= Label(root,text="0",foreground='darkred', background='darkseagreen',font=('verdana',15,BOLD))
gt1.place(x=550,y=500)


        
global total 
total =0
def show_item():
    global total
    for i in listbox.curselection():
        qw=listbox.get(i)
        if qw not in selected:
            selected.append((qw))
            total += int(qw.split('*')[-1])
            
    selected.sort()
    selected_listbox.delete(0,'end')
    for j in range(len(selected)):
        selected_listbox.insert(j+1,selected[j])
    gt1.configure(text=str(total))

def enter_new():
    selected_listbox.delete(0,'end')
    listbox.delete(0,'end')
    inser()
    selected.clear()
    global total
    total=0
    gt1.configure(text=str(total))
    DATA.clear()

def addition():
    global it1 
    sd=it1.get()
    global it2 
    sd1=it2.get()
    if len(sd)>0:
        item.append([sd,sd1])
        listbox.delete(0,'end')
        inser()
        book= dict(item)
        import json
        s = json.dumps(book)
        with open('book.txt','w') as f:
            f.write(s)


def insert_n():
    global qe
    ty = (qe.get())
    if ty=="abhay":
        df=Label(root,foreground='hotpink', background='lemonchiffon',font=('verdana',10,BOLD))
        df.place(x=500,y=440)
        df.configure(text="CORRECT PASSWORD")
        Label(root,text="ITEM",foreground='hotpink', background='lemonchiffon',font=('verdana',10,BOLD)).place(x=10,y=480)
        Label(root,text='PRICE',foreground='hotpink', background='lemonchiffon',font=('verdana',10,BOLD)).place(x=10,y=520)
        global it1
        it1 = Entry(root,width=20)
        it1.place(x=60,y=480)
        global it2
        it2 = Entry(root,width=20)
        it2.place(x=60,y=520)
        Button(root,text="SUBMIT",command= addition).place(x=200,y=500)


    else:
        df=Label(root,foreground='hotpink', background='lemonchiffon',font=('verdana',10,BOLD))
        df.place(x=500,y=440)
        df.configure(text='WRONG PASSWORD')



        
def add():
    add1.configure(text='ENTER PASSWORD : ')
    global qe
    qe = Entry(root,width=20)
    qe.place(x=250,y=440)
    Button(root,text="SUBMIT",command=insert_n).place(x=400,y=440)



# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(root, text='GENERATE BILL', command=selected_item)
btn1 = Button(root, text='REMOVE SOME ITEM', command=delete_item)
btn2 = Button(root, text='SHOW', command=show_item)
btn3 = Button(root, text='NEW', command=enter_new)

# Placing the button and listbox
btn.place(x=700,y=200)
btn1.place(x=700,y=100)
btn2.place(x=280,y=150)
btn3.place(x=700,y=300)

ite =  Label(root,text="ITEM LIST",foreground='indigo', background='lavender',font=('verdana',15,BOLD))
ite.place(x=60,y=70)

ites =  Label(root,text="SELECTED ITEM",foreground='hotpink', background='lemonchiffon',font=('verdana',15,BOLD))
ites.place(x=430,y=70)

it =  Label(root,text="select and press remove some item  to remove",foreground='black', background='bisque',font=('verdana',7,BOLD))
it.place(x=700,y=130)

it1 =  Label(root,text="click here to print bill",foreground='brown', background='burlywood',font=('verdana',7,BOLD))
it1.place(x=700,y=230)

it2 =  Label(root,text="click here to generate new bill",foreground='darkblue', background='darkgray',font=('verdana',7,BOLD))
it2.place(x=700,y=330)

it3 =  Label(root,text="show selected item",foreground='darkblue', background='darkgray',font=('verdana',7,BOLD))
it3.place(x=280,y=180)

ites1 =  Label(root,text="BILL GENERATOR",foreground='greenyellow', background='honeydew',font=('verdana',30,BOLD))
ites1.pack()

add =  Button(root,text="ADD ITEM",command=add)
add.place(x=10,y=440)

add1 =  Label(root,foreground='maroon', background='mediumaquamarine',font=('verdana',10,BOLD))
add1.place(x=90,y=440)

listbox.place(x=10,y=100)
selected_listbox.place(x=400,y=100)

root.mainloop()
