from tkinter import*
import os
import sys
from tkinter import messagebox
import mysql.connector
class myclass:
    def __init__(self):
        self.value='called crossmodule'
        print(self.value)
def cse():
    w=Tk()
    w.title('COMPUTER SCIENCE')
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
    crsr=mydb.cursor()
    crsr.execute('select * from cselst')
    l=crsr.fetchall()
    rw=len(l)
    cls=len(l[0])
    l1=Label(w,text='BOOK TITLE',font=('times new',15,'bold'),fg='purple',bg='light green')
    l1.grid(row=0,column=0)
    l2=Label(w,text='AUTHOR',font=('times new',15,'bold'),fg='purple',bg='light green')
    l2.grid(row=0,column=1)
    l3=Label(w,text='REF NO.',font=('times new',15,'bold'),fg='purple',bg='light green')
    l3.grid(row=0,column=2)
    l4=Label(w,text='STOCK',font=('times new',15,'bold'),fg='purple',bg='light green')
    l4.grid(row=0,column=3)
    for i in range(1,rw):
        for j in range(cls):
            e=Label(w,width=20,text=l[i][j],bd=4,bg='light cyan')
            e.grid(row=i,column=j)
def bio():
    w=Tk()
    w.title('BIOLOGY')
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
    crsr=mydb.cursor()
    crsr.execute('select * from biolst')
    l=crsr.fetchall()
    rw=len(l)
    cls=len(l[0])
    l1=Label(w,text='BOOK TITLE',font=('times new',15,'bold'),fg='purple',bg='light green')
    l1.grid(row=0,column=0)
    l2=Label(w,text='AUTHOR',font=('times new',15,'bold'),fg='purple',bg='light green')
    l2.grid(row=0,column=1)
    l3=Label(w,text='REF NO.',font=('times new',15,'bold'),fg='purple',bg='light green')
    l3.grid(row=0,column=2)
    l4=Label(w,text='STOCK',font=('times new',15,'bold'),fg='purple',bg='light green')
    l4.grid(row=0,column=3)
    for i in range(1,rw):
        for j in range(cls):
            e=Label(w,width=20,text=l[i][j],bd=4,bg='light cyan')
            e.grid(row=i,column=j)
def phy():
    w=Tk()
    w.title('PHYSICS')
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
    crsr=mydb.cursor()
    crsr.execute('select * from phylst')
    l=crsr.fetchall()
    rw=len(l)
    cls=len(l[0])
    l1=Label(w,text='BOOK TITLE',font=('times new',15,'bold'),fg='purple',bg='light green')
    l1.grid(row=0,column=0)
    l2=Label(w,text='AUTHOR',font=('times new',15,'bold'),fg='purple',bg='light green')
    l2.grid(row=0,column=1)
    l3=Label(w,text='REF NO.',font=('times new',15,'bold'),fg='purple',bg='light green')
    l3.grid(row=0,column=2)
    l4=Label(w,text='STOCK',font=('times new',15,'bold'),fg='purple',bg='light green')
    l4.grid(row=0,column=3)
    for i in range(1,rw):
        for j in range(cls):
            e=Label(w,width=20,text=l[i][j],bd=4,bg='light cyan')
            e.grid(row=i,column=j)
def novel():
    w=Tk()
    w.title('NOVELS')
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
    crsr=mydb.cursor()
    crsr.execute('select * from novellst')
    l=crsr.fetchall()
    rw=len(l)
    cls=len(l[0])
    l1=Label(w,text='BOOK TITLE',font=('times new',15,'bold'),fg='purple',bg='light green')
    l1.grid(row=0,column=0)
    l2=Label(w,text='AUTHOR',font=('times new',15,'bold'),fg='purple',bg='light green')
    l2.grid(row=0,column=1)
    l3=Label(w,text='REF NO.',font=('times new',15,'bold'),fg='purple',bg='light green')
    l3.grid(row=0,column=2)
    l4=Label(w,text='STOCK',font=('times new',15,'bold'),fg='purple',bg='light green')
    l4.grid(row=0,column=3)
    for i in range(1,rw):
        for j in range(cls):
            e=Label(w,width=20,text=l[i][j],bd=4,bg='light cyan')
            e.grid(row=i,column=j)   
def math():
    w=Tk()
    w.title('MATHEMATICS')
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
    crsr=mydb.cursor()
    crsr.execute('select * from mathlst')
    l=crsr.fetchall()
    rw=len(l)
    cls=len(l[0])
    l1=Label(w,text='BOOK TITLE',font=('times new',15,'bold'),fg='purple',bg='light green')
    l1.grid(row=0,column=0)
    l2=Label(w,text='AUTHOR',font=('times new',15,'bold'),fg='purple',bg='light green')
    l2.grid(row=0,column=1)
    l3=Label(w,text='REF NO.',font=('times new',15,'bold'),fg='purple',bg='light green')
    l3.grid(row=0,column=2)
    l4=Label(w,text='STOCK',font=('times new',15,'bold'),fg='purple',bg='light green')
    l4.grid(row=0,column=3)
    for i in range(1,rw):
        for j in range(cls):
            e=Label(w,width=20,text=l[i][j],bd=4,bg='light cyan')
            e.grid(row=i,column=j)            
def issue():
    sys.path.append("C:\\Users\\Swaraj Badhei\\Desktop\\cls python\\prjct\\cmpltd\\new_issue_final.py")
    from new_issue_final import newissue
def haha2(e11,e22,e33,wm):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
    crsr=mydb.cursor()
    sql="insert into sale(name,author,year) values('"+e11.get()+"','"+e22.get()+"','"+e33.get()+"')"
    crsr.execute(sql)
    mydb.commit()
    messagebox.showinfo('NOTE','SUCCESSFULLY RECORDED.PLEASE VISIT THE COUNTER')
    wm.destroy()
def sale():
    w2=Tk()
    w2.geometry('400x400')
    w2.title('sale')
    c=Canvas(w2,width=4000,height=4000,bg='lightgreen')
    c.place(x=0,y=0)
    l30=Label(w2,text='Enter Details',bg='lightgreen')
    l30.place(x=150,y=30)
    l31=Label(w2,text='BOOK TITTLE',bg='lightgreen')
    l31.place(x=60,y=80)
    e31=Entry(w2,bd=5,width=20)
    e31.place(x=180,y=80)
    l32=Label(w2,text='AUTHOR NAME',bg='lightgreen')
    l32.place(x=60,y=130)
    e32=Entry(w2,bd=5,width=20)
    e32.place(x=180,y=130)
    l33=Label(w2,text='PUBLICATION YEAR',bg='lightgreen')
    l33.place(x=60,y=180)
    e33=Entry(w2,bd=5,width=20)
    e33.place(x=180,y=180)
    b19=Button(w2,text='Proceed',command=lambda:haha2(e31,e32,e33,w2))
    b19.place(x=150,y=230)
    w2.mainloop()
def moveback(w3):
        w3.destroy()
def suggest(E9):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
    crsr=mydb.cursor()
    sql="insert into suggest(name) values('"+E9.get()+"')"
    crsr.execute(sql)
    mydb.commit()
    messagebox.showinfo('NOTE','SUCCESSFULLY RECORDED')
    E9.delete(0,END)
class strt:
    def __init__(self):
        w1=Tk()
        w1.geometry('800x600')
        w1.title('Register book')
        c=Canvas(width=4000,height=4000,bg='lightgreen')
        c.place(x=0,y=0)
        img=PhotoImage(file='C:\\Users\\Swaraj Badhei\\Desktop\\cls python\\prjct\\cmpltd\\Screenshot (11).png')
        img=img.subsample(2,2)
        c.create_image(160,90,image=img,anchor=NW)
        b3=Button(w1,text='New Issue',bd=5,bg='sky blue',height=2,width=15,command=issue)
        b3.place(x=10,y=50)
        b4=Button(w1,text='Issued Books',bd=5,bg='lime',height=2,width=15)
        b4.place(x=10,y=150)
        b5=Button(w1,text='Sale',bd=5,bg='red',height=2,width=15,command=sale)
        b5.place(x=10,y=250)
        b6=Button(w1,text='Quit',bd=5,bg='gray',height=2,width=15,command=w1.destroy)
        b6.place(x=10,y=352)
        b8=Button(w1,text='Logout',bd=5,bg='orange',height=1,width=8,command=lambda:moveback(w1))
        b8.place(x=679,y=20)
        l190=Label(w1,text='Show Stock Subjectwise',bg='light blue')
        l190.place(x=350,y=20)
        b12=Button(w1,text='BIOLOGY',width=7,command=bio,bg='cyan')
        b12.place(x=190,y=60)
        b13=Button(w1,text='CSE',width=7,command=cse,bg='cyan')
        b13.place(x=290,y=60)
        b14=Button(w1,text='MATHS',width=7,command=math,bg='cyan')
        b14.place(x=390,y=60)
        b15=Button(w1,text='PHYSICS',width=7,command=phy,bg='cyan')
        b15.place(x=490,y=60)
        b16=Button(w1,text='NOVELS',width=7,command=novel,bg='cyan')
        b16.place(x=590,y=60)
        e9=Entry(w1,bd=5,width=31)
        s=e9.get()
        e9.place(x=300,y=420)
        b11=Button(w1,text='Suggest',bg='cyan',command=lambda:suggest(e9))
        b11.place(x=530,y=420)
        w1.mainloop()
strt()