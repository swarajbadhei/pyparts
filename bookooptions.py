from tkinter import*
import os
import sys
def issue():
    sys.path.append("C:\\Users\\Swaraj Badhei\\Desktop\\cls python\\prjct\\cmpltd\\new_issue_module.py")
    from new_issue_module.py import haha
w=Tk()
w.geometry('800x600')
w.title('resister book')
b1=Button(w,text='New Issue',bd=5,height=3,width=15,command=issue)
b1.place(x=0,y=50)
b2=Button(w,text='Issued Books',bd=5,height=3,width=15)
b2.place(x=0,y=150)
b3=Button(w,text='Sale',bd=5,height=3,width=15)
b3.place(x=0,y=250)
b4=Button(w,text='Return',bd=5,height=3,width=15)
b4.place(x=0,y=350)
b5=Button(w,text='Show All',bd=5,height=3,width=15)
b5.place(x=0,y=450)
b6=Button(w,text='Logout',bd=5,height=3,width=15)
b6.place(x=679,y=250)
e1=Entry(w,bd=5,width=31)
r=e1.get()
e1.pack()
b7=Button(w,text='Search')
b7.pack()
e2=Entry(w,bd=5,width=31)
s=e2.get()
e2.pack()
b8=Button(w,text='Suggest')
b8.pack()
b9=Button(w,text='move back',command=back)
b9.pack()
w.mainloop()