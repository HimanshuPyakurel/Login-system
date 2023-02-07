from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

#create the class
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title(" Login and Registration for Apps")
        self.root.geometry("1366*700+0+0")
        self.root.resizable(False,False)
        self.loginform()

    def loginform(self):
        Frame_login = Frame(self.root,bg = "white")
        Frame_login.place(x=0,y=0,height=700,width=1366)

        self.img = ImageTk.PhotoImage(file = "background1.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,height=700,width=1366)

        frame_input=Frame(self.root,bg='white')
        frame_input.place(x=320,y=130,height=450,width=350)

        label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'), fg ='black', bg='white')
        label1.place(x=75,y=20)

        label2=Label(frame_input,text="Username",font=('Goudy old style',20,'bold'), fg ='orangered', bg='white')
        label2.place(x=30,y=95)

        self.email_txt = Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.email_txt.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input,text="Password",font=('Goudy old style',20,'bold'), fg ='orangered', bg='white')
        label3.place(x=30,y=195)
        
        self.password = Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.password.place(x=30,y=245,width=270,height=35)

        btnl1 = Button(frame_input,text="forget password?",cursor='hand2',font=('calibri',10), fg ='black', bg='white',bg=0)
        btnl1.place(x=90,y=305)

        btnl2 = Button(frame_input,text="Login",command =self.login, cursor='hand2',font=('times new roman',15), fg ='white', bg='orangered',bg=0,width=15,height=1)
        btnl2.place(x=90,y=340) 
        
        btnl3 = Button(frame_input,text="Not Registered?register",command=self.register,cursor='hand2',font=('calibri',10), fg ='black', bg='white',bg=0)
        btnl3.place(x=110,y=390)

root =Tk()
ob=Login(root)
root.mainloop()
