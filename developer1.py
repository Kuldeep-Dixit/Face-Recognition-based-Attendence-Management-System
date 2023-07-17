from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import tkinter
from datetime import datetime
from time import strftime


class First_Developer:
        def __init__(self, root):
                self.root = root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition System")
                
                

        # ======================= Title =================


                title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="red")
                title_lbl.place(x=0, y=0, width=1400, height=45)

                def time():
                        string = strftime('%H:%M:%S %p')
                        lbl.config(text = string)
                        lbl.after(1000, time)

                img4 = Image.open(r"Images\back.jpg")
                img4 = img4.resize((34,27),Image.Resampling.LANCZOS)
                self.photoimg4 = ImageTk.PhotoImage(img4)

                b1=Button(title_lbl,command=self.iExit,image=self.photoimg4, cursor="hand2")
                b1.place(x=5,y=2,width=40,height=40)

                lbl = Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
                lbl.place(x=50,y=10,width=110,height=20)
                time()

        

        # ============================ top Image ================

                img_top = Image.open(r"Images\dev.jpg")
                img_top = img_top.resize((1370, 650), Image.Resampling.LANCZOS)
                self.photoimg_top = ImageTk.PhotoImage(img_top)

                f_lbl = Label(self.root, image=self.photoimg_top)
                f_lbl.place(x=0, y=46, width=1370, height=650)


# ============================== Frame ================================

                main_frame = Frame(f_lbl,bd = 2, bg="white")
                main_frame.place(x=800, y=4, width=550, height=470)

                img_dev_1 = Image.open(r"Images\Document Photo.jpeg")
                img_dev_1 = img_dev_1.resize((160, 160), Image.Resampling.LANCZOS)
                self.photoimg_dev_1 = ImageTk.PhotoImage(img_dev_1)

                f_lbl = Label(main_frame, image=self.photoimg_dev_1)
                f_lbl.place(x=385, y=0, width=160, height=160)

# ======================= Developer Info================================
                dep_label = Label(main_frame, text="Hello! My Name is Kuldeep Dixit", font=("times now roman", 18, "bold"), bg="white")
                dep_label.place(x=0,y=5)




        def iExit(self):
                self.root.destroy()




if __name__ == "__main__":
    root = Tk()
    obj = First_Developer(root)
    root.mainloop()