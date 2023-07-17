from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from chatbot import ChatBot
import os
import mysql.connector
import tkinter
from datetime import datetime
from time  import strftime
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from attendence import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        # First Image
        img = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\un.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\facialrecognition.png")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\university.jpg")
        img2 = img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0, width=500, height=130)

        # # Background Image
        img3 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\download.jpg")
        img3 = img3.resize((1500,700),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130, width=1500, height=710)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)

# =======================time==================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=110,height=40)
        time()

        #Student Portal
        img4 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\student-portal_1.jpg")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4, cursor="hand2")
        b1.place(x=150,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=150,y=239,width=200,height=41)

        # Detect Face
        img5 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\face_detector1.jpg")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,command=self.Face_Recognition,image=self.photoimg5,cursor="hand2")
        b1.place(x=450,y=80,width=200,height=170)

        b1=Button(bg_img,text="Face Detector",command=self.Face_Recognition,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=450,y=240,width=200,height=40)

        # Attendence Face Button
        img6 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\report.jpg")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,command=self.Attendance,image=self.photoimg6,cursor="hand2")
        b1.place(x=750,y=80,width=200,height=200)

        b1=Button(bg_img,text="Attendence",command=self.Attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=750,y=240,width=200,height=40)

        # Help Button
        img7 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,command=self.help_data,image=self.photoimg7,cursor="hand2")
        b1.place(x=1050,y=80,width=200,height=200)

        b1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=1050,y=240,width=200,height=40)

         # Train Face Button
        img8 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\facial_recognition_action.jpg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b1.place(x=150,y=325,width=200,height=170)

        b1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=150,y=485,width=200,height=40)

        # Photo face Button
        img9 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=325,width=200,height=200)

        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=450,y=485,width=200,height=40)

        # Developer Option
        img10 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,command=self.Developer,image=self.photoimg10,cursor="hand2")
        b1.place(x=750,y=325,width=200,height=200)

        b1=Button(bg_img,text="Developer",command=self.Developer,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=750,y=485,width=200,height=40)

        # Exit Button
        img11 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\exit.jpg")
        img11 = img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,command=self.iExit,image=self.photoimg11,cursor="hand2")
        b1.place(x=1050,y=325,width=200,height=200)

        b1=Button(bg_img,command=self.iExit,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=1050,y=485,width=200,height=40)


# ================Function Buttons====================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def open_img(self):
        os.startfile("data") 

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def Face_Recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit the Project.",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
