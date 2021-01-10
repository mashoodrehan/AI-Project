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

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(100,10000)
    randomRef = str(x)
    Receipt_Ref.set("SS" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Item:\t\t\t'+ "Cost of Items\n")
    txtReceipt.insert(END, 'Doughnuts:\t\t\t'+E_Doughnuts.get()+"\n")
    txtReceipt.insert(END, 'Sandwich:\t\t\t'+E_Sandwich.get()+"\n")
    txtReceipt.insert(END, 'Pie:\t\t\t'+E_Pie.get()+"\n")
    txtReceipt.insert(END, 'Halwa(Gajar):\t\t\t'+ E_G_Halwa.get()+"\n")
    txtReceipt.insert(END, 'Kaju Katli:\t\t\t'+E_Brownies.get()+"\n")
    txtReceipt.insert(END, 'Ladoo(Besan):\t\t\t'+E_Bread.get()+"\n")
    txtReceipt.insert(END, 'Milk Cake:\t\t\t'+ E_M_Cake.get()+"\n")
    txtReceipt.insert(END, 'Mawa Barfi:\t\t\t'+ E_Barfi.get()+"\n")
    txtReceipt.insert(END, 'Misri Mawa:\t\t\t'+ E_Nankhatai.get()+"\n")
    txtReceipt.insert(END, 'Cold Drinks:\t\t\t'+E_C_Drinks.get()+"\n")
    txtReceipt.insert(END, 'Chips:\t\t\t'+E_Chips.get()+"\n")
    txtReceipt.insert(END, 'Ladoo(Bundi):\t\t\t'+E_Nimco.get()+"\n")
    txtReceipt.insert(END, 'Bengali Sweets:\t\t\t'+E_Rusk.get()+"\n")
    txtReceipt.insert(END, 'Rabri:\t\t\t'+E_Rabri.get()+"\n")
    txtReceipt.insert(END, 'Pudding:\t\t\t'+E_Pudding.get()+"\n")
    txtReceipt.insert(END, 'Pastry:\t\t\t'+E_Pastry.get()+"\n")

    txtReceipt.insert(END, "Cost of Items:\t\t\t" + (SubTotal.get()) + "\nTax:\t\t\t"+PaidTax.get() + "\n")
    txtReceipt.insert(END, "Sub Total:\t\t\t" + str(SubTotal.get()) + "\n")
    txtReceipt.insert(END, "Service Charge:\t\t\t" + ServiceCharge.get() + "\nTotal:\t\t\t"+str(TotalCost.get()))
#=====================================================================================================================================#
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator=""

E_Doughnuts=StringVar()
E_Sandwich=StringVar()
E_Pie=StringVar()
E_G_Halwa=StringVar()
E_Brownies=StringVar()
E_Bread=StringVar()
E_M_Cake=StringVar()
E_Barfi=StringVar()

E_Nankhatai=StringVar()
E_C_Drinks=StringVar()
E_Chips=StringVar() 
E_Nimco=StringVar()
E_Rusk=StringVar()
E_Rabri=StringVar()
E_Pudding=StringVar()
E_Pastry=StringVar()

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

DateofOrder.set(time.strftime("%d/%m/%Y"))
#======================================================================================================================================#
def chDoughnuts():
    if (var1.get() == 1):
        txtDoughnuts.configure(state=NORMAL)
        txtDoughnuts.focus()
        txtDoughnuts.delete('0',END)
        E_Doughnuts.set("")
    elif(var1.get() == 0):
        txtDoughnuts.configure(state=DISABLED)
        E_Doughnuts.set("0")
def chSandwich():
    if (var2.get() == 1):
        txtSandwich.configure(state=NORMAL)
        txtSandwich.focus()
        txtSandwich.delete('0',END)
        E_Sandwich.set("")
    elif(var2.get() == 0):
        txtSandwich.configure(state=DISABLED)
        E_Sandwich.set("0")
def chPie():
    if (var3.get() == 1):
        txtPie.configure(state=NORMAL)
        txtPie.focus()
        txtPie.delete('0',END)
        E_Pie.set("")
    elif(var3.get() == 0):
        txtPie.configure(state=DISABLED)
        E_Pie.set("0")
def chM_Cake():
    if (var7.get() == 1):
        txtM_Cake.configure(state=NORMAL)
        txtM_Cake.focus()
        txtM_Cake.delete('0',END)
        E_M_Cake.set("")
    elif(var7.get() == 0):
        txtM_Cake.configure(state=DISABLED)
        E_M_Cake.set("0")
def chBarfi():
    if (var8.get() == 1):
        txtBarfi.configure(state=NORMAL)
        txtBarfi.focus()
        txtBarfi.delete('0',END)
        E_Barfi.set("")
    elif(var8.get() == 0):
        txtBarfi.configure(state=DISABLED)
        E_Barfi.set("0")
def chG_Halwa():
    if (var4.get() == 1):
        txtG_Halwa.configure(state=NORMAL)
        txtG_Halwa.focus()
        txtG_Halwa.delete('0',END)
        E_G_Halwa.set("")
    elif(var4.get() == 0):
        txtG_Halwa.configure(state=DISABLED)
        E_G_Halwa.set("0")
def chBrownies():
    if (var5.get() == 1):
        txtBrownies.configure(state=NORMAL)
        txtBrownies.focus()
        txtBrownies.delete('0',END)
        E_Brownies.set("")
    elif(var5.get() == 0):
        txtBrownies.configure(state=DISABLED)
        E_Brownies.set("0")
def chBread():
    if (var6.get() == 1):
        txtBread.configure(state=NORMAL)
        txtBread.focus()
        txtBread.delete('0',END)
        E_Bread.set("")
    elif(var6.get() == 0):
        txtBread.configure(state=DISABLED)
        E_Bread.set("0")
def chPastry():
    if (var16.get() == 1):
        txtPastry.configure(state=NORMAL)
        txtPastry.focus()
        txtPastry.delete('0',END)
        E_Pastry.set("")
    elif(var16.get() == 0):
        txtPastry.configure(state=DISABLED)
        E_Pastry.set("0")
def chPudding():
    if (var15.get() == 1):
        txtPudding.configure(state=NORMAL)
        txtPudding.focus()
        txtPudding.delete('0',END)
        E_Pudding.set("")
    elif(var15.get() == 0):
        txtPudding.configure(state=DISABLED)
        E_Pudding.set("0")
def chRabri():
    if (var14.get() == 1):
        txtRabri.configure(state=NORMAL)
        txtRabri.focus()
        txtRabri.delete('0',END)
        E_Rabri.set("")
    elif(var14.get() == 0):
        txtRabri.configure(state=DISABLED)
        E_Rabri.set("0")
def chNimco():
    if (var12.get() == 1):
        txtNimco.configure(state=NORMAL)
        txtNimco.focus()
        txtNimco.delete('0',END)
        E_Nimco.set("")
    elif(var12.get() == 0):
        txtNimco.configure(state=DISABLED)
        E_Nimco.set("0")
def chChips():
    if (var11.get() == 1):
        txtChips.configure(state=NORMAL)
        txtChips.focus()
        txtChips.delete('0',END)
        E_Chips.set("")
    elif(var11.get() == 0):
        txtChips.configure(state=DISABLED)
        E_Chips.set("0")
def chRusk():
    if (var13.get() == 1):
        txtRusk.configure(state=NORMAL)
        txtRusk.focus()
        txtRusk.delete('0',END)
        E_Rusk.set("")
    elif(var13.get() == 0):
        txtRusk.configure(state=DISABLED)
        E_Rusk.set("0")
def chC_Drinks():
    if (var10.get() == 1):
        txtC_Drinks.configure(state=NORMAL)
        txtC_Drinks.focus()
        txtC_Drinks.delete('0',END)
        E_C_Drinks.set("")
    elif(var10.get() == 0):
        txtC_Drinks.configure(state=DISABLED)
        E_C_Drinks.set("0")
def chNankhatai():
    if (var9.get() == 1):
        txtNankhatai.configure(state=NORMAL)
        txtNankhatai.focus()
        txtNankhatai.delete('0',END)
        E_Nankhatai.set("")
    elif(var9.get() == 0):
        txtNankhatai.configure(state=DISABLED)
        E_Nankhatai.set("0")
#=========================================================LEFT MENU=======================================================================#
Doughnuts=Checkbutton(Right_C,text="Doughnuts",variable=var1,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chDoughnuts).grid(row=0,sticky=W)
Sandwich=Checkbutton(Right_C,text="Sandwich",variable=var2,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chSandwich).grid(row=1,sticky=W)
Pie=Checkbutton(Right_C,text="Pie",variable=var3,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chPie).grid(row=2,sticky=W)
G_Halwa=Checkbutton(Right_C,text="Gajar Halwa",variable=var4,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chG_Halwa).grid(row=3,sticky=W)
Brownies=Checkbutton(Right_C,text="Brownies",variable=var5,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chBrownies).grid(row=4,sticky=W)
Bread=Checkbutton(Right_C,text="Bread",variable=var6,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chBread).grid(row=5,sticky=W)
M_Cake=Checkbutton(Right_C,text="Milk Cake",variable=var7,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chM_Cake).grid(row=6,sticky=W)
Barfi=Checkbutton(Right_C,text="Barfi",variable=var8,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chBarfi).grid(row=7,sticky=W)
#=======================================================ENTRY==BOX==FOR==LEFT MENU=========================================================#
txtDoughnuts = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Doughnuts)
txtDoughnuts.grid(row=0,column=1)
txtSandwich = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Sandwich)
txtSandwich.grid(row=1,column=1)
txtPie = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Pie)
txtPie.grid(row=2,column=1)
txtG_Halwa = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_G_Halwa)
txtG_Halwa.grid(row=3,column=1)
txtBrownies = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Brownies)
txtBrownies.grid(row=4,column=1)
txtBread = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Bread)
txtBread.grid(row=5,column=1)
txtM_Cake = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_M_Cake)
txtM_Cake.grid(row=6,column=1)
txtBarfi = Entry(Right_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Barfi)

txtBarfi.grid(row=7,column=1)
#===============================================================RIGHT MENU===================================================================#
Nankhatai=Checkbutton(Left_C,text="Nankhatai",variable=var9,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chNankhatai).grid(row=0,sticky=W)
C_Drinks=Checkbutton(Left_C,text="Cold Drinks",variable=var10,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chC_Drinks).grid(row=1,sticky=W)
Chips=Checkbutton(Left_C,text="Chips",variable=var11,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chChips).grid(row=2,sticky=W)
Nimco=Checkbutton(Left_C,text="Nimco",variable=var12,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chNimco).grid(row=3,sticky=W)
Rusk=Checkbutton(Left_C,text="Rusk",variable=var13,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chRusk).grid(row=4,sticky=W)
Rabri=Checkbutton(Left_C,text="Rabri",variable=var14,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chRabri).grid(row=5,sticky=W)
Pudding=Checkbutton(Left_C,text="Pudding",variable=var15,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chPudding).grid(row=6,sticky=W)
Pastry=Checkbutton(Left_C,text="Pastry",variable=var16,onvalue=1,offvalue=0, font=('times',18,"bold italic"),bg='#312113', fg='#FFD700',command = chPastry).grid(row=7,sticky=W)
#=======================================================ENTRY==BOX==FOR==RIGHT MENU===========================================================#
txtNankhatai = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Nankhatai)
txtNankhatai.grid(row=0,column=1)
txtC_Drinks = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_C_Drinks)
txtC_Drinks.grid(row=1,column=1)
txtChips = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Chips)
txtChips.grid(row=2,column=1)
txtNimco = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Nimco)
txtNimco.grid(row=3,column=1)
txtRusk = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Rusk)
txtRusk.grid(row=4,column=1)
txtRabri = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Rabri)
txtRabri.grid(row=5,column=1)
txtPudding = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Pudding)
txtPudding.grid(row=6,column=1)
txtPastry = Entry(Left_C,font=('calibri',15),bd=7,width=6,justify=LEFT,state = DISABLED,textvariable=E_Pastry)
txtPastry.grid(row=7,column=1)
#============================================================Total Cost==================================================================#
lblCostofLeft = Label(Cost_F,font=('times',14,"bold italic"),text="Cost Of List1\t ",bg='#312113', fg='#FFD700')
lblCostofLeft.grid(row=0,column=0,sticky=W)
txtCostofLeft = Entry(Cost_F,font=('times',14),textvariable=CostofDrinks,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtCostofLeft.grid(row=0,column=1)
txtCostofLeft.configure(state = DISABLED)

lblCostofRight = Label(Cost_F,font=('times',14,"bold italic"),text="Cost Of List2 ",bg='#312113', fg='#FFD700')
lblCostofRight.grid(row=1,column=0,sticky=W)
txtCostofRight = Entry(Cost_F,font=('times',14),textvariable=CostofCakes,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtCostofRight.grid(row=1,column=1)
txtCostofRight.configure(state = DISABLED)

lblServiceCharge = Label(Cost_F,font=('times',14,"bold italic"),text="Service Charge ",bg='#312113', fg='#FFD700')
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge = Entry(Cost_F,font=('times',14),textvariable=ServiceCharge,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)
txtServiceCharge.configure(state = DISABLED)

lblPaidTax = Label(Cost_F,font=('times',14,"bold italic"),text="Paid Tax",bg='#312113', fg='#FFD700')
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax = Entry(Cost_F,font=('times',14),textvariable=PaidTax,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtPaidTax.grid(row=0,column=3)
txtPaidTax.configure(state = DISABLED)

lblSubTotal = Label(Cost_F,font=('times',14,"bold italic"),text="Sub Total",bg='#312113', fg='#FFD700')
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal = Entry(Cost_F,font=('times',14),textvariable=SubTotal,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtSubTotal.grid(row=1,column=3)
txtSubTotal.configure(state = DISABLED)

lblTotalCost = Label(Cost_F,font=('times',14,"bold italic"),text="Total Cost",bg='#312113', fg='#FFD700')
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost = Entry(Cost_F,font=('times',14),textvariable=TotalCost,bd=7,bg="white",insertwidth=2,justify=RIGHT)
txtTotalCost.grid(row=2,column=3)
txtTotalCost.configure(state = DISABLED)
#==============================================================RECEIPT===================================================================#
txtReceipt = Text(Receipt_F, width=46,height=12,bg="white",bd=4,font=('times',13))
txtReceipt.grid(row=0,column=0)
#==============================================================BUTTONS====================================================================#
btnTotal = Button(Buttons_F,padx=15,pady=1,fg="#FFD700",font=('times',15,'bold'),width=4,text="Total",bg="#81613C",command = CostofItem).grid(row=0,column=0)
btnReceipt = Button(Buttons_F,padx=15,pady=1,fg="#FFD700",font=('times',15,'bold'),width=4,text="Receipt",bg="#81613C",command = Receipt).grid(row=0,column=1)
btnReset = Button(Buttons_F,padx=15,pady=1,fg="#FFD700",font=('times',15,'bold'),width=4,text="Reset",bg="#81613C",command=Reset).grid(row=0,column=2)
btnExit = Button(Buttons_F,padx=15,pady=1,fg="#FFD700",font=('times',15,'bold'),width=4,text="Exit",bg="#81613C",command=iExit).grid(row=0,column=3)
#============================================================CALCULATOR DISPLAY===========================================================#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def btnClear():
    global operator
    operator=""
    text_Input.set("")
def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
txtDisplay = Entry(Cal_F, width=45,bg="white",bd=4,font=('Vrinda',12,'bold'),textvariable=text_Input,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
txtDisplay.configure(state = DISABLED)
#========================================================================Calculator Buttons=========================================================================#
btn7=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="7", bg="#81613C",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="8", bg="#81613C",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="9", bg="#81613C",command=lambda:btnClick(9)).grid(row=2,column=2)
btnAddition=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="+", bg="#654321",command=lambda:btnClick("+")).grid(row=2,column=3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
btn4=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="4", bg="#81613C",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="5", bg="#81613C",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="6", bg="#81613C",command=lambda:btnClick(6)).grid(row=3,column=2)
btnSubstraction=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="-", bg="#654321",command=lambda:btnClick("-")).grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
btn1=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="1", bg="#81613C",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="2", bg="#81613C",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="3", bg="#81613C",command=lambda:btnClick(3)).grid(row=4,column=2)
btnMultiply=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="x", bg="#654321",command=lambda:btnClick("*")).grid(row=4,column=3)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
btn0=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="0", bg="#81613C",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="C", bg="#654321",command=btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="=", bg="#654321",command=btnEquals).grid(row=5,column=2)
btnDivision=Button(Cal_F,padx=16, pady=1,fg="#FFD700", font=('times',19,'bold'),width=4,text="/", bg="#654321",command=lambda:btnClick("/")).grid(row=5,column=3)
#=============================================================================================================================================================================#
root.mainloop()
