from Tkinter import *
from random import *
from tkMessageBox import showerror
from github import Github
import math
import glob
import threading

master = Tk()
master.title("Ways To NOT Earn Money")
img1 = PhotoImage(file="img1.gif")
gold = PhotoImage(file="gold.gif")
Animation1 = PhotoImage(file="Animation1.gif")
Animation2 = PhotoImage(file="Animation2.gif")
Animation3 = PhotoImage(file="Animation3.gif")
norequirements = "You do not meet the requirements."
cannotafford = "You cannot afford this."
signincheck = 1
signinvalue = 1


# SAVEFILE UPDATER
def updatesavefile(var):
    temp = (str(var).decode("hex")).split("_")
    xbuildings = ["auto", temp[1], "print", temp[3], "counter", temp[5], "shares",
                  temp[7], "bank", int(0)]
    xmoney = ["quintillion", temp[25], "quadrillion", temp[27], "trillion", temp[29], "billion", temp[31],
              "million", temp[33], "money", temp[35]]
    xupgrades = ["upg1h1", temp[9], "upg1h2", temp[11], "upg2h1", temp[13], "upg2h2", temp[15], "upg3",
                 temp[17], "upg4", temp[19], "upg5", int(0), "cupg1", temp[21], "cupg2", temp[23]]
    tempbuildings = str((str("_".join(str(v) for v in xbuildings))).encode("hex") + ";")
    tempmoney = str((str("_".join(str(v) for v in xmoney))).encode("hex") + ";")
    tempupgrades = str((str("_".join(str(v) for v in xupgrades))).encode("hex") + ";")
    if len(temp) == 36:
        xmisc = ["time", int(0), "clicks", int(0)]
        tempmisc = str((str("_".join(str(v) for v in xmisc))).encode("hex") + ";")
        temp2 = str(tempbuildings + tempmisc + tempmoney + tempupgrades)
        return temp2
    elif len(temp) == 40:
        xmisc = ["time", temp[37], "clicks", temp[39]]
        tempmisc = str((str("_".join(str(v) for v in xmisc))).encode("hex") + ";")
        temp2 = str(tempbuildings + tempmisc + tempmoney + tempupgrades)
        return temp2


# SIGN-IN PAGE
def signin():
    global signincheck
    signincheck += 1

    def verifysignin():
        global g
        un = unentry.get()
        if ('savefile_' + un + '.txt') in glob.glob('savefile_*.txt'):
            global g2, signinvalue
            g = open('savefile_' + un + '.txt')
            g2 = (str(g.read()).split(";"))
            if len(g2) == 2:
                g2 = str(g2[0])
            try:
                global gbuildings, gmisc, gmoney, gupgrades
                gbuildings = (g2[0].decode("hex")).split("_")
                gmisc = (g2[1].decode("hex").split("_"))
                gmoney = (g2[2].decode("hex").split("_"))
                gupgrades = (g2[3].decode("hex").split("_"))
            except (IndexError, TypeError):
                print("Here!")
                g2 = updatesavefile(g2)
                g = open('savefile_' + un + '.txt', 'w')
                g.write(g2)
                verifysignin()
            for i in [l, unentry, b1, b2]:
                i.destroy()
            signinvalue += 1
        else:
            showerror(title='Error!', message='Wrong Username.')

    def createaccount():
        global g, g2, signinvalue, gbuildings, gmisc, gmoney, gupgrades
        print("Yes")
        un = unentry.get()
        _pressyes(username=un)
        g = open('savefile_' + un + '.txt')
        g2 = str(str(g.read()).split(";"))
        gbuildings = (g2[0].decode("hex")).split("_")
        gmisc = (g2[1].decode("hex").split("_"))
        gmoney = (g2[2].decode("hex").split("_"))
        gupgrades = (g2[3].decode("hex").split("_"))
        signinvalue += 1

    l = Label(master, text='Please enter your username.')
    l.grid(row=0, column=0)
    unentry = Entry(master, show='')
    unentry.grid(row=1, column=0)
    b1 = Button(master, text='Log in', command=verifysignin)
    b1.grid(row=2, column=0)
    b2 = Button(master, text='Create account under username', command=createaccount)
    b2.grid(row=3, column=0)


# REPORT AN ISSUE
def report():
    gl = globals()
    gl['t'] = Toplevel()
    Label(master=gl['t'],
          text="Make sure you are a collaborator of Ways to not make money, and you don't have a fork", bg='yellow') \
        .grid(row=0, column=0)
    Label(master=gl['t'],
          text='Please sign in to your Github account below. (Username first entry, passcode second)').grid(row=1,
                                                                                                            column=0)
    gl['une'] = Entry(master=gl['t'])
    gl['une'].grid(row=2, column=0)
    gl['pce'] = Entry(master=gl['t'], show="*")
    gl['pce'].grid(row=3, column=0)
    globals().update(gl)
    Button(master=gl['t'], text='Verify', command=_verify_report).grid(row=4, column=0)


# VERIFY IF USERNAME/PASSWORD MATCHES
def _verify_report():
    gl = globals()
    verified = False
    try:
        gl['user'] = Github(gl['une'].get(), gl['pce'].get())
    except:
        showerror('No username/passcode match, try again')
    else:
        for i in user.get_user().get_repos():
            if i.name == 'Ways-to-NOT-make-money':
                wtnmm = i
        try:
            print(wtnmm)
        except:
            showerror('Not a collaborator!')
        else:
            gl['t'].destroy()
            gl['wtnmm'] = wtnmm
            verified = True
    globals().update(gl)
    if verified:
        _create_report()


# CREATE THE SEPARATE REPORT WINDOW
def _create_report():
    gl = globals()
    gl['t'] = Toplevel()
    t = gl['t']
    Label(t, text='Issue Title: ').grid(row=0, column=0)
    gl['e'] = Entry(t)
    gl['e'].grid(row=0, column=1)
    Label(t, text='Issue Body: ').grid(row=1, column=0, columnspan=2)
    gl['tx'] = Text(t, width=35, height=10, wrap=WORD)
    gl['tx'].grid(row=2, column=0, columnspan=2)
    globals().update(gl)
    Button(t, text='Create Github Issue', command=_send_report).grid(row=3, column=0, rowspan=2)


# SENDS THE REPORT
def _send_report():
    gl = globals()
    title = gl['e'].get()
    body = gl['tx'].get(1.0, "end")
    rep = gl['wtnmm']
    rep.create_issue(title, body)
    gl['t'].destroy()
    globals().update(gl)


# BUG FIXER
def bugfixer():
    global sharecrash, counterfeit, printmoney, autoclick
    while mps > (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
        if mps - 969 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            global sharecrash2, shareprice
            sharecrash += (1 + upgcheck4 * 2)
            sharecrash2 += 1
            sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
            shareprice = int(42000 * (math.pow(1.2, sharecrash2)))
            sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
            continue
        elif mps - 321 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            global counterfeit2, counterfeitprice
            counterfeit += (1 + upgcheck3 * 2)
            counterfeit2 += 1
            counterfeittkinter.set("Counterfeit Companies Amount: " + str(counterfeit2))
            counterfeitprice = int(9001 * (math.pow(1.2, counterfeit2)))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
            continue
        elif mps - 15 >= (autoclick + printmoney * 15 + counterfeit * 321 + sharecrash * 969):
            global printmoney2, printprice
            printmoney += (1 + upgcheck2h1 * 2 + upgcheck2h2 * 18)
            printmoney2 += 1
            printmoneytkinter.set("Money Printers Amount: " + str(printmoney2))
            printprice = int(375 * (math.pow(1.2, printmoney2)))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        else:
            global autoclick2, autoprice
            autoclick += (1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
            autoclick2 += 1
            autoclicktkinter.set("Money Printers Amount: " + str(autoclick2))
            autoprice = int(20 * (math.pow(1.2, autoclick2)))
            autopricetkinter.set("Money Printer (Costs: $" + str(autoprice) + ")")
            continue


# CHOICE FOR AUTOMATIC MONEY
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
    global totalclickslabel, totalclicksvar, timevar, timelabel, statscheck, hidestatsbutton
    statsbutton.destroy()
    resetbutton.grid(row=4, column=0, sticky=W)
    savebutton.grid(row=4, column=2, sticky=E)
    reportbutton.grid(row=5, column=1)
    statscheck = True
    totalclicksvar = StringVar()
    totalclicksvar.set("Total clicks: " + str(totalclicks))
    totalclickslabel = Label(master, textvariable=totalclicksvar)
    totalclickslabel.grid(row=3, column=0, sticky=W)
    timevar = StringVar()
    timevar.set("Total time: " + str(timeplay))
    timelabel = Label(master, textvariable=timevar)
    timelabel.grid(row=3, column=2, sticky=E)
    hidestatsbutton = Button(master, text="Hide Stats", width=10, command=hidestats)
    hidestatsbutton.grid(row=2, column=0, sticky=W)


def hidestats():
    global statsbutton, statscheck
    statscheck = False
    totalclickslabel.destroy()
    timelabel.destroy()
    hidestatsbutton.destroy()
    resetbutton.grid(row=3, column=0, sticky=W)
    savebutton.grid(row=3, column=2, sticky=E)
    reportbutton.grid(row=4, column=1)
    statsbutton = Button(master, text="Stats", width=10, command=statsexpand)
    statsbutton.grid(row=2, column=0, sticky=W)
    if upgbuttoncheck:
        exitupgrades.grid(row=2, column=2, sticky=E)
    elif not upgbuttoncheck:
        pass


# AUTO CLICKER
def boostauto1h1():
    global money, autoclick, autoclick2, upgcheck1h1, mps
    if money < 5000 or autoclick2 == 0:
        global boostafford1h1
        boostbutton1h1.destroy()
        master.bell()
        boostafford1h1 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=int(1 - int(clickupgcheck1)), column=2, sticky=E)
        master.after(500, norequirements1h1)
    else:
        money -= 5000
        autoclick = int(autoclick * 15) / 10
        upgcheck1h1 += 1
        mps += autoclick2 * 2
        mpstkinter.set("MPS: " + str(mps))
        boostbutton1h1.destroy()
        boostbutton2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=2, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)


def norequirements1h1():
    global boostafford1h1, boostbutton1h1
    boostafford1h1.destroy()
    boostbutton1h1 = Button(frame2, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
    boostbutton1h1.grid(row=int(1 - int(clickupgcheck1)), column=2, sticky=E)


def boostauto1h2():
    global money, autoclick, autoclick2, upgcheck1h2, mps
    if money < 555555 or upgcheck1h1 == 0:
        global boostafford1h2
        boostbutton1h2.destroy()
        master.bell()
        boostafford1h2 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        master.after(500, norequirements1h2)
    else:
        money -= 555555
        autoclick = int(autoclick * 50) / 10
        upgcheck1h2 += 1
        mps += autoclick2 * 18
        mpstkinter.set("MPS: " + str(mps))
        boostbutton1h2.destroy()
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=2, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                    int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                  int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)


def norequirements1h2():
    global boostbutton1h2, boostafford1h2
    boostafford1h2.destroy()
    boostbutton1h2 = Button(frame2, text="Experienced Clickers (Costs: $555555)", width=35,
                            command=boostauto1h2)
    boostbutton1h2.grid(
            row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=2, sticky=E)


def deduction1():
    global money, autoclick, autoclick2, autoprice, counterfeit, printmoney, sharecrash, mps, inc
    if money < int(autoprice):
        global incafford1
        incbutton1.destroy()
        master.bell()
        incafford1 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford1.grid(row=0, column=0, sticky=W)
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
        autopricemillion = round((float(str(autoprice)[:-7]) / 10), 1)
        if len(str(autoprice)) <= 11:
            autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricemillion) + "m)")
        else:
            autopricebillion = round((float(str(autopricemillion)[:-4]) / 10), 1)
            if len(str(autoprice)) <= 14:
                autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricebillion) + "b)")
            else:
                autopricetrillion = round((float(str(autopricebillion)[:-4]) / 10), 1)
                if len(str(autoprice)) <= 17:
                    autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricetrillion) + "t)")
                else:
                    autopricequadrillion = round((float(str(autopricetrillion)[:-4]) / 10), 1)
                    if len(str(autoprice)) <= 20:
                        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricequadrillion) + "q)")
                    else:
                        autopricequintillion = round((float(str(autopricequadrillion)[:-4]) / 10), 1)
                        autopricetkinter.set("Auto-Clicker (Costs : $" + str(autopricequintillion) + "Q)")


def cannotafford1():
    global incafford1, incbutton1
    incafford1.destroy()
    incbutton1 = Button(frame1, textvariable=autopricetkinter, width=35, command=deduction1)
    incbutton1.grid(row=0, column=0, sticky=W)


# MONEY PRINTER
def boostauto2h1():
    global money, printmoney, printmoney2, upgcheck2h1, mps
    if money < 42000 or printmoney2 == 0:
        global boostafford2h1
        boostbutton2h1.destroy()
        master.bell()
        boostafford2h1 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        master.after(500, norequirements2h1)
    else:
        money -= 42000
        printmoney = int(float(printmoney * 15) / 10)
        upgcheck2h1 += 1
        mps += printmoney2 * 2
        mpstkinter.set("MPS: " + str(mps))
        boostbutton2h1.destroy()
        clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2, sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=2, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
                            sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)


def norequirements2h1():
    global boostbutton2h1
    boostafford2h1.destroy()
    boostbutton2h1 = Button(frame2, text="Unofficial Printer License (Costs: $42000)", width=35,
                            command=boostauto2h1)
    boostbutton2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)


def boostauto2h2():
    global money, printmoney, printmoney2, upgcheck2h2, mps
    if money < 7777777 or upgcheck2h1 == 0:
        global boostafford2h2
        boostbutton2h2.destroy()
        master.bell()
        boostafford2h2 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        master.after(500, norequirements2h2)
    else:
        money -= 7777777
        printmoney = int(float(printmoney * 50) / 10)
        upgcheck2h2 += 1
        mps += printmoney2 * 18
        mpstkinter.set("MPS: " + str(mps))
        boostbutton2h2.destroy()
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)


def norequirements2h2():
    global boostbutton2h2
    boostafford2h2.destroy()
    boostbutton2h2 = Button(frame2, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
    boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                     int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)


def deduction2():
    global money, printmoney, printmoney2, printprice, sharecrash, counterfeit, autoclick, mps, inc
    if money < int(printprice):
        global incafford2
        incbutton2.destroy()
        master.bell()
        incafford2 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford2.grid(row=2, column=0, sticky=W)
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
        printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
    else:
        printpricemillion = round((float(str(printprice)[:-7]) / 10), 1)
        if len(str(printprice)) <= 11:
            printpricetkinter.set("Money Printer (Costs: $" + str(printpricemillion) + "m)")
        else:
            printpricebillion = round((float(str(printpricemillion)[:-4]) / 10), 1)
            if len(str(printprice)) <= 14:
                printpricetkinter.set("Money Printer (Costs: $" + str(printpricebillion) + "b)")
            else:
                printpricetrillion = round((float(str(printpricebillion)[:-4]) / 10), 1)
                if len(str(printprice)) <= 17:
                    printpricetkinter.set("Money Printer (Costs: $" + str(printpricetrillion) + "t)")
                else:
                    printpricequadrillion = round((float(str(printpricetrillion)[:-4]) / 10), 1)
                    if len(str(printprice)) <= 20:
                        printpricetkinter.set("Money Printer (Costs: $" + str(printpricequadrillion) + "q)")
                    else:
                        printpricequintillion = round((float(str(printpricequadrillion)[:-4]) / 10), 1)
                        printpricetkinter.set("Money Printer (Costs : $" + str(printpricequintillion) + "Q)")


def cannotafford2():
    global incafford2, incbutton2
    incafford2.destroy()
    incbutton2 = Button(frame1, textvariable=printpricetkinter, width=35, command=deduction2)
    incbutton2.grid(row=2, column=0, sticky=W)


# COUNTERFEIT COMPANY
def boostauto3():
    global money, counterfeit, counterfeit2, upgcheck3, mps
    if money < 2133748 or counterfeit2 == 0:
        global boostafford3
        boostbutton3.destroy()
        master.bell()
        boostafford3 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=2, sticky=E)
        master.after(500, norequirements3)
    else:
        money -= 2133748
        counterfeit = int(counterfeit * 15) / 10
        mps += counterfeit2 * 2
        mpstkinter.set("MPS: " + str(mps))
        upgcheck3 += 1
        boostbutton3.destroy()
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)


def norequirements3():
    global boostbutton3
    boostafford3.destroy()
    boostbutton3 = Button(frame2, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                          command=boostauto3)
    boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                   int(clickupgcheck2))), column=2, sticky=E)


def deduction3():
    global money, counterfeit, counterfeit2, counterfeitprice, sharecrash, printmoney, autoclick, mps, inc
    if money < int(counterfeitprice):
        global incafford3
        incbutton3.destroy()
        master.bell()
        incafford3 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford3.grid(row=4, column=0, sticky=W)
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
        counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
    else:
        counterfeitpricemillion = round((float(str(counterfeitprice)[:-7]) / 10), 1)
        if len(str(counterfeitprice)) <= 11:
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitpricemillion) + "m)")
        else:
            counterfeitpricebillion = round((float(str(counterfeitpricemillion)[:-4]) / 10), 1)
            if len(str(counterfeitprice)) <= 14:
                counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitpricebillion) + "b)")
            else:
                counterfeitpricetrillion = round((float(str(counterfeitpricebillion)[:-4]) / 10), 1)
                if len(str(counterfeitprice)) <= 17:
                    counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitpricetrillion) + "t)")
                else:
                    counterfeitpricequadrillion = round((float(str(counterfeitpricetrillion)[:-4]) / 10), 1)
                    if len(str(counterfeitprice)) <= 20:
                        counterfeitpricetkinter.set("Counterfeit Company (Costs: $" +
                                                    str(counterfeitpricequadrillion) + "q)")
                    else:
                        counterfeitpricequintillion = round((float(str(counterfeitpricequadrillion)[:-4]) / 10), 1)
                        counterfeitpricetkinter.set("Counterfeit Company (Costs : $" +
                                                    str(counterfeitpricequintillion) + "Q)")


def cannotafford3():
    global incafford3, incbutton3
    incafford3.destroy()
    incbutton3 = Button(frame1, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
    incbutton3.grid(row=4, column=0, sticky=W)


# SHAREMARKET CRASH
def boostauto4():
    global money, sharecrash, sharecrash2, upgcheck4, mps
    if money < 12345678 or sharecrash2 == 0:
        global boostafford4
        boostbutton4.destroy()
        master.bell()
        boostafford4 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
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
    boostbutton4 = Button(frame2, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                          command=boostauto4)
    boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                   int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)


def deduction4():
    global money, sharecrash, sharecrash2, shareprice, counterfeit, printmoney, autoclick, mps, inc
    if money < int(shareprice):
        global incafford4
        incbutton4.destroy()
        master.bell()
        incafford4 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford4.grid(row=6, column=0, sticky=W)
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
        sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
    else:
        sharepricemillion = round((float(str(shareprice)[:-7]) / 10), 1)
        if len(str(shareprice)) <= 11:
            sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricemillion) + "m)")
        else:
            sharepricebillion = round((float(str(sharepricemillion)[:-4]) / 10), 1)
            if len(str(shareprice)) <= 14:
                sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricebillion) + "b)")
            else:
                sharepricetrillion = round((float(str(sharepricebillion)[:-4]) / 10), 1)
                if len(str(shareprice)) <= 17:
                    sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricetrillion) + "t)")
                else:
                    sharepricequadrillion = round((float(str(sharepricetrillion)[:-4]) / 10), 1)
                    if len(str(shareprice)) <= 20:
                        sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricequadrillion) + "q)")
                    else:
                        sharepricequintillion = round((float(str(sharepricequadrillion)[:-4]) / 10), 1)
                        sharepricetkinter.set("Sharemarket Crash (Costs : $" + str(sharepricequintillion) + "Q)")


def cannotafford4():
    global incafford4, incbutton4
    incafford4.destroy()
    incbutton4 = Button(frame1, textvariable=sharepricetkinter, width=35, command=deduction4)
    incbutton4.grid(row=6, column=0, sticky=W)


# BANK HEIST
def boostauto5():
    global money, bankheist, bankheist2, upgcheck5, mps
    if money < 91215000 or bankheist2 == 0:
        global boostafford5
        boostbutton5.destroy()
        master.bell()
        boostafford5 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)
        master.after(500, norequirements4)
    else:
        money -= 91215000
        bankheist = int(bankheist * 15) / 10
        mps += bankheist2 * 2
        mpstkinter.set("MPS: " + str(mps))
        upgcheck5 += 1
        boostbutton5.destroy()


def norequirements5():
    global boostbutton5
    boostafford5.destroy()
    boostbutton5 = Button(frame2, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                          command=boostauto4)
    boostbutton5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                   int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                      column=2, sticky=E)


def deduction5():
    global money, bankheist, bankheist2, bankprice, counterfeit, printmoney, autoclick, mps, inc
    if money < int(bankprice):
        global incafford5
        incbutton5.destroy()
        master.bell()
        incafford5 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford5.grid(row=8, column=0, sticky=W)
        master.after(500, cannotafford5)
    else:
        money -= int(bankprice)
        bankheist += (1 + upgcheck5 * 2)
        bankheist2 += 1
        mps += 2015 * (1 + upgcheck5 * 2)
        mpstkinter.set("MPS: " + str(mps))
        bankheisttkinter.set("Sharemarket Crashes Amount: " + str(bankheist2))
        bankprice = int(181700 * (math.pow(1.2, bankheist2)))
        bankpricechoice()
        inc = int(inc + math.pow(int(clickupgcheck2 * (autoclick + printmoney + counterfeit + bankheist)), 1.01))
        if bankheist == 1 and counterfeit == 0 and printmoney == 0 and autoclick == 0:
            automoney()


def bankpricechoice():
    if len(str(bankprice)) <= 8:
        bankpricetkinter.set("Sharemarket Crash (Costs: $" + str(bankprice) + ")")
    else:
        bankpricemillion = round((float(str(bankprice)[:-7]) / 10), 1)
        if len(str(bankprice)) <= 11:
            bankpricetkinter.set("Sharemarket Crash (Costs: $" + str(bankpricemillion) + "m)")
        else:
            bankpricebillion = round((float(str(bankpricemillion)[:-4]) / 10), 1)
            if len(str(bankprice)) <= 14:
                bankpricetkinter.set("Sharemarket Crash (Costs: $" + str(bankpricebillion) + "b)")
            else:
                bankpricetrillion = round((float(str(bankpricebillion)[:-4]) / 10), 1)
                if len(str(bankprice)) <= 17:
                    bankpricetkinter.set("Sharemarket Crash (Costs: $" + str(bankpricetrillion) + "t)")
                else:
                    bankpricequadrillion = round((float(str(bankpricetrillion)[:-4]) / 10), 1)
                    if len(str(bankprice)) <= 20:
                        bankpricetkinter.set("Sharemarket Crash (Costs: $" + str(bankpricequadrillion) + "q)")
                    else:
                        bankpricequintillion = round((float(str(bankpricequadrillion)[:-4]) / 10), 1)
                        bankpricetkinter.set("Sharemarket Crash (Costs : $" + str(bankpricequintillion) + "Q)")


def cannotafford5():
    global incafford5, incbutton5
    incafford5.destroy()
    incbutton5 = Button(frame1, textvariable=bankpricetkinter, width=35, command=deduction4)
    incbutton5.grid(row=8, column=0, sticky=W)


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
        clickafford1 = Label(frame2, text="%s" % norequirements, width=35)
        clickafford1.grid(row=0, column=2, sticky=E)
        master.after(500, norequirementsc1)
    else:
        money -= 2100
        inc += 2
        inctkinter.set("+" + str(inc) + " money!")
        clickupgcheck1 += 1
        clickbooster1.destroy()
        boostbutton1h1.grid(row=int(1 - int(clickupgcheck1)), column=2, sticky=E)
        boostbutton2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2, sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=2, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
                            sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)


def norequirementsc1():
    global clickbooster1
    clickafford1.destroy()
    clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
    clickbooster1.grid(row=0, column=2, sticky=E)


def clickboost2():
    global money, inc, mps, clickupgcheck2
    if money < 200000 or clickupgcheck1 == int(0):
        global clickafford2
        clickbooster2.destroy()
        clickafford2 = Label(frame2, text="%s" % norequirements, width=35)
        clickafford2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2,
                          sticky=E)
        master.after(500, norequirementsc2)
    else:
        money -= 200000
        inc += mps / 10
        inctkinter.set("+" + str(inc) + " money!")
        clickupgcheck2 += 1
        clickbooster2.destroy()
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=2, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
                            sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)


def norequirementsc2():
    global clickbooster2
    clickafford2.destroy()
    clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35,
                           command=clickboost2)
    clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2,
                       sticky=E)


# AUTOMATIC MONEY
def automoney():
    global money, autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, timeplay
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
            timevar.set("Total time: " + str(timeplay))
            totalclicksvar.set("Total clicks: " + str(totalclicks))
        bugfixer()
        timeplay += 1
    money += float(mps) / 10
    check += 1
    automoneychoice()


# AUTOMATIC MONEY (MILLIONS)
def automoney2():
    global money, autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, timeplay, money, \
        moneymillion, templist1
    if len(str(money)) >= 8:
        moneymillion = round((float(str(money)[:-7]) / 10), 1)
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
                timevar.set("Total time: " + str(timeplay))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            timeplay += 1
            templist1.append(moneymillion)
            if len(templist1) > 2:
                templist1.reverse()
                templist1.pop()
                templist1.reverse()
            if float(templist1[1]) != float(templist1[0]):
                moneymillion += float(templist1[1] - templist1[0]) / 10
        bugfixer()
        money += mps
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (BILLIONS)
def automoney3():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, timeplay, \
        moneybillion, moneymillion, money, templist2
    if len(str(moneymillion)) >= 5:
        moneybillion = round((float(str(moneymillion)[:-5]) / 10), 1)
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
                timevar.set("Total time: " + str(timeplay))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            timeplay += 1
            templist2.append(moneybillion)
            if len(templist2) > 2:
                templist2.reverse()
                templist2.pop()
                templist2.reverse()
            if float(templist2[1]) != float(templist2[0]):
                moneybillion += float(templist2[1] - templist2[0]) / 10
        bugfixer()
        moneymillion = float(math.floor((moneymillion + float(mps) / 10 ** 6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (TRILLIONS)
def automoney4():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, timeplay, \
        moneytrillion, moneybillion, moneymillion, money, templist3
    if len(str(moneybillion)) >= 5:
        moneytrillion = round((float(str(moneybillion)[:-5]) / 10), 1)
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
                timevar.set("Total time: " + str(timeplay))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            timeplay += 1
            templist3.append(moneytrillion)
            if len(templist3) > 2:
                templist3.reverse()
                templist3.pop()
                templist3.reverse()
            if float(templist3[1]) != float(templist3[0]):
                moneytrillion += float(templist3[1] - templist3[0]) / 10
        bugfixer()
        moneybillion = float(math.floor((moneybillion + float(mps) / 10 ** 9) * 10))
        moneymillion = float(math.floor((moneymillion + float(mps) / 10 ** 6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (QUADRILLIONS)
def automoney5():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, timeplay, \
        moneyquadrillion, moneytrillion, moneybillion, moneymillion, money, templist4
    if len(str(moneytrillion)) >= 5:
        moneyquadrillion = round((float(str(moneytrillion)[:-5]) / 10), 1)
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
                timevar.set("Total time: " + str(timeplay))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            timeplay += 1
            templist4.append(moneyquadrillion)
            if len(templist4) > 2:
                templist4.reverse()
                templist4.pop()
                templist4.reverse()
            if float(templist4[1]) != float(templist4[0]):
                moneyquadrillion += float(templist4[1] - templist4[0]) / 10
        bugfixer()
        moneytrillion = float(math.floor((moneytrillion + float(mps) / 10 ** 12) * 10))
        moneybillion = float(math.floor((moneybillion + float(mps) / 10 ** 9) * 10))
        moneymillion = float(math.floor((moneymillion + float(mps) / 10 ** 6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (QUINTILLIONS)
def automoney6():
    global autoclick, autoclick2, autoprice, printmoney, printmoney2, printprice, counterfeit, counterfeit2, \
        counterfeitprice, sharecrash, sharecrash2, shareprice, mps, check, goldbutton, goldcheck, timeplay, \
        moneyquintillion, moneyquadrillion, moneytrillion, moneybillion, moneymillion, money, templist5
    if len(str(moneyquadrillion)) >= 5:
        moneyquintillion = round((float(str(moneyquadrillion)[:-5]) / 10), 1)
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
                timevar.set("Total time: " + str(timeplay))
                totalclicksvar.set("Total clicks: " + str(totalclicks))
            timeplay += 1
            templist5.append(moneyquintillion)
            if len(templist5) > 2:
                templist5.reverse()
                templist5.pop()
                templist5.reverse()
            if float(templist5[1]) != float(templist5[0]):
                moneyquintillion += float(templist5[1] - templist5[0]) / 10
        bugfixer()
        moneyquadrillion = float(math.floor(moneyquadrillion + float(mps) / 10 ** 15) * 10)
        moneytrillion = float(math.floor((moneytrillion + float(mps) / 10 ** 12) * 10))
        moneybillion = float(math.floor((moneybillion + float(mps) / 10 ** 9) * 10))
        moneymillion = float(math.floor((moneymillion + float(mps) / 10 ** 6) * 10))
        money += mps
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# SAVING GAME
def savegame():
    username = g.name.split('_')[1].split('.')[0]
    xbuildings = ["auto", int(autoclick2), "print", int(printmoney2), "counter", int(counterfeit2), "shares",
                  int(sharecrash2)]
    xmisc = ["time", int(timeplay), "clicks", int(totalclicks)]
    xmoney = ["quintillion", int(moneyquintillion), "quadrillion", int(str(moneyquadrillion)[-5:-2]), "trillion",
              int(str(moneytrillion)[-5:-2]), "billion", int(str(moneybillion)[-5:-2]), "million",
              int(str(moneymillion)[-5:-2]), "money", float(str(money)[-8:])]
    xupgrades = ["upg1h1", int(upgcheck1h1), "upg1h2", int(upgcheck1h2), "upg2h1", int(upgcheck2h1), "upg2h2",
                 int(upgcheck2h2), "upg3", int(upgcheck3), "upg4", int(upgcheck4), "cupg1", int(clickupgcheck1),
                 "cupg2", int(clickupgcheck2)]
    savefilebuildings = str((str("_".join(str(v) for v in xbuildings))).encode("hex") + ";")
    savefilemisc = str((str("_".join(str(v) for v in xmisc))).encode("hex") + ";")
    savefilemoney = str((str("_".join(str(v) for v in xmoney))).encode("hex") + ";")
    savefileupgrades = str((str("_".join(str(v) for v in xupgrades))).encode("hex") + ";")
    savefile = str(savefilebuildings + savefilemisc + savefilemoney + savefileupgrades)
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
    if username is None:
        username = g.name.split('_')[1].split('.')[0]
    x = ["auto", int(0), "print", int(0), "counter", int(0), "shares", int(0), "upg1h1", int(0), "upg1h2", int(0),
         "upg2h1", int(0), "upg2h2", int(0), "upg3", int(0), "upg4", int(0), "cupg1", int(0), "cupg2", int(0),
         "quintillion", int(0), "quadrillion", int(0), "trillion", int(0), "billion", int(0), "million", int(0),
         "money", float(0), "time", int(0), "clicks", int(0)]
    resetfile = str((str("_".join(str(v) for v in x))).encode("hex") + ";")
    f = open("savefile_" + username + ".txt", "w")
    f.write(str(resetfile))
    f.close()


# UPGRADES WINDOW
def showupgrades():
    global upgbuttoncheck
    upgbuttoncheck = True
    global clickbooster1, boostbutton1h1, boostbutton2h1, clickbooster2, boostbutton1h2, boostbutton3, \
        boostbutton2h2, boostbutton4, boostbutton5, exitupgrades
    upgrades.destroy()
    if clickupgcheck1 == int(0):
        clickbooster1 = Button(frame2, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
        clickbooster1.grid(row=0, column=0, sticky=E)
    if upgcheck1h1 == int(0):
        boostbutton1h1 = Button(frame2, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
        boostbutton1h1.grid(row=int(1 - int(clickupgcheck1)), column=0, sticky=E)
    if upgcheck2h1 == int(0):
        boostbutton2h1 = Button(frame2, text="Unofficial Printer License (Costs: $42000)", width=35,
                                command=boostauto2h1)
        boostbutton2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=0, sticky=E)
    if clickupgcheck2 == int(0):
        clickbooster2 = Button(frame2, text="Stainless Steel Button (Costs: $200000)", width=35,
                               command=clickboost2)
        clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=0,
                           sticky=E)
    if upgcheck1h2 == int(0):
        boostbutton1h2 = Button(frame2, text="Experienced Clickers (Costs: $555555)", width=35,
                                command=boostauto1h2)
        boostbutton1h2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) +
                                         int(clickupgcheck2))), column=0, sticky=E)
    if upgcheck3 == int(0):
        boostbutton3 = Button(frame2, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                              command=boostauto3)
        boostbutton3.grid(
                row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                             int(clickupgcheck2))), column=0, sticky=E)
    if upgcheck2h2 == int(0):
        boostbutton2h2 = Button(frame2, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
    if upgcheck4 == int(0):
        boostbutton4 = Button(frame2, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                              command=boostauto4)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
    if upgcheck5 == int(0):
        boostbutton5 = Button(frame2, text="Bank Blueprints (Costs: $91215000)", width=35, command=boostauto5)
        boostbutton5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=0, sticky=E)
    exitupgrades = Button(master, text="Hide Upgrades", command=hideupgrades)
    if statscheck:
        global hidestatsbutton
        hidestatsbutton.grid(row=2, column=0, sticky=W)
        exitupgrades.grid(row=2, column=2, sticky=E)
        resetbutton.grid(row=4, column=0, sticky=W)
        savebutton.grid(row=4, column=2, sticky=E)
        reportbutton.grid(row=5, column=1)
    else:
        statsbutton.grid(row=2, column=0, sticky=W)
        exitupgrades.grid(row=2, column=2, sticky=E)
        resetbutton.grid(row=3, column=0, sticky=W)
        savebutton.grid(row=3, column=2, sticky=E)
        reportbutton.grid(row=4, column=1)


def hideupgrades():
    global exitupgrades, upgbuttoncheck
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
    if upgcheck5 == int(0):
        boostbutton5.destroy()
    global upgrades
    upgrades = Button(frame2, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=0, column=0, rowspan=8, sticky=E)
    exitupgrades.destroy()
    if statscheck:
        hidestatsbutton.grid(row=2, column=0, sticky=W)
        resetbutton.grid(row=4, column=0, sticky=W)
        savebutton.grid(row=4, column=2, sticky=E)
        reportbutton.grid(row=5, column=1)
    elif not statscheck:
        statsbutton.grid(row=2, column=0, sticky=W)
        resetbutton.grid(row=3, column=0, sticky=W)
        savebutton.grid(row=3, column=2, sticky=E)
        reportbutton.grid(row=4, column=1)


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
    global clickcolourcheck
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
    mps = float(mps) / 77
    mpstkinter = ("MPS: " + str(mps))


def main():
    # BUTTONS, LABELS AND ENTRIES
    global incbutton1, incbutton2, incbutton3, incbutton4, incbutton5, upgrades, resetbutton, savebutton, clickbutton, \
        statsbutton, reportbutton, canvas1, frame1, frame2
    background = Label(master, image=img1)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    background.image = img1

    canvas1 = Canvas(master, height=200, width=200)
    canvas1.grid(row=1, column=0, sticky=W)

    frame1 = Frame(canvas1, bg="white")
    canvas1.create_window((0, 0), window=frame1, anchor='ne')

    frame2 = Frame(master, bg="white")
    frame2.grid(row=1, column=2, sticky=N+S+E+W)

    upgrades = Button(frame2, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=0, column=0, rowspan=2, sticky=E)

    moneylabel = Label(master, textvariable=moneytkinter)
    moneylabel.grid(row=0, column=0, sticky=W)

    mpslabel = Label(master, textvariable=mpstkinter)
    mpslabel.grid(row=0, column=2, sticky=E)

    clickbutton = Button(master, textvariable=inctkinter, height=6, width=18, command=collectmoney, bg="red")
    clickbutton.grid(row=1, column=1)

    incbutton1 = Button(frame1, textvariable=autopricetkinter, width=35, command=deduction1)
    incbutton1.grid(row=0, column=0)

    checklabel1 = Label(frame1, textvariable=autoclicktkinter, width=35)
    checklabel1.grid(row=1, column=0)

    incbutton2 = Button(frame1, textvariable=printpricetkinter, width=35, command=deduction2)
    incbutton2.grid(row=2, column=0)

    checklabel2 = Label(frame1, textvariable=printmoneytkinter, width=35)
    checklabel2.grid(row=3, column=0)

    incbutton3 = Button(frame1, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
    incbutton3.grid(row=4, column=0)

    checklabel3 = Label(frame1, textvariable=counterfeittkinter, width=35)
    checklabel3.grid(row=5, column=0)

    incbutton4 = Button(frame1, textvariable=sharepricetkinter, width=35, command=deduction4)
    incbutton4.grid(row=6, column=0)

    checklabel4 = Label(frame1, textvariable=sharecrashtkinter, width=35)
    checklabel4.grid(row=7, column=0)

    incbutton5 = Button(frame1, textvariable=bankpricetkinter, width=35, command=deduction5)
    incbutton5.grid(row=8, column=0)

    checklabel5 = Label(frame1, textvariable=bankheisttkinter, width=35)
    checklabel5.grid(row=9, column=0)

    statsbutton = Button(master, text="Stats", width=10, command=statsexpand)
    statsbutton.grid(row=2, column=0)

    resetbutton = Button(master, text="Reset Game", width=10, command=resetgame)
    resetbutton.grid(row=3, column=0)

    savebutton = Button(master, text="Save Game", width=10, command=savegame)
    savebutton.grid(row=3, column=2, sticky=E)

    reportbutton = Button(master, text='Report Issue to Github', width=20, command=report)
    reportbutton.grid(row=4, column=1)

    scrollbar1 = Scrollbar(canvas1, orient="vertical", command=canvas1.yview)
    scrollbar1.pack(side="left", fill="y")
    canvas1.configure(yscrollcommand=scrollbar1.set)
    canvas1.configure(scrollregion=canvas1.bbox("all"), width=200, height=200)


thread = threading.Thread(target=master.mainloop)
thread.start()

while True:
    if signincheck == signinvalue:
        try:
            check = False
            upgbuttoncheck = False
            goldcheck = False
            statscheck = False
            animate = 0
            totalclicks = int(gmisc[3])
            timeplay = int(gmisc[1])
            click = 0
            clickcolourcheck = 1
            upgcheck1h1 = int(gupgrades[1])
            upgcheck1h2 = int(gupgrades[3])
            upgcheck2h1 = int(gupgrades[5])
            upgcheck2h2 = int(gupgrades[7])
            upgcheck3 = int(gupgrades[9])
            upgcheck4 = int(gupgrades[11])
            upgcheck5 = int(gupgrades[13])
            clickupgcheck1 = int(gupgrades[15])
            clickupgcheck2 = int(gupgrades[17])
            money = float(str(gmoney[1] + gmoney[3] + gmoney[5] + gmoney[7] + gmoney[9] + gmoney[11]))
            if len(str(money)) < 8:
                moneycheck = "0"
            else:
                moneycheck = str(money)[:1]
            moneymillion = round(float(str(gmoney[1] + gmoney[3] + gmoney[5] + gmoney[7] + gmoney[9]) + "." +
                                       moneycheck), 1)
            if len(str(moneymillion)) < 5:
                moneymillioncheck = "0"
            else:
                moneymillioncheck = str(moneymillion)[:1]
            moneybillion = round(float(str(gmoney[1] + gmoney[3] + gmoney[5] + gmoney[7]) + "." + moneymillioncheck),
                                 1)
            if len(str(moneybillion)) < 5:
                moneybillioncheck = "0"
            else:
                moneybillioncheck = str(moneybillion)[:1]
            moneytrillion = round(float(str(gmoney[1] + gmoney[3] + gmoney[5]) + "." + moneybillioncheck), 1)
            if len(str(moneytrillion)) < 5:
                moneytrillioncheck = "0"
            else:
                moneytrillioncheck = str(moneytrillion)[:1]
            moneyquadrillion = round(float(str(gmoney[1] + gmoney[3]) + "." + moneytrillioncheck), 1)
            if len(str(moneyquadrillion)) < 5:
                moneyquadrillioncheck = "0"
            else:
                moneyquadrillioncheck = str(moneyquadrillion)[:1]
            moneyquintillion = round(float(str(gmoney[1]) + "." + moneyquadrillioncheck), 1)
            moneytkinter = StringVar()
            if moneymillion == 0:
                moneytkinter.set("Balance: $" + str(money))
            elif moneybillion == 0:
                moneytkinter.set("Balance: $" + str(moneymillion) + "m")
            elif moneytrillion == 0:
                moneytkinter.set("Balance: $" + str(moneybillion) + "b")
            elif moneyquadrillion == 0:
                moneytkinter.set("Balance: $" + str(moneytrillion) + "t")
            elif moneyquintillion == 0:
                moneytkinter.set("Balance: $" + str(moneyquadrillion) + "q")
            else:
                moneytkinter.set("Balance: $" + str(moneyquintillion) + "Q")
            autoclick = int((gbuildings[1] * 18 * int(gupgrades[3])) + (gbuildings[1] * 2 * int(gupgrades[1])) + 
                            gbuildings[1])
            autoclick2 = int(gbuildings[1])
            autoclicktkinter = StringVar()
            autoclicktkinter.set("Auto-Clickers Amount: " + str(gbuildings[1]))
            autoprice = int(20 * (math.pow(1.2, int(gbuildings[1]))))
            autopricetkinter = StringVar()
            autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
            printmoney = int((gbuildings[3] * 2 * int(gupgrades[5])) + gbuildings[3])
            printmoney2 = int(gbuildings[3])
            printmoneytkinter = StringVar()
            printmoneytkinter.set("Money Printers Amount: " + str(gbuildings[3]))
            printprice = int(375 * (math.pow(1.2, int(gbuildings[3]))))
            printpricetkinter = StringVar()
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            counterfeit = int((gbuildings[5] * 2 * int(gupgrades[9])) + gbuildings[5])
            counterfeit2 = int(gbuildings[5])
            counterfeittkinter = StringVar()
            counterfeittkinter.set("Counterfeit Companies Amount: " + str(gbuildings[5]))
            counterfeitprice = int(9001 * (math.pow(1.2, int(gbuildings[5]))))
            counterfeitpricetkinter = StringVar()
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
            sharecrash = int((gbuildings[7] * 2 * int(gupgrades[11])) + gbuildings[7])
            sharecrash2 = int(gbuildings[7])
            sharecrashtkinter = StringVar()
            sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
            shareprice = int(42000 * (math.pow(1.2, int(gbuildings[7]))))
            sharepricetkinter = StringVar()
            sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
            bankheist = int((gbuildings[9]) * 2 * int(gupgrades[13]) + gbuildings[9])
            bankheist2 = int(gbuildings[9])
            bankheisttkinter = StringVar()
            bankheisttkinter.set("Bank Heists Amount: " + str(bankheist2))
            bankprice = int(181700 * (math.pow(1.2, bankheist2)))
            bankpricetkinter = StringVar()
            bankpricetkinter.set("Bank Heist (Costs: $" + str(bankprice) + ")")
            mps = autoclick + printmoney + counterfeit + sharecrash
            mpstkinter = StringVar()
            mpstkinter.set("MPS: " + str(mps))
            inc = int(1 + (int(gupgrades[15]) * 2) + int(gupgrades[17]) * (mps / 10))
            inctkinter = StringVar()
            inctkinter.set("+" + str(inc) + " money!")
            templist1 = [moneymillion] * 2
            templist2 = [moneybillion] * 2
            templist3 = [moneytrillion] * 2
            templist4 = [moneyquadrillion] * 2
            templist5 = [moneyquintillion] * 2
            if gupgrades[13] == int(1):
                clickbooster1.destroy()
            if gupgrades[1] == int(1):
                boostbutton1h1.destroy()
            if gupgrades[5] == int(1):
                boostbutton2h1.destroy()
            if gupgrades[15] == int(1):
                clickbooster2.destroy()
            if gupgrades[3] == int(1):
                boostbutton1h2.destroy()
            if gupgrades[9] == int(1):
                boostbutton3.destroy()
            if gupgrades[7] == int(1):
                boostbutton2h2.destroy()
            if gupgrades[11] == int(1):
                boostbutton4.destroy()
            if mps >= 1:
                automoneychoice()
            main()
            break
        except NameError as e:
            print(e)
            signin()
