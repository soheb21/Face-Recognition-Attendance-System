
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  # for Image style
from tkinter import messagebox
import mysql.connector # to connect with database
import cv2
import numpy as np
from time import strftime
from datetime import datetime


class recognize_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x520+0+0")
        self.root.title("Face Recognition System")

        face_detect_title_label =Label(self.root,text="FACE DETECT",font=("time new roman",35,"bold"),bg="white",fg="blue")
        face_detect_title_label.place(x=0,y=0,width=1400,height=45)

        #First Image
        img1 = Image.open(r"face-images\train.jpg")
        img1 = img1.resize((650, 600),Image.ANTIALIAS)#ANTIALIAS Helps to reduce your image size
        self.photoimg = ImageTk.PhotoImage(img1)

        first_recognize_label = Label(self.root, image=self.photoimg)
        first_recognize_label.place(x=0, y=55, width=650, height=600)    

        #Second Image
        img2 = Image.open(r"face-images\face_detact.jpg")
        img2 = img2.resize((600, 500),Image.ANTIALIAS)#ANTIALIAS Helps to reduce your image size
        self.photoimg1 = ImageTk.PhotoImage(img2)

        second_recognize_label = Label(self.root, image=self.photoimg1)
        second_recognize_label.place(x=670, y=55, width=600, height=500)

        #Recognizer Face Button
        recognize_data_btn=Button(self.root,text="CLICK HERE TO RECOGNIZE DATA",command=face_recog,cursor="hand2",font=("time new roman",22,"bold"),bg="darkred",fg="white")
        recognize_data_btn.place(x=670,y=520,width=650,height=70)

#***********Attendence System*******************
def mark_attendence(r,n,d):
    with open("Attendence.csv","r+",newline="\n") as f:
        my_data_list = f.readlines()
        name_list =[]
        for line in my_data_list:
            entry=line.split((",")) #shoeb,42,IT isliye split(",") ko use kiya ki data ko alag kr de through ","
            name_list.append(entry[0])
        if((r not in name_list) and  (n not in name_list) and (d not in name_list)):
            now = datetime.now()
            d1 = now.strftime("%d/%m/%y")
            dtString =now.strftime("%H:%M:%S")
            
            f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")
#***********Face Recognition Function *************

def face_recog():     
    def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

        coord=[]

        for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            id,predict=clf.predict(gray_img[y:y+h,x:x+w])
            confidence=int((100*(1-predict/300)))

            connect_to_sql= mysql.connector.connect(host="localhost",username="root",password="@dil1234",database="face_recognizer")    
            my_cursor = connect_to_sql.cursor()

            my_cursor.execute("select Name from student where Student_id="+str(id))
            n=my_cursor.fetchone()
            n="+".join(n)

            my_cursor.execute("select Roll from student where Student_id="+str(id))
            r=my_cursor.fetchone()
            r="+".join(r)

            my_cursor.execute("select Dep from student where Student_id="+str(id))
            d=my_cursor.fetchone()
            d="+".join(d)

            if confidence>75:
                cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                mark_attendence(r,n,d)
            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

            coord=[x,y,w,y]
        
        return coord

    def recognize(img,clf,faceCascade):
        coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
        return img

    faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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

if __name__ == "__main__":
    root = Tk()
    obj = recognize_data(root)
    root.mainloop()#create the GUI 