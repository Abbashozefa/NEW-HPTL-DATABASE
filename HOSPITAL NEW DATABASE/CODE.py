from tkinter import *
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
a=conn.cursor()
m=Tk()
m.title('HOSPITAL DATABASE')
L1=Label(m,text='ENTER PATIENT NAME')
L1.grid(row=0)
L2=Label(m,text='ENTER DOB')
L2.grid(row=1)
Button(m,text='1.RECEPTIONIST',command=receptionist).grid(row=2)
Button(m,text='2.OPTOMETRIST(GENERAL CHECKUP)',command=general).grid(row=3)
Button(m,text='3.OPTHALMOLOGIST(DOCTOR)',command=doctor).grid(row=4)

def receptionist():
            while(True):
            
                conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
                a=conn.cursor()
                a.execute("show tables")
                D=a.fetchone()
                if(D==None):
                    a.execute('CREATE TABLE PATIENT(PATIENT_ID INT ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')
                    
                print('-'*100)
                print('1.NEW PATIENT')
                print('2.ROUTINE CHECKUP PATIENT DETAILS ENTRY')
                print('3.VIEW PATIENT DETAILS')
                print('4.DELETE RECORD')
                print('5.GO BACK')
                
                print('-'*100)
                ch2=int(input('SELECT YOUR FIELD:::'))
                print('-'*100)                
                
                '''a.execute('CREATE TABLE PATIENT(PATIENT_ID INT ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')'''
                    
               
                if (ch2==1) :                  
                    
                    user=randint(10000,99999
                                 )
                    name=input('Enter PATIENT NAME:')
                    age=int(input('Enter PATIENT AGE:'))
                    G= str(datetime.date.today())
                    
                    
                    doc=input('Enter CONSULTING DOCTOR:')
                    print('PATIENT ENTRY DONE')
                     
                     

                    a.execute("insert into PATIENT values("+str(user)+",'"+name+"',"+str(age)+",'"+G+"','"+doc+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                elif(ch2==3):
                    user=int(input('Enter PATIENT ID:'))                    
                    a.execute("select PATIENT_ID  ,PATIENT_NAME,AGE,DATE_OF_LAST_VISIT,CONSULTING_DOCTOR from PATIENT where PATIENT_ID="+str(user))
                    D=a.fetchall()
                    data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR'])
                    data.set_index('PATIENT_ID ',inplace=True)
                    print('-'*100)
                    print(data.iloc[:,0:5])
                    print('-'*100)
                    
                    
                elif(ch2==2):
                    user=int(input('Enter PATIENT ID:'))
                    date=str(datetime.date.today())
                    age=int(input('Enter PATIENT AGE'))
                    a.execute("select distinct* from PATIENT where PATIENT_ID="+str(user) )
                    D=a.fetchall()             
                    a.execute("insert into PATIENT values("+str(user)+",'"+D[0][1]+"',"+str(age)+",'"+date+"','"+D[0][4]+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                elif(ch2==4):
                    user=input('Enter PATIENT ID which has to deleted:')
                    a.execute("delete from patient where PATIENT_ID="+str(user))
                              
                else:
                    break
                

                    
                    
                conn.commit()
def general():
            while(True):
                conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
                a=conn.cursor()
                print('-'*100)
                print('1.UPDATE PATIENTS EYE POWER')
                print('2.STATISTICS OF PATIENT')
                print('3.DELETE RECORD')
                print('4.GO BACK')
                print('-'*100)
                ch2=int(input('SELECT YOUR FIELD:::'))
                print('-'*100)        
                        
                    
               
                if (ch2==1) :                 
                    
                    user=input('Enter PATIENT ID:')
                    rsph=input('Enter RIGHT EYE AXIS:')
                    rcyl=input('Enter RIGHT EYE CYLINDRICAL:')
                    raxis=input('Enter RIGHT EYE AXIS:')
                    date=str(datetime.date.today())
                    lsph=input('Enter LEFT EYE AXIS:')
                    lcyl=input('Enter LEFT EYE CYLINDRICAL:')
                    laxis=input('Enter LEFT EYE AXIS:')                      

                    a.execute("update PATIENT set RIGHT_SPH ="+rsph+",RIGHT_CYL ="+rcyl+",RIGHT_AXIS ="+raxis+",LEFT_SPH ="+lsph+",LEFT_CYL ="+lcyl+",LEFT_AXIS="+laxis+"where PATIENT_ID="+user+" and DATE_OF_LAST_VISIT='"+date+"'")
                elif(ch2==3):
                    user=input('Enter PATIENT ID which has to deleted:')
                    a.execute("delete from patient where PATIENT_ID="+str(user))
                    
                elif(ch2==2):
                    user=input('Enter PATIENT ID:')
                    date=str(datetime.date.today())
                    a.execute("SELECT PATIENT_NAME,RIGHT_SPH ,RIGHT_CYL ,RIGHT_AXIS ,LEFT_SPH ,LEFT_CYL ,LEFT_AXIS FROM PATIENT where PATIENT_ID="+str(user)+" and DATE_OF_LAST_VISIT ='"+date+"'")
                              
                    D=a.fetchall()
                    plt.pie([D[0][1],D[0][2],D[0][3],D[0][4],D[0][5],D[0][6]],labels=['RIGHT_SPH ','RIGHT_CYL' ,'RIGHT_AXIS' ,'LEFT_SPH' ,'LEFT_CYL ','LEFT_AXIS'])
                    plt.title(D[0][0]
                              )
                    plt.show()                   
                                        
                else:
                    break    
                    
                conn.commit()
def doctor():
            while(True):
                conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
                a=conn.cursor()
                print('-'*100)
                print('1.CHECK COMPLETE RECORD')
                print('2.DELETE RECORD')
                print('3.GIVE PRESCRIPTION')
                print('4.GO BACK')
                print('-'*100)
                ch2=int(input('SELECT YOUR FIELD:::'))
                print('-'*100)
                
                
                
                    
               
                if (ch2==1) :
                    
                    

                    user=int(input('Enter PATIENT ID:'))
                    a.execute("select *from PATIENT WHERE PATIENT_ID="+str(user))
                    D=a.fetchall()
                    data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                    data.set_index('PATIENT_ID ',inplace=True)
                    print('-'*100)
                    print(data)
                    print('-'*100)                                   
                     

                   
                elif(ch2==3):
                    print('='*100
                          )
                    print('='*40,"PRESCRIPTION",'='*40)
                    
                    user=int(input('           PATIENT ID:: '))
                    print('-'*100)
                    date=str(datetime.date.today())
                    print('                     DATE::',date)                    
                    print('-'*100)
                    med=input('                   MEDICATIONS::')
                    print('-'*100)
                    a.execute("select *from PATIENT WHERE PATIENT_ID="+str(user)+" and DATE_OF_LAST_VISIT='"+date+"'")
                    D=a.fetchall()
                    print('                    NAME :: '+str(D[0][1]))
                    print('-'*100)
                    print('                  AGE :: '+str(D[0][2]))
                    print('-'*100)
                    
                    print('                  CONSULTING DOCTOR'+D[0][4])
                    print('-'*100)
                    data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                    data.set_index('PATIENT_ID ',inplace=True)
                    print(data.iloc[:,5:])
                    print('='*100)
                elif(ch2==2):
                    user=input('Enter PATIENT ID which has to deleted:')
                    a.execute("delete from patient where PATIENT_ID="+str(user))
                else:
                    break  
                conn.commit()    
        
conn.commit()

Button(m,text='yes',command=printing).grid(row=2,column=1)



m.mainloop()