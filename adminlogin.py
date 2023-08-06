from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    rollno = roll_entry.get()
    name = name_entry.get()
    contact = contact_entry.get()

    if(rollno=="" or name=="" or contact==""):
        MessageBox.showinfo("Insert Status","All Field are Required to be filled")
    else:
        mydb = mysql.connect(host="localhost",user="root",password="password",database="college")
        mycursor = mydb.cursor()
        sql="insert into students values(%s,%s,%s)"
        data=(rollno,name,contact)
        mycursor.execute(sql,data)
        mydb.commit()
        roll_entry.delete(0,'end')
        name_entry.delete(0,'end')
        contact_entry.delete(0,'end')
        
        row = mycursor.rowcount
        show()
        MessageBox.showinfo("Successful",f"{row} rows inserted")

def delete():
    if(roll_entry.get()==""):
        MessageBox.showinfo("Delete Error","Enter rollno to delete record")
    else:
        mydb = mysql.connect(host="localhost",user="root",password="password",database="college")
        mycursor = mydb.cursor()
        sql="delete from students where rollno = "+roll_entry.get()+""
        #data=(rollno,name,contact)
        mycursor.execute(sql)
        mydb.commit()
        roll_entry.delete(0,'end')
        name_entry.delete(0,'end')
        contact_entry.delete(0,'end')
        
        row = mycursor.rowcount
        show()
        MessageBox.showinfo("Successful",f"{row} rows deleted")
        
def update():

    if(roll_entry.get()==""):
        MessageBox.showinfo("Update Error","Enter rollno to delete record")
    else:
        mydb = mysql.connect(host="localhost",user="root",password="password",database="college")
        mycursor = mydb.cursor()
        sql="UPDATE students SET name = '"+name_entry.get()+"', contact = "+contact_entry.get()+" where rollno = "+roll_entry.get()+""
        #data=(rollno,name,contact)
        mycursor.execute(sql)
        mydb.commit()
        roll_entry.delete(0,'end')
        name_entry.delete(0,'end')
        contact_entry.delete(0,'end')
        
        row = mycursor.rowcount
        show()
        MessageBox.showinfo("Successful",f"{row} row updated!") 
        
def get():
    if(roll_entry.get()==""):
        MessageBox.showinfo("Display Error","Enter rollno to see all records")
    else:
        mydb = mysql.connect(host="localhost",user="root",password="password",database="college")
        mycursor = mydb.cursor()
        sql="Select * from students where rollno='"+roll_entry.get()+"'"
        #data=(rollno,name,contact)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        #mydb.commit()
        for row in result:
            name_entry.insert(0,row[1])
            contact_entry.insert(0,row[2])
        mydb.commit()
            
        
def show():
    mydb = mysql.connect(host="localhost",user="root",password="password",database="college")        
    mycursor=mydb.cursor()
    mycursor.execute("select * from students")
    result = mycursor.fetchall()
    list.delete(0,list.size())
    for row in result:
        insertData = str(row[0]) + '      ' + row[1] + '        ' + str(row[2])
        list.insert(list.size()+1,insertData)
            
root = Tk()
root.geometry("600x300")
root.title("Admin Area")

rollno = Label(root,text="Roll No",font=('lucide',10,'bold'))
rollno.place(x=20,y=30)

name = Label(root,text="Name",font=('lucide',10,'bold'))
name.place(x=20,y=60)

contact = Label(root,text="Contact",font=('lucide',10,'bold'))
contact.place(x=20,y=90)

roll_entry = Entry()
roll_entry.place(x=150,y=30)
name_entry = Entry()
name_entry.place(x=150,y=60)
contact_entry = Entry()
contact_entry.place(x=150,y=90)

insertbtn = Button(root,text="Insert",font=('lucide',10,'bold'),bg="white",command=insert)
insertbtn.place(x=20,y=140)

deletebtn = Button(root,text="Delete",font=('lucide',10,'bold'),bg="white",command=delete)
deletebtn.place(x=80,y=140)

updatebtn = Button(root,text="Update",font=('lucide',10,'bold'),bg="white",command=update)
updatebtn.place(x=145,y=140)

getbtn = Button(root,text="Get",font=('lucide',10,'bold'),bg="white",command=get)
getbtn.place(x=215,y=140)

list = Listbox(root)
list.place(x=300, y=30, width=230)
show()

root.mainloop()