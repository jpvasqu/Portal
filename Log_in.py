import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import mysql.connector

class mygui:
    def __init__(self):
        self.data = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
        )

        cursor = self.data.cursor()
        #MAO NI ANG CODE NGA MOHIMOG DATABASE
        cursor.execute("show databases like %s", ("portal",))
        result = cursor.fetchone()

        if result is None:

            cursor.execute("create database portal")
            cursor.execute("use portal")
            cursor.execute("create table student(id int not null primary key auto_increment,  student_id varchar(30), student_name varchar(50), password varchar(30), email varchar(30), time  timestamp)")
        
            self.data.commit()
            
        else:

            cursor.execute("use portal")
            self.data.commit()
        #KUTUB ARI.A OKAY NA

        self.main=tk.Tk()
        self.main.title("Log In")
        self.main.geometry("1200x630")
        
        self.main.resizable(False,False)

        

        
        


        self.frm_main=tk.Frame(width=854,height=580,background="#00F2D5")
        
        self.photo =ImageTk.PhotoImage(Image.open("evsu.jpg"))
        self.lbl_bg=tk.Label(self.frm_main,image=self.photo)

        self.lbl_bg.pack()
        self.frm_main.pack()

        #BINDING THE ENTRY USER
        def on_click(e):
            self.ent_name.delete(0,tk.END)

        def off_click(e):
             name=self.ent_name.get()
             if name=="":
                self.ent_name.insert(0,"Enter your Student ID")

        #BINDING THE ENTRY PASSWORD
        def on_click_pass(e):
            self.ent_password.delete(0,tk.END)
            self.ent_password.config(show="*")

        def off_click_pass(e):
             psw=self.ent_password.get()
             if psw=="":
                self.ent_password.config(show="")
                self.ent_password.insert(0,"Password:")


            

        #FRAME FOR SIGN IN
        self.frm_log_border=tk.Frame(master=self.frm_main,width=400,height=360,background="black")
        self.frm_log_border.place(x=465,y=169)
        
        self.frm_log=tk.Frame(self.frm_log_border,width=380,height=340,background="white")
        self.frm_log.place(x=10,y=10)

        


        #USER NAME ENRTY
        lbl_sign=tk.Label(master=self.frm_log,text="Sign In",font=("Goudy Old Style",20),bg="white",cursor="cross")
        self.ent_name=tk.Entry(master=self.frm_log,width=30,font=("Goudy Old Style",15),border=0)
        self.ent_password=tk.Entry(master=self.frm_log,width=30,font=("Goudy Old Style",15),border=0)
        
        lbl_sign.place(x=150,y=10)
        

        #POSSITION AND MORE
        self.ent_name.place(x=20,y=70)
        self.ent_name.insert(0,"Enter your Student ID")
        self.ent_name.bind('<FocusIn>',on_click)
        self.ent_name.bind('<FocusOut>',off_click)
        tk.Frame(self.frm_log,width=315,height=2,background='black').place(x=20,y=94)

        
        self.ent_password.place(x=20,y=120)
        self.ent_password.insert(0,"Password:")
        self.ent_password.bind('<FocusIn>',on_click_pass)
        self.ent_password.bind('<FocusOut>',off_click_pass)
        tk.Frame(self.frm_log,width=315,height=2,background='black').place(x=20,y=145)
        
        #BUTTONS
        btn_signin=tk.Button(master=self.frm_log,text="Sign In",font=("Alkatra",15),bg="#7be1e8",fg="#0347ad",border=0,width=15,activebackground="white",cursor='hand2',command=self.sign)
        btn_signin.place(x=109,y=160)

        lbl_create=tk.Label(master=self.frm_log,text="Don't have any account?",font=("Goudy Old Style",11),bg='white')
        lbl_create.place(x=110,y=225)

        btn_yes=tk.Button(master=self.frm_log,text="YES",font=("Alkatra",8),bg="white",fg="#0347ad",cursor="hand2",border=0,activebackground="white",command=self.create_account)
        btn_yes.place(x=256,y=228)


        btn_forget=tk.Button(master=self.frm_log,text="Forget Password?",font=("Alkatra",11),bg="white",fg="#0347ad",cursor="hand2",border=0,activebackground="white",command=self.forget_pass)
        btn_forget.place(x=135,y=200)
        
        self.btn_show=tk.Button(master=self.frm_log,text="Show",font=("Alkatra",11),bg="white",fg="Black",cursor="hand2",border=0,activebackground="white",command=self.show_password)
        self.btn_show.place(x=290,y=115)
        self.main.mainloop()

    #PAG CLICK NIMO SA BUTTON NGA SIGIN MAO NI NGA FUNCTION ANG MO GANA
    def sign(self):
        user=self.ent_name.get()
        passowrd=self.ent_password.get()

        mycursor=self.data.cursor()
        sql="select * from student where student_id=%s and password=%s"
        var=(user,passowrd)
        mycursor.execute(sql,var)
        result=mycursor.fetchone()

        if result != None:
            self.main.destroy()
            import main
            main.main()
        else:
            messagebox.showerror(title="Invalid choy",message="Invalid User Name Or Password")

    #WHEN YOU CLICK THE BUTTON CREATE MAO NI ANG MO GANA
    def create_account(self):

        #ATO.A GI IMPORT ANG FILE NGA CREATE ACOUNT
        import Create_account
        Create_account.create()
    
    def forget_pass(self):
        import forget_pass
        forget_pass.forgotpass()

        

    def show_password(self):
        if  self.btn_show["text"]=="Show":
             self.ent_password.config(show="")
             self.btn_show.config(text="Hide")

        else:
             self.ent_password.config(show="*")
             self.btn_show.config(text="Show")

mygui()