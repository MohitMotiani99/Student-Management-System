import os
import platform
import mysql.connector
def selection():
    print('-----------------------------------\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n-----------------------------------')
    print('a.NEW ADMISSION')
    print('b.UPDATE STUDENT DETAILS')
    print('c.DELETE A RECORD')
    c=input("Enter ur choice (a-c) : ")
    print('\nInitially the details are..\n')
    if c=='a':
        print("Initially the student details are:----\n")
        display1()
        print("Initially the marks details are:----\n")
        display2()
        insert1()
        print('\nModified details are..\n')
        print('\nModified Student details are..\n')
        display1()
        print('\nModified Marks details are..\n')
        display2()
    elif c=='b':
        print("Initially the student details are:----\n")
        display1()
        update1()
        print('\nModified Student details are..\n')
        display1()
    elif c=='c':
        print("Initially the student details are:----\n")
        display1()
        print("Initially the marks details are:----\n")
        display2()
        delete1()
        print('\nModified Student details are..\n')
        display1()
        print('\nModified Marks details are..\n')
        display2()
        
    else:
        print('Enter correct choice...!!')
def insert1():
    sname1=input("Enter Student Name : ")
    admno1=int(input("Enter Admission No : "))
    dob1=input("Enter Date of Birth(yyyy-mm-dd): ")
    cls1=input("Enter class for admission: ")
    cty1=input("Enter City : ")
    f1=input("Enter Father Name: ")
    m1=input("Enter Mother Name: ")
    num=input("Enter Father\'s Mobile Number: ")
    bus=input("Enter Bus Number(if any): ")
    bg=input("Enter your Blood Group: ")
    db = mysql.connector.connect(user='root', password='abcd', host='localhost',database='mysql')
    cursor = db.cursor()
    sql="insert into student (sname,admno,dob,cls,cty,father,mother,father_m_num,bus_num,blood_grp) values ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s')"%(sname1,admno1,dob1,cls1,cty1,f1,m1,num,bus,bg)
    sql2="insert into marks (admno,physics,chemistry,maths,english,comp_science) values ('%d',0,0,0,0,0)"%(admno1)
    try:
        cursor.execute(sql)
        cursor.execute(sql2)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
def display1():
    try:
        print("Student Name   Admission  Num   DOB   Class   City   Father\'s Name    Mother\'s Name    Father\'s Mobile Num   Bus Num   Blood Group\n")
        db = mysql.connector.connect(user='root', password='abcd', host='localhost',database='mysql')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            f=c[5]
            m=c[6]
            num=c[7]
            bus=c[8]
            bg=c[9]
            print ("%s                %d            %s           %s         %s        %s        %s        %s        %s          %s" % (sname,admno,dob,cls,cty,f,m,num,bus,bg))
    except:
        print ("Error: unable to fetch data")
        db.close()
def update1():
    try:
        db = mysql.connector.connect(user='root', password='abcd', host='localhost',database='mysql')
        cursor = db.cursor()
    except:
        print ("Error: unable to Establish Connection...")
    print()
    tempst=int(input("Enter Admission No : "))
    print("1:Update Student name\n")
    print("2:Update Admission Number\n")
    print("3:Update DOB\n")
    print("4:Update Class\n")
    print("5:Update City\n")
    print("6:Update Father\'s Name\n")
    print("7:Update Mother\'s Name\n")
    print("8:Update Father\'s Mobile Num\n")
    print("9:Update Bus Num\n")
    print("10:Update Blood Group\n")
    ans=int(input("Enter Choice: "))
    if ans==1:
        temp=input("Enter new Student Name : ")
        try:
            sql = "Update student set sname='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==2:
        temp=int(input("Enter new Admission Number : "))
        try:
            sql = "Update student set admno='%d' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==3:
        temp=input("Enter new DOB : ")
        try:
            sql = "Update student set dob='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==4:
        temp=input("Enter new Class : ")
        try:
            sql = "Update student set cls='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==5:
        temp=input("Enter new City : ")
        try:
            sql = "Update student set cty='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==6:
        temp=input("Enter Corrected Father\'s Name : ")
        try:
            sql = "Update student set father='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==7:
        temp=input("Enter Corrected Mother\'s Name : ")
        try:
            sql = "Update student set mother='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==8:
        temp=input("Enter new \'Father\'s Mobile Number\' : ")
        try:
            sql = "Update student set father_m_num='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==9:
        temp=input("Enter new Bus Number : ")
        try:
            sql = "Update student set bus_num='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==10:
        temp=input("Enter new Blood Group : ")
        try:
            sql = "Update student set blood_grp='%s' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    else :
        print("Enter Valid Choice.\n")

        
def delete1():
    try:
        db = mysql.connector.connect(user='root', password='abcd', host='localhost',database='mysql')
        cursor = db.cursor()
    except:
        print ("Error: unable to fetch data")
    temp=int(input("\nEnter adm no to be deleted : "))
    try:
        sql = "delete from student where admno='%d'" % (temp)
        sql2 = "delete from marks where admno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            cursor.execute(sql2)
            db.commit()
    except Exception as e:
        print (e)
        db.close()



def selection2():
    print('-----------------------------------\nWELCOME TO REPORT CARD MANAGEMENT CENTRE\n-----------------------------------')
    print("Initially the marks details are:----\n")
    display2()
    update2()
    print('\nModified Marks details are..\n')
    display2()
   
def display2():
    try:
        print("Admission Num        Physics          Chemistry         Maths       English        Computer Science\n")
        db = mysql.connector.connect(user='root', password='abcd', host='localhost',database='mysql')
        cursor = db.cursor()
        sql = "SELECT * FROM marks"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            p=c[1]
            chem=c[2]
            ma=c[3]
            e=c[4]
            cs=c[5]
            print ("%d                %d                %d               %d           %d                   %d" % (admno,p,chem,ma,e,cs))
    except:
        print ("Error: unable to fetch data")
        db.close()
def update2():
    try:
        db = mysql.connector.connect(user='root', password='abcd', host='localhost',database='mysql')
        cursor = db.cursor()
    except:
        print ("Error: unable to Establish Connection...")
    tempst=int(input("Enter Admission No : "))
    print("1:Update Physics Marks\n")
    print("2:Update Chemistry Marks\n")
    print("3:Update Maths Marks\n")
    print("4:Update English Marks\n")
    print("5:Update Comp Science Marks\n")
    ans=int(input("Enter Choice: "))
    if ans==1:
        temp=input("Enter new Physics Marks : ")
        try:
            sql = "Update marks set physics='%d' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==2:
        temp=int(input("Enter new Chemistry Marks : "))
        try:
            sql = "Update marks set chemistry='%d' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==3:
        temp=input("Enter new Maths marks : ")
        try:
            sql = "Update marks set maths='%d' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==4:
        temp=input("Enter new English Marks : ")
        try:
            sql = "Update marks set english='%d' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    elif ans==5:
        temp=input("Enter new Computer Science Marks : ")
        try:
            sql = "Update marks set comp_science='%d' where admno='%d'" % (temp,tempst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()
    else :
        print("Enter Valid Choice.\n")

        
ans='y'
while True :
    try:
        db = mysql.connector.connect(user='root', password='abcd', host='localhost',database='mysql')
        cursor = db.cursor()
    except:
        print ("Error: unable to fetch data")
    print("1:Enter as User")
    print("2:Enter as Admin")
    ch=int(input("Enter your Choice: "))
    if ch==1:
        print("===============================================WELCOME USER================================================================\n")
        print("\n1:See Profile")
        print("2:See Report Card")
        ch3=int(input("Enter option: "))
        if ch3==1:
            ans2=int(input("Enter password(admno): "))
            sql="select * from student where admno='%d'" %ans2
            cursor.execute(sql)
            res=cursor.fetchall();
            if len(res)==0:
                print("Wrong Password")
            else:
                print("\n-------------------------------------------Your INFORMATION--------------------------------------------------------\n")
                for c in res:
                    sname = c[0]
                    admno= c[1]
                    dob=c[2]
                    cls=c[3]
                    cty=c[4]
                    f=c[5]
                    m=c[6]
                    num=c[7]
                    bus=c[8]
                    bg=c[9]
                print("Student Name: %s"% sname)
                print("Admission Number: %d"% admno)
                print("Date of Birth: %s"% dob)
                print("Class: %s"% cls)
                print("City: %s"% cty)
                print("Father\'s Name: %s"% f)
                print("Mother\'s Name: %s"% m)
                print("Father\'s Mobile Number: %s"% num)
                print("Bus Number: %s"% bus)
                print("Blood Group: %s"% bg)
                print("-----------------------------------------------------------------------------------------------------------------------\n")
        elif ch3==2:
            ans2=int(input("Enter password(admno): "))
            sql="select * from marks where admno='%d'" %ans2
            cursor.execute(sql)
            res=cursor.fetchall();
            if len(res)==0:
                print("Wrong Password")
            else:
                print("\n-------------------------------------------REPORT CARD--------------------------------------------------------\n")
                for c in res:
                    admno= c[0]
                    p=c[1]
                    chem=c[2]
                    ma=c[3]
                    e=c[4]
                    cs=c[5]
                sql="select sname,cls from student where admno='%d'" %ans2
                cursor.execute(sql)
                res=cursor.fetchall();
                for c in res:
                    sname=c[0]
                    cls=c[1]
                print("Student Name: %s"% sname)
                print("Admission Number: %d"% admno)
                print("Class: %s"% cls)
                print("----------------------------------------------------------------------------------------------\n")
                print("Subjects       Physics       Chemistry        Maths         English         Computer Science\n")
                print("Marks             %d             %d             %d             %d                   %d"%(p,chem,ma,e,cs))
                print("----------------------------------------------------------------------------------------------\n")
                percent=(p+ma+chem+e+cs)/5
                if percent>=80 :
                    print("GRADE:A")
                elif percent>=60:
                    print("GRADE:B")
                elif percent>=40 :
                    print("GRADE:C")
                elif percent>=20 :
                    print("GRADE:D")
                else :
                    print("GRADE:E")
              
                print("-----------------------------------------------------------------------------------------------------------------------\n")
            
            
    elif ch==2:
        print("==============================================WELCOME ADMIN==================================================================\n")
        ch2=input("Enter Administrative Password:")
        if ch2=='root':
            print("\n1:Update Student Details")
            print("2:Update Report Card\n")
            ch4=int(input("Enter your Choice: "))
            if ch4==1 :
                selection()
            elif ch4==2 :
                selection2()
            print("-----------------------------------------------------------------------------------------------------------------------\n")
        else:
            print("Enter Valid Administrative Password")
    else:
        print("Enter Valid Choice")
    ans=input("Do you want to continue?(y/n) ")
    if ans!='y' :
        print("\n**************************************THANK YOU*****************************************************************\n")
        break



