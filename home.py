from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import tkinter.messagebox as tmsg


root = Tk()

root.geometry("1920x1280")
root.minsize(1920,1280)
root.maxsize(1920,1280)
root.title("College Management")

mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="homedb")

mycursor = mydb.cursor() 

logo = PhotoImage(file="logo.png")
root.iconphoto(False,logo)

def adminwindow():
    
    def close():
        adminwindow.destroy()
    def insert():
        rollno = roll_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        email = email_entry.get()
        contact = contact_entry.get()
        
        if(rollno=="" or name=="" or contact==""):
            tmsg.showinfo("Insert Status","All Field are Required to be filled")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="projectdb")
            mycursor = mydb.cursor()
            sql="insert into project2 values(%s,%s,%s,%s,%s,%s)"
            data=(rollno,name,age,gender,email,contact)
            mycursor.execute(sql,data)
            mydb.commit()
            roll_entry.delete(0,'end')
            name_entry.delete(0,'end')
            age_entry.delete(0,'end')
            gender_entry.delete(0,'end')
            contact_entry.delete(0,'end')
            email_entry.delete(0,'end')
            
            row = mycursor.rowcount
            show()
            tmsg.showinfo("Successful",f"{row} rows inserted")
            

    def delete():
        if(roll_entry.get()==""):
            tmsg.showinfo("Delete Error","Enter rollno to delete record")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="projectdb")
            mycursor = mydb.cursor()
            sql="delete from project2 where rollno = "+roll_entry.get()+""
            #data=(rollno,name,contact)
            mycursor.execute(sql)
            mydb.commit()
            roll_entry.delete(0,'end')
            name_entry.delete(0,'end')
            contact_entry.delete(0,'end')
            
            row = mycursor.rowcount
            show()
            tmsg.showinfo("Successful",f"{row} rows deleted")
            
    def update():

        if(roll_entry.get()==""):
            tmsg.showinfo("Update Error","Enter rollno to delete record")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="projectdb")
            mycursor = mydb.cursor()
            sql="UPDATE project2 SET name = '"+name_entry.get()+"',age = "+age_entry.get()+",gender = '"+gender_entry.get()+"',email = '"+email_entry.get()+"' , contact = "+contact_entry.get()+" where rollno = "+roll_entry.get()+""
            #data=(rollno,name,contact)
            mycursor.execute(sql)
            mydb.commit()
            roll_entry.delete(0,'end')
            name_entry.delete(0,'end')
            contact_entry.delete(0,'end')
            
            row = mycursor.rowcount
            show()
            tmsg.showinfo("Successful",f"{row} row updated!") 
            
    def get():
        if(roll_entry.get()==""):
            tmsg.showinfo("Display Error","Enter rollno to see all records")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="projectdb")
            mycursor = mydb.cursor()
            sql="Select * from project2 where rollno='"+roll_entry.get()+"'"
            #data=(rollno,name,contact)
            mycursor.execute(sql)
            result = mycursor.fetchall()
            #mydb.commit()
            for row in result:
                name_entry.insert(0,row[1])
                age_entry.insert(0,row[2])
                gender_entry.insert(0,row[3])
                email_entry.insert(0,row[4])
                contact_entry.insert(0,row[5])
                
            mydb.commit()
                
            
    def show():
        mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="projectdb")        
        mycursor=mydb.cursor()
        mycursor.execute("select * from project2")
        result = mycursor.fetchall()
        list.delete(0,list.size())
        for row in result:
            insertData = str(row[0]) + '      ' + row[1] + '        ' + str(row[2]) + '      ' + row[3] + '      ' + row[4] + '      ' + str(row[5]) 
            list.insert(list.size()+1,insertData)
                
    adminwindow = Toplevel(root)
    adminwindow.geometry("1000x300")
    adminwindow.title("Admin Area")
    logo = PhotoImage(file="logo.png")
    adminwindow.iconphoto(False,logo)
    
    bg = PhotoImage(file = "homeimage.png")
    label1 = Label(adminwindow, image = bg)
    label1.place(x = 0, y = 0)

    rollno = Label(adminwindow,text="Roll No",font=('lucide',10,'bold'))
    rollno.place(x=20,y=30)
    roll_entry = Entry(adminwindow)
    roll_entry.place(x=150,y=30)

    name = Label(adminwindow,text="Name",font=('lucide',10,'bold'))
    name.place(x=20,y=60)
    name_entry = Entry(adminwindow)
    name_entry.place(x=150,y=60)

    age = Label(adminwindow,text="Age",font=('lucide',10,'bold'))
    age.place(x=20,y=90)
    age_entry = Entry(adminwindow)
    age_entry.place(x=150,y=90)
    
    gender = Label(adminwindow,text="Gender",font=('lucide',10,'bold'))
    gender.place(x=20,y=120)
    gender_entry = Entry(adminwindow)
    gender_entry.place(x=150,y=120)
    
    contact = Label(adminwindow,text="Contact",font=('lucide',10,'bold'))
    contact.place(x=20,y=150)
    contact_entry = Entry(adminwindow)
    contact_entry.place(x=150,y=150)
    
    email = Label(adminwindow,text="Email",font=('lucide',10,'bold'))
    email.place(x=20,y=180)
    email_entry = Entry(adminwindow)
    email_entry.place(x=150,y=180)
    

    insertbtn = Button(adminwindow,text="Insert",font=('lucide',10,'bold'),bg="white",command=insert)
    insertbtn.place(x=20,y=230)

    deletebtn = Button(adminwindow,text="Delete",font=('lucide',10,'bold'),bg="white",command=delete)
    deletebtn.place(x=80,y=230)

    updatebtn = Button(adminwindow,text="Update",font=('lucide',10,'bold'),bg="white",command=update)
    updatebtn.place(x=145,y=230)

    getbtn = Button(adminwindow,text="Get",font=('lucide',10,'bold'),bg="white",command=get)
    getbtn.place(x=215,y=230)

    list = Listbox(adminwindow)
    list.place(x=350, y=30, width=620)
    show()
    
    
  

def regwindow():
    def close():
        regwindow.destroy()
    regwindow = Toplevel(root)
    regwindow.title("Register Yourself")
    regwindow.geometry("500x500")
    logo = PhotoImage(file="logo.png")
    regwindow.iconphoto(False,logo)
    
    regwindow.bind('<Return>',lambda event: [regdetails()] )  
    def regdetails():
        #print(f"Name is : {namevalue.get()} , Username is : {uservalue.get()} , Password is : {passvalue.get()}")
        namevalue = nameentry.get()
        uservalue = userentry.get()
        passvalue = passentry.get()
        
        if(namevalue=="" or uservalue=="" or passvalue==""):
            tmsg.showinfo("Insert Status","All Field are Required to be filled")
        else:

            sql = "insert into hometable values(%s,%s,%s)"
            data = (namevalue,uservalue,passvalue)
            mycursor.execute(sql,data)
            mydb.commit()
            
            row = mycursor.rowcount
            print(row, " rows inserted")
            
            tmsg.showinfo( "PopUp" ,f"{row} Rows inserted")
            logwindow()
            close()
                
    titleLabel = Label(regwindow, text="Student Registration Form",width=20,font=("bold", 20),fg="red").place(x=50,y=33)        
    namelabel = Label(regwindow,text="Full Name",width=20,font=("bold",10)).grid(row=0,column=0,padx=(20,0),pady=(100,5))
    userlabel = Label(regwindow,text="Username",width=20,font=("bold",10)).grid(row=1,column=0,padx=(20,0),pady=(20,20))
    passlabel = Label(regwindow,text="Password",width=20,font=("bold",10)).grid(row=2,column=0,padx=(20,0),pady=(10,20)) 
    agelabel = Label(regwindow,text="Age",width=20,font=("bold",10)).grid(row=3,column=0,padx=(20,0),pady=(15,20)) 
    genderlabel = Label(regwindow,text="Gender",width=20,font=("bold",10)).grid(row=4,column=0,padx=(0,0),pady=(10,20))
    var = StringVar(regwindow) 
    Radiobutton(regwindow, text="Male",value="Male",variable=var).place(x=200,y=320) 
    Radiobutton(regwindow, text="Female",value="Female",variable=var).place(x=300,y=320)
    gendervalue = var.get()
    
    maillabel = Label(regwindow,text="Email").grid(row=5,column=0,padx=(20,0)) 
    
    
    nameentry = Entry(regwindow)
    nameentry.grid(row=0,column=1,pady=(100,10))
    userentry = Entry(regwindow)
    userentry.grid(row=1,column=1,pady=(5,0))
    passentry = Entry(regwindow,show="*")
    passentry.grid(row=2,column=1)
    ageentry = Entry(regwindow)
    ageentry.grid(row=3,column=1)
    mailentry = Entry(regwindow)
    mailentry.grid(row=5,column=1,pady=(5,0))
    
    
    submitbtn = Button(regwindow,text="Submit",width=10,bg='brown',fg='white',command=lambda:[regdetails()]).grid(row=6,column=1,pady=(25,20))       

    


def logwindow():
    def close():
        logwindow.destroy()
    logwindow = Toplevel(root)
    logwindow.title("Login")
    logwindow.geometry("300x300")
    logo = PhotoImage(file="logo.png")
    logwindow.iconphoto(False,logo)
    
    logwindow.bind('<Return>',lambda event: [log_details()] )  

    def log_details():
        uservalue = userentry.get()
        passvalue = passentry.get()
        
        def studentwindow():
            studentwindow = Toplevel(root)
            studentwindow.title("Student Details")
            studentwindow.geometry("300x300")
            logo = PhotoImage(file="logo.png")
            studentwindow.iconphoto(False,logo)
            
            
            def show():
                mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="homedb")        
                mycursor=mydb.cursor()
                mycursor.execute("Select * from hometable where Password='"+passentry.get()+"'")
                # mycursor.execute("Select * from hometable")
                result = mycursor.fetchall()
                list.delete(0,list.size())
                for row in result:
                    # default = "Name" + '        ' + "UserName" + '          ' + "Password"
                    # list.insert(list.size,default)
                    insertData = str(row[0]) + '        ' + row[1] + '        ' + str(row[2])
                    list.insert(list.size()+1,insertData)
            
            list = Listbox(studentwindow)
            list.place(x=30, y=30, width=230)
            show()
    
        if(uservalue=="" or passvalue==""):
            tmsg.showinfo("Insert Status","All Fields are Required to be filled")
        else:
            studentwindow()
            # sql = "Select * from hometable where Password='"+passentry.get()+"'"
            # mycursor.execute(sql)
            # #mydb.commit()
            # result = mycursor.fetchall()
            # #mydb.commit()
            # for row in result:
            #     userentry.insert(0,row[1])
            #     passentry.insert(0,row[2])
            # mydb.commit()
            # row = mycursor.rowcount
            # print(row, " row displayed")
            
            # tmsg.showinfo( "PopUp" ,f"{row} Row displayed")
            # #close()
        
    # uservalue = StringVar
    # passvalue = StringVar
        
    userlabel = Label(logwindow,text="Username").grid(row=0,column=0,padx=(20,0),pady=(100,0))
    passlabel = Label(logwindow,text="Password").grid(row=1,column=0,padx=(20,0),pady=(0,0))
    
    userentry = Entry(logwindow)
    userentry.grid(row=0,column=1,pady=(100,10))
    passentry = Entry(logwindow,show="*")
    passentry.grid(row=1,column=1,pady=(0,10))
    
    image = Image.open("homeimage.png")
    photo = ImageTk.PhotoImage(image)
    image_label = Label(image=photo)
    image_label.pack()  
    
    submitbtn = Button(logwindow,text="Submit",command=lambda:[log_details()]).grid(row=2,column=1) 
    
        
       

    
## Insert Image
# photo = PhotoImage(file="homeimage.png")
# image_label = Label(image=photo)
# image_label.pack()

image = Image.open("homeimage.png")
photo = ImageTk.PhotoImage(image)
image_label = Label(image=photo)
image_label.pack()

regbtn = Button(root,text="Register",command=regwindow,padx=25,pady=10,font=('lucide',15,'bold'),width=7,height=1,bg='brown',fg='white',border=5)
regbtn.place(relx = 0.483, rely = 0.5,anchor=CENTER)

loginbtn = Button(root,text="Login",command=logwindow,padx=35,pady=10,font=('lucide',15,'bold'),width=5,height=1,bg='brown',fg='white',border=5)
loginbtn.place(relx = 0.57, rely = 0.5,anchor=CENTER)

adminbtn = Button(root,text="Admin",command=adminwindow,padx=15,pady=10,font=('lucide',15,'bold'),width=7,height=1,bg='yellow',fg='black',border=5)
adminbtn.place(relx = 0.40, rely = 0.5,anchor=CENTER)


root.mainloop()
