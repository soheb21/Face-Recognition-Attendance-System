
from tkinter import*
from tkinter import ttk # for style
from PIL import Image, ImageTk  # for Image style
from tkinter import messagebox
import mysql.connector # to connect with database
import cv2,os



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x520+0+0")
        self.root.title("Face Recognition System")

        #********Variables********
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_name=StringVar()
        self.var_num=StringVar()
        self.var_div=StringVar()



        #First Image
        

       
        

        main_frame=Frame(self.root,bd=2,bg="blue")
        main_frame.place(x=0,y=0,width=1400,height=900)

        #background image
        img4 = Image.open(r"face-images\heading.jpg")
        img4 = img4.resize((1400, 700),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img4)

        bg_img = Label(main_frame, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1400, height=700)


        title_label =Label(main_frame,text="STUDENT DETAILS",font=("time new roman",35,"bold"),bg="darkblue",fg="white")
        title_label.place(x=0,y=0,width=1400,height=45)

        #left Label Frame
        Left_frame = LabelFrame(main_frame)
        Left_frame.place(x=10,y=70,width=400,height=550)

        #current course
        current_crs = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Info",font=("time new roman",12,"bold"))
        current_crs.place(x=5,y=5,width=400,height=550)

            #Department
        dep_lable=Label(current_crs,text="Deparment",font=("time new roman",12,"bold"),bg="white")
        dep_lable.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_crs,textvariable=self.var_dep,font=("time new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","IOT","Civil","Mechanical","Ecectrical","Ai-Ds")
        dep_combo.current(0)#Select Department
        dep_combo.grid(row=0,column=0,padx=2,pady=10)

            #Courses
        course_lable=Label(current_crs,text="Course",font=("time new roman",12,"bold"),bg="white")
        course_lable.grid(row=1,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_crs,textvariable=self.var_course,font=("time new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","FE")
        course_combo.current(0)#Select Course
        course_combo.grid(row=1,column=0,padx=2,pady=10,sticky=W)

            #Year
        year_lable=Label(current_crs,text="Year",font=("time new roman",12,"bold"),bg="white")
        year_lable.grid(row=2,column=0)

        year_combo=ttk.Combobox(current_crs,textvariable=self.var_year,font=("time new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)#Select year
        year_combo.grid(row=2,column=0,padx=2,pady=10,sticky=W)

            #Semester
        semester_lable=Label(current_crs,text="Semester",font=("time new roman",12,"bold"),bg="white")
        semester_lable.grid(row=3,column=0,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_crs,textvariable=self.var_sem,font=("time new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)#Select Course
        semester_combo.grid(row=3,column=0,padx=2,pady=10,sticky=W)   


             

            #Student Number
        student_id_lable=Label(current_crs,text="StudentID:",font=("time new roman",10,"bold"),bg="white")
        student_id_lable.grid(row=4,column=0,padx=0,sticky=W)

        student_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_id,font=("time new roman",10,"bold"))
        student_entry.grid(row=4,column=1,padx=0,sticky=W)  

            #Student name
        student_name_lable=Label(current_crs,text="Student Name:",font=("time new roman",10,"bold"),bg="white")
        student_name_lable.grid(row=5,column=0,pady=5,sticky=W)

        student_name_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_name,font=("time new roman",10,"bold"))
        student_name_entry.grid(row=5,column=1,pady=5,sticky=W)
            #Class Division
        student_div_lable=Label(current_crs,text="Class Div:",font=("time new roman",10,"bold"),bg="white")
        student_div_lable.grid(row=6,column=0,pady=3,sticky=W)

        student_div_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_div,font=("time new roman",10,"bold"))
        student_div_entry.grid(row=6,column=1,pady=3,sticky=W)
            #roll no 
        student_roll_lable=Label(current_crs,text="Roll No:",font=("time new roman",10,"bold"),bg="white")
        student_roll_lable.grid(row=7,column=0,pady=3,sticky=W)

        student_roll_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_rollno,font=("time new roman",10,"bold"))
        student_roll_entry.grid(row=7,column=1,pady=3,sticky=W)

            #Gender
        student_gender_lable=Label(current_crs,text="Gender:",font=("time new roman",10,"bold"),bg="white")
        student_gender_lable.grid(row=8,column=0,pady=3,sticky=W)

        student_gender_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_gender,font=("time new roman",10,"bold"))
        student_gender_entry.grid(row=8,column=1,pady=3,sticky=W)

            #DOB
        student_dob_lable=Label(current_crs,text="DOB:",font=("time new roman",10,"bold"),bg="white")
        student_dob_lable.grid(row=9,column=0,pady=3,sticky=W)

        student_dob_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_dob,font=("time new roman",10,"bold"))
        student_dob_entry.grid(row=9,column=1,pady=3,sticky=W)

            #Email
        student_email_lable=Label(current_crs,text="Email:",font=("time new roman",10,"bold"),bg="white")
        student_email_lable.grid(row=10,column=0,pady=3,sticky=W)

        student_email_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_email,font=("time new roman",10,"bold"))
        student_email_entry.grid(row=10,column=1,pady=3,sticky=W)

            #phone no
        student_phn_lable=Label(current_crs,text="Phone no:",font=("time new roman",10,"bold"),bg="white")
        student_phn_lable.grid(row=11,column=0,pady=3,sticky=W)

        student_phn_entry=ttk.Entry(current_crs,width=20,textvariable=self.var_num,font=("time new roman",10,"bold"))
        student_phn_entry.grid(row=11,column=1,pady=3,sticky=W) 

            #Save Button
        save_button=Button(current_crs,text="Save",width=20,command=self.add_data,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        save_button.grid(row=13,column=0,padx=3,pady=5)

            #update Button
        update_button=Button(current_crs,text="update",command=self.update_data,width=20,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        update_button.grid(row=13,column=1,pady=5)

            #Delete Button
        del_button=Button(current_crs,text="Delete",command=self.delete_data,width=20,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        del_button.grid(row=14,column=0,pady=5)

            #Reset Button
        reset_button=Button(current_crs,text="Reset",command=self.reset_data,width=20,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        reset_button.grid(row=14,column=1,pady=5)

            #Add Photo Sample Button
        add_button=Button(current_crs,text="Add Photo Sample",command=self.take_pht,width=20,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        add_button.grid(row=15,column=0,pady=5)

            #Update Photo Sample Button
        update_pht_button=Button(current_crs,text="update Photo Sample",width=20,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        update_pht_button.grid(row=15,column=1,pady=5)

#-------------------------------------------------------------------------->

        #right Label Frame
        right_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        right_frame.place(x=470,y=70,width=800,height=580)

            #Search System
        search_class = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("time new roman",10,"bold"))
        search_class.place(x=5,y=0,width=800,height=70)

        search_lable=Label(search_class,text="Search By:",font=("time new roman",12,"bold"),bg="darkblue",fg="white")
        search_lable.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_class,width=15,font=("time new roman",10,"bold"),state="readonly")
        search_combo["values"]=("Select Option","Roll No","PNR Number")
        search_combo.current(0)#Select Option
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        #Entry fill
        search_entry=ttk.Entry(search_class,width=17,font=("time new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        #search Button
        search_button=Button(search_class,text="Search",width=10,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        search_button.grid(row=0,column=3,padx=4)

        #Show All Button
        showAll_button=Button(search_class,text="Show All",width=10,font=("time new roman",10,"bold"),bg="darkblue",fg="white",cursor="hand2")  
        showAll_button.grid(row=0,column=4,padx=4)

        #Table Flame

        table_flame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_flame.place(x=5,y=70,width=790,height=460)

        #Scroll bar in Table Frame

        scroll_x=ttk.Scrollbar(table_flame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_flame,orient=VERTICAL)

        self.student_table =ttk.Treeview(table_flame,columns=("dep","course","year","sem","id","name","div","dob","email","phn","rollno","gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)                                 
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")                              
        self.student_table.heading("course",text="Course")                              
        self.student_table.heading("year",text="Year")  
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Div")
        self.student_table.heading("dob",text="DOB")  
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phn",text="Phn_Number")
        self.student_table.heading("rollno",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table["show"]="headings" #upper heading main first box emty na ho start ho department

        #heading width
        self.student_table.column("course",width=100)                              
        self.student_table.column("dep",width=100)                            
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dob",width=100)  
        self.student_table.column("email",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("phn",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)



        self.student_table.pack(fill=BOTH,expand=1) 
        self.student_table.bind("<ButtonRelease>",self.get_cursor) 
        self.show_data()

     #*******Function Declaration******   

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
             messagebox.showerror("Error","All Fields are requried")
        else:
            try:
                connect_to_sql= mysql.connector.connect(host="localhost",username="root",password="@dil1234",database="face_recognizer")    
                my_cursor = connect_to_sql.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_num.get(),
                                                                                                self.var_rollno.get(),
                                                                                                self.var_gender.get()
                                                                                                ))
                connect_to_sql.commit()
                self.show_data()
                connect_to_sql.close()
                messagebox.showinfo("Success","Details Added successfully",parent=self.root)  

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)                                                                                   

#*****************Function for Show data in project************

    def show_data(self):
        connect_to_sql= mysql.connector.connect(host="localhost",username="root",password="@dil1234",database="face_recognizer")    
        my_cursor = connect_to_sql.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall() #In (data) all data in database is fetch

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            connect_to_sql.commit()
            connect_to_sql.close()    

    #******* Function for show details in left side *************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        
        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_email.set(data[8]),
        self.var_num.set(data[9]),
        self.var_rollno.set(data[10]),
        self.var_gender.set(data[11])
        
  #*******Update Button Function *****************   

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
             messagebox.showerror("Error","All Fields are requried")
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want this student details",parent=self.root)
                connect_to_sql= mysql.connector.connect(host="localhost",username="root",password="@dil1234",database="face_recognizer")    
                my_cursor = connect_to_sql.cursor()
                
                                            #Saare naam Database k Coloumn k hai.
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Dob=%s,Email=%s,Phone=%s,Roll=%s,Gender=%s where Student_id=%s ",(
                                                                                                                                                                        self.var_dep.get(),                                                                                                                                                                           
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_num.get(),
                                                                                                                                                                        self.var_rollno.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_id.get()

                                                                                                                                                                         ))
                messagebox.showinfo("Success","Student Details Update Successfully",parent=self.root)
                connect_to_sql.commit()
                self.show_data()
                connect_to_sql.close()
            except Exception as e :
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)


                #***************Function for Delete Button***************
                           
    def delete_data(self):
        if self.var_id.get()=="":
                messagebox.showerror("Error","Student must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details",parent=self.root)
                connect_to_sql= mysql.connector.connect(host="localhost",username="root",password="@dil1234",database="face_recognizer")    
                my_cursor = connect_to_sql.cursor()
                sql='delete from student where Student_id=%s'
                val=(self.var_id.get(),)#Tuple
                my_cursor.execute(sql,val)
                
                if not delete:
                    return
                connect_to_sql.commit()
                self.show_data()
                connect_to_sql.close()
                messagebox.showinfo("Delete","Successfully deleted Student Details",parent=self.root)      
            except Exception as e :
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
    #******Function for Reset Button********

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_name.set("")
        self.var_div.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_num.set("")
        self.var_rollno.set("")
        self.var_gender.set("")
        self.var_id.set("")

#****************take Photo Button Function******************

    def take_pht(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
             messagebox.showerror("Error","All Fields are requried")

        else:
            try:
                connect_to_sql= mysql.connector.connect(host="localhost",username="root",password="@dil1234",database="face_recognizer")    
                my_cursor = connect_to_sql.cursor()
                my_cursor.execute("select * from student")
                myresult= my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Dob=%s,Email=%s,Phone=%s,Roll=%s,Gender=%s where Student_id=%s ",(
                                                                                                                                                                        self.var_dep.get(),                                                                                                                                                                           
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_num.get(),
                                                                                                                                                                        self.var_rollno.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_id.get()==id+1
                                                                                                                                                                         ))    
                connect_to_sql.commit()
                self.show_data()
                self.reset_data()
                connect_to_sql.close()
            
            #**********Open Cv ************
                

                    
                haar_file = 'haarcascade_frontalface_default.xml'
                
                path=("dataset/")
                dir = os.path.dirname(path)
                if not os.path.exists(dir):
                    os.makedirs(dir) 
                    # Start capturing video

                face_detector = cv2.CascadeClassifier(haar_file)    
                vid_cam = cv2.VideoCapture(0)
                    # Detect object in video stream using Haarcascade Frontal Face
                    # Initialize sample face image
                count = 0
                    # Start looping
                while (True):

                    # Capture video frame
                    _, image_frame = vid_cam.read()

                    # Convert frame to grayscale
                    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

                    # Detect frames of different sizes, list of faces rectangles
                    faces = face_detector.detectMultiScale(gray, 1.3, 5)

                    # Loops for each faces
                    for (x, y, w, h) in faces:
                        # Crop the image frame into rectangle
                        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Increment sample face image
                        count += 1

                        # Save the captured image into the datasets folder
                        cv2.imwrite("dataset/User."  +str(id)+'.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

                        # Display the video frame, with bounded rectangle on the person's face
                        cv2.imshow('frame', image_frame)

                    # To stop taking video, press 'q' for at least 100ms
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break

                    # If image taken reach 100, stop taking video
                    elif count >= 50:
                        break

                    # Stop video
                vid_cam.release()
                cv2.destroyAllWindows()    
                                
                                
                messagebox.showinfo("Result","Generating data Set Completed")   

            except Exception as e :
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)



if __name__ == "__main__":
    root = Tk() 
    obj = Student(root)
    root.mainloop()#create the GUI  

    #***************Code End *******************       