from Tkinter import *
import math
import time

master = Tk()
master.title("Money Sim")

#VARIABLES
n = int(0)
inc = int(1)
inctkinter = StringVar()
inctkinter.set("+" + str(inc) + " money!")
money = int(0)
moneytkinter = StringVar()
moneytkinter.set("Balance: $" + str(money))
autoclick = int(0)
autoclicktkinter = StringVar()
autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick*10)))
autoclick2 = int(0)
autoprice = int(20*(math.pow(1.25,int(autoclick2*10))))
autopricetkinter = StringVar()
autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
printmoney = int(0)
printmoneytkinter = StringVar()
printmoneytkinter.set("Money Printers Amount: " + str(int(printmoney*10)))
printmoney2 = int(0)
printprice = int(250*(math.pow(1.25,int(printmoney2*10))))
printpricetkinter = StringVar()
printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
mps = int(0)
mpstkinter = StringVar()
mpstkinter.set("MPS: " + str(mps))

#AUTO CLICKER
def boostauto1():
    global money, autoclick, autoclick2
    if money < 5000 or autoclick2 == 0:
        print("You do not meet the requirements.")
    elif money >= 5000 and autoclick2 > 0:
        money = money - 5000
        autoclick = int(autoclick*30)/10
        boostbutton1.destroy()

def deduction1():
    global money, autoclick, autoclick2, autoprice, mps
    if money < int(autoprice):
        print("You cannot afford this.")
    elif money >= int(autoprice):
        money = money - int(autoprice)
        autoclick = autoclick + 0.1
        autoclick2 = autoclick2 + 0.1
        mps = mps + 1
        mpstkinter.set("MPS: " + str(mps))
        autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick2*10)))
        autoprice = int(20*(math.pow(1.25,int(autoclick2*10))))
        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
        if autoclick == 0.1:
            automoney1()

def automoney1():
    global money, automoney, autoprice, autoclick
    money = money + autoclick
    moneytkinter.set("Balance: $" + str(money))
    master.after(100, automoney1)

#MONEY PRINTER
def boostauto2():
    global money, printmoney, printmoney2
    if money < 100000 or printmoney2 == 0:
        print("You do not meet the requirements.")
    elif money >= 100000 and printmoney2 > 0:
        money = money - 100000
        autoclick = int(printmoney*30)/10
        boostbutton2.destroy()

def deduction2():
    global money, printmoney, printmoney2, printprice, mps
    if money < int(printprice):
        print("You cannot afford this.")
    elif money >= int(printprice):
        money = money - int(printprice)
        printmoney = printmoney + 1.5
        printmoney2 = printmoney2 + 1.5
        mps = mps + 15
        mpstkinter.set("MPS: " + str(mps))
        printmoneytkinter.set("Money Printers Amount: " + str(int(float(int(printmoney2*10)/15))))
        printprice = int(250*(math.pow(1.25,float(int(printmoney2*10)/15))))
        printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
        if printmoney == 1.5:
            automoney2()

def automoney2():
    global money, printmoney
    money = money + printmoney
    moneytkinter.set("Balance: $" + str(money))
    master.after(100, automoney2)
        
#CLICKS
def collectmoney():
    global n, inc, money
    n = n + inc
    money = money + n
    n = n - inc
    moneytkinter.set("Balance: $" + str(money))

def clickboost1():
    global inc
    inc = inc + 2
    inctkinter.set("+" + str(inc) + " money!")
    clickboost1.destroy()

checklabel1 = Label(master, textvariable=moneytkinter)
checklabel1.grid(row=0, sticky=W)
checklabel1.pack()

mpslabel = Label(master, textvariable=mpstkinter)
mpslabel.grid(row=0, sticky=E)
mpslabel.pack()

clickbutton = Button(master, textvariable=inctkinter, command=collectmoney)
clickbutton.grid(row=1, column=1)
clickbutton.pack()

incbutton1 = Button(master, textvariable=autopricetkinter, command=deduction1)
incbutton1.grid(row=1, sticky=W)
incbutton1.pack()

checklabel2 = Label(master, textvariable=autoclicktkinter)
checklabel2.grid(row=2, sticky=W)
checklabel2.pack()

incbutton2 = Button(master, textvariable=printpricetkinter, command=deduction2)
incbutton2.grid(row=3, sticky=W)
incbutton2.pack()

checklabel3 = Label(master, textvariable=printmoneytkinter)
checklabel3.grid(row=4, sticky=W)
checklabel3.pack()

clickboost1 = Button(master, text="Click Boost (Costs: $2000)", command=clickboost1)
clickboost1.grid(row=1, sticky=E)
clickboost1.pack()

boostbutton1 = Button(master, text="Auto Clicker Boost (Costs: $5000)", command=boostauto1)
boostbutton1.grid(row=2, sticky=E)
boostbutton1.pack()

boostbutton2 = Button(master, text="Money Printer Boost (Costs: $100000)", command=boostauto2)
boostbutton2.grid(row=3, sticky=E)
boostbutton2.pack()

mainloop()

