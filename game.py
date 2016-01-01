from Tkinter import *
from random import *
from tkMessageBox import showerror
import math
import glob
import time as _time

master = Tk()
master.title("Ways To NOT Earn Money")
img1 = PhotoImage(file="img1.gif")
gold = PhotoImage(file="gold.gif")
Animation1 = PhotoImage(file="Animation1.gif")
Animation2 = PhotoImage(file="Animation2.gif")
Animation3 = PhotoImage(file="Animation3.gif")
norequirements = "You do not meet the requirements."
cannotafford = "You cannot afford this."


# BUG FIXER
def bugfixer():
    global sharecrash, sharecrash2, shareprice, counterfeit, counterfeit2, counterfeitprice, printmoney, printmoney2, \
        printprice, autoclick, autoclick2, autoprice
    while mps > (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
        if mps - 969 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            sharecrash += (1 + upgcheck4 * 2)
            sharecrash2 += 1
            sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
            shareprice = int(42000 * (math.pow(1.2, sharecrash2)))
            sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
            continue
        elif mps - 321 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            counterfeit += (1 + upgcheck3 * 2)
            counterfeit2 += 1
            counterfeittkinter.set("Counterfeit Companies Amount: " + str(counterfeit2))
            counterfeitprice = int(9001 * (math.pow(1.2, counterfeit2)))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
            continue
        elif mps - 15 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            printmoney += (1 + upgcheck2h1 * 2 + upgcheck2h2 * 18)
            printmoney2 += 1
            printmoneytkinter.set("Money Printers Amount: " + str(printmoney2))
            printprice = int(375 * (math.pow(1.2, printmoney2)))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        else:
            autoclick += (1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
            autoclick2 += 1
            autoclicktkinter.set("Money Printers Amount: " + str(autoclick2))
            autoprice = int(20 * (math.pow(1.2, autoclick2)))
            autopricetkinter.set("Money Printer (Costs: $" + str(autoprice) + ")")
            continue


def automoneychoice():
    if len(str(money)) <= 8:
        moneytkinter.set("Balance: $" + str(money))
        master.after(100, automoney)
    elif len(str(money)) <= 11:
        moneytkinter.set("Balance: $" + str(moneymillion) + "m")
        master.after(100, automoney2)
    elif len(str(money)) <= 14:
        moneytkinter.set("Balance: $" + str(moneybillion) + "b")
        master.after(100, automoney3)
    elif len(str(money)) <= 17:
        moneytkinter.set("Balance: $" + str(moneytrillion) + "t")
        master.after(100, automoney4)
    elif len(str(money)) <= 20:
        moneytkinter.set("Balance: $" + str(moneyquadrillion) + "q")
        master.after(100, automoney5)
    else:
        moneytkinter.set("Balance: $" + str(moneyquintillion) + "Q")
        master.after(100, automoney6)


# STATS STUFF
def statsexpand():
    global totalclicks, totalclickslabel, totalclicksvar, time, timevar, timelabel, statscheck, hidestatsbutton
    statsbutton.destroy()
    resetbutton.grid(row=11, column=0, sticky=W)
    savebutton.grid(row=11, column=2, sticky=E)
    statscheck = True
    totalclicksvar = StringVar()
    totalclicksvar.set("Total clicks: " + str(totalclicks))
    totalclickslabel = Label(master, textvariable=totalclicksvar)
    totalclickslabel.grid(row=10, column=0, sticky=W)
    timevar = StringVar()
    timevar.set("Total time: " + str(time))
    timelabel = Label(master, textvariable=timevar)
    timelabel.grid(row=10, column=2, sticky=E)
    hidestatsbutton = Button(master, text="Hide Stats", width=10, command=hidestats)
    hidestatsbutton.grid(row=9, column=0, sticky=W)


def hidestats():
    global statsbutton, statscheck
    statscheck = False
    totalclickslabel.destroy()
    timelabel.destroy()
    hidestatsbutton.destroy()
    resetbutton.grid(row=10, column=0, sticky=W)
    savebutton.grid(row=10, column=2, sticky=E)
    statsbutton = Button(master, text="Stats", width=10, command=statsexpand)
    statsbutton.grid(row=9, column=0, sticky=W)
    if upgbuttoncheck:
        exitupgrades.grid(row=9, column=2, sticky=E)
    elif not upgbuttoncheck:
        pass


# AUTO CLICKER
def boostauto1h1():
    global money, autoclick, autoclick2, upgcheck1h1, mps
    if money < 5000 or autoclick2 == 0:
        global boostafford1h1
        boostbutton1h1.destroy()
        master.bell()
        boostafford1h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=int(2 - int(clickupgcheck1)), column=2, sticky=E)
        master.after(500, norequirements1h1)
    else:
        money -= 5000
        autoclick = int(autoclick * 15) / 10
        upgcheck1h1 += 1
        mps += autoclick2 * 2
        mpstkinter.set("MPS: " + str(mps))
        boostbutton1h1.destroy()
        boostbutton2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
            row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
            sticky=E)
        boostbutton3.grid(row=int(
            6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)
        boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(clickupgcheck1) + int(
                clickupgcheck2))))
        boostbutton4.grid(row=int(8 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(
                clickupgcheck2))), column=2, sticky=E)


def norequirements1h1():
    global boostafford1h1, boostbutton1h1
    boostafford1h1.destroy()
    boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
    boostbutton1h1.grid(row=int(2 - int(clickupgcheck1)), column=2, sticky=E)


def boostauto1h2():
    global money, autoclick, autoclick2, upgcheck1h2, mps
    if money < 555555 or upgcheck1h1 == 0:
        global boostafford1h2
        boostbutton1h2.destroy()
        master.bell()
        boostafford1h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h2.grid(
            row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
            sticky=E)
        master.after(500, norequirements1h2)
    else:
        money -= 555555
        autoclick = int(autoclick * 50) / 10
        upgcheck1h2 += 1
        mps += autoclick2 * 18
        mpstkinter.set("MPS: " + str(mps))
        boostbutton1h2.destroy()
        boostbutton3.grid(row=int(
            6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)
        boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(upgcheck4) + int(
                clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(8 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(
                clickupgcheck2))), column=2, sticky=E)


def norequirements1h2():
    global boostbutton1h2, boostafford1h2
    boostafford1h2.destroy()
    boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35,
                            command=boostauto1h2)
    boostbutton1h2.grid(
            row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)


def deduction1():
    global money, autoclick, autoclick2, autoprice, counterfeit, printmoney, sharecrash, mps, inc
    if money < int(autoprice):
        global incafford1, incbutton1
        incbutton1.destroy()
        master.bell()
        incafford1 = Label(master, text="%s" % cannotafford, width=35)
        incafford1.grid(row=1, column=0, sticky=W)
        master.after(500, cannotafford1)
    else:
        money -= int(autoprice)
        autoclick += (1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
        autoclick2 += 1
        mps += (1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
        mpstkinter.set("MPS: " + str(mps))
        autoclicktkinter.set("Auto-Clickers Amount: " + str(autoclick2))
        autoprice = int(20 * (math.pow(1.2, autoclick2)))
        autopricechoice()
    inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
    if autoclick == 1 and sharecrash == 0 and counterfeit == 0 and printmoney == 0:
        automoney()


def autopricechoice():
    if len(str(autoprice)) <= 8:
        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
    else:
        autopricemillion = round((float(str(autoprice)[:-7])/10), 1)
        if len(str(autoprice)) <= 11:
            autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricemillion) + "m)")
        else:
            autopricebillion = round((float(str(autopricemillion)[:-4])/10), 1)
            if len(str(autoprice)) <= 14:
                autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricebillion) + "b)")
            else:
                autopricetrillion = round((float(str(autopricebillion)[:-4])/10), 1)
                if len(str(autoprice)) <= 17:
                    autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricetrillion) + "t)")
                else:
                    autopricequadrillion = round((float(str(autopricetrillion)[:-4])/10), 1)
                    if len(str(autoprice)) <= 20:
                        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricequadrillion) + "q)")
                    else:
                        autopricequintillion = round((float(str(autopricequadrillion)[:-4])/10), 1)
                        autopricetkinter.set("Auto-Clicker (Costs : $" + str(autopricequintillion) + "Q)")


def cannotafford1():
    global incafford1, incbutton1
    incafford1.destroy()
    incbutton1 = Button(master, textvariable=autopricetkinter, width=35, command=deduction1)
    incbutton1.grid(row=1, column=0, sticky=W)


# MONEY PRINTER
def boostauto2h1():
    global money, printmoney, printmoney2, upgcheck2h1, mps
    if money < 42000 or printmoney2 == 0:
        global boostafford2h1
        boostbutton2h1.destroy()
        master.bell()
        boostafford2h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        master.after(500, norequirements2h1)
    else:
        money -= 42000
        printmoney = int(float(printmoney * 15) / 10)
        upgcheck2h1 += 1
        mps += printmoney2 * 2
        mpstkinter.set("MPS: " + str(mps))
        boostbutton2h1.destroy()
        clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
            row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
            sticky=E)
        boostbutton3.grid(row=int(
            6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)
        boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(upgcheck4) + int(
                clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(8 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(
                clickupgcheck2))), column=2, sticky=E)


def norequirements2h1():
    global boostbutton2h1
    boostafford2h1.destroy()
    boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                            command=boostauto2h1)
    boostbutton2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)


def boostauto2h2():
    global money, printmoney, printmoney2, upgcheck2h2, mps
    if money < 7777777 or upgcheck2h1 == 0:
        global boostafford2h2
        boostbutton2h2.destroy()
        master.bell()
        boostafford2h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
                            sticky=E)
        master.after(500, norequirements2h2)
    else:
        money -= 7777777
        printmoney = int(float(printmoney * 50) / 10)
        upgcheck2h2 += 1
        mps += printmoney2 * 18
        mpstkinter.set("MPS: " + str(mps))
        boostbutton2h2.destroy()
        boostbutton4.grid(row=int(8 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)


def norequirements2h2():
    global boostbutton2h2
    boostafford2h2.destroy()
    boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
    boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(clickupgcheck1) + int(
                clickupgcheck2))), column=2, sticky=E)


def deduction2():
    global money, printmoney, printmoney2, printprice, sharecrash, counterfeit, autoclick, mps, inc
    if money < int(printprice):
        global incafford2, incbutton2
        incbutton2.destroy()
        master.bell()
        incafford2 = Label(master, text="%s" % cannotafford, width=35)
        incafford2.grid(row=3, column=0, sticky=W)
        master.after(500, cannotafford2)
    else:
        money -= int(printprice)
        printmoney += (1 + upgcheck2h1 * 2 + upgcheck2h2 * 18)
        printmoney2 += 1
        mps += 15 * (1 + upgcheck2h1 * 2 + upgcheck2h2 * 18)
        mpstkinter.set("MPS: " + str(mps))
        printmoneytkinter.set("Money Printers Amount: " + str(printmoney2))
        printprice = int(375 * (math.pow(1.2, printmoney2)))
        printpricechoice()
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
        if printmoney == 1 and sharecrash == 0 and counterfeit == 0 and autoclick == 0:
            automoney()


def printpricechoice():
    if len(str(printprice)) <= 8:
        printpricetkinter.set("Auto-Clicker (Costs: $" + str(printprice) + ")")
    else:
        printpricemillion = round((float(str(printprice)[:-7])/10), 1)
        if len(str(printprice)) <= 11:
            printpricetkinter.set("Auto-Clicker (Costs: $" + str(printpricemillion) + "m)")
        else:
            printpricebillion = round((float(str(printpricemillion)[:-4])/10), 1)
            if len(str(printprice)) <= 14:
                printpricetkinter.set("Auto-Clicker (Costs: $" + str(printpricebillion) + "b)")
            else:
                printpricetrillion = round((float(str(printpricebillion)[:-4])/10), 1)
                if len(str(printprice)) <= 17:
                    printpricetkinter.set("Auto-Clicker (Costs: $" + str(printpricetrillion) + "t)")
                else:
                    printpricequadrillion = round((float(str(printpricetrillion)[:-4])/10), 1)
                    if len(str(printprice)) <= 20:
                        printpricetkinter.set("Auto-Clicker (Costs: $" + str(printpricequadrillion) + "q)")
                    else:
                        printpricequintillion = round((float(str(printpricequadrillion)[:-4])/10), 1)
                        printpricetkinter.set("Auto-Clicker (Costs : $" + str(printpricequintillion) + "Q)")


def cannotafford2():
    global incafford2, incbutton2
    incafford2.destroy()
    incbutton2 = Button(master, textvariable=printpricetkinter, width=35, command=deduction2)
    incbutton2.grid(row=3, column=0, sticky=W)


# COUNTERFEIT COMPANY
def boostauto3():
    global money, counterfeit, counterfeit2, upgcheck3, mps
    if money < 2133748 or counterfeit2 == 0:
        global boostafford3
        boostbutton3.destroy()
        master.bell()
        boostafford3 = Label(master, text="%s" % norequirements, width=35)
        boostafford3.grid(row=int(
            6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)
        master.after(500, norequirements3)
    else:
        money -= 2133748
        counterfeit = int(counterfeit * 15) / 10
        mps += counterfeit2 * 2
        mpstkinter.set("MPS: " + str(mps))
        upgcheck3 += 1
        boostbutton3.destroy()
        boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(upgcheck4) + int(
                clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)


def norequirements3():
    global boostbutton3
    boostafford3.destroy()
    boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                          command=boostauto3)
    boostbutton3.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                      int(clickupgcheck2))), column=2, sticky=E)


def deduction3():
    global money, counterfeit, counterfeit2, counterfeitprice, sharecrash, printmoney, autoclick, mps, inc
    if money < int(counterfeitprice):
        global incafford3, incbutton3
        incbutton3.destroy()
        master.bell()
        incafford3 = Label(master, text="%s" % cannotafford, width=35)
        incafford3.grid(row=5, column=0, sticky=W)
        master.after(500, cannotafford3)
    else:
        money -= int(counterfeitprice)
        counterfeit += (1 + upgcheck3 * 2)
        counterfeit2 += 1
        mps += 321 * (1 + upgcheck3 * 2)
        mpstkinter.set("MPS: " + str(mps))
        counterfeittkinter.set("Counterfeit Companies Amount: " + str(counterfeit2))
        counterfeitprice = int(9001 * (math.pow(1.2, counterfeit2)))
        counterfeitpricechoice()
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
        if counterfeit == 1 and sharecrash == 0 and printmoney == 0 and autoclick == 0:
            automoney()


def counterfeitpricechoice():
    if len(str(counterfeitprice)) <= 8:
        counterfeitpricetkinter.set("Auto-Clicker (Costs: $" + str(counterfeitprice) + ")")
    else:
        counterfeitpricemillion = round((float(str(counterfeitprice)[:-7])/10), 1)
        if len(str(counterfeitprice)) <= 11:
            counterfeitpricetkinter.set("Auto-Clicker (Costs: $" + str(counterfeitpricemillion) + "m)")
        else:
            counterfeitpricebillion = round((float(str(counterfeitpricemillion)[:-4])/10), 1)
            if len(str(counterfeitprice)) <= 14:
                counterfeitpricetkinter.set("Auto-Clicker (Costs: $" + str(counterfeitpricebillion) + "b)")
            else:
                counterfeitpricetrillion = round((float(str(counterfeitpricebillion)[:-4])/10), 1)
                if len(str(counterfeitprice)) <= 17:
                    counterfeitpricetkinter.set("Auto-Clicker (Costs: $" + str(counterfeitpricetrillion) + "t)")
                else:
                    counterfeitpricequadrillion = round((float(str(counterfeitpricetrillion)[:-4])/10), 1)
                    if len(str(counterfeitprice)) <= 20:
                        counterfeitpricetkinter.set("Auto-Clicker (Costs: $" + str(counterfeitpricequadrillion) + "q)")
                    else:
                        counterfeitpricequintillion = round((float(str(counterfeitpricequadrillion)[:-4])/10), 1)
                        counterfeitpricetkinter.set("Auto-Clicker (Costs : $" + str(counterfeitpricequintillion) + "Q)")


def cannotafford3():
    global incafford3, incbutton3
    incafford3.destroy()
    incbutton3 = Button(master, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
    incbutton3.grid(row=5, column=0, sticky=W)


# SHAREMARKET CRASH
def boostauto4():
    global money, sharecrash, sharecrash2, upgcheck4, mps
    if money < 12345678 or sharecrash2 == 0:
        global boostafford4
        boostbutton4.destroy()
        master.bell()
        boostafford4 = Label(master, text="%s" % norequirements, width=35)
        boostafford4.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        master.after(500, norequirements4)
    else:
        money -= 12345678
        sharecrash = int(sharecrash * 15) / 10
        mps += sharecrash2 * 2
        mpstkinter.set("MPS: " + str(mps))
        upgcheck4 += 1
        boostbutton4.destroy()


def norequirements4():
    global boostbutton4
    boostafford4.destroy()
    boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                          command=boostauto4)
    boostbutton4.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                   int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)


def deduction4():
    global money, sharecrash, sharecrash2, shareprice, counterfeit, printmoney, autoclick, mps, inc
    if money < int(shareprice):
        global incafford4, incbutton4
        incbutton4.destroy()
        master.bell()
        incafford4 = Label(master, text="%s" % cannotafford, width=35)
        incafford4.grid(row=7, column=0, sticky=W)
        master.after(500, cannotafford4)
    else:
        money -= int(shareprice)
        sharecrash += (1 + upgcheck4 * 2)
        sharecrash2 += 1
        mps += 969 * (1 + upgcheck4 * 2)
        mpstkinter.set("MPS: " + str(mps))
        sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
        shareprice = int(42000 * (math.pow(1.2, sharecrash2)))
        sharepricechoice()
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
        if sharecrash == 1 and counterfeit == 0 and printmoney == 0 and autoclick == 0:
            automoney()


def sharepricechoice():
    if len(str(shareprice)) <= 8:
        sharepricetkinter.set("Auto-Clicker (Costs: $" + str(shareprice) + ")")
    else:
        sharepricemillion = round((float(str(shareprice)[:-7])/10), 1)
        if len(str(shareprice)) <= 11:
            sharepricetkinter.set("Auto-Clicker (Costs: $" + str(sharepricemillion) + "m)")
        else:
            sharepricebillion = round((float(str(sharepricemillion)[:-4])/10), 1)
            if len(str(shareprice)) <= 14:
                sharepricetkinter.set("Auto-Clicker (Costs: $" + str(sharepricebillion) + "b)")
            else:
                sharepricetrillion = round((float(str(sharepricebillion)[:-4])/10), 1)
                if len(str(shareprice)) <= 17:
                    sharepricetkinter.set("Auto-Clicker (Costs: $" + str(sharepricetrillion) + "t)")
                else:
                    sharepricequadrillion = round((float(str(sharepricetrillion)[:-4])/10), 1)
                    if len(str(shareprice)) <= 20:
                        sharepricetkinter.set("Auto-Clicker (Costs: $" + str(sharepricequadrillion) + "q)")
                    else:
                        sharepricequintillion = round((float(str(sharepricequadrillion)[:-4])/10), 1)
                        sharepricetkinter.set("Auto-Clicker (Costs : $" + str(sharepricequintillion) + "Q)")


def cannotafford4():
    global incafford4, incbutton4
    incafford4.destroy()
    incbutton4 = Button(master, textvariable=sharepricetkinter, width=35, command=deduction4)
    incbutton4.grid(row=7, column=0, sticky=W)


# CLICKS
def collectmoney():
    global inc, money, animate, totalclicks
    money += inc
    if moneymillion == 0:
        moneytkinter.set("Balance: $" + str(money))
    else:
        moneytkinter.set("Balance: $" + str(moneymillion) + "m")
    animate += 1
    if animate > 3:
        animate = 1
    animationthingy()
    totalclicks += 1


def clickboost1():
    global money, inc, clickupgcheck1
    if money < 2100:
        global clickafford1
        clickbooster1.destroy()
        clickafford1 = Label(master, text="%s" % norequirements, width=35)
        clickafford1.grid(row=1, column=2, sticky=E)
        master.after(500, norequirementsc1)
    else:
        money -= 2100
        inc += 2
        inctkinter.set("+" + str(inc) + " money!")
        clickupgcheck1 += 1
        clickbooster1.destroy()
        boostbutton1h1.grid(row=int(2 - int(clickupgcheck1)), column=2, sticky=E)
        boostbutton2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
            row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
            sticky=E)
        boostbutton3.grid(row=int(
            6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)
        boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(upgcheck4) + int(
                clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(8 -
                                  (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(
                                      upgcheck3) + int(clickupgcheck1) + int(
                                      clickupgcheck2))), column=2, sticky=E)


def norequirementsc1():
    global clickbooster1
    clickafford1.destroy()
    clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
    clickbooster1.grid(row=1, column=2, sticky=E)


def clickboost2():
    global money, inc, mps, clickupgcheck2
    if money < 200000 or clickupgcheck1 == int(0):
        global clickafford2
        clickbooster2.destroy()
        clickafford2 = Label(master, text="%s" % norequirements, width=35)
        clickafford2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2,
                          sticky=E)
        master.after(500, norequirementsc2)
    else:
        money -= 200000
        inc += mps/10
        inctkinter.set("+" + str(inc) + " money!")
        clickupgcheck2 += 1
        clickbooster2.destroy()
        boostbutton1h2.grid(
            row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
            sticky=E)
        boostbutton3.grid(row=int(
            6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)
        boostbutton4.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(
                clickupgcheck2))), column=2, sticky=E)


def norequirementsc2():
    global clickbooster2
    clickafford2.destroy()
    clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35,
                           command=clickboost2)
    clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2,
                       sticky=E)


# AUTOMATIC MONEY
def automoney():
    global money, autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, time
    money = round(money, 1)
    if check == int(10):
        global timevar
        # GOLD UPGRADE
        random1 = randint(1, 300)
        check = int(1)
        if random1 == int(1) and goldcheck == int(0):
            goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
            goldbutton.image = gold
            goldbutton.place(x=(int(randint(0, 450))), y=(int(randint(0, 200))))
            goldcheck = int(1)
        # ACHIEVEMENT UPDATES
        if statscheck == 1:
            timevar.set("Total time: " + str(time))
            totalclicksvar.set("Total clicks: " + str(totalclicks))
        bugfixer()
        time += 1
    money += float(mps)/10
    check += 1
    automoneychoice()


# AUTOMATIC MONEY (MILLIONS)
def automoney2():
    global money, autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, time, money, \
        moneymillion, templist1
    if len(str(money)) >= 8:
        moneymillion = round((float(str(money)[:-7])/10), 1)
        if check == int(10):
            global timevar
            # GOLD UPGRADE
            random1 = randint(1, 300)
            check = int(1)
            if random1 == int(1) and goldcheck == int(0):
                goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
                goldbutton.image = gold
                goldbutton.place(x=(int(randint(0, 450))), y=(int(randint(0, 200))))
                goldcheck = int(1)
            # ACHIEVEMENT UPDATES
            if statscheck == 1:
                timevar.set("Total time: " + str(time))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            time += 1
            templist1.append(moneymillion)
            if len(templist1) > 2:
                templist1.reverse()
                templist1.pop()
                templist1.reverse()
            if float(templist1[1]) != float(templist1[0]):
                moneymillion += float(templist1[1] - templist1[0])/10
        bugfixer()
        money += mps
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (BILLIONS)
def automoney3():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, time, moneybillion, \
        moneymillion, money, templist2
    if len(str(moneymillion)) >= 5:
        moneybillion = round((float(str(moneymillion)[:-5])/10), 1)
        if check == int(10):
            global timevar
            # GOLD UPGRADE
            random1 = randint(1, 300)
            check = int(1)
            if random1 == int(1) and goldcheck == int(0):
                goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
                goldbutton.image = gold
                goldbutton.place(x=(int(randint(0, 450))), y=(int(randint(0, 200))))
                goldcheck = int(1)
            # ACHIEVEMENT UPDATES
            if statscheck == 1:
                timevar.set("Total time: " + str(time))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            time += 1
            templist2.append(moneybillion)
            if len(templist2) > 2:
                templist2.reverse()
                templist2.pop()
                templist2.reverse()
            if float(templist2[1]) != float(templist2[0]):
                moneybillion += float(templist2[1] - templist2[0])/10
        bugfixer()
        moneymillion = float(math.floor((moneymillion + float(mps)/10**6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (TRILLIONS)
def automoney4():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, time, moneytrillion, \
        moneybillion, moneymillion, money, templist3
    if len(str(moneybillion)) >= 5:
        moneytrillion = round((float(str(moneybillion)[:-5])/10), 1)
        if check == int(10):
            global timevar
            # GOLD UPGRADE
            random1 = randint(1, 300)
            check = int(1)
            if random1 == int(1) and goldcheck == int(0):
                goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
                goldbutton.image = gold
                goldbutton.place(x=(int(randint(0, 450))), y=(int(randint(0, 200))))
                goldcheck = int(1)
            # ACHIEVEMENT UPDATES
            if statscheck == 1:
                timevar.set("Total time: " + str(time))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            time += 1
            templist3.append(moneytrillion)
            if len(templist3) > 2:
                templist3.reverse()
                templist3.pop()
                templist3.reverse()
            if float(templist3[1]) != float(templist3[0]):
                moneytrillion += float(templist3[1] - templist3[0])/10
        bugfixer()
        moneybillion = float(math.floor((moneybillion + float(mps)/10**9) * 10))
        moneymillion = float(math.floor((moneymillion + float(mps)/10**6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (QUADRILLIONS)
def automoney5():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, time, \
        moneyquadrillion, moneytrillion, moneybillion, moneymillion, money, templist4
    if len(str(moneytrillion)) >= 5:
        moneyquadrillion = round((float(str(moneytrillion)[:-5])/10), 1)
        if check == int(10):
            global timevar
            # GOLD UPGRADE
            random1 = randint(1, 300)
            check = int(1)
            if random1 == int(1) and goldcheck == int(0):
                goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
                goldbutton.image = gold
                goldbutton.place(x=(int(randint(0, 450))), y=(int(randint(0, 200))))
                goldcheck = int(1)
            # ACHIEVEMENT UPDATES
            if statscheck == 1:
                timevar.set("Total time: " + str(time))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            time += 1
            templist4.append(moneyquadrillion)
            if len(templist4) > 2:
                templist4.reverse()
                templist4.pop()
                templist4.reverse()
            if float(templist4[1]) != float(templist4[0]):
                moneyquadrillion += float(templist4[1] - templist4[0])/10
        bugfixer()
        moneytrillion = float(math.floor((moneytrillion + float(mps)/10**12) * 10))
        moneybillion = float(math.floor((moneybillion + float(mps)/10**9) * 10))
        moneymillion = float(math.floor((moneymillion + float(mps)/10**6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (QUINTILLIONS)
def automoney6():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, time, \
        moneyquintillion, moneyquadrillion, moneytrillion, moneybillion, moneymillion, money, templist5
    if len(str(moneyquadrillion)) >= 5:
        moneyquintillion = round((float(str(moneyquadrillion)[:-5])/10), 1)
        if check == int(10):
            global timevar
            # GOLD UPGRADE
            random1 = randint(1, 300)
            check = int(1)
            if random1 == int(1) and goldcheck == int(0):
                goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
                goldbutton.image = gold
                goldbutton.place(x=(int(randint(0, 450))), y=(int(randint(0, 200))))
                goldcheck = int(1)
            # ACHIEVEMENT UPDATES
            if statscheck == 1:
                timevar.set("Total time: " + str(time))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            time += 1
            templist5.append(moneyquintillion)
            if len(templist5) > 2:
                templist5.reverse()
                templist5.pop()
                templist5.reverse()
            if float(templist5[1]) != float(templist5[0]):
                moneyquintillion += float(templist5[1] - templist5[0])/10
        bugfixer()
        moneyquadrillion = float(math.floor(moneyquadrillion + float(mps)/10**15) * 10)
        moneytrillion = float(math.floor((moneytrillion + float(mps)/10**12) * 10))
        moneybillion = float(math.floor((moneybillion + float(mps)/10**9) * 10))
        moneymillion = float(math.floor((moneymillion + float(mps)/10**6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# SAVING GAME
def savegame():
    global g
    username = (g.name).split('_')[1].split('.')[0]
    x = ["auto", int(autoclick2), "print", int(printmoney2), "counter", int(counterfeit2), "shares", int(sharecrash2),
         "upg1h1", int(upgcheck1h1), "upg1h2", int(upgcheck1h2), "upg2h1", int(upgcheck2h1), "upg2h2", int(upgcheck2h2),
         "upg3", int(upgcheck3), "upg4", int(upgcheck4), "cupg1", int(clickupgcheck1), "cupg2", int(clickupgcheck2),
         "quintillion", int(moneyquintillion), "quadrillion", int(str(moneyquadrillion)[-5:-2]), "trillion",
         int(str(moneytrillion)[-5:-2]), "billion", int(str(moneybillion)[-5:-2]), "million",
         int(str(moneymillion)[-5:-2]), "money", float(str(money)[-8:])]
    savefile = str((str("_".join(str(v) for v in x))).encode("hex") + ";")
    f = open("savefile_" + username + ".txt", "w")
    f.write(str(savefile))
    f.close()
    toplevel = Toplevel()
    msg = Message(toplevel, text="Game saved!")
    msg.pack()


# RESETTING GAME
def resetgame():
    toplevel = Toplevel()
    msg = Label(toplevel, text="Are you sure you want to reset?")
    msg.grid(row=0, column=0, columnspan=2)

    yesbutton = Button(toplevel, text="Yes", command=_pressyes)
    yesbutton.grid(row=1, column=0)
    nobutton = Button(toplevel, text="No", command=toplevel.destroy)
    nobutton.grid(row=1, column=1)

def _pressyes(username=None):
    global g
    if username is None:
        username = (g.name).split('_')[1].split('.')[0]
    x = ["auto", int(0), "print", int(0), "counter", int(0), "shares", int(0), "upg1h1", int(0), "upg1h2", int(0),
         "upg2h1", int(0), "upg2h2", int(0), "upg3", int(0), "upg4", int(0), "cupg1", int(0), "cupg2", int(0),
         "quintillion", int(0), "quadrillion", int(0), "trillion", int(0), "billion", int(0), "million", int(0),
         "money", float(0)]
    resetfile = str((str("_".join(str(v) for v in x))).encode("hex") + ";")
    f = open("savefile_" + username + ".txt", "w")
    f.write(str(resetfile))
    f.close()




# UPGRADES WINDOW
def showupgrades():
    global upgbuttoncheck
    upgbuttoncheck = True
    global upgrades, clickbooster1, boostbutton1h1, boostbutton2h1, clickbooster2, boostbutton1h2, boostbutton3, \
        boostbutton2h2, boostbutton4, exitupgrades
    upgrades.destroy()
    if clickupgcheck1 == int(0):
        clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
        clickbooster1.grid(row=1, column=2, sticky=E)
    if upgcheck1h1 == int(0):
        boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
        boostbutton1h1.grid(row=int(2 - int(clickupgcheck1)), column=2, sticky=E)
    if upgcheck2h1 == int(0):
        boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                                command=boostauto2h1)
        boostbutton2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
    if clickupgcheck2 == int(0):
        clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35,
                               command=clickboost2)
        clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2,
                           sticky=E)
    if upgcheck1h2 == int(0):
        boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35,
                                command=boostauto1h2)
        boostbutton1h2.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) +
                                         int(clickupgcheck2))), column=2, sticky=E)
    if upgcheck3 == int(0):
        boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                              command=boostauto3)
        boostbutton3.grid(
            row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                         int(clickupgcheck2))), column=2, sticky=E)
    if upgcheck2h2 == int(0):
        boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
        boostbutton2h2.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
    if upgcheck4 == int(0):
        boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                              command=boostauto4)
        boostbutton4.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
    exitupgrades = Button(master, text="Hide Upgrades", command=hideupgrades)
    if statscheck:
        global hidestatsbutton
        hidestatsbutton.grid(row=9, column=0, sticky=W)
        exitupgrades.grid(row=9, column=2, sticky=E)
        resetbutton.grid(row=11, column=0, sticky=W)
        savebutton.grid(row=11, column=2, sticky=E)
    else:
        statsbutton.grid(row=9, column=0, sticky=W)
        exitupgrades.grid(row=9, column=2, sticky=E)
        resetbutton.grid(row=10, column=0, sticky=W)
        savebutton.grid(row=10, column=2, sticky=E)


def hideupgrades():
    global upgrades, exitupgrades, upgbuttoncheck
    upgbuttoncheck = False
    if clickupgcheck1 == int(0):
        clickbooster1.destroy()
    if upgcheck1h1 == int(0):
        boostbutton1h1.destroy()
    if upgcheck2h1 == int(0):
        boostbutton2h1.destroy()
    if clickupgcheck2 == int(0):
        clickbooster2.destroy()
    if upgcheck1h2 == int(0):
        boostbutton1h2.destroy()
    if upgcheck3 == int(0):
        boostbutton3.destroy()
    if upgcheck2h2 == int(0):
        boostbutton2h2.destroy()
    if upgcheck4 == int(0):
        boostbutton4.destroy()
    upgrades = Button(master, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=1, column=2, rowspan=8, sticky=E)
    exitupgrades.destroy()
    if statscheck:
        hidestatsbutton.grid(row=9, column=0, sticky=W)
        resetbutton.grid(row=11, column=0, sticky=W)
        savebutton.grid(row=11, column=2, sticky=E)
    elif not statscheck:
        statsbutton.grid(row=9, column=0, sticky=W)
        resetbutton.grid(row=10, column=0, sticky=W)
        savebutton.grid(row=10, column=2, sticky=E)


# ANIMATION
def animationthingy():
    if animate == 1:
        animation1 = Label(master, image=Animation1)
        animation1.place(x=253, y=0)
        animation1.image = Animation1
    elif animate == 2:
        animation2 = Label(master, image=Animation2)
        animation2.place(x=253, y=0)
        animation2.image = Animation2
    elif animate == 3:
        animation3 = Label(master, image=Animation3)
        animation3.place(x=253, y=0)
        animation3.image = Animation3
    clickcolour()


# PSYCHEDELIC COLOURS
def clickcolour():
    global clickcolourcheck, clickbutton
    clickcolourcheck += 1
    if clickcolourcheck == 2:
        clickbutton.configure(bg="red")
    elif clickcolourcheck == 3:
        clickbutton.configure(bg="orange")
    elif clickcolourcheck == 4:
        clickbutton.configure(bg="yellow")
    elif clickcolourcheck == 5:
        clickbutton.configure(bg="green")
    elif clickcolourcheck == 6:
        clickbutton.configure(bg="blue")
    elif clickcolourcheck == 7:
        clickbutton.configure(bg="purple")
    elif clickcolourcheck == 8:
        clickbutton.configure(bg="violet")
        clickcolourcheck = 1


# GOLD BUTTON
def goldupgrade():
    global goldbutton, money, mps, mpstkinter, goldcheck
    goldbutton.destroy()
    goldcheck = int(0)
    goldupgcheck = randint(1, 77)
    if goldupgcheck == int(1):
        mps *= 77
        mpstkinter = ("MPS: " + str(mps))
        toplevel = Toplevel()
        goldtime = Message(toplevel,
                           text="Gold Upgrade Activated (multiply current MPS by 77 for 7.7 seconds!)")
        goldtime.pack()
        master.after(7700, goldmpsstop)
    else:
        money += int(mps * 50)
        toplevel = Toplevel()
        goldtime2 = Message(toplevel, text="Gold Upgrade Activated (get money equal to *50 MPS!)")
        goldtime2.pack()


def goldmpsstop():
    global mps, mpstkinter
    mps = float(mps)/77
    mpstkinter = ("MPS: " + str(mps))

def signin():
    def verifySignIn():
        global g
        un = unEntry.get()
        if ('savefile_' + un + '.txt') in glob.glob('savefile_*.txt'):
            g = open('savefile_' + un + '.txt')
            for i in [l, unEntry, b1, b2]:
                i.destroy()
            main()
        else:
            showerror('Wrong Username')
    def createAccount():
        global g
        un = unEntry.get()
        _pressyes(username=un)
        g = open('savefile_' + un + '.txt')
        main()
    l = Label(master, text='Please enter username')
    l.grid(row=1, column=1)
    unEntry = Entry(master, show='*')
    unEntry.grid(row=2, column=1)
    b1 = Button(master, text='Log in', command=verifySignIn)
    b1.grid(row=3, column=1)
    b2 = Button(master, text='Create account under username', command=createAccount)
    b2.grid(row=4, column=1)
    
    
g = None
signin()

def main():
    global g
    globals()['check'] = False
    globals()['upgbuttoncheck'] = False
    globals()['goldcheck'] = False
    globals()['statscheck'] = False
    globals()['animate'] = 0
    globals()['totalclicks'] = 0
    globals()['time'] = 0
    globals()['click'] = 0
    globals()['clickcolourcheck'] = 1
    globals()['g2'] = (str(str(g.read()).split(";")[0]).decode("hex")).split("_")
    globals()['upgcheck1h1'] = int(globals()['g2'][9])
    globals()['upgcheck1h2'] = int(globals()['g2'][11])
    globals()['upgcheck2h1'] = int(globals()['g2'][13])
    globals()['upgcheck2h2'] = int(globals()['g2'][15])
    globals()['upgcheck3'] = int(globals()['g2'][17])
    globals()['upgcheck4'] = int(globals()['g2'][19])
    globals()['clickupgcheck1'] = int(globals()['g2'][21])
    globals()['clickupgcheck2'] = int(globals()['g2'][23])
    globals()['money'] = float(str(globals()['g2'][25] + globals()['g2'][27] +
                                   globals()['g2'][29] + globals()['g2'][31] +
                                   globals()['g2'][33] + globals()['g2'][35]))
    if len(str(globals()['money'])) < 8:
        globals()['moneycheck'] = "0"
    else:
        globals()['moneycheck'] = str(globals()['money'])[:1]
    globals()['moneymillion'] = round(float(str(globals()['g2'][25] + globals()['g2'][27] +
                                                globals()['g2'][29] + globals()['g2'][31] +
                                                globals()['g2'][33]) + "." +
                                            globals()['moneycheck']), 1)
    if len(str(globals()['moneymillion'])) < 5:
        globals()['moneymillioncheck'] = "0"
    else:
        globals()['moneymillioncheck'] = str(globals()['moneymillion'])[:1]
    globals()['moneybillion'] = round(float(str(globals()['g2'][25] + globals()['g2'][27] +
                                                globals()['g2'][29] + globals()['g2'][31]) +
                                            "." + globals()['moneymillioncheck']), 1)
    if len(str(globals()['moneybillion'])) < 5:
        globals()['moneybillioncheck'] = "0"
    else:
        globals()['moneybillioncheck'] = str(globals()['moneybillion'])[:1]
    globals()['moneytrillion'] = round(float(str(globals()['g2'][25] + globals()['g2'][27] +
                                                 globals()['g2'][29]) + "." +
                                             globals()['moneybillioncheck']), 1)
    if len(str(globals()['moneytrillion'])) < 5:
        globals()['moneytrillioncheck'] = "0"
    else:
        globals()['moneytrillioncheck'] = str(globals()['moneytrillion'])[:1]
    globals()['moneyquadrillion'] = round(float(str(globals()['g2'][25] + globals()['g2'][27])
                                                + "." + globals()['moneytrillioncheck']), 1)
    if len(str(globals()['moneyquadrillion'])) < 5:
        globals()['moneyquadrillioncheck'] = "0"
    else:
        globals()['moneyquadrillioncheck'] = str(moneyquadrillion)[:1]
    globals()['moneyquintillion'] = round(float(str(globals()['g2'][25]) + "." +\
                                                globals()['moneyquadrillioncheck']), 1)
    globals()['moneytkinter'] = StringVar()
    if globals()['moneymillion'] == 0:
        globals()['moneytkinter'].set("Balance: $" + str(globals()['money']))
    elif globals()['moneybillion'] == 0:
        globals()['moneytkinter'].set("Balance: $" + str(globals()['moneymillion']) + "m")
    elif globals()['moneytrillion'] == 0:
        globals()['moneytkinter'].set("Balance: $" + str(globals()['moneybillion']) + "b")
    elif globals()['moneyquadrillion'] == 0:
        globals()['moneytkinter'].set("Balance: $" + str(globals()['moneytrillion']) + "t")
    elif globals()['moneyquintillion'] == 0:
        globals()['moneytkinter'].set("Balance: $" + str(globals()['moneyquadrillion']) + "q")
    else:
        globals()['moneytkinter'].set("Balance: $" + str(globals()['moneyquintillion']) + "Q")
    globals()['autoclick'] = int((globals()['g2'][1] * 18 * int(globals()['g2'][11])) +\
                                 (globals()['g2'][1] * 2 * int(globals()['g2'][9])) +\
                                 globals()['g2'][1])
    globals()['autoclick2'] = int(globals()['g2'][1])
    globals()['autoclicktkinter'] = StringVar()
    globals()['autoclicktkinter'].set("Auto-Clickers Amount: " + str(globals()['g2'][1]))
    globals()['autoprice'] = int(20 * (math.pow(1.2, int(globals()['g2'][1]))))
    globals()['autopricetkinter'] = StringVar()
    globals()['autopricetkinter'].set("Auto-Clicker (Costs: $" + str(globals()['autoprice']) + ")")
    globals()['printmoney'] = int((globals()['g2'][3] * 2 * int(globals()['g2'][13])) +\
                                  globals()['g2'][3])
    globals()['printmoney2'] = int(globals()['g2'][3])
    globals()['printmoneytkinter'] = StringVar()
    globals()['printmoneytkinter'].set("Money Printers Amount: " + str(globals()['g2'][3]))
    globals()['printprice'] = int(375 * (math.pow(1.2, int(globals()['g2'][3]))))
    globals()['printpricetkinter'] = StringVar()
    globals()['printpricetkinter'].set("Money Printer (Costs: $" + str(globals()['printprice']) + ")")
    globals()['counterfeit'] = int((globals()['g2'][5] * 2 * int(globals()['g2'][17])) +\
                                   globals()['g2'][5])
    globals()['counterfeit2'] = int(globals()['g2'][5])
    globals()['counterfeittkinter'] = StringVar()
    globals()['counterfeittkinter'].set("Counterfeit Companies Amount: " + str(globals()['g2'][5]))
    globals()['counterfeitprice'] = int(9001 * (math.pow(1.2, int(globals()['g2'][5]))))
    globals()['counterfeitpricetkinter'] = StringVar()
    globals()['counterfeitpricetkinter'].set("Counterfeit Company (Costs: $" +\
                                             str(globals()['counterfeitprice']) + ")")
    globals()['sharecrash'] = int((globals()['g2'][7] * 2 * int(globals()['g2'][19])) + globals()['g2'][7])
    globals()['sharecrash2'] = int(globals()['g2'][7])
    globals()['sharecrashtkinter'] = StringVar()
    globals()['sharecrashtkinter'].set("Sharemarket Crashes Amount: " + str(globals()['sharecrash2']))
    globals()['shareprice'] = int(42000 * (math.pow(1.2, int(globals()['g2'][7]))))
    globals()['sharepricetkinter'] = StringVar()
    globals()['sharepricetkinter'].set("Sharemarket Crash (Costs: $" + str(globals()['shareprice']) + ")")
    globals()['mps'] = int(globals()['g2'][1]) + 15 * int(globals()['g2'][3]) + 321 * \
                       int(globals()['g2'][5]) + 969 * int(globals()['g2'][7])
    globals()['mpstkinter'] = StringVar()
    globals()['mpstkinter'].set("MPS: " + str(globals()['mps']))
    globals()['inc'] = int(1 + (int(globals()['g2'][21]) * 2) + int(globals()['g2'][23]) * (globals()['mps']/10))
    globals()['inctkinter'] = StringVar()
    globals()['inctkinter'].set("+" + str(globals()['inc']) + " money!")
    globals()['templist1'] = [globals()['moneymillion']]*2
    globals()['templist2'] = [globals()['moneybillion']]*2
    globals()['templist3'] = [globals()['moneytrillion']]*2
    globals()['templist4'] = [globals()['moneyquadrillion']]*2
    globals()['templist5'] = [globals()['moneyquintillion']]*2
    if globals()['g2'][21] == int(1):
        globals()['clickbooster1'].destroy()
    if globals()['g2'][9] == int(1):
        globals()['boostbutton1h1'].destroy()
    if globals()['g2'][13] == int(1):
        globals()['boostbutton2h1'].destroy()
    if globals()['g2'][23] == int(1):
        globals()['clickbooster2'].destroy()
    if globals()['g2'][11] == int(1):
        globals()['boostbutton1h2'].destroy()
    if globals()['g2'][17] == int(1):
        globals()['boostbutton3'].destroy()
    if globals()['g2'][15] == int(1):
        globals()['boostbutton2h2'].destroy()
    if globals()['g2'][19] == int(1):
        globals()['boostbutton4'].destroy()
    if globals()['mps'] >= 1:
        automoneychoice()


    # BUTTONS, LABELS AND ENTRIES
    globals()['background'] = Label(master, image=img1)
    globals()['background'].place(x=0, y=0, relwidth=1, relheight=1)
    globals()['background'].image = img1

    globals()['upgrades'] = Button(master, text="Upgrades", height=12, width=15, command=showupgrades)
    globals()['upgrades'].grid(row=1, column=2, rowspan=8, sticky=E)

    globals()['moneylabel'] = Label(master, textvariable=globals()['moneytkinter'])
    globals()['moneylabel'].grid(row=0, column=0, sticky=W)

    globals()['mpslabel'] = Label(master, textvariable=globals()['mpstkinter'])
    globals()['mpslabel'].grid(row=0, column=2, sticky=E)

    globals()['clickbutton'] = Button(master, textvariable=globals()['inctkinter'],
                                      height=6, width=18, command=collectmoney, bg="red")
    globals()['clickbutton'].grid(row=3, column=1, rowspan=4)

    globals()['incbutton1'] = Button(master, textvariable=globals()['autopricetkinter'], width=35, command=deduction1)
    globals()['incbutton1'].grid(row=1, column=0, sticky=W)

    globals()['checklabel1'] = Label(master, textvariable=globals()['autoclicktkinter'], width=35)
    globals()['checklabel1'].grid(row=2, column=0, sticky=W)

    globals()['incbutton2'] = Button(master, textvariable=globals()['printpricetkinter'], width=35, command=deduction2)
    globals()['incbutton2'].grid(row=3, column=0, sticky=W)

    globals()['checklabel2'] = Label(master, textvariable=globals()['printmoneytkinter'], width=35)
    globals()['checklabel2'].grid(row=4, column=0, sticky=W)

    globals()['incbutton3'] = Button(master, textvariable=globals()['counterfeitpricetkinter'], width=35, command=deduction3)
    globals()['incbutton3'].grid(row=5, column=0, sticky=W)

    globals()['checklabel3'] = Label(master, textvariable=globals()['counterfeittkinter'], width=35)
    globals()['checklabel3'].grid(row=6, column=0, sticky=W)

    globals()['incbutton4'] = Button(master, textvariable=globals()['sharepricetkinter'], width=35, command=deduction4)
    globals()['incbutton4'].grid(row=7, column=0, sticky=W)

    globals()['checklabel4'] = Label(master, textvariable=globals()['sharecrashtkinter'], width=35)
    globals()['checklabel4'].grid(row=8, column=0, sticky=W)

    globals()['statsbutton'] = Button(master, text="Stats", width=10, command=statsexpand)
    globals()['statsbutton'].grid(row=9, column=0, sticky=W)

    globals()['resetbutton'] = Button(master, text="Reset Game", width=10, command=resetgame)
    globals()['resetbutton'].grid(row=10, column=0, sticky=W)

    globals()['savebutton'] = Button(master, text="Save Game", width=10, command=savegame)
    globals()['savebutton'].grid(row=10, column=2, sticky=E)


mainloop()


