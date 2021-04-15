from tkinter import *
from tkinter import messagebox,ttk 
from tkinter.messagebox import *
import pymysql 
import time
import os
import tempfile
import pandas

class EmployeeSystem:
    #code for main window here we intialize our main window having 3 frames with different functionalities
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Management & Salary Receipt Generator System | Developed BY Sanmesh Yashwantrao")
        self.root.geometry("1920x1080+-10+0")                  
        title = Label(self.root,text = "EMSRG System",font=("Verdana",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp = Button(self.root,text = "Employees Data",command=self.employee_frame,font=("Helvetica",20,"bold"),bg="LightSeaGreen",fg="black").place(x=1250,y=10,height=40,width=230)
        btn_emp = Button(self.root,text = "SAVE ALL EMP DATA",command=self.print_emp_data,font=("Helvetica",15,"bold"),bg="LightSeaGreen",fg="black").place(x=1000,y=10,height=40,width=230)
    #=============== FRAME1 ======================

    #================= Variables for frame 1======================
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_experience=StringVar()
        self.var_proof_id=StringVar()    #aadhar card
        self.var_contact=StringVar()
        self.var_status=StringVar()
  

    #code for frame 1 personal details of employee
        Frame1 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=700)
        title2 = Label(Frame1,text = "Employee Details",font=("BodoniAnt",20,"bold"),bg="cyan",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
    
    #========= ROW1 ============

    #code for employee
        lb1_code = Label(Frame1,text = "Employee Code",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=50)
        self.txt_code = Entry(Frame1,font=("times new roman",15),textvariable=self.var_emp_code,bg="lightcyan",fg="black")
        self.txt_code.place(x=220,y=60,width = 220)
        btn_search = Button(Frame1,text = "Search",command = self.search,font=("times new roman",20,"bold"),bg="Aquamarine",fg="black").place(x=510,y=50,height=40,width=140)
    #========= ROW2 ============

    #code for  Designation    
        lb1_designation = Label(Frame1,text = "Designation",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=100)
        txt_designation = Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="LightCyan",fg="black").place(x=170,y=110,width = 140)

    #code for  Date of birth
        lb1_dob = Label(Frame1,text = "D.O.B",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=100)
        txt_dob = Entry(Frame1,font=("times new roman",15),textvariable=self.var_dob ,bg="LightCyan",fg="black").place(x=510,y=110,width = 200)  

    #========= ROW3 ============

    #code for Name   
        lb1_name = Label(Frame1,text = "Name",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=150)
        txt_name = Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,bg="LightCyan",fg="black").place(x=110,y=160,width = 200)

    #code for Date of joining
        lb1_doj = Label(Frame1,text = "D.O.J",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=150)
        txt_doj = Entry(Frame1,font=("times new roman",15),textvariable=self.var_doj,bg="LightCyan",fg="black").place(x=510,y=160,width = 200)


    #========= ROW4 ============

    #code for age   
        lb1_age = Label(Frame1,text = "Age",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=200)
        txt_age = Entry(Frame1,font=("times new roman",15),textvariable=self.var_age,bg="LightCyan",fg="black").place(x=110,y=210,width = 200)

    #code for Expeirence
        lb1_experience = Label(Frame1,text = "Experience",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=200)
        txt_experience = Entry(Frame1,font=("times new roman",15),textvariable=self.var_experience,bg="LightCyan",fg="black").place(x=510,y=210,width = 200)


    #========= ROW5 ============

    #code for Gender    
        lb1_gender = Label(Frame1,text = "Gender",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=250)
        txt_gender = Entry(Frame1,font=("times new roman",15),textvariable=self.var_gender,bg="LightCyan",fg="black").place(x=110,y=260,width = 200)

    #code for Proof ID
        lb1_proof = Label(Frame1,text = "Proof ID",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=250)
        txt_proof = Entry(Frame1,font=("times new roman",15),textvariable=self.var_proof_id,bg="LightCyan",fg="black").place(x=510,y=260,width = 200)


    #========= ROW6 ============

    #code for Email    
        lb1_email = Label(Frame1,text = "Email",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=300)
        txt_email = Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="LightCyan",fg="black").place(x=110,y=310,width = 200)

    #code for Contact No
        lb1_contact = Label(Frame1,text = "Contact",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=300)
        txt_contact = Entry(Frame1,font=("times new roman",15),textvariable=self.var_contact,bg="LightCyan",fg="black").place(x=510,y=310,width = 200)
    

    #========= ROW7 ============

    #code for Hired Location   
        lb1_hired = Label(Frame1,text = "Hired Loc.",wraplength = 280,font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=350)
        txt_hired = Entry(Frame1,font=("times new roman",15),textvariable=self.var_hr_location,bg="LightCyan",fg="black").place(x=150,y=360,width = 160)

    #code for status
        lb1_status = Label(Frame1,text = "Status",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=350)
        txt_status = Entry(Frame1,font=("times new roman",15),textvariable=self.var_status,bg="LightCyan",fg="black").place(x=510,y=360,width = 200)
         

    #========= ROW8 ============

    #code for address
        lb1_address = Label(Frame1,text = "Address",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=430)
        self.txt_address = Text(Frame1,font=("times new roman",15),bg="LightCyan",fg="black")
        self.txt_address.place(x=140,y=440,width = 570,height = 200)
         



    #================= FRAME2 ===================

    #================= Variables for frame 2======================
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_conveyance=StringVar()
        self.var_net_salary=StringVar()
        



    #code for frame 2 working and payment details of employee
        Frame2 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=750,height=350)
        title3 = Label(Frame2,text = "Employee Salary Details",font=("LORA",20,"bold"),bg="cyan",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
    
    #========= ROW1 ============

    #code for month
        lb1_month = Label(Frame2,text = "Month",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=50)
        txt_month = Entry(Frame2,font=("times new roman",15),textvariable=self.var_month,bg="LightCyan",fg="black").place(x=100,y=60,width = 140)

    #code for year
        lb1_year = Label(Frame2,text = "Year",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=260,y=50)
        txt_year = Entry(Frame2,font=("times new roman",15),textvariable=self.var_year,bg="LightCyan",fg="black").place(x=330,y=60,width = 140)
    
    #code for salary
        lb1_salary = Label(Frame2,text = "Salary",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=500,y=50)
        txt_salary = Entry(Frame2,font=("times new roman",15),textvariable=self.var_salary,bg="LightCyan",fg="black").place(x=590,y=60,width = 140)


    #========= ROW2 ============

    #code for  Total Days    
        lb1_totaldays = Label(Frame2,text = "Total Days",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=110)
        txt_totaldays = Entry(Frame2,font=("times new roman",15),textvariable=self.var_t_days,bg="LightCyan",fg="black").place(x=170,y=120,width = 140)

    #code for  Absents
        lb1_Absents = Label(Frame2,text = "Absents",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=110)
        txt_Absents = Entry(Frame2,font=("times new roman",15),textvariable=self.var_absent,bg="LightCyan",fg="black").place(x=510,y=120,width = 140) 

    #========= ROW3 ============

    #code for medical   
        lb1_medical = Label(Frame2,text = "Medical",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=160)
        txt_medical = Entry(Frame2,font=("times new roman",15),textvariable=self.var_medical,bg="LightCyan",fg="black").place(x=170,y=170,width = 140)

    #code for pf
        lb1_pf = Label(Frame2,text = "PF",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=160)
        txt_pf = Entry(Frame2,font=("times new roman",15),textvariable=self.var_pf,bg="LightCyan",fg="black").place(x=510,y=170,width = 140)


    #========= ROW4 ============

    #code for coveyance    
        lb1_conveyance = Label(Frame2,text = "Conveyance",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=10,y=200)
        txt_conveyance = Entry(Frame2,font=("times new roman",15),textvariable=self.var_conveyance,bg="LightCyan",fg="black").place(x=170,y=210,width = 140)

    #code for Net Salary
        lb1_netsalary = Label(Frame2,text = "Net Salary",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=350,y=200)
        txt_netsalary = Entry(Frame2,font=("times new roman",15),textvariable=self.var_net_salary,bg="LightCyan",fg="black").place(x=510,y=210,width = 140)

    #========= ROW5 =============
        btn_calculate = Button(Frame2,text = "Calculate",command = self.calculate,font=("times new roman",20,"bold"),bg="LightSeaGreen",fg="black").place(x=10,y=280,height=40,width=120)
        self.btn_save = Button(Frame2,text = "Save",command = self.save,font=("times new roman",20,"bold"),bg="OrangeRed",fg="black")
        self.btn_save.place(x=140,y=280,height=40,width=140)
        btn_clear = Button(Frame2,text = "Clear",command=self.clear,font=("times new roman",20,"bold"),bg="SteelBlue",fg="black").place(x=290,y=280,height=40,width=140)
        self.btn_update = Button(Frame2,text = "Update",command=self.update,state=DISABLED,font=("times new roman",20,"bold"),bg="DarkMagenta",fg="black")
        self.btn_update.place(x=440,y=280,height=40,width=140)
        self.btn_delete = Button(Frame2,text = "Delete",command = self.delete,state=DISABLED,font=("times new roman",20,"bold"),bg="Crimson",fg="black")
        self.btn_delete.place(x=590,y=280,height=40,width=140)




    #================= FRAME3 ===================
    #code for frame 3 salary Receipt & Calculator 
        Frame3 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=430,width=750,height=340)

    #=========== Working Function for GUI Calculator =========== 

    #code for mouseclick entry in GUI Calculator 
        self.var_txt = StringVar()
        self.var_operator =''
        def btn_click(num):
            self.var_operator = self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
    #code for calculating the result  
        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator =''
    #code for clearing the display of calculator
        def clear_cal():
            self.var_txt.set('')
            self.var_operator =''
    #code for calculator button
        def phcet():
            messagebox.showinfo("Welcome","Welcome to PHCET Computer Department")
            if askyesno("Employee Searching","Do You Want To Open CLI Searching & Filterring Script ?"):
                self.root.destroy()
                import DSF
            elif askyesno("Employee Plotting","Do You Want To Open CLI Plotting Script ?"):
                self.root.destroy()
                import PLOT
            else:
                pass






    #==================== Calculator Frame ================

        Cal_Frame = Frame(Frame3,bg="white",bd=3,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width = 247,height=335)
        
        
        txt_Result = Entry(Cal_Frame,bg="LightSalmon",textvariable = self.var_txt,justify = RIGHT,font=("times new roman",20,"bold")).place(x=0,y=0,relwidth=1,height=45)

    #=================== ROW1 ===========================
        btn_phcet = Button(Cal_Frame,text='PHCET',command = phcet,bg="Aquamarine",font=("roboto",15,"bold")).place(x=0,y=46,w=121,h=43)
        btn_dot = Button(Cal_Frame,text='.',command = lambda:btn_click('.'),font=("roboto",15,"bold")).place(x=122,y=46,w=121,h=43)

    #=================== ROW2 ===========================
        btn_7 = Button(Cal_Frame,text='7',command = lambda:btn_click(7),font=("roboto",15,"bold")).place(x=0,y=88,w=60,h=60)
        btn_8 = Button(Cal_Frame,text='8',command = lambda:btn_click(8),font=("roboto",15,"bold")).place(x=61,y=88,w=60,h=60)
        btn_9 = Button(Cal_Frame,text='9',command = lambda:btn_click(9),font=("roboto",15,"bold")).place(x=122,y=88,w=60,h=60)
        btn_div = Button(Cal_Frame,text='/',command = lambda:btn_click('/'),font=("roboto",15,"bold")).place(x=183,y=88,w=60,h=60)

    #=================== ROW3 ===========================
        btn_4 = Button(Cal_Frame,text='4',command = lambda:btn_click(4),font=("roboto",15,"bold")).place(x=0,y=148,w=60,h=60)
        btn_5 = Button(Cal_Frame,text='5',command = lambda:btn_click(5),font=("roboto",15,"bold")).place(x=61,y=148,w=60,h=60)
        btn_6 = Button(Cal_Frame,text='6',command = lambda:btn_click(6),font=("roboto",15,"bold")).place(x=122,y=148,w=60,h=60)
        btn_mul = Button(Cal_Frame,text='*',command = lambda:btn_click('*'),font=("roboto",15,"bold")).place(x=183,y=148,w=60,h=60)

    #=================== ROW4 ===========================
        btn_1 = Button(Cal_Frame,text='1',command = lambda:btn_click(1),font=("roboto",15,"bold")).place(x=0,y=208,w=60,h=60)
        btn_2 = Button(Cal_Frame,text='2',command = lambda:btn_click(2),font=("roboto",15,"bold")).place(x=61,y=208,w=60,h=60)
        btn_3 = Button(Cal_Frame,text='3',command = lambda:btn_click(3),font=("roboto",15,"bold")).place(x=122,y=208,w=60,h=60)
        btn_min = Button(Cal_Frame,text='-',command = lambda:btn_click('-'),font=("roboto",15,"bold")).place(x=183,y=208,w=60,h=60)

    #=================== ROW5 ===========================
        btn_0 = Button(Cal_Frame,text='0',command = lambda:btn_click(0),font=("roboto",15,"bold")).place(x=0,y=268,w=60,h=60)
        btn_clear = Button(Cal_Frame,text='AC',command = clear_cal,font=("roboto",15,"bold")).place(x=61,y=268,w=60,h=60)
        btn_sum = Button(Cal_Frame,text='+',command = lambda:btn_click('+'),font=("roboto",15,"bold")).place(x=122,y=268,w=60,h=60)
        btn_equal = Button(Cal_Frame,text='=',command = result,font=("roboto",15,"bold")).place(x=183,y=268,w=60,h=60)
        
    #===================== Salary Frame =====================

        sal_Frame = Frame(Frame3,bg="white",bd=3,relief=RIDGE)
        sal_Frame.place(x=250,y=2,width = 493,height=334)
        title_sal = Label(sal_Frame,text = "Salary Receipt",font=("LORA",18,"bold"),bg="cyan",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
    
        sal_Frame2 = Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=250)

        self.sample = f'''\tCompany Name: PHCET\n\tAddress: Rasayni , Panvel
----------------------------------------------------------
Employee ID\t\t: 
Employee Name\t\t: 
Salary Of\t\t: Mon-YYYY
Employee Designation\t\t:
Generated On\t\t: DD-MM-YYYY
----------------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Conveyance\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.-------
Net Salary\t\t:  Rs.-------
----------------------------------------------------------
This is Computer generated slip. 
You Can save this slip 
in csv,pdf,txt,doc format 
'''

    #code for scrollbar
        scroll_y = Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
    
        self.txt_salary_recipt = Text(sal_Frame2,font=("Helvetica",15,"italic"),bg="lightcyan",yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,self.sample)   #code showing sample of receipt
    #code for print
        self.btn_print = Button(sal_Frame,text = "Print",state=DISABLED,command=self.print,font=("times new roman",20,"bold"),bg="LightCoral",fg="black")
        self.btn_print.place(x=180,y=282,height=45,width=150)


    #calling for check_connection function 
        self.check_connection()




    #=========== Working Function for Buttons Start Here =============

    def search(self):
        try:
                con = pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id = %s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Emp ID Error","Invalid Employee ID Please Try again with another employee ID",parent =self.root)
                else:
                    print(row)
                    self.var_emp_code.set(row[0])
                    self.var_designation.set(row[1])
                    self.var_name.set(row[2])
                    self.var_age.set(row[3])
                    self.var_gender.set(row[4])
                    self.var_email.set(row[5])
                    self.var_hr_location.set(row[6])
                    self.var_doj.set(row[7])
                    self.var_dob.set(row[8])
                    self.var_experience.set(row[9])
                    self.var_proof_id.set(row[10])    
                    self.var_contact.set(row[11])
                    self.var_status.set(row[12])
                    self.txt_address.delete('1.0',END)
                    self.txt_address.insert(END,row[13])
                    self.var_month.set(row[14])
                    self.var_year.set(row[15])
                    self.var_salary.set(row[16])
                    self.var_t_days.set(row[17])
                    self.var_absent.set(row[18])
                    self.var_medical.set(row[19])
                    self.var_pf.set(row[20])
                    self.var_conveyance.set(row[21])
                    self.var_net_salary.set(row[22])
                    file_=open('Salary_receipt/'+str(row[23]),'r')
                    self.txt_salary_recipt.delete('1.0',END)
                    for i in file_:
                        self.txt_salary_recipt.insert(END,i)
                    file_.close()
                    self.btn_save.config(state=DISABLED)
                    self.btn_update.config(state=NORMAL)
                    self.btn_delete.config(state=NORMAL)
                    self.btn_print.config(state=NORMAL)
                    self.txt_code.config(state="readonly")
        except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')

    #code for clear the entry fields
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')    
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0',END)


        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_conveyance.set('')
        self.var_net_salary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)


    #code for delete the record 
    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee Id must be required ")
        else:
            try:
                    con = pymysql.connect(host='localhost',user='root',password='',db='ems')
                    cur = con.cursor()
                    cur.execute("select * from emp_salary where e_id = %s",(self.var_emp_code.get()))
                    row=cur.fetchone()
                    if row == None:
                        messagebox.showerror("Emp ID Error","Invalid Employee ID Please Try again with another employee ID",parent =self.root)
                    else:
                        op = messagebox.askyesno("Confirm","Do you really want to delete")
                        #print(op)
                        if op==True:
                            cur.execute("delete from emp_salary where e_id = %s",(self.var_emp_code.get()))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Delete","Employee Record Deleted Successfuly",parent =self.root)
                            self.clear()
            except Exception as ex:
                    messagebox.showerror("Error",f'Error due to: {str(ex)}')
                    con.rollback()

    #for taking the data from our text field or entry box

    #for saving employee details 
    def save(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:       
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id = %s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Emp ID Error","This Employee Id has already available in our record try again with another ID",parent =self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                            self.var_emp_code.get(),
                            self.var_designation.get(),
                            self.var_name.get(),
                            self.var_age.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_hr_location.get(),
                            self.var_doj.get(),
                            self.var_dob.get(),
                            self.var_experience.get(),
                            self.var_proof_id.get(),    
                            self.var_contact.get(),
                            self.var_status.get(),
                            self.txt_address.get('1.0',END),
                            self.var_month.get(),
                            self.var_year.get(),
                            self.var_salary.get(),
                            self.var_t_days.get(),
                            self.var_absent.get(),
                            self.var_medical.get(),
                            self.var_pf.get(),
                            self.var_conveyance.get(),
                            self.var_net_salary.get(),
                            self.var_emp_code.get()+".txt"
                    )
                    )
                    con.commit()
                    con.close() 
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Added Successfully")
                    self.btn_delete.config(state=NORMAL)
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                con.rollback()

    #for updating employee details
    def update(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:       
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id = %s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","This Employee Id is Invalid try again with another ID",parent =self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`conveyance`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
                    (
                            self.var_designation.get(),
                            self.var_name.get(),
                            self.var_age.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_hr_location.get(),
                            self.var_doj.get(),
                            self.var_dob.get(),
                            self.var_experience.get(),
                            self.var_proof_id.get(),    
                            self.var_contact.get(),
                            self.var_status.get(),
                            self.txt_address.get('1.0',END),
                            self.var_month.get(),
                            self.var_year.get(),
                            self.var_salary.get(),
                            self.var_t_days.get(),
                            self.var_absent.get(),
                            self.var_medical.get(),
                            self.var_pf.get(),
                            self.var_conveyance.get(),
                            self.var_net_salary.get(),
                            self.var_emp_code.get()+".txt",
                            self.var_emp_code.get()
                    )
                    )
                    con.commit()
                    con.close() 
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Updated Successfully")
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                con.rollback()


    # for caluclating the net_salary @calculation function is below
    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or  self.var_t_days.get()=='' or self.var_absent.get()=='' or self.var_medical.get()== '' or self.var_pf.get()=='' or self.var_conveyance.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            per_day = int(self.var_salary.get())/int(self.var_t_days.get())
            work_day = int(self.var_t_days.get())-int(self.var_absent.get())
            sal_ = per_day * work_day  
            deduct = int(self.var_medical.get())+int(self.var_pf.get())
            addition = int(self.var_conveyance.get())
            net_sal = sal_-deduct+addition
            self.var_net_salary.set(str(round(net_sal,2)))

#======== For Updating the Receipt =========
            new_sample = f'''\tCompany Name: PHCET\n\tAddress: Rasayni , Panvel
--------------------------------------------------------------
Employee ID\t\t: {self.var_emp_code.get()}
Employee Name\t\t: {self.var_name.get()}
Employee Designation\t\t: {self.var_designation.get()}
Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t: {str(time.strftime("%d-%m-%y"))}
--------------------------------------------------------------
Total Days\t\t:  {self.var_t_days.get()}
Total Present\t\t:  {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
Conveyance\t\t:  Rs.{self.var_conveyance.get()}
Medical\t\t:  Rs.{self.var_medical.get()}
PF\t\t:  Rs.{self.var_pf.get()}
Gross Payment\t\t:  Rs.{self.var_salary.get()}
Net Salary\t\t:  Rs.{self.var_net_salary.get()}
--------------------------------------------------------------
This is Computer generated slip.
You Can save this slip 
in csv,pdf,txt,doc format 
'''
            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert(END,new_sample)
# to check Connection with database
    def check_connection(self):
        try:
            con = pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            rows = cur.fetchall()
            #print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')

 
    def show(self):
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary")
                rows = cur.fetchall()
                #print(rows)
                self.employee_tree.delete(*self.employee_tree.get_children())
                for row in rows:
                    self.employee_tree.insert('',END,values=row)
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')

# to showAll employee data in employee frame
    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Payroll Management System | Developed BY Sanmesh Yashwantrao")
        self.root2.geometry("1000x600+220+100") 
        self.root2.config(bg="white")                  
        title = Label(self.root2,text = "Company Employees Data ",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side = TOP,fill =X,)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)

        self.employee_tree = ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days', 'medical', 'pf', 'conveyance', 'net_salary', 'salary_receipt'),yscrollcommand = scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id', text='EID')
        self.employee_tree.heading('designation', text='Designation')
        self.employee_tree.heading('name', text='Name')
        self.employee_tree.heading('age', text='Age')
        self.employee_tree.heading('gender', text='Gender')
        self.employee_tree.heading('email', text='Email id')
        self.employee_tree.heading('hr_location', text='Hired Location')
        self.employee_tree.heading('doj', text='Date of Joining')
        self.employee_tree.heading('dob', text='Date of Birth')
        self.employee_tree.heading('experience', text='Experience')
        self.employee_tree.heading('proof_id', text='ID proof')
        self.employee_tree.heading('contact', text='Contact')
        self.employee_tree.heading('status', text='Status')
        self.employee_tree.heading('address', text='Address')
        self.employee_tree.heading('month', text='Month')
        self.employee_tree.heading('year', text='Year')
        self.employee_tree.heading('basic_salary', text='Basic Salary')
        self.employee_tree.heading('t_days', text='Total Days')
        self.employee_tree.heading('absent_days', text='Absent Days')
        self.employee_tree.heading('medical', text='Medical')
        self.employee_tree.heading('pf', text='PF')
        self.employee_tree.heading('conveyance', text='Conveyance')
        self.employee_tree.heading('net_salary', text='Net Salary')
        self.employee_tree.heading('salary_receipt', text='Salary Receipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('designation', width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age', width=100)
        self.employee_tree.column('gender', width=100)
        self.employee_tree.column('email', width=100)
        self.employee_tree.column('hr_location', width=100)
        self.employee_tree.column('doj', width=100)
        self.employee_tree.column('dob', width=100)
        self.employee_tree.column('experience', width=100)
        self.employee_tree.column('proof_id', width=100)
        self.employee_tree.column('contact', width=100)
        self.employee_tree.column('status', width=100)
        self.employee_tree.column('address', width=500)
        self.employee_tree.column('month', width=100)
        self.employee_tree.column('year', width=100)
        self.employee_tree.column('basic_salary', width=100)
        self.employee_tree.column('t_days', width=100)
        self.employee_tree.column('absent_days', width=100)
        self.employee_tree.column('medical', width=100)
        self.employee_tree.column('pf', width=100)
        self.employee_tree.column('conveyance', width=100)
        self.employee_tree.column('net_salary', width=100)
        self.employee_tree.column('salary_receipt', width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()

        self.root2.mainloop()
  #to print the recipt
    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_recipt.get('1.0',END))
        os.startfile(file_,'print')
 #to save all employeee data in csv fromat 
    def print_emp_data(self):
        conn = pymysql.connect(host='localhost', user='root', password='', database='ems')
        cur = conn.cursor()
        query = 'select * from emp_salary'
        cur.execute(query)
        result = pandas.read_sql_query(query, conn)
        result.to_csv("Employee Data"+".csv", index=False)
#code for permission window while quit
def wd():
    if askokcancel("QUIT","Are You Sure want to quit"):
        root.destroy()
        


root =Tk()
obj = EmployeeSystem(root)  
root.protocol("WM_DELETE_WINDOW",wd)      
root.mainloop()
