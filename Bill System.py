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

Receipt_F=Frame(ReceiptCal_F,bg='#312113',bd=4,relief=RIDGE)
Receipt_F.pack(side=TOP)

MenuFrame = Frame(root,bg='#312113',bd=5,pady=5,relief=GROOVE)
MenuFrame.pack(side=LEFT)

Cost_F=Frame(MenuFrame,bg='#312113',bd=4, relief=FLAT)
Cost_F.pack(side=BOTTOM)

Right_C=Frame(MenuFrame,bg='#312113',bd=10, relief=FLAT)
Right_C.pack(side=TOP)

Right_C=Frame(MenuFrame,bg='#312113',bd=10,width=300,height=400,relief=FLAT)
Right_C.pack(side=LEFT)

Left_C=Frame(MenuFrame,bg='#312113',bd=10,relief=FLAT)
Left_C.pack(side=RIGHT)

#=====================================================================================================================================#
def iExit():
    iExit = tkinter.messagebox.askyesno("Exit","Confirm you want to exit")
    if iExit>0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Doughnuts.set("0")
    E_Sandwich.set("0")
    E_Pie.set("0")
    E_G_Halwa.set("0")
    E_Brownies.set("0")
    E_Bread.set("0")
    E_M_Cake.set("0")
    E_Barfi.set("0")

    E_Nankhatai.set("0")
    E_C_Drinks.set("0")
    E_Chips.set("0")
    E_Nimco.set("0")
    E_Rusk.set("0")
    E_Rabri.set("0")
    E_Pudding.set("0")
    E_Pastry.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtDoughnuts.configure(state = DISABLED)
    txtSandwich.configure(state = DISABLED)
    txtPie.configure(state = DISABLED)
    txtG_Halwa.configure(state = DISABLED)
    txtBrownies.configure(state = DISABLED)
    txtBread.configure(state = DISABLED)
    txtM_Cake.configure(state = DISABLED)
    txtBarfi.configure(state = DISABLED)
    txtNankhatai.configure(state = DISABLED)
    txtC_Drinks.configure(state = DISABLED)
    txtChips.configure(state = DISABLED)
    txtNimco.configure(state = DISABLED)
    txtRusk.configure(state = DISABLED)
    txtRabri.configure(state = DISABLED)
    txtPudding.configure(state = DISABLED)
    txtPastry.configure(state = DISABLED)

