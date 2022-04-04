
from sre_parse import expand_template
from tkinter import*
from tkinter import ttk
import tkinter  # for style
from PIL import Image, ImageTk  # for Image style
from student import Student # Join the page 
import os
from train import Train_data
from face_recoginizer import recognize_data
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo

class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x520+0+0")
        self.root.title("Face Recognition System")

        

        

        #background image
        img4 = Image.open("face-images\\heading.jpg")
        img4 = img4.resize((1400, 580),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=580)
        

        #*****Video*********************
        right_frame = LabelFrame(self.root)
        right_frame.place(x=550,y=50,width=700,height=660)


        video_lable=Label(right_frame)
        video_lable.config(anchor=CENTER)
        video_lable.pack()

        videoplayer = TkinterVideo(master=right_frame, scaled=True, pre_load=False)
        videoplayer.load("acpce.webm")
        videoplayer.pack(expand=True, fill="both")

        videoplayer.play()

        #First image
        img1 = Image.open("face-images\\heading1.jpeg")
        img1 = img1.resize((200, 130),Image.ANTIALIAS)#ANTIALIAS Helps to reduce your image size
        self.photoimg = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=200, height=135)


        title_label =Label(self.root,text="FACE ATTENDANCE SYSTEM",font=("time new roman",40,"bold"),bg="darkblue",fg="white")
        title_label.place(x=200,y=0,width=1200,height=130)
        #student Button
        img5 = Image.open(r"face-images\images.jpg")
        img5 = img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=50,y=100,width=130,height=180)

        b2=Button(bg_img,text="Student Details",cursor="hand2",font=("time new roman",11,"bold"),bg="darkblue",fg="white",command=self.student_details)
        b2.place(x=50,y=240,width=130,height=40)

         #Detact Face Button
        img6 = Image.open(r"face-images\face_detact.jpg")
        img6 = img6.resize((130,130),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_detect)
        b1.place(x=200,y=100,width=130,height=180)

        b2=Button(bg_img,text="Face Detact",cursor="hand2",command=self.face_detect,font=("time new roman",11,"bold"),bg="darkblue",fg="white")
        b2.place(x= 200,y=240,width=130,height=40)

        #Attendence Face Button
        img7 = Image.open(r"face-images\Attendence.png")
        img7 = img7.resize((130,130),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_button)
        b1.place(x=360,y=100,width=130,height=180)

        b2=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_button,font=("time new roman",11,"bold"),bg="darkblue",fg="white")
        b2.place(x=360,y=240,width=130,height=40)


        #Train Face Button
        img9 = Image.open(r"face-images\train.jpg")
        img9 = img9.resize((130,130),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_image)
        b1.place(x=50,y=310,width=130,height=180)

        b2=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_image,font=("time new roman",11,"bold"),bg="darkblue",fg="white")
        b2.place(x=50,y=450,width=130,height=40)

        #Images Face Button
        img10 = Image.open(r"C:\Users\rpsam\Desktop\Face-Recognization-system\face-images\student.jfif")
        img10 = img10.resize((130,130),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.photo_Button)
        b1.place(x=200,y=310,width=130,height=180)

        b2=Button(bg_img,text="Images",cursor="hand2",command=self.photo_Button,font=("time new roman",11,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=450,width=130,height=40)

        #Exit Face Button
        img11 = Image.open(r"face-images\exit.jpg")
        img11 = img11.resize((130,130),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Exit_Button)
        b1.place(x=360,y=310,width=130,height=180)

        b2=Button(bg_img,text="Exit",cursor="hand2",command=self.Exit_Button,font=("time new roman",11,"bold"),bg="darkblue",fg="white")
        b2.place(x=360,y=450,width=130,height=40)

    #**************Click Image Button*******************

    def photo_Button(self):
        os.startfile("dataset")#Path ko call krta hai 'startfile'

    def attendence_button(self):
        os.startfile("Attendence.csv")

    def Exit_Button(self):
        self.Exit_Button=tkinter.messagebox.askyesno("Face Recognition"," Are you sure",parent=self.root)
        if self.Exit_Button >0:
            self.root.destroy()
        else:
            return   

            #Click Function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_image(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_data(self.new_window)

    def face_detect(self):
        self.new_window=Toplevel(self.root)
        self.app=recognize_data(self.new_window)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()#create the GUI

    #********* Code End ************
