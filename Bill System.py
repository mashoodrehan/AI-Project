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

def CostofItem():
    Item1=float(E_Doughnuts.get())
    Item2=float(E_Sandwich.get())
    Item3=float(E_Pie.get())
    Item4=float(E_G_Halwa.get())
    Item5=float(E_Brownies.get())
    Item6=float(E_Bread.get())
    Item7=float(E_M_Cake.get())
    Item8=float(E_Barfi.get())
    Item9=float(E_Nankhatai.get())
    Item10=float(E_C_Drinks.get())
    Item11=float(E_Chips.get())
    Item12=float(E_Nimco.get())
    Item13=float(E_Rusk.get())
    Item14=float(E_Rabri.get())
    Item15=float(E_Pudding.get())
    Item16=float(E_Pastry.get())

    CostofLine1 = (Item1*150) + (Item2*70) + (Item3*200) + (Item4*450) + (Item5*30)+ (Item6*50) + (Item7*850) + (Item8*660)
    CostofLine2 = (Item9*350) + (Item10*60) + (Item11*70) + (Item12*120) + (Item13*60) + (Item14*550) + (Item15*400) + (Item16*80)

    TotalC = CostofLine1 + CostofLine2
    ServiceC = 0
    PTax = (TotalC)*0.03
    STotal = TotalC + ServiceC + PTax
    TTotal = STotal

    Line1Price = "Rs.",str('%.2f'%(CostofLine1))
    Line2Price = "Rs.",str('%.2f'%(CostofLine2))
    CostofCakes.set(Line2Price)
    CostofDrinks.set(Line1Price)
    SC = "Rs.", str('%.2f'%(ServiceC))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs.",str('%.2f'%(STotal))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs.",str('%.2f'%(PTax))
    PaidTax.set(Tax)
    TC = "Rs.",str('%.2f'%(TTotal))
    TotalCost.set(TC)
