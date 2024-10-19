from tkinter import *
root=Tk()
root.geometry("600x500")
c1=Canvas(root,height='500',width='600')
l1= Label(text='FD CALCULATOR',font=('cambria',18),fg='red')
l1.place(x='200',y='10')
def one():
    l3=Label(text="enter duration (in years):",font=(13))
    l3.place(x='120',y='120')
    e2=Entry()
    e2.place(x="350",y="130")
    
    
    def two():
       
        t=e2.get()
        t=int(t)
        
        if t>=5:
            l3=Label(text="interest rate :",font=(13))
            l3.place(x='170',y='210')
            e3=Entry()
            e3.place(x="300",y="220")
            def three():
                c1.create_rectangle(100,310,500,45)
                c1.create_oval(100,320,480,440,fill='red')
                
                p=e1.get()
                r=e3.get()
                r=float(r)
    
                p=int(p)
                s=(p*r*t)/100
            
                a=((p*r*t)/100)+p
                l6=Label(text='simple interest:',font=(13),fg='white',bg='red')
                l6.place(x='170',y='350')
                l7=Label(text=s,font=(13),fg='white',bg='red')
                l7.place(x='310',y='350')
                l5=Label(text="final amount :",font=(13),fg='white',bg='red')
                l5.place(x='170',y='390')
                l7=Label(text=a,font=(13),fg='white',bg='red')
                l7.place(x='300',y='390')
            b1=Button(text="calculate",font=(13),command=three,fg='white',bg='blue')
            b1.place(x="250",y="250")
            
        else:
            l3=Label(text="interest rate: 6",font=(13))
            l3.place(x='200',y='210')
            
            
            def three():
                c1.create_rectangle(100,310,500,45)
                c1.create_oval(100,320,480,440,fill='red')
                
                p=e1.get()
        
                r=6
    
                p=int(p)
    
                s=(p*r*t)/100
            
                a=((p*r*t)/100)+p
                l6=Label(text='simple interest:',font=(13),fg='white',bg='red')
                l6.place(x='170',y='350')
                l7=Label(text=s,font=(13),fg='white',bg='red')
                l7.place(x='310',y='350')
                l5=Label(text="final amount :",font=(13),fg='white',bg='red')
                l5.place(x='170',y='390')
                l7=Label(text=a,font=(13),fg='white',bg='red')
                l7.place(x='300',y='390')
            b1=Button(text="calculate",font=(13),command=three,bg='blue',fg='white')
            b1.place(x="250",y="250")
            
    b3=Button(text="enter",font=(10),command=two)
    b3.place(x="250",y="170")
    
        
        
    
l2=Label(text="enter amount to deposit:",font=(13))
l2.place(x='120',y='50')
e1=Entry()
e1.place(x="350",y="60")
b2=Button(text="enter",font=(10),command=one)
b2.place(x="250",y="80")
c1.pack()




            
