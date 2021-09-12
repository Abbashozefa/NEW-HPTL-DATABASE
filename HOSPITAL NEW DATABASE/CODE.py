from tkinter import *
import pymysql
import datetime
conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
a=conn.cursor()
m=Tk()
m.title('HOSPITAL DATABASE')
def ets():
    E1=e.get
    print(E1)

e=Entry(m).grid(row=0)
Button(m,text="yes",command=ets).grid(row=1)






def receptionist():
                def send():
                    pass
                def newp():

                    Label(m,text='PATIENT ID').grid(row=7)
                    user=Entry(m).grid(row=7,column=1)
                    Label(m,text='Enter PATIENT NAME:').grid(row=8)
                    name=Entry(m).grid(row=8,column=1)
                    Label(m,text='Enter PATIENT AGE:').grid(row=9)
                    age=Entry(m).grid(row=9,column=1)
                    Label(m,text='Enter CONSULTING DOCTOR:').grid(row=10)
                    doc=Entry(m).grid(row=10,column=1)
                    G= str(datetime.date.today())
                    
                    
                    
                    
                    
                    
                    Button(m,text='PATIENT ENTRY DONE',command=send)

                def rcpde():
                    Label(m,text='PATIENT ID').grid(row=7)
                    user=Entry(m).grid(row=7,column=1)
                    Label(m,text='Enter PATIENT NAME:').grid(row=8)
                    name=Entry(m).grid(row=8,column=1)
                    Label(m,text='Enter PATIENT AGE:').grid(row=9)
                    age=Entry(m).grid(row=9,column=1)
                    Label(m,text='Enter CONSULTING DOCTOR:').grid(row=10)
                    doc=Entry(m).grid(row=10,column=1)
                    G= str(datetime.date.today())


                def vpd():
                    Label(m,text='PATIENT ID').grid(row=7)
                    user=Entry(m).grid(row=7,column=1)
                    Label(m,text='Enter PATIENT NAME:').grid(row=8)
                    name=Entry(m).grid(row=8,column=1)
                    Label(m,text='Enter PATIENT AGE:').grid(row=9)
                    age=Entry(m).grid(row=9,column=1)
                    Label(m,text='Enter CONSULTING DOCTOR:').grid(row=10)
                    doc=Entry(m).grid(row=10,column=1)
                    G= str(datetime.date.today())

                def delre():
                    Label(m,text='PATIENT ID').grid(row=7)
                    user=Entry(m).grid(row=7,column=1)
                    Label(m,text='Enter PATIENT NAME:').grid(row=8)
                    name=Entry(m).grid(row=8,column=1)
                    Label(m,text='Enter PATIENT AGE:').grid(row=9)
                    age=Entry(m).grid(row=9,column=1)
                    Label(m,text='Enter CONSULTING DOCTOR:').grid(row=10)
                    doc=Entry(m).grid(row=10,column=1)
                    G= str(datetime.date.today())

                Button(m,text='1.NEW PATIENT',command= newp).grid(row=5)
                Button(m,text='2.ROUTINE CHECKUP PATIENT DETAILS ENTRY',command=rcpde).grid(row=6)
                Button(m,text='3.VIEW PATIENT DETAILS',command=vpd).grid(row=7)
                Button(m,text='4.DELETE RECORD',command= delre).grid(row=8)
                Button(m,text='5.GO BACK').grid(row=9)
               
                            
                
                
                    
                    
                    
                     
                     

                   
                
               
                   

                    
                    
               
def general():
                def upep():
                    pass

                def sop():
                    pass


                def dr():
                    pass

               
                Button(m,text='1.UPDATE PATIENTS EYE POWER',command=upep).grid(row=5)
                Button(m,text='2.STATISTICS OF PATIENT',command=sop).grid(row=6)
                Button(m,text='3.DELETE RECORD',command=dr).grid(row=7)
                Button(m,text='4.GO BACK').grid(row=8)
                
                print('1.UPDATE PATIENTS EYE POWER')
                print('2.STATISTICS OF PATIENT')
                print('3.DELETE RECORD')
                print('4.GO BACK')
               
                      
                        
                    
               
               
                    
                    
                
def doctor():
                def ccr():
                    pass

                def delr():
                    pass


                def givpre():
                    pass

                Button(m,text='1.CHECK COMPLETE RECORD',command=ccr).grid(row=5)
                Button(m,text='2.DELETE RECORD',command=delr).grid(row=6)
                Button(m,text='3.GIVE PRESCRIPTION',command=givpre).grid(row=7)
                Button(m,text='4.GO BACK').grid(row=8)
                print('1.CHECK COMPLETE RECORD')
                print('2.DELETE RECORD')
                print('3.GIVE PRESCRIPTION')
                print('4.GO BACK')
                
                
                
                
                    
               
                      
        
conn.commit()
Button(m,text='1.RECEPTIONIST',command=receptionist).grid(row=2)
Button(m,text='2.OPTOMETRIST(GENERAL CHECKUP)',command=general).grid(row=3)
Button(m,text='3.OPTHALMOLOGIST(DOCTOR)',command=doctor).grid(row=4)




m.mainloop()