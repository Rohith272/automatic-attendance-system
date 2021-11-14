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

root=Tk()
root.minsize(height=500,width=900)
def tab1():
    def tab2():
        label1.destroy()
        button1.destroy()
        button2.destroy()
        label2=Label(root,text='Staff Portal',font=('Times_New_Roman',25))
        label2.pack()
        def back():
            label2.destroy()
            staff_back.destroy()
            tab1()
        staff_back=Button(root,text='Back to Home',font=('Times_New_Roman',25),command=back)
        staff_back.pack()
        
    def tab3():
        label1.destroy()
        button1.destroy()
        button2.destroy()
        label3=Label(root,text='Student Portal',font=('Times_New_Roman',25))
        label3.pack()

        def back2():
            label3.destroy()
            student_back.destroy()
            tab1()
        student_back=Button(root,text='Back to Home',font=('Times_New_Roman',25),command=back2)
        student_back.pack()

    label1=Label(root,text='Automatic Attendance Management System',font=('Times_New_Roman',25))
    label1.pack()
    button1=Button(root,text='Staff Portal',font=('Times_New_Roman',25),command=tab2)
    button1.pack()
    button2=Button(root,text='Student Portal',font=('Times_New_Roman',25),command=tab3)
    button2.pack()
tab1()
root.mainloop()