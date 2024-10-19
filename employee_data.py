from tkinter import *
def create():
    root=Tk()
    root.geometry('500x500')
    l1=Label(root,text='enter name',font=(13))
    l1.pack()
    e1=Entry(root)
    e1.pack()
    l1=Label(root,text='enter salary',font=(13))
    l1.pack()
    e2=Entry(root)
    e2.pack()
    l1=Label(root,text='enter position',font=(13))
    l1.pack()
    e3=Entry(root)
    e3.pack()
    
    def add():
        a=e1.get()
        b=e2.get()
        c=e3.get()
        import mysql.connector
        con=mysql.connector.connect(host="localhost",user="root",db="employee")
        c1=con.cursor()
        s="insert into admin(name,salary,position) values('"+a+"','"+b+"','"+c+"')"
        c1.execute(s)
        con.commit()
        import mysql.connector
        con=mysql.connector.connect(host="localhost",user="root",db="employee")
        c1=con.cursor()
        l="select * from admin"
        c1.execute(l)
        result=c1.fetchall()
        for i in result:
            l5=Label(root,text=i,font=(13))
            l5.pack()
    b6=Button(root,text="add record",font=(13),command=add)
    b6.pack()
    
    def search():
        root=Tk()
        root.geometry('500x500')
        l1=Label(root,text='enter e_id',font=(13))
        l1.pack()
        e7=Entry(root)
        e7.pack()
        def get():
            t=int(e7.get())
            import mysql.connector
            con=mysql.connector.connect(host="localhost",user="root",db="employee")
            c1=con.cursor()
            y="select * from admin"
            c1.execute(y)
            result=c1.fetchall()
            try:
                l8=Label(root,text=result[t-1],font=(13))
                l8.pack()
            except:
                l9=Label(root,text="data not found",font=(13))
                l9.pack()
                
        b9=Button(root,text="search",font=(13),command=get)
        b9.pack()

            
        
        
    def edit():
        root=Tk()
        root.geometry('700x700')
        result=c1.fetchall()
        for i in result:
            l4=Label(root,text=i,font=(13))
            l4.pack()
        l1=Label(root,text='enter employee name',font=(13))
        l1.pack()
        e4=Entry(root)
        e4.pack()
        
        def change():
            l1=Label(root,text='enter salary',font=(13))
            l1.pack()
            e5=Entry(root)
            e5.pack()
            l1=Label(root,text='enter position',font=(13))
            l1.pack()
            e6=Entry(root)
            e6.pack()
        
            
            def update():
                f=e4.get()
                g=e5.get()
                h=e6.get()
                import mysql.connector
                con=mysql.connector.connect(host="localhost",user="root",db="employee")
                c1=con.cursor()
        
                q="update admin set salary='"+g+"' where name='"+f+"'"
                c1.execute(q)
                con.commit()
                import mysql.connector
                con=mysql.connector.connect(host="localhost",user="root",db="employee")
                c1=con.cursor()
                r="update admin set position='"+h+"' where name='"+f+"'"
                c1.execute(r)
                con.commit()
                import mysql.connector
                con=mysql.connector.connect(host="localhost",user="root",db="employee")
                c1=con.cursor()
                l="select * from admin"
                c1.execute(l)
                result=c1.fetchall()
                for i in result:
                    l5=Label(root,text=i,font=(13))
                    l5.pack()
            b2=Button(root,text="update",font=(13),command=update)
            b2.pack()
        b2=Button(root,text="edit details",font=(13),command=change)
        b2.pack()
            
        
    b2=Button(root,text="Edit employee details",font=(13),command=edit)
    b2.pack()
    b3=Button(root,text="search employee data",font=(13),command=search)
    b3.pack()
    
root=Tk()
root.geometry('500x500')
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',db='employee')
c1=con.cursor()
s="select * from admin"
c1.execute(s)
result=c1.fetchall()
l1=Label(text="Employee Details ",font=('cambria',25),fg='red')
l1.pack()
for i in result:
    l3=Label(text=i,font=(20))
    l3.pack()
b1=Button(text="add new employee",font=(13),command=create)
b1.pack()
