from tkinter import *
import random
import datetime
import time
import tkinter.messagebox

root = Tk()
root.geometry("1300x750+0+0")
root.title("Bahria Bakery Billing System")
root.configure(background = '#312113')

text_Input = StringVar()
operator = ""

Tops = Frame(root,bg='#312113',bd=5,pady=5,relief=GROOVE)
Tops.pack(side=TOP)
lblTitle = Label(Tops,font=('times',30,'bold italic'),text="Bahria Bakery",bd=18,bg='#312113',fg='#FFD700',justify=CENTER)
lblTitle.grid(row=0,column=0)

Copyright = Label(root ,bg = '#312113',fg='#FFD700', width = 1200, font=('times', 10, 'bold italic') , text = '© 2020 Copyright. All Rights Reserved')
Copyright.pack(side = BOTTOM)

ReceiptCal_F = Frame(root,bg='#312113',bd=5,padx=20,relief=FLAT)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='#312113',bd=4,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='#312113',bd=6,relief=RIDGE)
Cal_F.pack(side=BOTTOM)

