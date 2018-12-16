from tkinter import*
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
def newissue(nm,auth,sub):
    if(len(nm.get())==0):
        sql="select * from "+sub.get()+"lst "+"where author='"+auth.get()+"'"
        crsr=mydb.cursor()
        crsr.execute(sql)
        x=crsr.fetchall()
        if(len(x)==0):
            messagebox.showwarning('NOTE','BOOK NOT AVAILABLE OF SELECTED AUTHOR')
        else:
            rw=len(x)
            cls=len(x[0])
            w=Tk()
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
            w.mainloop()        
def issue(sub,code,W3):
     mydb=mysql.connector.connect(host='localhost',user='root',passwd='swaraj1998',database='alinfo')
     crsr=mydb.cursor()
     sql="update "+sub.get()+"lst "+"set stock=stock-1 where srlno='"+code.get()+"'"
     sql2="select * from "+sub.get()+"lst "+"where srlno='"+code.get()+"'"
     if(len(code.get())==0):
          messagebox.showwarning('NOTE','PLEASE ENTER BOOK CODE')
     else:
          crsr.execute(sql)
          mydb.commit()
          crsr.execute(sql2)
          messagebox.showinfo('NOTE','PLEAESE PAY AT COUNTER AND COLLECT YOUR BOOK')
          W3.destroy()
class another:
    def __init__(self):
        w3=Tk()
        w3.title('New Issue')
        w3.geometry('400x400')
        c8=Canvas(w3,width=4000,height=4000,bg='light green')
        c8.place(x=0,y=0)
        l10=Label(w3,text='By name',bg='light green')
        l10.place(x=100,y=30)
        e20=Entry(w3,bd=3)
        ab=e20.get()
        e20.place(x=170,y=30)
        l11=Label(w3,text='By author',bg='light green')
        l11.place(x=100,y=80)
        e21=Entry(w3,bd=3)
        bc=e21.get()
        e21.place(x=170,y=80)
        l12=Label(w3,text='Sub',bg='light green')
        l12.place(x=100,y=130)
        e22=Entry(w3,bd=3)
        cd=e22.get()
        e22.place(x=170,y=130)
        b10=Button(w3,bd=3,text='search',width=14,command=lambda:newissue(e20,e21,e22))
        b10.place(x=140,y=180)
        l13=Label(w3,text='book code',bg='light green')
        l13.place(x=100,y=230)
        e23=Entry(w3,bd=3)
        e23.place(x=170,y=230)
        b11=Button(w3,text='issue',width=14,command=lambda:issue(e22,e23,w3))
        b11.place(x=140,y=280)
        w3.mainloop()
another()
