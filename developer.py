from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
# from attendance import Attendance
import os
import tkinter
from datetime import datetime
from time import strftime
from developer1 import First_Developer

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images\banner.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images\bg4.png")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text = string)
                lbl.after(1000, time)
                
        img4 = Image.open(r"Images\back.jpg")
        img4 = img4.resize((34,27),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.iExit,image=self.photoimg4, cursor="hand2")
        b1.place(x=10,y=2,width=40,height=40)

        lbl = Label(title_lb1, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=50,y=10,width=110,height=20)
        time()

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        # std_img_btn=Image.open(r"Images\Document Photo.jpeg")
        # std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        # self.std_img1=ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button(bg_img,command=self.developer1,image=self.std_img1,cursor="hand2")
        # std_b1.place(x=250,y=200,width=180,height=180)

        # std_b1_1 = Button(bg_img,text="Kuldeep Dixit",command=self.developer1,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        # std_b1_1.place(x=250,y=380,width=180,height=45)

        # =============================== Second Developer =========================
        det_img_btn=Image.open(r"Images\Document Photo.jpeg")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.developer1,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Kuldeep Dixit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # ============================== Third Developer ==========================
        # att_img_btn=Image.open(r"Images\det1.jpg")
        # att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        # self.att_img1=ImageTk.PhotoImage(att_img_btn)

        # att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        # att_b1.place(x=710,y=200,width=180,height=180)

        # att_b1_1 = Button(bg_img,text="Dev Sharma",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        # att_b1_1.place(x=710,y=380,width=180,height=45)

         # =========================== Fourth Developer=================================
        # hlp_img_btn=Image.open(r"Images\det1.jpg")
        # hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        # self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        # hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        # hlp_b1.place(x=940,y=200,width=180,height=180)

        # hlp_b1_1 = Button(bg_img,text="Vimal Pal",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        # hlp_b1_1.place(x=940,y=380,width=180,height=45)


    def iExit(self):
        self.root.destroy()

    def developer1(self):
        self.new_window = Toplevel(self.root)
        self.app = First_Developer(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()