from Tkinter import *
from random import *
import math

master = Tk()
master.title("Ways To NOT Earn Money")
img1 = PhotoImage(file="img1.gif")
gold = PhotoImage(file="gold.gif")
clickcolourcheck = 1


def statcollapse():
    statcollapse.destroy()

# AUTO CLICKER
def boostauto1h1():
    global money, autoclick, autoclick2, upgcheck1h1, mps
    if money < 5000 or autoclick2 == 0:
        toplevel = Toplevel()
        norequirements1 = Message(toplevel, text="You do not meet the requirements.")
        norequirements1.pack()
    else:
        money -= 5000
        autoclick = int(autoclick * 30) / 10
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


def boostauto1h2():
    global money, autoclick, autoclick2, upgcheck1h2, mps
    if money < 555555 or upgcheck1h1 == 0:
        toplevel = Toplevel()
        norequirements2 = Message(toplevel, text="You do not meet the requirements.")
        norequirements2.pack()
    else:
        money -= 555555
        autoclick = int(autoclick * 70) / 10
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


def deduction1():
    global money, autoclick, autoclick2, autoprice, counterfeit, printmoney, sharecrash, mps, inc
    if money < int(autoprice):
        toplevel = Toplevel()
        cannotafford1 = Message(toplevel, text="You cannot afford this.")
        cannotafford1.pack()
    else:
        money -= int(autoprice)
        autoclick += (1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
        autoclick2 += 1
        mps += 1
        mpstkinter.set("MPS: " + str(mps))
        autoclicktkinter.set("Auto-Clickers Amount: " + str(autoclick2))
        autoprice = int(20 * (math.pow(1.15, autoclick2)))
        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
        if autoclick == 1 and sharecrash == 0 and counterfeit == 0 and printmoney == 0:
            automoney()


# MONEY PRINTER
def boostauto2h1():
    global money, printmoney, printmoney2, upgcheck2h1, mps
    if money < 42000 or printmoney2 == 0:
        toplevel = Toplevel()
        norequirements3 = Message(toplevel, text="You do not meet the requirements.")
        norequirements3.pack()
    else:
        money -= 42000
        printmoney = int(float(printmoney * 30) / 10)
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


def boostauto2h2():
    global money, printmoney, printmoney2, upgcheck2h2, mps
    if money < 7777777 or upgcheck2h1 == 0:
        toplevel = Toplevel()
        norequirements4 = Message(toplevel, text="You do not meet the requirements.")
        norequirements4.pack()
    else:
        money -= 7777777
        printmoney = int(float(printmoney * 70) / 10)
        upgcheck2h2 += 1
        mps += printmoney2 * 18
        mpstkinter.set("MPS: " + str(mps))
        boostbutton2h2.destroy()
        boostbutton4.grid(row=int(8 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(
                clickupgcheck2))), column=2, sticky=E)


def deduction2():
    global money, printmoney, printmoney2, printprice, sharecrash, counterfeit, autoclick, mps, inc
    if money < int(printprice):
        toplevel = Toplevel()
        cannotafford2 = Message(toplevel, text="You cannot afford this.")
        cannotafford2.pack()
    else:
        money -= int(printprice)
        printmoney += (1 + (upgcheck2h1 * 2) + (upgcheck2h2 * 18))
        printmoney2 += 1
        mps += 15
        mpstkinter.set("MPS: " + str(mps))
        printmoneytkinter.set("Money Printers Amount: " + str(printmoney2))
        printprice = int(275 * (math.pow(1.15, printmoney2)))
        printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
        if printmoney == 1 and sharecrash == 0 and counterfeit == 0 and autoclick == 0:
            automoney()


# COUNTERFEIT COMPANY
def boostauto3():
    global money, counterfeit, counterfeit2, upgcheck3, mps
    if money < 2133748 or counterfeit2 == 0:
        toplevel = Toplevel()
        norequirements5 = Message(toplevel, text="You do not meet the requirements.")
        norequirements5.pack()
    else:
        money -= 2133748
        counterfeit = int(counterfeit * 30) / 10
        mps += counterfeit2 * 2
        mpstkinter.set("MPS: " + str(mps))
        upgcheck3 += 1
        boostbutton3.destroy()
        boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(upgcheck4) + int(
                clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(8 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(
                clickupgcheck2))), column=2, sticky=E)


def deduction3():
    global money, counterfeit, counterfeit2, counterfeitprice, sharecrash, printmoney, autoclick, mps, inc
    if money < int(counterfeitprice):
        toplevel = Toplevel()
        cannotafford3 = Message(toplevel, text="You cannot afford this.")
        cannotafford3.pack()
    else:
        money -= int(counterfeitprice)
        counterfeit += (1 + upgcheck3 * 2)
        counterfeit2 += 1
        mps += 321
        mpstkinter.set("MPS: " + str(mps))
        counterfeittkinter.set("Counterfeit Companies Amount: " + str(counterfeit2))
        counterfeitprice = int(9001 * (math.pow(1.15, counterfeit2)))
        counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
        if counterfeit == 1 and sharecrash == 0 and printmoney == 0 and autoclick == 0:
            automoney()


# SHAREMARKET CRASH
def boostauto4():
    global money, sharecrash, sharecrash2, upgcheck4, mps
    if money < 12345678 or sharecrash2 == 0:
        toplevel = Toplevel()
        norequirements6 = Message(toplevel, text="You do not meet the requirements.")
        norequirements6.pack()
    else:
        money -= 12345678
        sharecrash = int(sharecrash * 30) / 10
        mps += sharecrash2 * 2
        mpstkinter.set("MPS: " + str(mps))
        upgcheck4 += 1
        boostbutton4.destroy()


def deduction4():
    global money, sharecrash, sharecrash2, shareprice, counterfeit, printmoney, autoclick, mps, inc
    if money < int(shareprice):
        toplevel = Toplevel()
        cannotafford4 = Message(toplevel, text="You cannot afford this.")
        cannotafford4.pack()
    else:
        money -= int(shareprice)
        sharecrash += (1 + upgcheck4 * 2)
        sharecrash2 += 1
        mps += 969
        mpstkinter.set("MPS: " + str(mps))
        sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
        shareprice = int(42000 * (math.pow(1.15, sharecrash2)))
        sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
        if sharecrash == 1 and counterfeit == 0 and printmoney == 0 and autoclick == 0:
            automoney()


# CLICKS
def collectmoney():
    global inc, money, animate
    money = money + inc
    moneytkinter.set("Balance: $" + str(money))
    animate += 1
    if animate > 3:
        animate = 1
    animationthingy()


def clickboost1():
    global money, inc, clickupgcheck1
    if money < 2100:
        toplevel = Toplevel()
        norequirements7 = Message(toplevel, text="You do not meet the requirements.")
        norequirements7.pack()
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


def clickboost2():
    global money, inc, mps, clickupgcheck2
    if money < 200000 or clickupgcheck1 == int(0):
        toplevel = Toplevel()
        norequirements8 = Message(toplevel, text="You do not meet the requirements.")
        norequirements8.pack()
    else:
        money -= 200000
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + sharecrash)), 1.01))
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

# AUTOMATIC MONEY
def automoney():
    global money, autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck
    money = round(float(money), 2)

    # gold UPGRADE
    if check == int(10):
        random1 = randint(1, 600)
        check = int(1)
        if random1 == int(1):
            if goldcheck == int(0):
                goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
                goldbutton.image = gold
                goldbutton.place(x=(int(randint(0, 500))), y=(int(randint(0, 200))))
                goldcheck = int(1)

    # BUG FIXER
    while mps > (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
        if mps - 969 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            sharecrash += (1 + upgcheck4 * 2)
            sharecrash2 += 1
            sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
            shareprice = int(42000 * (math.pow(1.15, sharecrash2)))
            sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
            continue
        elif mps - 321 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            counterfeit += (1 + upgcheck3 * 2)
            counterfeit2 += 1
            counterfeittkinter.set("Counterfeit Companies Amount: " + str(counterfeit2))
            counterfeitprice = int(9001 * (math.pow(1.15, counterfeit2)))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
            continue
        elif mps - 15 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            printmoney += (1 + upgcheck2h1 * 2 + upgcheck2h2 * 18)
            printmoney2 += 1
            printmoneytkinter.set("Money Printers Amount: " + str(printmoney2))
            printprice = int(275 * (math.pow(1.15, printmoney2)))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        else:
            autoclick += (1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
            autoclick2 += 1
            autoclicktkinter.set("Money Printers Amount: " + str(autoclick2))
            autoprice = int(20 * (math.pow(1.15, autoclick2)))
            autopricetkinter.set("Money Printer (Costs: $" + str(autoprice) + ")")
            continue
    moneytkinter.set("Balance: $" + str(money))
    money += float(mps) / 10
    check += 1
    master.after(100, automoney)


# SAVING GAME
def savegame():
    x = ["auto", int(autoclick2), "print", int(printmoney2), "counter", int(counterfeit2), "shares", int(sharecrash2),
         "upg1h1", int(upgcheck1h1), "upg1h2", int(upgcheck1h2), "upg2h1", int(upgcheck2h1), "upg2h2", int(upgcheck2h2),
         "upg3", int(upgcheck3), "upg4",
         int(upgcheck4), "cupg1", int(clickupgcheck1), "cupg2", int(clickupgcheck2), "money", float(money)]
    savefile = (str("_".join(str(v) for v in x))).encode("hex")
    f = open("savefile.txt", "w")
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

    def pressyes():
        x = ["auto", int(0), "print", int(0), "counter", int(0), "shares", int(0), "upg1h1", int(0), "upg1h2", int(0),
             "upg2h1", int(0), "upg2h2", int(0), "upg3", int(0), "upg4", int(0), "cupg1", int(0), "cupg2", int(0),
             "money", float(0)]
        resetfile = (str("_".join(str(v) for v in x))).encode("hex")
        f = open("savefile.txt", "w")
        f.write(str(resetfile))
        f.close()
        master.destroy()

    def pressno():
        toplevel.destroy()

    yesbutton = Button(toplevel, text="Yes", command=pressyes)
    yesbutton.grid(row=1, column=0)
    nobutton = Button(toplevel, text="No", command=pressno)
    nobutton.grid(row=1, column=1)


# UPGRADES WINDOW
def showupgrades():
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
        boostbutton1h2.grid(
            row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)
    if upgcheck3 == int(0):
        boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                              command=boostauto3)
        boostbutton3.grid(
            row=int(6 - (
                int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(
                    clickupgcheck2))),
            column=2, sticky=E)
    if upgcheck2h2 == int(0):
        boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
        boostbutton2h2.grid(row=int(7 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) + int(clickupgcheck1) + int(
                clickupgcheck2))),
                            column=2, sticky=E)
    if upgcheck4 == int(0):
        boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                              command=boostauto4)
        boostbutton4.grid(row=int(8 - (
            int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) + int(upgcheck3) + int(
                clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)
    exitupgrades = Button(master, text="Hide Upgrades", command=hideupgrades)
    exitupgrades.grid(row=9, column=2, sticky=E)
    resetbutton.grid(row=10, column=0, sticky=W)
    savebutton.grid(row=10, column=2, sticky=E)


def hideupgrades():
    global upgrades, exitupgrades
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
    resetbutton.grid(row=9, column=0, sticky=W)
    savebutton.grid(row=9, column=2, sticky=E)


# SAVE IMPORTS AND VARIABLES
check = 0
upgbuttoncheck = 0
goldcheck = 0
click = 0
animate = 0
g = open("savefile.txt")
g2 = (str(g.readline()).decode("hex")).split("_")
upgcheck1h1 = int(g2[9])
upgcheck1h2 = int(g2[11])
upgcheck2h1 = int(g2[13])
upgcheck2h2 = int(g2[15])
upgcheck3 = int(g2[17])
upgcheck4 = int(g2[19])
clickupgcheck1 = int(g2[21])
clickupgcheck2 = int(g2[23])
money = float(g2[25])
moneytkinter = StringVar()
moneytkinter.set("Balance: $" + str(money))
autoclick = int((g2[1] * int(18 * g2[11])) + (g2[1] * int(2 * g2[9])) + g2[1])
autoclick2 = int(g2[1])
autoclicktkinter = StringVar()
autoclicktkinter.set("Auto-Clickers Amount: " + str(g2[1]))
autoprice = int(20 * (math.pow(1.15, int(g2[1]))))
autopricetkinter = StringVar()
autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
printmoney = int((g2[3] * int(2 * g2[13])) + g2[3])
printmoney2 = int(g2[3])
printmoneytkinter = StringVar()
printmoneytkinter.set("Money Printers Amount: " + str(g2[3]))
printprice = int(275 * (math.pow(1.15, int(g2[3]))))
printpricetkinter = StringVar()
printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
counterfeit = int((g2[5] * int(2 * g2[17])) + g2[5])
counterfeit2 = int(g2[5])
counterfeittkinter = StringVar()
counterfeittkinter.set("Counterfeit Companies Amount: " + str(g2[5]))
counterfeitprice = int(9001 * (math.pow(1.15, int(g2[5]))))
counterfeitpricetkinter = StringVar()
counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
sharecrash = int((g2[7] * int(2 * g2[19])) + g2[7])
sharecrash2 = int(g2[7])
sharecrashtkinter = StringVar()
sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
shareprice = int(42000 * (math.pow(1.15, int(g2[7]))))
sharepricetkinter = StringVar()
sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
inc = int(1 + (int(g2[21]) * 2))
inctkinter = StringVar()
inctkinter.set("+" + str(inc) + " money!")
mps = int(g2[1]) + 15 * int(g2[3]) + 321 * int(g2[5]) + 969 * int(g2[7])
mpstkinter = StringVar()
mpstkinter.set("MPS: " + str(mps))
if g2[21] == int(1):
    clickbooster1.destroy()
if g2[9] == int(1):
    boostbutton1h1.destroy()
if g2[13] == int(1):
    boostbutton2h1.destroy()
if g2[23] == int(1):
    clickbooster2.destroy()
if g2[11] == int(1):
    boostbutton1h2.destroy()
if g2[17] == int(1):
    boostbutton3.destroy()
if g2[15] == int(1):
    boostbutton2h2.destroy()
if g2[19] == int(1):
    boostbutton4.destroy()
if mps >= 1:
    automoney()


# BUTTONS, LABELS AND ENTRIES
def goldupgrade():
    global goldbutton, money, mps, goldcheck
    money += int(mps * 50)
    goldbutton.destroy()
    goldcheck = int(0)
    toplevel = Toplevel()
    goldtime = Message(toplevel, text="Gold Upgrade Activated (get money equal to *50 MPS!)")
    goldtime.pack()


background = Label(master, image=img1)
background.place(x=0, y=0, relwidth=1, relheight=1)
background.image = img1

upgrades = Button(master, text="Upgrades", height=12, width=15, command=showupgrades)
upgrades.grid(row=1, column=2, rowspan=8, sticky=E)

moneylabel = Label(master, textvariable=moneytkinter)
moneylabel.grid(row=0, column=0, sticky=W)

mpslabel = Label(master, textvariable=mpstkinter)
mpslabel.grid(row=0, column=2, sticky=E)

clickbutton = Button(master, textvariable=inctkinter, height=6, width=18, command=collectmoney, bg="red")
clickbutton.grid(row=3, column=1, rowspan=4)

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

incbutton4 = Button(master, textvariable=sharepricetkinter, width=35, command=deduction4)
incbutton4.grid(row=7, column=0, sticky=W)

checklabel4 = Label(master, textvariable=sharecrashtkinter, width=35)
checklabel4.grid(row=8, column=0, sticky=W)

statcollapse = Button(master, text="Stats", width=10, command=statcollapse)
statcollapse.grid(row=9, column=0, sticky=W)

resetbutton = Button(master, text="Reset Game", width=10, command=resetgame)
resetbutton.grid(row=10, column=0, sticky=W)

savebutton = Button(master, text="Save Game", width=10, command=savegame)
savebutton.grid(row=9, column=2, sticky=E)

Animation1 = PhotoImage(file="Animation1.gif")
Animation2 = PhotoImage(file="Animation2.gif")
Animation3 = PhotoImage(file="Animation3.gif")


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

def clickcolour():
    global clickcolourcheck
    clickcolourcheck += 1
    if clickcolourcheck == 2         clickbutton.configure(bg="red")
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


mainloop()
