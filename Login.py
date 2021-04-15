from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter import ttk
import pymysql
import getpass
import re
class Login:
        def __init__(self,root):
            self.root = root
            self.root.title("Login System")
            self.root.geometry("500x600+500+130")
            self.root.resizable(False,False)
            
            #==========BG Image=============
            self.bg = ImageTk.PhotoImage(file="bg.jpg")
            self.bg_image = Label(self.root,image = self.bg).place(x=0,y=0,relwidth=1,relheight=1)

            #===== Login Frame ============
            Frame_login=Frame(self.root,bg="white")
            Frame_login.place(x=50,y=60,height=430,width=400)

            #login label
            title = Label(Frame_login,text="Login Here",font=("ADAM.CG PRO",28,"bold"),fg="DarkCyan",bg="white").place(x=100,y=10)
            desc = Label(Frame_login,text="Employee Administrator \nLogin Panel",font=("Goudy old style",20,"bold"),fg="DarkCyan",bg="white").place(x=60,y=70)
            
            #username label
            lbl_user = Label(Frame_login,text="Username",font=("Goudy old style",20,"bold"),fg="OrangeRed",bg="white").place(x=5,y=160)
            self.txt_user = Entry(Frame_login,font=("times new roman",15),bg="LightPink")
            self.txt_user.place(x=140,y=163,width=240,height=35)
            #passsword label
            lbl_pass = Label(Frame_login,text="Password",font=("Goudy old style",20,"bold"),fg="OrangeRed",bg="white").place(x=5,y=240)
            self.txt_pass = Entry(Frame_login,font=("times new roman",15),bg="LightPink")
            self.txt_pass.place(x=140,y=243,width=240,height=35)
            #forget button
            btn_forget = Button(Frame_login,text="Forget Password?",command = self.forget_password_window,cursor="hand2",bg="white",fg="OrangeRed",bd=0,font=("times new roman" ,20,'underline')).place(x=100,y=320)
            #ogin button
            btn_Login = Button(self.root,text="LOGIN",command= self.login_function,cursor="hand2",bg="DarkCyan",fg="white",font=("times new roman" ,17,)).place(x=170,y=465,width=160)
        
        #reset clear function
        def reset(self):
            self.cmb_quest.current(0)
            self.txt_new_pass.delete(0,END)
            self.txt_answer.delete(0,END)
            self.txt_pass.delete(0,END)
            self.txt_user.delete(0,END)

        # forget password function
        def forget_password(self):
            if(self.cmb_quest.get()=="Select" or self.txt_answer.get()==""or self.txt_answer.get()=="" or self.txt_new_pass.get()==""):
                messagebox.showerror("Error","All fields are required",parent =self.root2)
            else:
                try:
                    con = pymysql.connect(host = 'localhost',user = 'root' ,password = '',database='login')
                    cur = con.cursor()
                    cur.execute("select * from login_details where username = %s and question = %s and answer = %s", (self.txt_user.get(),self.cmb_quest.get(),self.txt_answer.get()))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root2)
                    else:    
                        cur.execute("update login_details set password = %s where username = %s",(self.txt_new_pass.get(),self.txt_user.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Your Password has been reset,Please login with new password",parent = self.root2)
                        self.reset()
                        self.root2.destroy()
                except Exception as es:
                   messagebox.showerror("Error",f"Error Due to: {str(es)}",parent = self.root) 

        #forget password window function
        def forget_password_window(self):
            if self.txt_user.get()=="":
                messagebox.showerror("Error","Please enter the username to reset your password")
            else:
                try:
                    con = pymysql.connect(host = 'localhost',user = 'root' ,password = '',database='login')
                    cur = con.cursor()
                    cur.execute("select * from login_details where username = %s" ,self.txt_user.get())
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Please enter the valid username to reset your password")
                    else:
                        con.close()
                        self.root2=Toplevel()
                        self.root2.title("Forget Password")
                        self.root2.geometry("400x400+550+220")
                        self.root2.resizable(False,False)
                        self.root2.configure(bg="white")
                        self.root2.focus_force()
                        self.root2.grab_set()
                    #=======================FORGET WINDOW ================== 

                        t = Label(self.root2,text="Forget Password",font=("times new roman",25,"bold"),bg="white",fg="DarkCyan").place(x=0,y=15,relwidth=1)
                        #forget password question
                        question = Label(self.root2,text="Security Questions",font=("times new roman",15,"bold"),bg ="white",fg="OrangeRed").place(x=70,y=100)

                        self.cmb_quest = ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state='readonly',justify=CENTER)
                        self.cmb_quest['values']=("select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                        self.cmb_quest.place(x=70,y=130,width=250)
                        self.cmb_quest.current(0)

                        answer = Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg = "white",fg="OrangeRed").place(x=70,y=180)
                        self.txt_answer =Entry(self.root2,font=("times new roman",15),bg="LightPink")
                        self.txt_answer.place(x=70,y=210,width=250)

                        new_password = Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg = "white",fg="OrangeRed").place(x=70,y=260)
                        self.txt_new_pass = (Entry(self.root2,font=("times new roman",15),bg="LightPink"))
                        self.txt_new_pass.place(x=70,y=290,width=250)

                        btn_change_password = Button(self.root2,text="Reset Password",command=self.forget_password,cursor="hand2",bg="DarkCyan",fg="white",font=("times new roman",15,"bold")).place(x=120,y=335,width=160)
       
                except Exception as es:
                   messagebox.showerror("Error",f"Error Due to: {str(es)}",parent = self.root) 


        #stopwatch function and window
        def stopwatch(self):
            self.root3=Toplevel()
            self.root3.title("Forget Password")
            self.root3.geometry("400x400+550+220")
            self.root3.resizable(False,False)
            self.root3.configure(bg="white")
            self.root3.focus_force()
            self.root3.grab_set()

        #login function
        def login_function(self):
            if self.txt_user.get()=="" or self.txt_pass.get()=="":
                messagebox.showerror("Error","All Fields are required",parent = self.root)
            else:
                try:
                    con = pymysql.connect(host = 'localhost',user = 'root' ,password = '',database='login')
                    cur = con.cursor()
                    cur.execute("select * from login_details where username = %s and password = %s",(self.txt_user.get(),self.txt_pass.get()))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                    else:
                        messagebox.showinfo("Welcome",f"Welcome to Employee Payroll Management System\nYour Usrename is: {self.txt_user.get()} \nYour Password is : {self.txt_pass.get()}",parent=self.root)  
                        self.root.destroy()
                        import tp3
                    con.close()  
   
                except Exception as es:
                   messagebox.showerror("Error",f"Error Due to: {str(es)}",parent = self.root) 
            
        #code for permission window while quit
def wd():
    if askokcancel("QUIT","Are You Sure"):
        root.destroy()

            

root = Tk()
obj = Login(root)
root.protocol("WM_DELETE_WINDOW",wd)
root.mainloop()
