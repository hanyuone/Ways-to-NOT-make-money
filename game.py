from Tkinter import *
import math

master = Tk()
master.title("Ways To NOT Earn Money")

#AUTO CLICKER
def boostauto1():
    global money, autoclick, autoclick2, upgcheck1
    if money < 5000 or autoclick2 == 0:
        toplevel = Toplevel()
        cannotafford1 = Message(toplevel, text="You do not meet the requirements.")
        cannotafford1.pack()
    elif money >= 5000 and autoclick2 > 0:
        money = money - 5000
        autoclick = int(autoclick*30)/10
        upgcheck1 = upgcheck1 + 1
        boostbutton1.destroy()
        boostbutton2.grid(row=int(3 - (int(upgcheck1) + int(clickupgcheck1))), column=4, sticky=E)
        clickbooster2.grid(row=int(4 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1))), column=4, sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1) + int(clickupgcheck2))), column=4, sticky=E)
def deduction1():
    global money, autoclick, autoclick2, autoprice, counterfeit, printmoney, mps
    if money < int(autoprice):
        print("You cannot afford this.")
    elif money >= int(autoprice):
        money = money - int(autoprice)
        autoclick = autoclick + 0.1*(1 + upgcheck1*2)
        autoclick2 = autoclick2 + 0.1
        mps = mps + 1
        mpstkinter.set("MPS: " + str(mps))
        autoclicktkinter.set("Auto-Clickers Amount: " + str(int(autoclick2*10)))
        autoprice = int(20*(math.pow(1.25,int(autoclick2*10))))
        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
        if autoclick == 0.1 and counterfeit == 0 and printmoney == 0:
            automoney()

#MONEY PRINTER
def boostauto2():
    global money, printmoney, printmoney2, upgcheck2
    if money < 100000 or printmoney2 == 0:
        toplevel = Toplevel()
        cannotafford2 = Message(toplevel, text="You do not meet the requirements.")
        cannotafford2.pack()
    elif money >= 100000 and printmoney2 > 0:
        money = money - 100000
        autoclick = int(printmoney*30)/10
        upgcheck2 = upgcheck2 + 1
        boostbutton2.destroy()
        clickbooster2.grid(row=int(4 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1))), column=4, sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1) + int(clickupgcheck2))), column=4, sticky=E)
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
        printprice = int(275*(math.pow(1.25,float(int(printmoney2*10)/15))))
        printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
        if printmoney == 1.5 and counterfeit == 0 and autoclick == 0:
            automoney()

#COUNTERFEIT COMPANY
def boostauto3():
    global money, counterfeit, counterfeit2, upgcheck3
    if money < 2133748 or counterfeit2 == 0:
        toplevel = Toplevel()
        cannotafford3 = Message(toplevel, text="You do not meet the requirements.")
        cannotafford3.pack()
    elif money >= 2133748 and counterfeit2 > 0:
        money = money - 2133748
        counterfeit = int(counterfeit*30)/10
        upgcheck3 = upgcheck3 + 1
        boostbutton3.destroy()
def deduction3():
    global money, counterfeit, counterfeit2, counterfeitprice, printmoney, automoney, mps
    if money < int(autoprice):
        print("You cannot afford this.")
    elif money >= int(autoprice):
        money = money - int(autoprice)
        counterfeit = counterfeit + 22.1
        counterfeit2 = counterfeit2 + 22.1
        mps = mps + 221
        mpstkinter.set("MPS: " + str(mps))
        counterfeittkinter.set("Counterfeit Companies Amount: " + str(int(float(counterfeit2*10)/221)))
        counterfeitprice = int(9001*(math.pow(1.25,float(int(counterfeit2*10)/221))))
        counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
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
        toplevel = Toplevel()
        cannotafford4 = Message(toplevel, text="You do not meet the requirements.")
        cannotafford4.pack()
    elif money >= 2000:
        money = money - 2000
        inc = inc + 2
        inctkinter.set("+" + str(inc) + " money!")
        clickupgcheck1 = clickupgcheck1 + 1
        clickbooster1.destroy()
        boostbutton1.grid(row=int(2 - int(clickupgcheck1)), column=4, sticky=E)
        boostbutton2.grid(row=int(3 - (int(upgcheck1) + int(clickupgcheck1))), column=4, sticky=E)
        clickbooster2.grid(row=int(4 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1))), column=4, sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1) + int(clickupgcheck2))), column=4, sticky=E)
def clickboost2():
    global money, inc, mps, clickupgcheck2
    if money < 200000 or clickupgcheck1 == int(0):
        toplevel = Toplevel()
        cannotafford5 = Message(toplevel, text="You do not meet the requirements.")
        cannotafford5.pack()
    elif money >= 200000 and clickupgcheck1 == int(1):
        money = money - 200000
        inc = int(inc*(math.pow(1.01, mps)))
        inctkinter.set("+" + str(inc) + " money!")
        clickupgcheck2 = clickupgcheck2 + 1
        clickbooster2.destroy()
        boostbutton3.grid(row=int(5 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1) + int(clickupgcheck2))), column=4, sticky=E)

#AUTOMATIC MONEY
def automoney():
    global money, autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, counterfeitprice, mps
    #BUG FIXER
    while mps > 10*(autoclick + printmoney + counterfeit):
        if mps - 221 >= 10*(autoclick + printmoney + counterfeit):
            counterfeit = counterfeit + 22.1*(1 + upgcheck3*2)
            counterfeit2 = counterfeit2 + 22.1
            counterfeittkinter.set("Counterfeit Companies Amount: " + str(int(float(counterfeit2*10)/221)))
            counterfeitprice = int(9001*(math.pow(1.25,int(float(counterfeit2*10)/221))))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
            continue
        elif mps - 15 >= 10*(autoclick + printmoney + counterfeit):
            printmoney = printmoney + 1.5*(1 + upgcheck2*2)
            printmoney2 = printmoney2 + 1.5
            printmoneytkinter.set("Money Printers Amount: " + str(int(float(printmoney2*10)/15)))
            printprice = int(275*(math.pow(1.25,int(float(printmoney2*10)/15))))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        else:
            autoclick = autoclick + 0.1*(1 + upgcheck1*2)
            autoclick2 = autoclick2 + 0.1
            autoclicktkinter.set("Money Printers Amount: " + str(int(autoclick2*10)))
            autoprice = int(275*(math.pow(1.25,int(autoclick2*10))))
            autopricetkinter.set("Money Printer (Costs: $" + str(autoprice) + ")")
            continue
    moneytkinter.set("Balance: $" + str(money))
    money = money + float(mps)/10
    master.after(100, automoney)

#SAVING GAME
def savegame():
    x = ["auto", int(float(autoclick2)*10), "print", int(float(int(printmoney2*10))/15), "counter", int(float(int(counterfeit2*10))/221), \
         "upg1", int(upgcheck1), "upg2", int(upgcheck2), "upg3", int(upgcheck3), "cupg1", int(clickupgcheck1), "cupg2", int(clickupgcheck2), "money", int(money)]
    savefile = (str("_".join(str(v) for v in x))).encode("hex")
    f = open("savefile.txt", "w")
    f.write(str(savefile))
    f.close()
    toplevel = Toplevel()
    msg = Message(toplevel, text="Game saved!")
    msg.pack()

#SAVE IMPORTS AND VARIABLES
g = open("savefile.txt")
g2 = str(g.read())
g2 = (g2.decode("hex")).split("_")
upgcheck1 = int(g2[7])
upgcheck2 = int(g2[9])
upgcheck3 = int(g2[11])
clickupgcheck1 = int(g2[13])
money = int(g2[17])
moneytkinter = StringVar()
moneytkinter.set("Balance: $" + str(money))
autoclick = ((float(g2[1])/10)*int(2*g2[7])) + (float(g2[1])/10)
autoclick2 = float(g2[1])/10
autoclicktkinter = StringVar()
autoclicktkinter.set("Auto-Clickers Amount: " + str(g2[1]))
autoprice = int(20*(math.pow(1.25,int(g2[1]))))
autopricetkinter = StringVar()
autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
printmoney = (float(int(g2[3])*15)/10)*int((2*g2[9])) + (float(int(g2[3])*15)/10)
printmoney2 = float(int(g2[3])*15)/10
printmoneytkinter = StringVar()
printmoneytkinter.set("Money Printers Amount: " + str(g2[3]))
printprice = int(275*(math.pow(1.25,int(g2[3]))))
printpricetkinter = StringVar()
printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
counterfeit = (float(int(g2[5])*221)/10)*int((2*g2[11])) + (float(int(g2[5])*221)/10)
counterfeit2 = int(float(int(g2[5])*221)/10)
counterfeittkinter = StringVar()
counterfeittkinter.set("Counterfeit Companies Amount: " + str(g2[5]))
counterfeitprice = int(9001*(math.pow(1.25,int(g2[5]*10))))
counterfeitpricetkinter = StringVar()
counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
inc = int(1 + (int(g2[13])*2))
inctkinter = StringVar()
inctkinter.set("+" + str(inc) + " money!")
mps = int(g2[1]) + 15*int(g2[3]) + 221*int(g2[5])
mpstkinter = StringVar()
mpstkinter.set("MPS: " + str(mps))
if g2[13] == int(0):
    clickbooster1.grid(row=1, column=4, sticky=E)
if g2[7] == int(0):
    boostbutton1.grid(row=int(2 - int(clickupgcheck1)), column=4, sticky=E)
if g2[9] == int(0):
    boostbutton2.grid(row=int(3 - (int(upgcheck1) + int(clickupgcheck1))), column=4, sticky=E)
if g2[15] == int(0):
    clickbooster2.grid(row=int(4 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1))), column=4, sticky=E)
if g2[11] == int(0):    
    boostbutton3.grid(row=int(5 - (int(upgcheck1) + int(upgcheck2) + int(clickupgcheck1) + int(clickupgcheck2))), column=4, sticky=E)   
automoney()

#BUTTONS, LABELS AND ENTRIES
moneylabel = Label(master, textvariable=moneytkinter)
moneylabel.grid(row=0, column=0, sticky=W)

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

checklabel1 = Label(master, textvariable=autoclicktkinter, width=35)
checklabel1.grid(row=2, column=0, sticky=W)

incbutton2 = Button(master, textvariable=printpricetkinter, width=35, command=deduction2)
incbutton2.grid(row=3, column=0, sticky=W)

checklabel2 = Label(master, textvariable=printmoneytkinter, width=35)
checklabel2.grid(row=4, column=0, sticky=W)

incbutton3 = Button(master, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
incbutton3.grid(row=5, column=0, sticky=W)

checklabel3 = Label(master, textvariable=counterfeittkinter, width=35)   
checklabel3.grid(row=6, column=0, sticky=W)

clickbooster1 = Button(master, text="Click Boost (Costs: $2000)", width=35, command=clickboost1)
clickbooster1.grid(row=1, column=4, sticky=E)

boostbutton1 = Button(master, text="Auto Clicker Boost (Costs: $5000)", width=35, command=boostauto1)
boostbutton1.grid(row=2, column=4, sticky=E)

boostbutton2 = Button(master, text="Money Printer Boost (Costs: $100000)", width=35, command=boostauto2)
boostbutton2.grid(row=3, column=4, sticky=E)

clickbooster2 = Button(master, text="Better Click Boost (Costs: $200000)", width=35, command=clickboost2)
clickbooster2.grid(row=4, column=4, sticky=E)

boostbutton3 = Button(master, text="Counterfeit Company Boost (Costs: $2133748)", width=35, command=boostauto3)
boostbutton3.grid(row=5, column=4, sticky=E)

savebutton = Button(master, text="Save game", width=10, command=savegame)
savebutton.grid(row=6, column=4, sticky=E)

mainloop()
