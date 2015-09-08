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
    global money, automoney, autoprice, autoclick, printmoney
    money = money + autoclick
    round(money, 2)
    while mps > 10*(autoclick + printmoney):
        if mps - 15 >= 10*(autoclick + printmoney):
            printmoney = printmoney + 1        
            printmoneytkinter.set("Money Printers Amount: " + str(int(float(int(printmoney2*10)/15))))
            printprice = int(275*(math.pow(1.25,float(int(printmoney2*10)/15))))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        elif mps - 15 < 10*(autoclick + printmoney):
            for a in range(int((10*(autoclick + printmoney))), mps):
                autoclick = autoclick + 1
                autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick2*10)))
                autoprice = int(20*(math.pow(1.25,int(autoclick2*10))))
                autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
            continue
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
    global money, autoclick, printmoney, printprice
    money = money + printmoney
    round(money, 2)
    while mps > 10*(autoclick + printmoney):
        if mps - 15 >= 10*(autoclick + printmoney):
            printmoney = printmoney + 1        
            printmoneytkinter.set("Money Printers Amount: " + str(int(float(int(printmoney2*10)/15))))
            printprice = int(275*(math.pow(1.25,float(int(printmoney2*10)/15))))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        elif mps - 15 < 10*(autoclick + printmoney):
            for a in range(int((10*(autoclick + printmoney))), mps):
                autoclick = autoclick + 1
                autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick2*10)))
                autoprice = int(20*(math.pow(1.25,int(autoclick2*10))))
                autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
            continue
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

#BUTTONS AND LABELS (WIDGETS)
checklabel1 = Label(master, textvariable=moneytkinter)
checklabel1.grid(row=0, column=0, sticky=W)

mpslabel = Label(master, textvariable=mpstkinter)
mpslabel.grid(row=0, column=2, sticky=E)

clickbutton = Button(master, textvariable=inctkinter, command=collectmoney)
clickbutton.grid(row=1, column=1, rowspan=2)

placeholder1 = Label(master, text='', width=3)
placeholder1.grid(row=1, column=1)

placeholder2 = Label(master, text='', width=3)
placeholder2.grid(row=1, column=3)

incbutton1 = Button(master, textvariable=autopricetkinter, width=29, command=deduction1)
incbutton1.grid(row=1, column=0, sticky=W)

checklabel2 = Label(master, textvariable=autoclicktkinter, width=29)
checklabel2.grid(row=2, column=0, sticky=W)

incbutton2 = Button(master, textvariable=printpricetkinter, width=29, command=deduction2)
incbutton2.grid(row=3, column=0, sticky=W)

checklabel3 = Label(master, textvariable=printmoneytkinter, width=29)
checklabel3.grid(row=4, column=0, sticky=W)

clickboost1 = Button(master, text="Click Boost (Costs: $2000)", width=29, command=clickboost1)
clickboost1.grid(row=1, column=2, sticky=E)

boostbutton1 = Button(master, text="Auto Clicker Boost (Costs: $5000)", width=29, command=boostauto1)
boostbutton1.grid(row=2, column=2, sticky=E)

boostbutton2 = Button(master, text="Money Printer Boost (Costs: $100000)", width=29, command=boostauto2)
boostbutton2.grid(row=3, column=2, sticky=E)

mainloop()
