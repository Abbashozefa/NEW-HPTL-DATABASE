from tkinter import *
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
a=conn.cursor()
m=Tk()
m.title('HOSPITAL DATABASE')
e=Entry(m)
e.grid(row=0)

e1=e.get()
print(e1)



def receptionist():
            
                
                Button(m,text='1.NEW PATIENT').grid(row=5)
                Button(m,text='2.ROUTINE CHECKUP PATIENT DETAILS ENTRY').grid(row=6)
                Button(m,text='3.VIEW PATIENT DETAILS').grid(row=7)
                Button(m,text='4.DELETE RECORD').grid(row=8)
                Button(m,text='5.GO BACK').grid(row=9)
               
                            
                
                
                    
                    
                    
                     
                     

                   
                
               
                   

                    
                    
               
def general():
                Button(m,text='1.UPDATE PATIENTS EYE POWER').grid(row=5)
                Button(m,text='2.STATISTICS OF PATIENT').grid(row=6)
                Button(m,text='3.DELETE RECORD').grid(row=7)
                Button(m,text='4.GO BACK').grid(row=8)
                
                print('1.UPDATE PATIENTS EYE POWER')
                print('2.STATISTICS OF PATIENT')
                print('3.DELETE RECORD')
                print('4.GO BACK')
               
                      
                        
                    
               
               
                    
                    
                
def doctor():
                Button(m,text='1.CHECK COMPLETE RECORD').grid(row=5)
                Button(m,text='2.DELETE RECORD').grid(row=6)
                Button(m,text='3.GIVE PRESCRIPTION').grid(row=7)
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