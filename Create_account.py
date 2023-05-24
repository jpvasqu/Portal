from tkinter import *
import mysql.connector
from tkinter import messagebox
import os

class create:

    def __init__(self):
        self.frm_log_border=Frame(width=400,height=360,background="black")
        self.frm_log_border.place(x=465,y=169)
        self.frm_create=Frame(master=self.frm_log_border,width=380,height=340,background="white")
        self.frm_create.place(x=10,y=10)

        btn_lbl=Button(master=self.frm_create,text="Create Account",
                       font=("Goudy Old Style",15),background="white",
                       border=0,command= self.sign_in
                       )
        btn_lbl.place(x=130,y=5)

        self.student_id=Entry(master=self.frm_create,width=50,font=("Arial",10),
                        border=0)
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=60)

        self.student_name=Entry(master=self.frm_create,width=50,font=("Arial",10),
                        border=0)
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=90)

        self.passowrd=Entry(master=self.frm_create,width=50,
                            font=("Arial",10),border=0)
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=120)


        self.email=Entry(master=self.frm_create,
                         width=50,font=("Arial",10),border=0)        
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=150)
                
        
        


        #BINDING STUDENT ID
        def on_click(e):
            self.student_id.delete(0,END)
        def off_click(e):
            ID=self.student_id.get()
            if ID=="":
                self.student_id.insert(0,"Student Id:")
        self.student_id.place(x=20,y=40)
        self.student_id.insert(0,"Student Id:")
        self.student_id.bind('<FocusIn>',on_click)
        self.student_id.bind('<FocusOut>',off_click)


        #BINDING STUDENT NAME
        def on_click(e):
            self.student_name.delete(0,END)
        def off_click(e):
            name=self.student_name.get()
            if name=="":
                self.student_name.insert(0,"Student Name:")
        self.student_name.place(x=20,y=70)
        self.student_name.insert(0,"Student Name:")
        self.student_name.bind('<FocusIn>',on_click)
        self.student_name.bind('<FocusOut>',off_click)


        #BINDING USER PASSWORD
        def on_click(e):
            self.passowrd.delete(0,END)
        def off_click(e):
            name=self.passowrd.get()
            if name=="":
                self.passowrd.insert(0,"Password:")
        self.passowrd.place(x=20,y=100)
        self.passowrd.insert(0,"Password:")
        self.passowrd.bind('<FocusIn>',on_click)
        self.passowrd.bind('<FocusOut>',off_click)

        #BINDING USER EMAIL
        def on_click(e):
            self.email.delete(0,END)
        def off_click(e):
            name=self.email.get()
            if name=="":
                self.email.insert(0,"Email Address:")
        self.email.place(x=20,y=130)
        self.email.insert(0,"Email Address:")
        self.email.bind('<FocusIn>',on_click)
        self.email.bind('<FocusOut>',off_click)


        def create_acc():
            user_id = self.student_id.get()
            name = self.student_name.get()
            password = self.passowrd.get()
            email = self.email.get()
           
            email = self.email.get()
            data= mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='portal'
                    )
            mycursor=data.cursor()
            if user_id  == " " or password == " " or email == " ":
                messagebox.showerror(title="Invalid choy",message="Please Fill up The form")
            elif user_id  == "Student Id:":
                messagebox.showerror(title="Invalid choy",message="Invalid User Name")
            elif password == "Password:":
                messagebox.showerror(title="Invalid choy",message="Invalid Password")
            elif email == "Email Address:":
                messagebox.showerror(title="Invalid choy",message="Invalid Email Address")
            else:
               
                sql="select * from student where email=%s or email=%s"
                var=(email,email)
                mycursor.execute(sql,var)
                result=mycursor.fetchone()
                if result != None:
                    messagebox.showerror(title="Invalid choy",message=" Account Is Taken ")                  
                else:
                    sql=" insert into student(student_name,student_id,password,email)value(%s,%s,%s,%s)"
                    var=(name,user_id,password,email)
                    mycursor.execute(sql,var)
                    data.commit()
                    messagebox.showinfo(title="Successful",message="Create Account Successful")
            
                    self.frm_log_border.destroy()     
        btn_create=Button(master=self.frm_create,text="Create Account",font=("Alkatra",15),bg="#7be1e8",fg="#0347ad",border=0,width=15,activebackground="white",cursor='hand2',command=create_acc)
        btn_create.place(x=110,y=170)
    def sign_in(self):
         self.frm_log_border.destroy() 