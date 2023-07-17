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


class Train:
        def __init__(self, root):
                self.root = root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition System")
                
                

        # ======================= Title =================


                title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
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

                img_top = Image.open(r"Images\facialrecognition.png")
                img_top = img_top.resize((1370, 250), Image.Resampling.LANCZOS)
                self.photoimg_top = ImageTk.PhotoImage(img_top)

                f_lbl = Label(self.root, image=self.photoimg_top)
                f_lbl.place(x=0, y=46, width=1370, height=250)

                

        # ========================== BUtton ========================
                b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
                b1_1.place(x=0,y=296,width=1370,height=70)


# =========================== Bottom Image=====================
                img_bottom = Image.open(r"Images\facial-recognition_0.jpg")
                img_bottom = img_bottom.resize((1370, 250), Image.Resampling.LANCZOS)
                self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

                f_lbl = Label(self.root, image=self.photoimg_bottom)
                f_lbl.place(x=0, y=450, width=1370, height=250)

        def train_classifier(self):
                data_dir = ("data")
                path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

                faces = []
                ids = []

                for image in path:
                        img = Image.open(image).convert('L') #Gray Scale Image
                        imageNp=np.array(img,'uint8')
                        id =int(os.path.split(image)[1].split('.')[1])

                        faces.append(imageNp)
                        ids.append(id)
                        cv2.imshow("Training",imageNp)
                        cv2.waitKey(1)==13
                ids = np.array(ids)

                # =============== Train the classifier and save ===================
                clf = cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces,ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data Set is Successfully Trained",parent=self.root)

        def iExit(self):
                self.root.destroy()




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
