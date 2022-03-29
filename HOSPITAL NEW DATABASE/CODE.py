from tkinter import *
import pymysql
import datetime
import pandas as pd
conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
a=conn.cursor()
m=Tk()


m.title('HOSPITAL DATABASE')
def receptionist():
               

                
                def send(user_,name_,age_,doc_):
                    

                    user1=user_.get()
                    name1=name_.get()
                    age1=age_.get()
                    doc1=doc_.get()
                    a.execute("insert into PATIENT values("+str(user1)+",'"+name1+"',"+str(age1)+",'"+str(datetime.date.today())+"','"+doc1+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                    
                    
                def newp():
                    
                    Label(m,text='PATIENT ID').pack()
                    user=Entry(m).pack()
                    Label(m,text='Enter PATIENT NAME:').pack()
                    name=Entry(m).pack()
                    Label(m,text='Enter PATIENT AGE:').pack()
                    age=Entry(m).pack()
                    Label(m,text='Enter CONSULTING DOCTOR:').pack()
                    doc=Entry(m).pack()             
                                 
                                
                                        
                    Button(m,text='PATIENT ENTRY DONE',command=send(user,name,age,doc)).pack()

                def send1(user,age):
                    
                    user1=user.get()
                    
                    age1=age.get()
                    a.execute("select distinct* from PATIENT where PATIENT_ID="+str(user) )
                    D=a.fetchall()             
                    a.execute("insert into PATIENT values("+str(user)+",'"+D[0][1]+"',"+str(age)+",'"+str(datetime.date.today())+"','"+D[0][4]+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                def rcpde():
                    
                    Label(m,text='Enter PATIENT ID:').pack( )
                    user=Entry(m).pack()
                    
                    
                    Label(m,text='Enter PATIENT AGE').pack()
                    age=Entry(m).pack()
                    Button(m,text='DONE',command=send1(user,age)).pack()

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
                    Label(m,text='PATIENT ID').pack()
                    user=Entry(m).pack()
                    Button(m,text='Display',command=send2(user)).pack()
                def send3(user):
                    
                    user1=user.get()
                    a.execute("delete from patient where PATIENT_ID="+str(user))
                def delre():
                    Label(m,text='Enter PATIENT ID which has to deleted:').pack()
                    user=Entry(m).pack()
                    Button(m,text='Display',command=send3(user)).pack()
                     
                Button(m,text='1.NEW PATIENT',command= newp).pack()
                Button(m,text='2.ROUTINE CHECKUP PATIENT DETAILS ENTRY',command=rcpde).pack()
                Button(m,text='3.VIEW PATIENT DETAILS',command=vpd).pack()
                Button(m,text='4.DELETE RECORD',command= delre).pack()
                Button(m,text='5.GO BACK',command=receptionist).pack()          
                              
                                                                                                                       
def general():
                def upep():
                    pass

                def sop():
                    pass


                def dr():
                    pass

               
                Button(m,text='1.UPDATE PATIENTS EYE POWER',command=upep).pack()
                Button(m,text='2.STATISTICS OF PATIENT',command=sop).pack()
                Button(m,text='3.DELETE RECORD',command=dr).pack()
                Button(m,text='4.GO BACK').pack()
                
                            
                                                           
                      
def doctor():
                def ccr():
                    pass

                def delr():
                    pass


                def givpre():
                    pass

                Button(m,text='1.CHECK COMPLETE RECORD',command=ccr).pack()
                Button(m,text='2.DELETE RECORD',command=delr).pack()
                Button(m,text='3.GIVE PRESCRIPTION',command=givpre).pack()
                Button(m,text='4.GO BACK').pack()
                
          
                
                
                    
               
                      
        
conn.commit()
Button(m,text='1.RECEPTIONIST',command=receptionist).pack()
Button(m,text='2.OPTOMETRIST(GENERAL CHECKUP)',command=general).pack()
Button(m,text='3.OPTHALMOLOGIST(DOCTOR)',command=doctor).pack()




m.mainloop()