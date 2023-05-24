import smtplib
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import mysql.connector

class main:
    def __init__(self):
        self.main=Tk()
        self.main.title("EVSU BULLING SYSTEM")
        self.main.geometry("1200x730")
        self.main.config(background="#00F2D5")
        self.main.resizable(False,False)

        self.data = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database="portal"
        )
        self.mycursor=self.data.cursor()

        #FRAMES

        self.frm_evsu=Frame(master=self.main,background="#5cd6c6",width=1200,height=80)
        self.frm_evsu.pack()

        self.frm_student_details=Frame(master=self.main,background="#5cd6c6",
                                       width=1100,height=100)
        self.frm_student_details.pack()

        self.space=Frame(master=self.main,background="#00F2D5",
                                       width=1100,height=15)
        self.space.pack()

        self.frm_fhe=Frame(master=self.main,background="#5cd6c6",
                                       width=1100,height=480)
        self.frm_fhe.pack()

        #LABELS
        self.lbl_evsu=Label(master=self.frm_evsu,text="EVSU BILLING SYSTEM",
                            background="#5cd6c6",font=("Courier New Baltic",30))
        self.lbl_evsu.place(x=365,y=15)
        #BUTTON
        btn_log_out=Button(master=self.frm_evsu,text="Log Out",background="#476662",font=("arial bold",15)
                             ,width=10,foreground="#dfe8a2",command=self.log_out)
        btn_log_out.place(x=1050,y=15)
        


        #LABELS FOR STUDENT DETAILS

        self.lbl_student_details=Label(master=self.main,text="Student Details",
                                       background="#00F2D5",font=("Courier New Baltic",20))
        
        self.lbl_student_details.pack(before=self.frm_student_details)

        self.lbl_student_name=Label(master=self.frm_student_details,text="Student Name:",
                                    background="#5cd6c6",font=("Courier New Baltic",15))
        
        self.lbl_student_name.place(x=10,y=8)

        self.lbl_year=Label(master=self.frm_student_details,text="Year Level:",
                            background="#5cd6c6",font=("Courier New Baltic",15))
        
        self.lbl_year.place(x=350,y=8)

        self.lbl_course=Label(master=self.frm_student_details,text="Course:",
                              background="#5cd6c6",font=("Courier New Baltic",15))
        
        self.lbl_course.place(x=350,y=50)

        self.lbl_unit=Label(master=self.frm_student_details,text="No. of Units:",
                            background="#5cd6c6",font=("Courier New Baltic",15))
        
        self.lbl_unit.place(x=630,y=8)

        self.lbl_rate=Label(master=self.frm_student_details,text="Rate Per Units:",
                            background="#5cd6c6",font=("Courier New Baltic",15))
        
        self.lbl_rate.place(x=630,y=50)

        #LABEL FOR FHE
        

        self.lbl_fhe=Label(master=self.frm_fhe,text="FHE COVERED",
                            background="#5cd6c6",font=("Bold",20))
        
        self.lbl_fhe.place(x=490,y=30)

        #FHE LABELS
        self.laboratory_fee=Label(master=self.frm_fhe,text="Laboratory Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.laboratory_fee.place(x=150,y=110)
    
        self.library_fee=Label(master=self.frm_fhe,text="Library Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.library_fee.place(x=150,y=150)

        self.rigistration_fee=Label(master=self.frm_fhe,text="Rigistration Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.rigistration_fee.place(x=150,y=190)

        self.tuition_fee=Label(master=self.frm_fhe,text="Tuition Fee: ",
                            background="#5cd6c6",font=("Bold",15))
        
        self.tuition_fee.place(x=150,y=230)

        self.athletic_fee=Label(master=self.frm_fhe,text="Athletic Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.athletic_fee.place(x=150,y=270)

        self.computer_fee=Label(master=self.frm_fhe,text="Computer Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.computer_fee.place(x=150,y=310)

        self.scuaa_fee=Label(master=self.frm_fhe,text="SCUAA Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.scuaa_fee.place(x=150,y=350)

        self.development_fee=Label(master=self.frm_fhe,text="Development Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.development_fee.place(x=150,y=390)




        self.internet_fee=Label(master=self.frm_fhe,text="Internet Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.internet_fee.place(x=550,y=110)

        self.dental_fee=Label(master=self.frm_fhe,text="Dental  Fee :",
                            background="#5cd6c6",font=("Bold",15))
        
        self.dental_fee.place(x=550,y=150)

        self.school_organ_fee=Label(master=self.frm_fhe,text="School Organ Fee :",
                            background="#5cd6c6",font=("Bold",15))
        
        self.school_organ_fee.place(x=550,y=190)

        self.activity_fee=Label(master=self.frm_fhe,text="Student Activity Fee :",
                            background="#5cd6c6",font=("Bold",15))
        
        self.activity_fee.place(x=550,y=230)

        self.nstp_fee=Label(master=self.frm_fhe,text="NSTP Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.nstp_fee.place(x=550,y=270)

        self.council_fee=Label(master=self.frm_fhe,text="Student Council Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.council_fee.place(x=550,y=310)

        self.guidance_fee=Label(master=self.frm_fhe,text="Guidance Fee :",
                            background="#5cd6c6",font=("Bold",15))
        
        self.guidance_fee.place(x=550,y=350)

        self.medical_fee=Label(master=self.frm_fhe,text="Medical Fee:",
                            background="#5cd6c6",font=("Bold",15))
        
        self.medical_fee.place(x=550,y=390)







        #ENTRYS

        #ENTRYS FOR STUDENT DETAILS
        self.ent_student_name=Entry(master=self.frm_student_details,width=20,font=("arial",20))
        self.ent_student_name.place(x=10,y=40)
        
        #DROP BOX
        options = [
                    "1st Year",
                    "2nd Year",
                    "3rd Year",
                    "4th Year",
                
                    ]
      
        self.clicked_year = StringVar()
        self.clicked_year.set("1st Year")

        self.ent_year=OptionMenu(self.frm_student_details , self.clicked_year , *options )
        self.ent_year.config(border=1,width=10,font=("arial",10))
        self.ent_year.place(x=460,y=8)

        course=[
                "BSIT",
                "BSIE",
                "BSME",
                "BEED",
                "BPEd"
        ]
        self.clicked_course = StringVar()
        self.clicked_course.set("BSIT")

        self.ent_course=OptionMenu(self.frm_student_details , self.clicked_course, *course )
        self.ent_course.config(border=1,width=10,font=("arial",10))
        self.ent_course.place(x=460,y=50)

        self.ent_unit=Entry(master=self.frm_student_details,width=10,font=("arial",20))
        self.ent_unit.place(x=780,y=8)

        self.ent_rate=Entry(master=self.frm_student_details,width=10,font=("arial",20))
        self.ent_rate.place(x=780,y=50)


        #ENTRY FOR FHE
       
        paid_lab=[0,
                100,
                200,
                300,
                400,
                500
        ]
        
        self.paid_lab = IntVar()
        self.paid_lab.set(0)

        self.ent_laboratory_fee=OptionMenu(self.frm_fhe, self.paid_lab, *paid_lab )
        self.ent_laboratory_fee.config(border=1,width=10,font=("arial",10))
        self.ent_laboratory_fee.place(x=335,y=110)
        

        paid_lib=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_lib = IntVar()
        self.paid_lib.set(0)
        self.ent_library_fee=OptionMenu(self.frm_fhe, self.paid_lib, *paid_lib )
        self.ent_library_fee.config(border=1,width=10,font=("arial",10))
        self.ent_library_fee.place(x=335,y=150)

        paid_rig=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_rig = IntVar()
        self.paid_rig.set(0)

        self.ent_rigistration_fee=OptionMenu(self.frm_fhe, self.paid_rig, *paid_rig )
        self.ent_rigistration_fee.config(border=1,width=10,font=("arial",10))
        self.ent_rigistration_fee.place(x=335,y=190)

        paid_tui=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_tui = IntVar()
        self.paid_tui.set(0)

        self.ent_tuition_fee=OptionMenu(self.frm_fhe, self.paid_tui, *paid_tui )
        self.ent_tuition_fee.config(border=1,width=10,font=("arial",10))
        self.ent_tuition_fee.place(x=335,y=230)

        paid_ath=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_ath = IntVar()
        self.paid_ath.set(0)

        self.ent_athletic_fee=OptionMenu(self.frm_fhe, self.paid_ath, *paid_ath )
        self.ent_athletic_fee.config(border=1,width=10,font=("arial",10))
        self.ent_athletic_fee.place(x=335,y=270)

        paid_com=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_com = IntVar()
        self.paid_com.set(0)

        self.ent_computer_fee=OptionMenu(self.frm_fhe, self.paid_com, *paid_com )
        self.ent_computer_fee.config(border=1,width=10,font=("arial",10))
        self.ent_computer_fee.place(x=335,y=310)

        paid_scu=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_scu = IntVar()
        self.paid_scu.set(0)

        self.ent_scuaa_fee=OptionMenu(self.frm_fhe, self.paid_scu, *paid_scu )
        self.ent_scuaa_fee.config(border=1,width=10,font=("arial",10))
        self.ent_scuaa_fee.place(x=335,y=350)

        paid_dev=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_dev = IntVar()
        self.paid_dev.set(0)

        self.ent_development_fee=OptionMenu(self.frm_fhe, self.paid_dev, *paid_dev )
        self.ent_development_fee.config(border=1,width=10,font=("arial",10))
        self.ent_development_fee.place(x=335,y=390)

        paid_int=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_int = IntVar()
        self.paid_int.set(0)


        self.ent_internet_fee=OptionMenu(self.frm_fhe, self.paid_int, *paid_int )
        self.ent_internet_fee.config(border=1,width=10,font=("arial",10))
        self.ent_internet_fee.place(x=760,y=110)

        paid_den=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_den = IntVar()
        self.paid_den.set(0)

        self.ent_dental_fee=OptionMenu(self.frm_fhe, self.paid_den, *paid_den )
        self.ent_dental_fee.config(border=1,width=10,font=("arial",10))
        self.ent_dental_fee.place(x=760,y=150)

        paid_sch=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_sch = IntVar()
        self.paid_sch.set(0)

        self.ent_school_organ_fee=OptionMenu(self.frm_fhe, self.paid_sch, *paid_sch)
        self.ent_school_organ_fee.config(border=1,width=10,font=("arial",10))
        self.ent_school_organ_fee.place(x=760,y=190)

        paid_act=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_act = IntVar()
        self.paid_act.set(0)

        self.ent_activity_fee=OptionMenu(self.frm_fhe, self.paid_act, *paid_act )
        self.ent_activity_fee.config(border=1,width=10,font=("arial",10))
        self.ent_activity_fee.place(x=760,y=230)

        paid_nstp=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_nstp = IntVar()
        self.paid_nstp.set(0)


        self.ent_nstp_fee=OptionMenu(self.frm_fhe, self.paid_nstp, *paid_nstp )
        self.ent_nstp_fee.config(border=1,width=10,font=("arial",10))
        self.ent_nstp_fee.place(x=760,y=270)

        paid_cou=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_cou = IntVar()
        self.paid_cou.set(0)


        self.ent_council_fee=OptionMenu(self.frm_fhe, self.paid_cou, *paid_cou )
        self.ent_council_fee.config(border=1,width=10,font=("arial",10))
        self.ent_council_fee.place(x=760,y=310)

        paid_gui=[0,
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_gui = IntVar()
        self.paid_gui.set(0)


        self.ent_guidance_fee=OptionMenu(self.frm_fhe, self.paid_gui, *paid_gui )
        self.ent_guidance_fee.config(border=1,width=10,font=("arial",10))
        self.ent_guidance_fee.place(x=760,y=350)

        paid_med=[
                100,
                200,
                300,
                400,
                500
        ]

        self.paid_med = IntVar()
        self.paid_med.set(0)


        self.ent_medical_fee=OptionMenu(self.frm_fhe, self.paid_med, *paid_med)
        self.ent_medical_fee.config(border=1,width=10,font=("arial",10))
        self.ent_medical_fee.place(x=760,y=390)

        




        #BUTTONS
        btn_proceced=Button(master=self.frm_student_details,text="Procced payment",
                            background="#476662",font=("arial",10),height=2,foreground="#dfe8a2",command=self.page2)
        
        btn_proceced.place(x=970,y=8)

        btn_clear=Button(master=self.frm_student_details,text="Clear",
                            background="#476662",font=("arial",9),width=6,height=2,foreground="#dfe8a2",command=self.clear)
        
        btn_clear.place(x=995,y=55)

        
        
        self.main.mainloop()
    def log_out(self):
        self.main.destroy()
        import Log_in
        Log_in.mygui()


    def clear(self):
        self.ent_student_name.delete(0,END)
        self.clicked_course.set("BSIT")
        self.clicked_year.set("1st Year")
        self.ent_unit.delete(0,END)
        self.ent_rate.delete(0,END)
        self.paid_lab.set(0)
        self.paid_lib.set(0)
        self.paid_rig.set(0)
        self.paid_tui.set(0)
        self.paid_ath.set(0)
        self.paid_com.set(0)
        self.paid_dev.set(0)
        self.paid_int.set(0)
        self.paid_den.set(0)
        self.paid_sch.set(0)
        self.paid_act.set(0)
        self.paid_nstp.set(0)
        self.paid_cou.set(0)
        self.paid_gui.set(0)
        self.paid_med.set(0)
        



    def page2(self):
        name=self.ent_student_name.get()
        sql="select * from student where student_name=%s or student_name=%s"
        var=(name,name)
        self.mycursor.execute(sql,var)
        result=self.mycursor.fetchone()

        if result != None:
                #COMPUTE THE INPUTED DATA
                lab=self.paid_lab.get()
                lib=self.paid_lib.get()
                rig=self.paid_rig .get()
                tui=self.paid_tui.get()
                ath=self.paid_ath.get()
                com=self.paid_com .get()
                scu=self.paid_scu.get()
                dev=self.paid_dev.get()
                inte=self.paid_int.get()
                den=self.paid_den.get()
                sch=self.paid_sch.get()
                act=self.paid_act.get()
                nstp=self.paid_nstp.get()
                coun=self.paid_cou.get()
                gui=self.paid_gui.get()
                med=self.paid_med.get()
                self.total= int(lab)+int(lib)+int(rig)+int(tui)+int(ath)+int(com)+int(scu)+int(dev)+int(inte)+int(den)+int(sch)+int(act)+int(nstp)+int(coun)+int(gui)+int(med)

                #FORGET
                self.frm_student_details.pack_forget()
                self.frm_fhe.pack_forget()
                self.lbl_student_details.pack_forget()
                self.space.pack_forget()

                #FRAME
                self.frm_payment=Frame(master=self.main,background="#dedbd5",width=320,height=400)
                self.frm_payment.place(x=470,y=150)

                


                #LABEL

                self.lbl_payment=Label(master=self.main,text="PAYMENT:",font=("arial",20),background="#00F2D5")
                self.lbl_payment.place(x=560,y=110)
                
               
                #LABEL PAYMENT
                self.lbl_total_charge=Label(self.frm_payment,text="Total Charge:",font=("arial",15),background="#dedbd5")
                self.lbl_total_charge.place(x=20,y=50)

                self.lbl_total=Label(self.frm_payment,text = self.total, font=("arial",15),background="#dedbd5")
                self.lbl_total.place(x=170,y=50)

                self.lbl_amount_paid=Label(self.frm_payment,text="Amount Paid:",font=("arial",15),background="#dedbd5")
                self.lbl_amount_paid.place(x=20,y=100)

                


                #ENTRY
                self.ent_amount_paid=Entry(master=self.frm_payment,width=10,font=("arial",15))
                self.ent_amount_paid.place(x=155,y=100)

                #BUTTON
                self.btn_main=Button(master=self.frm_payment,text="Back",background="#476662",font=("arial bold",15)
                                ,width=10,foreground="#dfe8a2",command=self.home)
                self.btn_main.place(x=90,y=300)

                #BUTTON PAYMENT
                self.btn_enter=Button(master=self.frm_payment,text="Enter",background="#476662",font=("arial bold",15)
                                ,width=10,foreground="#dfe8a2",command=self.compute)
                self.btn_enter.place(x=90,y=250)

    def compute(self):
        amount=self.ent_amount_paid.get()
        total=self.total
        self.t= int(amount)-int(total)

        self.lbl_change=Label(self.frm_payment,text="Change:",font=("arial",15),background="#dedbd5")
        self.lbl_change.place(x=20,y=150)

        self.lbl_change_total=Label(self.frm_payment,text= self.t ,font=("arial",15),background="#dedbd5")
        self.lbl_change_total.place(x=170,y=150)

        self.btn_enter=Button(master=self.frm_payment,text="Gcash",background="#476662",font=("arial bold",15)
                             ,width=10,foreground="#dfe8a2",command=self.gcash)
        self.btn_enter.place(x=90,y=350)



    def gcash(self):
        
        name=self.ent_student_name.get()
        sql="select * from student where student_name=%s or student_name=%s"
        var=(name,name)
        self.mycursor.execute(sql,var)
        result=self.mycursor.fetchone()

        if result != None:
                webbrowser.open("https://www.gcash.com/")

                s = smtplib.SMTP('smtp.gmail.com', 587)

                # start TLS for security
                s.starttls()

                # Authentication
                
                mycursor=self.data.cursor()
                sql="select email from student where student_name=%s or student_name = %s"
                var=(name,name)
                mycursor.execute(sql,var)
                result=mycursor.fetchone()

                
                s.login("maxp16666@gmail.com", "ycrizekkdjhutyok")

                # message to be sent
                name=self.ent_student_name.get()
                coure=self.clicked_course.get()
                year=self.clicked_year.get()
                unit=self.ent_unit.get()
                rate=self.ent_rate.get()

                lab=str(self.paid_lab.get())
                lib=str(self.paid_lib.get())
                rig=str(self.paid_rig .get())
                tui=str(self.paid_tui.get())
                ath=str(self.paid_ath.get())
                com=str(self.paid_com .get())
                scu=str(self.paid_scu.get())
                dev=str(self.paid_dev.get())
                inte=str(self.paid_int.get())
                den=str(self.paid_den.get())
                sch=str(self.paid_sch.get())
                act=str(self.paid_act.get())
                nstp=str(self.paid_nstp.get())
                coun=str(self.paid_cou.get())
                gui=str(self.paid_gui.get())
                med=str(self.paid_med.get())

                paid = self.ent_amount_paid.get()

                title = "FHE RECEIPT"

                message = (title+"\nStudent name: "+name+"\nCoure: "+coure+"\nYear :"+year+"\nUnit: "+unit+"\nRate: "+rate+
                        "\n\nLaboratory Fee: "+lab+"\nLibrary Fee: "+lib+"\nRigistration Fee: "+rig+"\nTuition Fee: "
                        +tui+"\nAthletic Fee: "+ath+"\nComputer Fee: "+com+"\nSCUAA Fee: "+scu+"\nDevelopment Fee: "+dev
                        +"\n Internet Fee: "+inte+"\nDental Fee: "+den+"\nSchool Organ Fee: "+sch+"\nSchool Activity Fee: "+act
                        +"\nNSTP Fee: "+nstp+"\nStudent Council Fee: "+coun+"\nGuidance Fee: "+gui+"\nMedical Fee: "+med+
                        "\n\n\nTotal Charge: "+str(self.total)+"\nAmount Paid: "+paid+"\nChange: "+str(self.t))

                # sending the mail
                s.sendmail("vasquezjohnpaul709@gmail.com",result[0], message)

                # terminating the session
                s.quit()

                self.btn_main.destroy()
                self.frm_payment.destroy()
                #self.frm_receipt.destroy()
                #self.lbl_receipt.destroy()
                self.lbl_payment.destroy()

                self.lbl_student_details.pack()
                self.frm_student_details.pack()
                self.space.pack()
                self.frm_fhe.pack()
                #Clear
                self.ent_student_name.delete(0,END)
                self.clicked_course.set("BSIT")
                self.clicked_year.set("1st Year")
                self.ent_unit.delete(0,END)
                self.ent_rate.delete(0,END)
                self.paid_lab.set(0)
                self.paid_lib.set(0)
                self.paid_rig.set(0)
                self.paid_tui.set(0)
                self.paid_ath.set(0)
                self.paid_com.set(0)
                self.paid_dev.set(0)
                self.paid_int.set(0)
                self.paid_den.set(0)
                self.paid_sch.set(0)
                self.paid_act.set(0)
                self.paid_nstp.set(0)
                self.paid_cou.set(0)
                self.paid_gui.set(0)
                self.paid_med.set(0)
        else:
            messagebox.showerror(message="Invalid Student Name")
        


    def home(self):
        self.btn_main.destroy()
        self.frm_payment.destroy()
        #self.frm_receipt.destroy()
        #self.lbl_receipt.destroy()
        self.lbl_payment.destroy()

        self.lbl_student_details.pack()
        self.frm_student_details.pack()
        self.space.pack()
        self.frm_fhe.pack()

main()
        


