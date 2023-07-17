from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from datetime import datetime
from time import strftime
import tkinter


class Student:
     def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        # ========= Variables ============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_enroll = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_serial = StringVar()
        self.var_search = StringVar()
        self.var_searchTX = StringVar()

     # First Image
        img = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\face-recognition.png")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\smart-attendance.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\abcd.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # # Background Image
        img3 = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\wp2551980.jpg")
        img3 = img3.resize((1500, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1500, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1335, height=500)

        def time():
           

            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        img4 = Image.open(r"Images\back.jpg")
        img4 = img4.resize((34,27),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.iExit,image=self.photoimg4, cursor="hand2")
        b1.place(x=10,y=2,width=40,height=40)

        lbl = Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=50,y=0,width=110,height=40)
        time()

        

#----------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#

        # left side label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=625, height=470)

        img_left = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((614, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=4, y=0, width=614, height=130)

        # current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,text="Current Course Imformation", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=10, y=130, width=600, height=100)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times now roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=0, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times now roman", 12), state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "CIVIL", "AGRICULTURE", "PRODUCTION", "AUTOMOBILE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=0, pady=5, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times now roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times now roman", 12), state="readonly")
        course_combo["values"] = ("Select Course", "DIPLOMA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=0, pady=0, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times now roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=0, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times now roman", 12), state="readonly")
        year_combo["values"] = ("Current Year", "FIRST YEAR", "SECOND YEAR", "FINAL YEAR")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=0, pady=0, sticky=W)

        # Semester
        
        semester_label = Label(current_course_frame, text="Semester", font=("times now roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=5, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times now roman", 12), state="readonly")
        semester_combo["values"] = ("Current Semester", "FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=0, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=10, y=225, width=600, height=218)
        
        
        # Student ID
        studentId_label = Label(class_student_frame, text="Enrollment ID : ", font=("times now roman", 10, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=3,pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_enroll,width=20,font=("times now roman", 10, "bold"))
        studentId_entry.grid(row=0,column=1, padx=3, sticky=W)
        
        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name : ", font=("times now roman", 10, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_name,font=("times now roman", 10, "bold"))
        studentName_entry.grid(row=0,column=3, padx=5, sticky=W)


        # Roll No.
        roll_no_label = Label(class_student_frame, text="Roll No.", font=("times now roman", 10, "bold"), bg="white")
        roll_no_label.grid(row=1, column=0, padx=3, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times now roman", 10, "bold"))
        roll_no_entry.grid(row=1,column=1, padx=3, sticky=W)


        # Gender
        gender_label = Label(class_student_frame, text="Gender : ", font=("times now roman", 10, "bold"), bg="white")
        gender_label.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times now roman", 10,"bold"), state="readonly")
        gender_combo["values"] = ("Select Your Gender", "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=5, pady=0, sticky=W)

        # Date of Birth
        dob_label = Label(class_student_frame, text="Date of Birth : ", font=("times now roman", 10, "bold"), bg="white")
        dob_label.grid(row=2, column=0, padx=3,pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times now roman", 10, "bold"))
        dob_entry.grid(row=2,column=1, padx=3, sticky=W)

        # Phone Number
        phone_no_label = Label(class_student_frame, text="Phone No. : ", font=("times now roman", 10, "bold"), bg="white")
        phone_no_label.grid(row=2, column=2, padx=10,pady=5, sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times now roman", 10, "bold"))
        phone_no_entry.grid(row=2,column=3, padx=5, sticky=W)
        
        
        # Radio Button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample", value="YES")
        radiobtn1.grid(row=3,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Do not take Photo Sample", value="No")
        radiobtn2.grid(row=3,column=1)

        # buttons Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=130,width=588,height=30)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,height=-10,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)
        
        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,height=-10,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)
        
        #delete button
        delete_btn=Button(btn_frame,text="Delete",width=17,command=self.delete_data,height=-10,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)
        
        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,height=-10,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

        # Photo Buttons
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=6,y=160,width=584,height=30)

        #Take photo sample button
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,height=-10,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        take_photo_btn.grid(row=0,column=0)

        #update photo samples button
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",command=self.update_dataset,width=35,height=-10,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        update_photo_btn.grid(row=0,column=1)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#     
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        # right side label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=645, y=10, width=670, height=470)

        img_right = Image.open(r"F:\\CSE (Study Material,Documents)\\Python\\Attendence Management\\Images\\student.jpg")
        img_right = img_right.resize((700, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=4, y=0, width=658, height=130)

        # =========Search System==========
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=130, width=656, height=65)

        search_label = Label(search_frame, text="Search By:", font=("times now roman", 11, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame,textvariable=self.var_searchTX, font=("times now roman", 10,"bold"), state="readonly",width=15)
        search_combo["values"] = ("Select", "Name", "Enrollment ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=0, pady=0, sticky=W)

        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("times now roman", 10, "bold"))
        search_entry.grid(row=0,column=2, padx=10, sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=12,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        search_btn.grid(row=0,column=3, padx=4)

        showall_photo_btn=Button(search_frame,command=self.show_all,text="Show All",width=12,font=("time now roman",10,"bold"),bg="blue",fg="white",cursor="hand2")
        showall_photo_btn.grid(row=0,column=4, padx=4)

        #=======================table frame =====================
        table_frame =Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=200, width=656, height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Enrollment_No","Roll_No","Name","Gender","DOB","Phone_No","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Enrollment_No",text="Enrollment_No")
        self.student_table.heading("Roll_No",text="Roll_No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Phone_No",text="Phone_No")
        self.student_table.heading("PhotoSample",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=70)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Enrollment_No",width=100)
        self.student_table.column("Roll_No",width=70)
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=70)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Phone_No",width=100)
        self.student_table.column("PhotoSample",width=125)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

     #=====================function decration ============================
     def add_data(self):
        
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_enroll.get()==0:
                messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
                try:
                        conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
                        my_cursor = conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_enroll.get(),
                                self.var_roll.get(),
                                self.var_name.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_phone.get(),
                                self.var_radio1.get(),      
                        ))
                        
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Students Details has been added Successfully.",parent=self.root)
        
                except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        # =============== fetching data from Database =======================
     def fetch_data(self):
                conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                data = my_cursor.fetchall()

                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)
                        conn.commit()
                conn.close()


        #================ get Cursor =======================
     def get_cursor(self,event =""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_enroll.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_name.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_radio1.set(data[10])

#=================update button==================================
     def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_enroll.get()==0 or self.var_course.get()=="Current Course":
                messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
                try:
                        update = messagebox.askyesno("Update","Do you want to update this student Details.",parent=self.root)
                        if update>0:
                                conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
                                my_cursor = conn.cursor()
                                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Roll_No=%s,Name=%s,Gender=%s,DOB=%s,Phone=%s,PhotoSample=%s where Enrollment_No=%s",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_roll.get(),
                                        self.var_name.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_phone.get(),
                                        self.var_radio1.get(),
                                        self.var_enroll.get()
                                        ))
                        else:
                                if not update:
                                        return
                        messagebox.showinfo("Success","Student Details has been updated Successfully.",parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

# =================== Delete Function====================
     def delete_data(self):
        if self.var_enroll.get()=="":
                messagebox.showerror("Error","Student ID must be requied",parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("Delete Data","Do you want to delete this Student Data",parent=self.root)
                        if delete>0:
                                conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
                                my_cursor = conn.cursor()
                                sql="delete from student where Enrollment_No=%s"
                                val=(self.var_enroll.get(),)
                                my_cursor.execute(sql,val)
                        else:
                                if not delete:
                                        messagebox.showinfo("Error","Can not delete Student Data.",parent=self.root)                                        
                                        return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete","Student Details has been deleted Successfully",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
# ===================== Reset Function=================
     def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Current Year")
        self.var_semester.set("Current Semester")
        self.var_enroll.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_gender.set("Select your Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_radio1.set("")


# ========================== search bar ==========================================
        # ===================== Search Tab============
     def search_data(self):
             if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
                 messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)

             elif self.var_searchTX.get()=="Name":
                 try:
                     conn = mysql.connector.connect(username='root', password='Kuldeep@16',host='localhost',database='face_recognizer')
                     my_cursor = conn.cursor()
                     sql = "SELECT Department,Course,Year,Semester,Enrollment_No,Roll_No,Name,Gender,DOB,Phone,PhotoSample FROM student where Name='" +str(self.var_search.get()) + "'" 
                     my_cursor.execute(sql)
                     # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                     rows=my_cursor.fetchall()        
                     if len(rows)!=0:
                         self.student_table.delete(*self.student_table.get_children())
                         for i in rows:
                             self.student_table.insert("",END,values=i)
                         if rows==None:
                             messagebox.showerror("Error","Data Not Found",parent=self.root)
                             conn.commit()
                     conn.close()
                 except Exception as es:
                     messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

             elif self.var_searchTX.get()=="Enrollment ID":
                 try:
                     conn = mysql.connector.connect(username='root', password='Kuldeep@16',host='localhost',database='face_recognizer')
                     my_cursor = conn.cursor()
                     sql = "SELECT Department,Course,Year,Semester,Enrollment_No,Roll_No,Name,Gender,DOB,PhotoSample FROM student where Enrollment_No='" +str(self.var_search.get()) + "'" 
                     my_cursor.execute(sql)
                     # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                     rows=my_cursor.fetchall()        
                     if len(rows)!=0:
                         self.student_table.delete(*self.student_table.get_children())
                         for i in rows:
                             self.student_table.insert("",END,values=i)
                         if rows==None:
                             messagebox.showerror("Error","Data Not Found",parent=self.root)
                             conn.commit()
                     conn.close()
                 except Exception as es:
                     messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



        # =================== Show All Tab ==============
     def show_all(self):
        self.var_search.set("")
        self.var_searchTX.set("Select")

        conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()
        if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()

# ============= Generate Data set and take photo samples===================
     def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_enroll.get()==0 or self.var_course.get()=="Current Course":
                messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
                try:
                        conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
                        my_cursor = conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                                id+=1
                        my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Roll_No=%s,Name=%s,Gender=%s,DOB=%s,Phone=%s,PhotoSample=%s where Enrollment_No=%s",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_roll.get(),
                                        self.var_name.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_phone.get(),
                                        self.var_radio1.get(),
                                        self.var_enroll.get()==id+1
                                        ))

                        conn.commit()
                        # self.add_data()
                        self.fetch_data()
                        self.reset_data()

                        # ================== Load Predifined data on face frontals from opencv=================/

                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces=face_classifier.detectMultiScale(gray,1.3,5)
                                #scaling factor=1.3
                                #Minimum Neighbor=5

                                for(x,y,w,h) in faces:
                                        face_cropped=img[y:y+h,x:x+w]
                                        return face_cropped

                        cap = cv2.VideoCapture(0)
                        img_id=0
                        while True:
                                ret,my_frame = cap.read()
                                if face_cropped(my_frame) is not None:
                                        img_id+=1
                                        face = cv2.resize(face_cropped(my_frame),(200,200))
                                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                        cv2.imwrite(file_name_path,face)
                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                        cv2.imshow("Cropped Face",face)
                                
                                if cv2.waitKey(1)==13 or int(img_id)==100:
                                        break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Taking of Dataset Completed Successfully!",parent=self.root)

                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    
     def update_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_enroll.get()==0 or self.var_course.get()=="Current Course":
                messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
                try:
                        conn = mysql.connector.connect(host="localhost",username="root",password="Kuldeep@16",database="face_recognizer")
                        my_cursor = conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                                id+=1
                        my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Enrollment_No=%s,Roll_No=%s,Name=%s,Gender=%s,DOB=%s,Phone=%s,PhotoSample=%s where Enrollment_No=%s",(
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_enroll.get(),
                                                        self.var_semester.get(),
                                                        self.var_roll.get(),
                                                        self.var_name.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_phone.get(),
                                                        self.var_radio1.get(),
                                                        self.var_enroll.get()==id+1
                                                        ))

                        conn.commit()
                        self.fetch_data()
                        self.reset_data()

                        # ================== Load Predifined data on face frontals from opencv=================/

                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces=face_classifier.detectMultiScale(gray,1.3,5)
                                #scaling factor=1.3
                                #Minimum Neighbor=5

                                for(x,y,w,h) in faces:
                                        face_cropped=img[y:y+h,x:x+w]
                                        return face_cropped

                        cap = cv2.VideoCapture(1)
                        img_id=0
                        while True:
                                ret,my_frame = cap.read()
                                if face_cropped(my_frame) is not None:
                                        img_id+=1
                                        face = cv2.resize(face_cropped(my_frame),(450,450))
                                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                        cv2.imwrite(file_name_path,face)
                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                        cv2.imshow("Cropped Face",face)
                                
                                if cv2.waitKey(1)==13 or int(img_id)==100:
                                        break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Taking of Dataset Completed Successfully!",parent=self.root)

                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


     def iExit(self):
        self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


