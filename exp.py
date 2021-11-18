from tkinter import*
from tkinter import font
import tkinter as tk
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
from tkinter import messagebox
from csv import writer


root=Tk()
root.minsize(height=500,width=900)

def tab1():
    def tab2():
        x_cord = 75;
        y_cord = 20;
        label1.destroy()
        button1.destroy()
        button2.destroy()
        label2=Label(root,text='Staff Portal',font=('Times_New_Roman',25))
        label2.pack()
        def back():
            label2.destroy()
            staff_back.destroy()
            lbl.destroy()
            txt.destroy()
            lbl2.destroy()
            txt2.destroy()
            lbl3.destroy()
            lbl4.destroy()
            lbl5.destroy()
            message.destroy()
            takeImg.destroy()
            trainImg.destroy()
            tab1()
        staff_back=Button(root,text='Back to Home',font=('Times_New_Roman',25),command=back)
        staff_back.pack()
        lbl = Label(root,text="Enter College id",width=20  ,height=2  ,fg="black"  ,bg="Pink" ,font=('Times New Roman', 25, ' bold ') ) 
        lbl.place(x=200-x_cord, y=200-y_cord)
        txt = Entry(root,width=30,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
        txt.place(x=250-x_cord, y=300-y_cord)
        lbl2 = Label(root, text="Enter the name",width=20  ,fg="black"  ,bg="pink"    ,height=2 ,font=('Times New Roman', 25, ' bold ')) 
        lbl2.place(x=600-x_cord, y=200-y_cord)
        txt2 = Entry(root,width=30  ,bg="white"  ,fg="blue",font=('Times New Roman', 15, ' bold ')  )
        txt2.place(x=650-x_cord, y=300-y_cord)
        lbl3 = Label(root, text="NOTIFICATION",width=20  ,fg="black"  ,bg="pink"  ,height=2 ,font=('Times New Roman', 25, ' bold ')) 
        lbl3.place(x=1060-x_cord, y=200-y_cord)
        message = Label(root, text="" ,bg="white"  ,fg="blue"  ,width=30  ,height=1, activebackground = "white" ,font=('Times New Roman', 15, ' bold ')) 
        message.place(x=1075-x_cord, y=300-y_cord)
        lbl4 = Label(root, text="STEP 1",width=20  ,fg="green"  ,bg="pink"  ,height=2 ,font=('Times New Roman', 20, ' bold '))
        lbl4.place(x=240-x_cord, y=375-y_cord)
        lbl5 = Label(root, text="STEP 2",width=20  ,fg="green"  ,bg="pink"  ,height=2 ,font=('Times New Roman', 20, ' bold ')) 
        lbl5.place(x=645-x_cord, y=375-y_cord)
        def clear1():
            txt.delete(0, 'end')    
            res = ""
            message.configure(text= res)
        def clear2():
            txt2.delete(0, 'end')    
            res = ""
            message.configure(text= res)
        def TakeImages():        
            Id=(txt.get())
            name=(txt2.get())
            if not Id:
                res="Please enter Id"
                message.configure(text = res)
                MsgBox = messagebox.askquestion ("Warning","Please enter roll number properly , press yes if you understood",icon = 'warning')
                if MsgBox == 'no':
                    messagebox.showinfo('Your need','Please go through the readme file properly')
            elif not name:
                res="Please enter Name"
                message.configure(text = res)
                MsgBox = messagebox.askquestion ("Warning","Please enter your name properly , press yes if you understood",icon = 'warning')
                if MsgBox == 'no':
                    messagebox.showinfo('Your need','Please go through the readme file properly')
        
            else:
                cam = cv2.VideoCapture(0)
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector=cv2.CascadeClassifier(harcascadePath)
                sampleNum=0
                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)         
                        sampleNum=sampleNum+1
                        cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                        cv2.imshow('frame',img)
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    elif sampleNum>60:
                        break
                cam.release()
                cv2.destroyAllWindows() 
                res = "Images Saved for ID : " + Id +" Name : "+ name
                row = [Id , name]
                with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                message.configure(text= res)
         
        def TrainImages():
            recognizer = cv2.face_LBPHFaceRecognizer.create()
            faces,Id = getImagesAndLabels("TrainingImage")
            recognizer.train(faces, np.array(Id))
            recognizer.save("TrainingImageLabel\Trainner.yml")
            res = "Image Trained"
            clear1();
            clear2();
            message.configure(text= res)
            tk.messagebox.showinfo('Completed','Your model has been trained successfully!!')
        def getImagesAndLabels(path):
            imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    
            faces=[]

            Ids=[]

            for imagePath in imagePaths:
                pilImage=Image.open(imagePath).convert('L')
                imageNp=np.array(pilImage,'uint8')
                Id=int(os.path.split(imagePath)[-1].split(".")[1])
                faces.append(imageNp)
                Ids.append(Id)        
            return faces,Ids 
        takeImg = Button(root, text="IMAGE CAPTURE BUTTON", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=25  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
        takeImg.place(x=245-x_cord, y=425-y_cord)
        trainImg = Button(root, text="MODEL TRAINING BUTTON", command=TrainImages  ,fg="white"  ,bg="blue"  ,width=25  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
        trainImg.place(x=645-x_cord, y=425-y_cord)

    
    def tab3():
        x_cord = 75;
        y_cord = 20;
        label1.destroy()
        button1.destroy()
        button2.destroy()
        label3=Label(root,text='Student Portal',font=('Times_New_Roman',25))
        label3.pack()
        
        def back2():
            quitWindow.destroy()
            trackImg.destroy()
            label3.destroy()
            student_back.destroy()
            tab1()

        def TrackImages():
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read("TrainingImageLabel\Trainner.yml")
            harcascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath);    
            df=pd.read_csv("StudentDetails\StudentDetails.csv")
            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX        
            col_names =  ['Id','Name','Date','Time']
            attendance = pd.DataFrame(columns = col_names)    
            while True:
                ret, im =cam.read()
                gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                faces=faceCascade.detectMultiScale(gray, 1.2,5)    
                for(x,y,w,h) in faces:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                    Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                    if(conf < 50):
                        ts = time.time()      
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        aa=df.loc[df['Id'] == Id]['Name'].values
                        tt=str(Id)+"-"+aa
                        attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                        atd = [Id,aa[0],date,timeStamp]
                
                    else:
                        Id='Unknown'                
                        tt=str(Id)  
                    if(conf > 75):
                        noOfFile=len(os.listdir("ImagesUnknown"))+1
                        cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                    cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
                attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
                cv2.imshow('im',im) 
                if (cv2.waitKey(1)==ord('q')):
                    break
            ts = time.time()      
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour,Minute,Second=timeStamp.split(":")
            with open('attend.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(atd)
                f_object.close()
            cam.release()
            cv2.destroyAllWindows()
    
        def quit_window():
            MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                messagebox.showinfo("Greetings", "Thank You very much for using our software. Have a nice day ahead!!")
                root.destroy()
    
        student_back=Button(root,text='Back to Home',font=('Times_New_Roman',25),command=back2)
        student_back.pack()

        trackImg = Button(root, text="ATTENDANCE MARKING BUTTON", command=TrackImages  ,fg="white"  ,bg="red"  ,width=30  ,height=3, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
        trackImg.place(x=1075-x_cord, y=412-y_cord)
        quitWindow = Button(root, text="QUIT", command=quit_window  ,fg="white"  ,bg="red"  ,width=10  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
        quitWindow.place(x=700, y=735-y_cord)

        
    label1=Label(root,text='Automatic Attendance Management System',font=('Times_New_Roman',25))
    label1.pack()
    button1=Button(root,text='Staff Portal',font=('Times_New_Roman',25),command=tab2)
    button1.pack()
    button2=Button(root,text='Student Portal',font=('Times_New_Roman',25),command=tab3)
    button2.pack()
tab1()
root.mainloop()