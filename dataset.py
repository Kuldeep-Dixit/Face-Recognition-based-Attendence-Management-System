     def generate_dataset(self):

        

        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='Kuldeep@16',host='localhost',database='face_recognizer')
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult = mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1

                mycursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Roll_No=%s,Name=%s,Gender=%s,DOB=%s,Phone=%s,PhotoSample=%s where Enrollment_No=%s",( 
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
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)







def update_photo(self):

        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_enroll.get()==0 or self.var_course.get()=="Current Course":
                messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
                try:
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
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='Kuldeep@16',host='localhost',database='face_recognizer')
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult = mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1

                mycursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Roll_No=%s,Name=%s,Gender=%s,DOB=%s,Phone=%s,PhotoSample=%s where Enrollment_No=%s",( 
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
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)