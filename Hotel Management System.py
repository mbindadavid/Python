from tkinter import *
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_Input = StringVar()
operator = " "

Tops = Frame(root, width=1600,height = 50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800,height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300,height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

#   >>>>>>>>>>>>>>>>>>>Time<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
localtime=time.asctime(time.localtime(time.time())) #DATE TIME FUNCTION
#   >>>>>>>>>>>>>>>>>>>>>>>Info<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

lblinfo = Label(Tops, font=('arial',50,'bold'),text="Mbinda \n Restaurant System",fg="Steel Blue",bd=10, anchor='w')
lblinfo.grid(row=0,column=0)
lblDateTime = Label(Tops, font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10, anchor='w')
lblDateTime.grid(row=1,column=0)

# >>>>>>>>>>>>>>>>>>>>>>>Calculator<<<<<<<<<<<<<<<<<<<<<<<<<<
def btnClick(numbers):
    global  operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator= " "
    text_Input.set(" ")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set (sumup)
    operator=" "

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF =float(Fries.get())
    CoD =float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChicBurger =float(Chiken_Burger.get())
    CoCheese_Burger =float(Chees_Burger.get())

    CoastofFries = CoF * 0.99
    CoastofDrinks = CoD * 1.00
    CoastofFilet = CoFilet * 2.99
    CoastofBurger = CoBurger * 2.87
    CoastChiken_Burger = CoChicBurger * 2.89
    CostChees_Burger = CoCheese_Burger * 2.69

    CostofMeal = "£", str('%.2f' %  (CoastofFries + CoastofDrinks + CoastofFilet + CoastofBurger
                                     + CoastChiken_Burger + CostChees_Burger))

    PayTax =  ((CoastofFries + CoastofDrinks + CoastofFilet + CoastofBurger
                                     + CoastChiken_Burger + CostChees_Burger) * 0.2)

    TotalCost =  (CoastofFries + CoastofDrinks + CoastofFilet + CoastofBurger
                                     + CoastChiken_Burger + CostChees_Burger )

    Ser_Charge = ((CoastofFries + CoastofDrinks + CoastofFilet + CoastofBurger
                                     + CoastChiken_Burger + CostChees_Burger)/99)

    Service = "£" , str('%.2f' % Ser_Charge)
    OverAllCost =  "£" , str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "£" , str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()

def Reset():
    rand.set(" ")
    Fries.set(" ")
    Burger.set(" ")
    Filet.set(" ")
    SubTotal.set(" ")
    Total.set(" ")
    Drinks.set(" ")
    #Reference.set(" ")
    Tax.set(" ")
    Cost.set(" ")
    Chiken_Burger.set(" ")
    Chees_Burger.set(" ")
    Service_Charge.set(" ")




txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg='powder blue', justify='right')
txtDisplay.grid(columnspan=4)

#=======================================================ROW 2===================================================

btn7=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='+', bg='powder blue', command=lambda: btnClick("+")).grid(row=2,column=3)

  #========================================================ROW 3=====================================================

btn4=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='-', bg='powder blue', command=lambda: btnClick("-")).grid(row=3,column=3)

#=============================================================ROW 4=================================================

btn1=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='*', bg='powder blue', command=lambda: btnClick("*")).grid(row=4,column=3)

#===================================================================ROW 5===========================================

btn0=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='C', bg='powder blue', command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='=', bg='powder blue',command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg='black', font=('arial',20,'bold'),
            text='/', bg='powder blue', command=lambda: btnClick("/")).grid(row=5,column=3)
#=============================================================================================================

#====================================================Restaurent Info 1.===========================================

rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
#TotalCost = StringVar()
Total = StringVar()
Drinks = StringVar()
Reference = StringVar()
#StateTax = StringVar()
Tax = StringVar()
Cost = StringVar()
Chiken_Burger = StringVar()
Chees_Burger = StringVar()
Service_Charge = StringVar()


lblReference = Label(f1, font=('arial',16,'bold'),text="Reference",bd=16, anchor="w")
lblReference.grid(row=0,column=0)
textReference=Entry(f1,font=("arial", 16,'bold'), textvariable=rand, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
textReference.grid(row=0,column=1)

lblFries = Label(f1, font=('arial',16,'bold'),text="Large Fries",bd=16, anchor="w")
lblFries.grid(row=1,column=0)
textFries=Entry(f1,font=("arial", 16,'bold'), textvariable=Fries, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
textFries.grid(row=1,column=1)

lblBurger = Label(f1, font=('arial',16,'bold'),text="Burger Meal",bd=16, anchor="w")
lblBurger.grid(row=2,column=0)
textBurger=Entry(f1,font=("arial", 16,'bold'), textvariable=Burger, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
textBurger.grid(row=2,column=1)

lblFilet = Label(f1, font=('arial',16,'bold'),text="Filet_o_Meal",bd=16, anchor="w")
lblFilet.grid(row=3,column=0)
textFilet=Entry(f1,font=("arial", 16,'bold'), textvariable=Filet, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
textFilet.grid(row=3,column=1)

lblChicken = Label(f1, font=('arial',16,'bold'),text="Chicken Meal",bd=16, anchor="w")
lblChicken.grid(row=4,column=0)
textChicken=Entry(f1,font=("arial", 16,'bold'), textvariable=Chiken_Burger, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
textChicken.grid(row=4,column=1)

lblChees = Label(f1, font=('arial',16,'bold'),text="Chees Meal",bd=16, anchor="w")
lblChees.grid(row=5,column=0)
textChees=Entry(f1,font=("arial", 16,'bold'), textvariable=Chees_Burger, bd=10, insertwidth=4,
                    bg="powder blue", justify = 'right')
textChees.grid(row=5,column=1)


#====================================================Restaurent Info 2.===========================================

lblDrinks = Label(f1, font=('arial',16,'bold'),text="Drinks",bd=16, anchor="w")
lblDrinks.grid(row=0,column=2)
textDrinks=Entry(f1,font=("arial", 16,'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
textDrinks.grid(row=0,column=3)

lblCost = Label(f1, font=('arial',16,'bold'),text="Cost of Meal",bd=16, anchor="w")
lblCost.grid(row=1,column=2)
textCost=Entry(f1,font=("arial", 16,'bold'), textvariable=Cost, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
textCost.grid(row=1,column=3)

lblService = Label(f1, font=('arial',16,'bold'),text="Services Charge",bd=16, anchor="w")
lblService.grid(row=2,column=2)
textService=Entry(f1,font=("arial", 16,'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
textService.grid(row=2,column=3)

lblStateTax = Label(f1, font=('arial',16,'bold'),text="State Tax",bd=16, anchor="w")
lblStateTax.grid(row=3,column=2)
textTax=Entry(f1,font=("arial", 16,'bold'), textvariable=Tax, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
textTax.grid(row=3,column=3)

lblSubTotal = Label(f1, font=('arial',16,'bold'),text="Sub Total",bd=16, anchor="w")
lblSubTotal.grid(row=4,column=2)
textSubTotal=Entry(f1,font=("arial", 16,'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
textSubTotal.grid(row=4,column=3)

lblCost = Label(f1, font=('arial',16,'bold'),text="Total Cost",bd=16, anchor="w")
lblCost.grid(row=5,column=2)
textCost=Entry(f1,font=("arial", 16,'bold'), textvariable=Cost, bd=10, insertwidth=4,
                    bg="#ffffff", justify = 'right')
textCost.grid(row=5,column=3)

 #===================================================Buttons=================================================
btnTotal=Button(f1,padx=16,pady=8, bd=16, fg="black",font=("arial", 16,'bold') ,width=10,
                text="Total", bg="powder blue", command = Ref).grid(row=7, column=1)

btnReset=Button(f1,padx=16,pady=8, bd=16, fg="black",font=("arial", 16,'bold') ,width=10,
                text="Reset", bg="powder blue", command = Reset).grid(row=7, column=2)

btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=("arial", 16,'bold') ,width=10,
                text="Exit", bg="powder blue", command = qExit).grid(row=7, column=3)



root.mainloop()

