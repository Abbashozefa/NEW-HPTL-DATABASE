from tkinter import *
import pymysql
import datetime
import pandas as pd
conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
a=conn.cursor()
m=Tk()
m.title('HOSPITAL DATABASE')
def receptionist():
               

                
                def send(user,name,age,doc):
                    

                    user1=user.get()
                    name1=name.get()
                    age1=age.get()
                    doc1=doc.get()
                    a.execute("insert into PATIENT values("+str(user1)+",'"+name1+"',"+str(age1)+",'"+str(datetime.date.today())+"','"+doc1+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                    
                    
                def newp():
                    
                    Label(m,text='PATIENT ID').grid(row=10)
                    user=Entry(m).grid(row=10,column=1)
                    Label(m,text='Enter PATIENT NAME:').grid(row=11)
                    name=Entry(m).grid(row=11,column=1)
                    Label(m,text='Enter PATIENT AGE:').grid(row=12)
                    age=Entry(m).grid(row=12,column=1)
                    Label(m,text='Enter CONSULTING DOCTOR:').grid(row=13)
                    doc=Entry(m).grid(row=13,column=1)             
                                 
                                
                                        
                    Button(m,text='PATIENT ENTRY DONE',command=send(user,name,age,doc)).pack()

                def send1(user,age):
                    
                    user1=user.get()
                    
                    age1=age.get()
                    a.execute("select distinct* from PATIENT where PATIENT_ID="+str(user) )
                    D=a.fetchall()             
                    a.execute("insert into PATIENT values("+str(user)+",'"+D[0][1]+"',"+str(age)+",'"+str(datetime.date.today())+"','"+D[0][4]+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                def rcpde():
                    
                    Label(m,text='Enter PATIENT ID:').grid(row=17)
                    user=Entry(m).grid(row=15,column=1)
                    
                    
                    Label(m,text='Enter PATIENT AGE').grid(row=16)
                    age=Entry(m).grid(row=16,column=1)
                    Button(m,text='DONE',command=send1(user,age)).grid(row=17,column=3)

                def send2(user):
                   
                    user1=user.get()
                    a.execute("select PATIENT_ID  ,PATIENT_NAME,AGE,DATE_OF_LAST_VISIT,CONSULTING_DOCTOR from PATIENT where PATIENT_ID="+str(user))
                    D=a.fetchall()
                    data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR'])
                    data.set_index('PATIENT_ID ',inplace=True)
                    print('-'*100)
                    print(data.iloc[:,0:5])
                    print('-'*100)
                def vpd():
                    Label(m,text='PATIENT ID').grid(row=18)
                    user=Entry(m).grid(row=18,column=1)
                    Button(m,text='Display',command=send2(user)).grid(row=19,column=1)
                def send3(user):
                    
                    user1=user.get()
                    a.execute("delete from patient where PATIENT_ID="+str(user))
                def delre():
                    Label(m,text='Enter PATIENT ID which has to deleted:').grid(row=7)
                    user=Entry(m).grid(row=20,column=1)
                    Button(m,text='Display',command=send3(user)).grid(row=19,column=1)
                     
                Button(m,text='1.NEW PATIENT',command= newp).grid(row=5)
                Button(m,text='2.ROUTINE CHECKUP PATIENT DETAILS ENTRY',command=rcpde).grid(row=6)
                Button(m,text='3.VIEW PATIENT DETAILS',command=vpd).grid(row=7)
                Button(m,text='4.DELETE RECORD',command= delre).grid(row=8)
                Button(m,text='5.GO BACK',command=receptionist).grid(row=9)          
                              
                                                                                                                       
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
                
          
                
                
                    
               
                      
        
conn.commit()
Button(m,text='1.RECEPTIONIST',command=receptionist).grid(row=2)
Button(m,text='2.OPTOMETRIST(GENERAL CHECKUP)',command=general).grid(row=3)
Button(m,text='3.OPTHALMOLOGIST(DOCTOR)',command=doctor).grid(row=4)




m.mainloop()