from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # for Image style
from tkinter import messagebox
import mysql.connector  # to connect with database
import cv2
import os
import numpy as np


class Train_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x520+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="TRAIN DATA SET", font=("time new roman", 35, "bold"), bg="white",
                            fg="darkblue")
        title_label.place(x=0, y=0, width=1400, height=45)

        # First Image
        img1 = Image.open(r"face-images\heading.jpg")
        img1 = img1.resize((700, 280), Image.ANTIALIAS)  # ANTIALIAS Helps to reduce your image size
        self.photoimg = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=55, width=700, height=280)

        # second image
        img2 = Image.open(r"face-images\heading3.jpg")
        img2 = img2.resize((800, 280), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img2)

        second_label = Label(self.root, image=self.photoimg1)
        second_label.place(x=600, y=55, width=800, height=280)

        # Image Down Button
        img_down = Image.open(r"face-images\image_down.jpg")
        img_down = img_down.resize((1400, 300), Image.ANTIALIAS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        third_label = Label(self.root, image=self.photoimg_down)
        third_label.place(x=0, y=420, width=1400, height=300)

        # Tain Face Button
        tain_data_btn = Button(self.root, text="CLICK HERE TO TRAIN DATA", command=self.train_classifier,
                               cursor="hand2", font=("time new roman", 22, "bold"), bg="darkblue", fg="white")
        tain_data_btn.place(x=0, y=320, width=1400, height=100)

    def train_classifier(self):
        data_dir = ("dataset")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]  # list comphrihinson

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale Image
            imageNp = np.array(img,'uint8')  # 'uint8' is a datatype
            id=int(os.path.split(image)[-1].split(".")[1])
            

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13  # Close window when we Click the 'enter'

        ids = np.array(ids)

        # ***************Train the Classifier *****************

        clf =cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed !")


if __name__ == "__main__":
    root = Tk()
    obj = Train_data(root)
    root.mainloop()  # create the GUI
