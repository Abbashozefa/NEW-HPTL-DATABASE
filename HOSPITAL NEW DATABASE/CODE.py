import tkinter as tk


m=tk.Tk()
m.title('HOSPITAL DATABASE')
L1=Label(m,text='ENTER PATIENT NAME')
L1.grid(row=0)
L2=Label(m,text='ENTER DOB')
L2.grid(row=1)
E1=Entry(m)
E1.grid(row=0,column=1)
E2=Entry(m)
E2.grid(row=1,column=1)
m.mainloop()