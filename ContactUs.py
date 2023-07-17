from tkinter import*
from PIL import Image,ImageTk
import webbrowser
from datetime import datetime
from time import strftime


class Helpsupport:
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
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
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
        # website button 1
        std_img_btn=Image.open(r"Images\web.png")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=380,width=180,height=45)

        # facebook  button 2
        det_img_btn=Image.open(r"Images\fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # instagram button 3
        att_img_btn=Image.open(r"Images\instagram-1581266__340.webp")
        att_img_btn=att_img_btn.resize((230,230),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.instagram,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.instagram,text="Instagram",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=710,y=380,width=180,height=45)

         # twitter button 4
        hlp_img_btn=Image.open(r"Images\images.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.twitter,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.twitter,text="Twitter",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=940,y=380,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://kuldeeppanditg1234.wixsite.com/mysite"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com"
        webbrowser.open(self.url,new=self.new)
    
    def instagram(self):
        self.new = 1
        self.url = "https://www.instagram.com/dixit_kuldeep/"
        webbrowser.open(self.url,new=self.new)
    
    def twitter(self):
        self.new = 1
        self.url = "https://twitter.com/Kuldeep02952876"
        webbrowser.open(self.url,new=self.new)

    def iExit(self):
        self.root.destroy()






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()