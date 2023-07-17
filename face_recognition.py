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


class Face_Recognition:
        def __init__(self, root):
                self.root = root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition System")

                title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
                title_lbl.place(x=0, y=0, width=1400, height=45)

                def time():
                        string = strftime('%H:%M:%S %p')
                        lbl.config(text = string)
                        lbl.after(1000, time)
                        
                img4 = Image.open(r"Images\back.jpg")
                img4 = img4.resize((34,27),Image.Resampling.LANCZOS)
                self.photoimg4 = ImageTk.PhotoImage(img4)

                b1=Button(title_lbl,command=self.iExit,image=self.photoimg4, cursor="hand2")
                b1.place(x=10,y=2,width=40,height=40)

                lbl = Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
                lbl.place(x=50,y=10,width=110,height=20)
                time()

                
# ======================== first image ==============
                img_top = Image.open(r"Images\face_detector1.jpg")
                img_top = img_top.resize((700, 600), Image.Resampling.LANCZOS)
                self.photoimg_top = ImageTk.PhotoImage(img_top)

                f_lbl = Label(self.root, image=self.photoimg_top)
                f_lbl.place(x=0, y=50, width=700, height=650)
                
# ========================= second image==============
                img_bottom = Image.open(r"Images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
                img_bottom = img_bottom.resize((700, 600), Image.Resampling.LANCZOS)
                self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

                f_lbl = Label(self.root, image=self.photoimg_bottom)
                f_lbl.place(x=650, y=50, width=700, height=650)

# ======================== button =========================
                b1_1=Button(f_lbl,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
                b1_1.place(x=242,y=550,width=210,height=40)
                

# =============================== attendence =========================
        
        def mark_attendence(self,enroll,d,ye,n):
                
                with open("attendence.csv","r+",newline="\n") as f:
                        myDataList=f.readlines()
                        name_list=[]
                        now =datetime.now()
                        d1=datetime.now().strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S %p")
                        for line in myDataList:
                                entry=line.split((","))
                                name_list.append(entry[0])

                                               
                        if((enroll not in name_list) and (d not in name_list) and (n not in name_list)and (d1 not in name_list)):
                                
                                f.writelines(f"\n{enroll}, {d} , {ye} , {n} ,{dtString} ,{d1} ,Present")


# ================== Face_Recognition==================
        def face_recog(self):
                def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                        
                        gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                        coord=[]

                        for (x,y,w,h) in features:
                                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                                confidence=int((100*(1-predict/300)))

                                conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
                                my_cursor = conn.cursor()

                                my_cursor.execute("select Name from student where Enrollment_No="+str(id))
                                n=my_cursor.fetchone()
                                n="+".join(n)

                                my_cursor.execute("select Department from student where Enrollment_No="+str(id))
                                d=my_cursor.fetchone()
                                d="+".join(d)
                                
                                my_cursor.execute("select Year from student where Enrollment_No="+str(id))
                                ye=my_cursor.fetchone()
                                ye="+".join(ye)
                                
                                my_cursor.execute("select Enrollment_No from student where Enrollment_No="+str(id))
                                enroll=my_cursor.fetchone()
                                enroll="+".join(enroll) 

                                if confidence>82:
                                        cv2.putText(img,f"Department:{d} {ye}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                                        cv2.putText(img,f"Enrollment No.:{enroll}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                                        self.mark_attendence(enroll,d,ye,n)
                                        # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                                        # cv2.putText(img,"Detected",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                                else:
                                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
 
                                coord=[x,y,w,y]
                        return coord
                
                def recognize(img,clf,faceCascade):
                        coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                        return img

                faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.read("classifier.xml")

                video_cap=cv2.VideoCapture(0)

                while True:
                        ret,img=video_cap.read()
                        img=recognize(img,clf,faceCascade)
                        cv2.imshow("Welcome to Face Recognition",img)

                        if cv2.waitKey(1)==13:
                                break
                video_cap.release()
                cv2.destroyAllWindows()



        def iExit(self):
                self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()