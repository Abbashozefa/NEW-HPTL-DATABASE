from tkinter import *


m=Tk()
m.title('HOSPITAL DATABASE')
L1=Label(m,text='ENTER PATIENT NAME')
L1.grid(row=0)
L2=Label(m,text='ENTER DOB')
L2.grid(row=1)
def printing():
    name=e1.get()
    Label(m,text=name).grid(row=3,column=1)
e1=Entry(m)
e1.grid(row=0,column=1)

E2=Entry(m)
E2.grid(row=1,column=1)
Button(m,text='yes',command=printing).grid(row=2,column=1)



m.mainloop()