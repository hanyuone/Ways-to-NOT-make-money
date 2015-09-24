from Tkinter import *
import math
import time

master = Tk()
master.title("Ways To NOT Earn Money")

#VARIABLES
upgcheck1 = int(0)
upgcheck2 = int(0)
upgcheck3 = int(0)
clickupgcheck1 = int(0)
inc = int(1)
inctkinter = StringVar()
inctkinter.set("+" + str(inc) + " money!")
money = int(0)
moneytkinter = StringVar()
moneytkinter.set("Balance: $" + str(money))
autoclick = int(0)
autoclick2 = int(0)
autoclicktkinter = StringVar()
autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick2*10)))
autoprice = int(20*(math.pow(1.1,int(autoclick2*10))))
autopricetkinter = StringVar()
autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
printmoney = int(0)
printmoney2 = int(0)
printmoneytkinter = StringVar()
printmoneytkinter.set("Money Printers Amount: " + str(int(float(printmoney2*10)/15)))
printprice = int(275*(math.pow(1.1,int(printmoney2*10))))
printpricetkinter = StringVar()
printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
counterfeit = int(0)
counterfeit2 = int(0)
counterfeittkinter = StringVar()
counterfeittkinter.set("Counterfeit Companies Amount: " + str(int(float(counterfeit2*10)/221)))
counterfeitprice = int(9001*(math.pow(1.1,int(counterfeit2*10))))
counterfeitpricetkinter = StringVar()
counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
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
        upgcheck1 = upgcheck1 + 1
        boostbutton1.destroy()
        boostbutton2.grid(row=2, column=4, sticky=E)

def deduction1():
    global money, autoclick, autoclick2, autoprice, counterfeit, printmoney, mps
    if money < int(autoprice):
        print("You cannot afford this.")
    elif money >= int(autoprice):
        money = money - int(autoprice)
        autoclick = autoclick + 0.1
        autoclick2 = autoclick2 + 0.1
        mps = mps + 1
        mpstkinter.set("MPS: " + str(mps))
        autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick2*10)))
        autoprice = int(20*(math.pow(1.1,int(autoclick2*10))))
        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
        if autoclick == 0.1 and counterfeit == 0 and printmoney == 0:
            automoney()

#MONEY PRINTER
def boostauto2():
    global money, printmoney, printmoney2, upgcheck2
    if money < 100000 or printmoney2 == 0:
        print("You do not meet the requirements.")
    elif money >= 100000 and printmoney2 > 0:
        money = money - 100000
        autoclick = int(printmoney*30)/10
        upgcheck2 = upgcheck2 + 1
        boostbutton2.destroy()

def deduction2():
    global money, printmoney, printmoney2, printprice, mps, counterfeit
    if money < int(printprice):
        print("You cannot afford this.")
    elif money >= int(printprice):
        money = money - int(printprice)
        printmoney = printmoney + 1.5
        printmoney2 = printmoney2 + 1.5
        mps = mps + 15
        mpstkinter.set("MPS: " + str(mps))
        printmoneytkinter.set("Money Printers Amount: " + str(int(float(printmoney2*10)/15)))
        printprice = int(275*(math.pow(1.1,float(int(printmoney2*10)/15))))
        printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
        if printmoney == 0.75 and counterfeit == 0 and autoclick == 0:
            automoney()

#COUNTERFEIT COMPANY
def boostauto3():
    global money, counterfeit, counterfeit2, upgcheck3
    if money < 2133748 or counterfeit2 == 0:
        print("You do not meet the requirements.")
    elif money >= 2133748 and counterfeit2 > 0:
        money = money - 2133748
        counterfeit = int(counterfeit*30)/10
        upgcheck3 = upgcheck3 + 1
        boostbutton3.destroy()

def deduction3():
    global money, countefeit, counterfeit2, countefeitprice, printmoney, automoney, mps
    if money < int(autoprice):
        print("You cannot afford this.")
    elif money >= int(autoprice):
        money = money - int(autoprice)
        counterfeit = counterfeit + 22.1
        counterfeit2 = counterfeit2 + 22.1
        mps = mps + 221
        mpstkinter.set("MPS: " + str(mps))
        counterfeittkinter.set("Auto-Clickers Amount: " + str(int(float(counterfeit2*10)/221)))
        counterfeitprice = int(20*(math.pow(1.1,int(countefeit2*10))))
        counterfeitpricetkinter.set("Auto-Clicker (Costs: $" + str(counterfeit) + ")")
        if counterfeit == 22.1 and printmoney == 0 and automoney == 0:
            automoney()
        
#CLICKS
def collectmoney():
    global inc, money
    money = money + inc
    moneytkinter.set("Balance: $" + str(money))

def clickboost1():
    global money, inc, clickupgcheck1
    if money < 2000:
        print("You cannot afford this.")
    elif money >= 2000:
        money = money - 2000
        inc = inc + 2
        inctkinter.set("+" + str(inc) + " money!")
        clickupgcheck1 = clickupgcheck1 + 1
        clickboost1.destroy()
        boostbutton1.grid(row=1, column=4, sticky=E)
        boostbutton2.grid(row=2, column=4, sticky=E)

#AUTOMATIC MONEY
def automoney():
    global money, automoney, autoprice, autoclick, printmoney, printprice, counterfeit, counterfeitprice
    money = money + (autoclick + printmoney + counterfeit)
    round(money, 2)
    while mps > 10*(autoclick + printmoney + counterfeit):
        if mps - 221 >= 10*(autoclick + printmoney + counterfeit):
            counterfeit = counterfeit + 22.1
            counterfeittkinter.set("Counterfeit Companies Amount: " + str(int(float(counterfeit2*10)/221)))
            counterfeitprice = int(9001*math.pow(1.1,float(int(counterfeitprice*10)/221)))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
            continue
        elif mps - 221 < 10*(autoclick + printmoney + counterfeit) and mps - 15 >= 10*(autoclick + printmoney + counterfeit):
            printmoney = printmoney + 1.5        
            printmoneytkinter.set("Money Printers Amount: " + str(int(float(printmoney2*10)/15)))
            printprice = int(275*(math.pow(1.1,float(int(printmoney2*10)/15))))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        elif mps - 15 < 10*(autoclick + printmoney):
            for a in range(int((10*(autoclick + printmoney + counterfeit))), mps):
                autoclick = autoclick + 0.1
                autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick2*10)))
                autoprice = int(20*(math.pow(1.1,int(autoclick2*10))))
                autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
            continue
    moneytkinter.set("Balance: $" + str(money))
    master.after(100, automoney)

#SAVING GAME
def savegame():
    x = ["auto", int(float(autoclick2)*10), "print", int(float(int(printmoney2*10))/15), "counter", int(float(int(counterfeit2))/221), \
         "upg1", int(upgcheck1), "upg2", int(upgcheck2), "upg3", int(upgcheck3), "cupg1", int(clickupgcheck1), "money", int(money)]
    savefile = (str("_".join(str(v) for v in x))).encode("hex")
    f = open("savefile.txt", "w")
    f.write(str(savefile))
    f.close()
    toplevel1 = Toplevel()
    msg = Message(toplevel1, text="Game saved!")
    
#SAVE IMPORTS
g = open("savefile.txt")
g2 = str(g.read())
g2 = (g2.decode("hex")).split("_")
money = int(g2[15])
moneytkinter.set("Balance: $" + str(money))
autoclick = int((int(float(g2[1])/10)*int(2*g2[7])) + int(float(g2[1])/10))
autoclick2 = int(float(g2[1])/10)
autoclicktkinter.set("Auto-Clickers Amount: " + str(int(g2[1])))
autoprice = int(20*(math.pow(1.1,int(g2[1]))))
autopricetkinter.set("Auto-Clicker (Costs: $" + str(int(20*(math.pow(1.1,int(g2[1]))))) + ")")
printmoney = int((int(float(g2[3])/10)*int((2*g2[9]))) + int(float(g2[3])/10))
printmoney2 = int(float(g2[3])/10)
printmoneytkinter.set("Money Printers Amount: " + str(int(float(g2[3])/15)))
printprice = int(275*(math.pow(1.1,int(g2[3]))))
printpricetkinter.set("Money Printer (Costs: $" + str(int(275*(math.pow(1.1,int(g2[3]))))) + ")")
counterfeit = int((int(float(g2[5])/10)*int((2*g2[11]))) + int(float(g2[5])/10))
counterfeit2 = int(float(g2[5])/10)
counterfeittkinter.set("Counterfeit Companies Amount: " + str(int(float(g2[5])/221)))
counterfeitprice = int(9001*(math.pow(1.1,int(g2[5]*10))))
counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(int(9001*(math.pow(1.1,int(g2[5]*10))))) + ")")
inc = int(1 + (int(g2[13])*2))
inctkinter.set("+" + str(int(1 + int(g2[13])*2)) + " money!")
mps = int(float(int(g2[1] + g2[3] + g2[5]))/100)
mpstkinter.set("MPS: " + str(int(float(int(g2[1] + g2[3] + g2[5]))/100)))
automoney()

#BUTTONS, LABELS AND ENTRIES
checklabel1 = Label(master, textvariable=moneytkinter)
checklabel1.grid(row=0, column=0, sticky=W)

mpslabel = Label(master, textvariable=mpstkinter)
mpslabel.grid(row=0, column=4, sticky=E)

placeholder1 = Label(master, text="", width=3)
placeholder1.grid(row=1, column=1)

placeholder2 = Label(master, text="", width=3)
placeholder2.grid(row=1, column=3)

clickbutton = Button(master, textvariable=inctkinter, height=3, command=collectmoney)
clickbutton.grid(row=1, column=2, rowspan=4)

incbutton1 = Button(master, textvariable=autopricetkinter, width=35, command=deduction1)
incbutton1.grid(row=1, column=0, sticky=W)

checklabel2 = Label(master, textvariable=autoclicktkinter, width=35)
checklabel2.grid(row=2, column=0, sticky=W)

incbutton2 = Button(master, textvariable=printpricetkinter, width=35, command=deduction2)
incbutton2.grid(row=3, column=0, sticky=W)

checklabel3 = Label(master, textvariable=printmoneytkinter, width=35)
checklabel3.grid(row=4, column=0, sticky=W)

incbutton3 = Button(master, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
incbutton3.grid(row=5, column=0, sticky=W)

checklabel4 = Label(master, textvariable=counterfeittkinter, width=35)   
checklabel4.grid(row=6, column=0, sticky=W)

clickbooster1 = Button(master, text="Click Boost (Costs: $2000)", width=35, command=clickboost1)
clickbooster1.grid(row=1, column=4, sticky=E)

boostbutton1 = Button(master, text="Auto Clicker Boost (Costs: $5000)", width=35, command=boostauto1)
boostbutton1.grid(row=2, column=4, sticky=E)

boostbutton2 = Button(master, text="Money Printer Boost (Costs: $100000)", width=35, command=boostauto2)
boostbutton2.grid(row=3, column=4, sticky=E)

boostbutton3 = Button(master, text="Counterfeit Company Boost (Costs: $2133748)", width=35, command=boostauto3)
boostbutton3.grid(row=4, column=4, sticky=E)

savebutton = Button(master, text="Save game", width=10, command=savegame)
savebutton.grid(row=5, column=4, sticky=E)

mainloop()
