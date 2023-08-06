from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import tkinter.messagebox as tmsg

root = Tk()

root.geometry("500x500")
#root.geometry("300x300")
root.minsize(300,300)
root.maxsize(500,500)
root.title("Registration Form")


mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="sampledb")

mycursor = mydb.cursor() 
  
labl_0 = Label(root, text="Registration form",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  
  
  
labl_1 = Label(root, text="FullName",width=20,font=("bold", 10))  
labl_1.place(x=80,y=130)  
  
entry_1 = Entry(root)  
entry_1.place(x=240,y=130)  
  
labl_2 = Label(root, text="Email",width=20,font=("bold", 10))  
labl_2.place(x=68,y=180)  
  
entry_02 = Entry(root)  
entry_02.place(x=240,y=180)  
  
labl_3 = Label(root, text="Gender",width=20,font=("bold", 10))  
labl_3.place(x=70,y=230)  
varblbl = StringVar(root,"Male")  
Radiobutton(root, text="Male",padx = 5, value=1).place(x=235,y=230)  
Radiobutton(root, text="Female",padx = 30, value=2).place(x=290,y=230)  
  
labl_4 = Label(root, text="Age:",width=20,font=("bold", 10))  
labl_4.place(x=70,y=280)  
  
  
entry_02 = Entry(root)  
entry_02.place(x=240,y=280)  
  
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)  
# it will be used for displaying the registration form onto the window   
print("Registration form is created seccussfully...")  

# root.title("College Management")

# def sayhello():
#     #print(namevalue.get(), agevalue.get() , salaryvalue.get())
#     namevalue = entername.get()
#     agevalue = enterage.get()
#     salaryvalue = entersalary.get()

#     sql = "insert into sampletable values(%s,%s,%s)"
#     data = (namevalue,agevalue,salaryvalue)
#     mycursor.execute(sql,data)
#     mydb.commit()
    
#     row = mycursor.rowcount
#     print(row, " rows inserted")
    
#     tmsg.showinfo( "PopUp" ,f"{row} Rows inserted")

# label1 = Label(root,text='Username',font="arial,10,bold")
# label1.grid(row=0,column=0,padx=20,pady=20,sticky=W)

# label2 = Label(root,text='Age', font="arial,10,bold")
# label2.grid(row=1,column=0,padx=20,pady=20,sticky=W)

# label3 = Label(root,text='Salary', font="arial,10,bold")
# label3.grid(row=2,column=0,padx=20,pady=20,sticky=W)

# salaryvalue = IntVar()
# agevalue = IntVar()
# namevalue = IntVar()
# IntVar
# entername = Entry(root,textvariable=namevalue)
# entername.grid(row=0,column=1,padx=20,pady=20)

# enterage = Entry(root,textvariable=agevalue)
# enterage.grid(row=1,column=1,padx=20,pady=20)

# entersalary = Entry(root,textvariable=salaryvalue)
# entersalary.grid(row=2,column=1,padx=20,pady=20)

# entername = Entry(root)
# entername.grid(row=0,column=1,padx=20,pady=20)

# enterage = Entry(root)
# enterage.grid(row=1,column=1,padx=20,pady=20)

# entersalary = Entry(root)
# entersalary.grid(row=2,column=1,padx=20,pady=20)



# btn = Button(root,text="Click Me", command=sayhello).grid(row=3,column=1)


root.mainloop()
