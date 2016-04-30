from tkinter import *
from random import *
from tkinter.messagebox import showerror
import math
import save_and_load
import game_model
import webbrowser

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
save_needed = False
main_laid_out = False
data_loaded = False
username = ''

game_state = None

print('Debug [Y/N]: ', end='')
debug = (input()[0].upper() == 'Y')

def log(*args):
    if debug:
        print(*args)

def savegame():
    global game_state
    log('savegame invoked')
    data = ["auto", game_state.autoclick2, "print", game_state.printmoney2, "counter", game_state.counterfeit2,
            "shares", game_state.sharecrash2, "bank", game_state.bankheist2, "upg1h1", game_state.upgcheck1h1,
            "upg1h2", game_state.upgcheck1h2, "upg2h1", game_state.upgcheck2h1, "upg2h2", game_state.upgcheck2h2,
            "upg3", game_state.upgcheck3, "upg4", game_state.upgcheck4, "upg5", game_state.upgcheck5,
            "cupg1", game_state.clickupgcheck1, "cupg2", game_state.clickupgcheck2, "money",
            float(str(game_state.money)[-8:]), "time", game_state.timeplay, "clicks",
            game_state.totalclicks, "lotto", game_state.lottoprice]

    save_and_load.encode_and_save(username, data)

    toplevel = Toplevel()
    msg = Message(toplevel, text="Game saved!")
    msg.pack()


def signin():
    global signincheck, game_state
    log('signin invoked')
    signincheck += 1

    def verifysignin():
        global username, game_state, save_needed
        username = unentry.get()
        if save_and_load.save_file_exists(username):
            global g2, signinvalue
            try:
                g2 = save_and_load.read_game_data(username)
                log('g2', g2)
            except IOError as ioe:
                log(ioe)
            save_and_load.encode_and_save(username, g2)
            game_state = game_model.GameState(g2)
            log('game_state', str(game_state))
            for i in [l, unentry, b1, b2]:
                i.destroy()

            signinvalue += 1
            save_needed = True
        else:
            showerror(title='Error!', message='Wrong Username.')

    def createaccount():
        global signinvalue, username, game_state, save_needed
        log("createaccount invoked")
        username = unentry.get()
        save_and_load.encode_and_save(username, data=None)
        try:
            g2 = save_and_load.read_game_data(username)
            game_state = game_model.GameState(g2)
            log('game_state', str(game_state))
        except IOError as ioe:
            log(ioe)
        signinvalue += 1
        save_needed = True

    l = Label(master, text='Please enter your username.')
    l.grid(row=1, column=1)
    unentry = Entry(master, show='')
    unentry.grid(row=2, column=1)
    b1 = Button(master, text='Log in', command=verifysignin)
    b1.grid(row=3, column=1)
    b2 = Button(master, text='Create account under username', command=createaccount)
    b2.grid(row=4, column=1)


def set_stats(state, clicksvar, timepassedvar, spentvar):
    log('set_stats  invoked')
    clicksvar.set("Total clicks: %s" % state.totalclicks)
    timepassedvar.set("Total time: %s" % state.timeplay)
    spentvar.set("Total money spent: %s" % state.get_totalspent())


def report():
    log('report invoked')
    webbrowser.open("https://github.com/DerpfacePython/Ways-to-NOT-make-money/issues/new", new=0, autoraise=True)


# BUG FIXER
def bugfixer():
    global game_state
    while game_state.mps > (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                            game_state.sharecrash * 969 + game_state.bankheist * 2015):
        if game_state.mps - 2015 >= (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                                     game_state.sharecrash * 969 + game_state.bankheist * 2015):
            game_state.bankheist += 1 + game_state.upgcheck5 * 2
            game_state.bankheist2 += 1
            bankheisttkinter.set(game_state.bankheist2)
            game_state.bankprice = int(42000 * (math.pow(1.1, game_state.bankheist2)))
            bankpricetkinter.set("Bank Heist (Costs: $%s)" % game_state.bankprice)
            continue

        elif game_state.mps - 969 >= (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                                      game_state.sharecrash * 969 + game_state.bankheist * 2015):
            game_state.sharecrash += 1 + game_state.upgcheck4 * 2
            game_state.sharecrash2 += 1
            sharecrashtkinter.set(game_state.sharecrash2)
            game_state.shareprice = int(42000 * (math.pow(1.4, game_state.sharecrash2)))
            sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % game_state.shareprice)
            continue
        elif game_state.mps - 321 >= (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                                      game_state.sharecrash * 969 + game_state.bankheist * 2015):
            game_state.counterfeit += 1 + game_state.upgcheck3 * 2
            game_state.counterfeit2 += 1
            counterfeittkinter.set(game_state.counterfeit2)
            game_state.counterprice = int(9001 * (math.pow(1.3, game_state.counterfeit2)))
            counterpricetkinter.set("Counterfeit Company (Costs: $%s)" % game_state.counterprice)
            continue
        elif game_state.mps - 15 >= (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                                     game_state.sharecrash * 969 + game_state.bankheist * 2015):
            game_state.printmoney += (1 + game_state.upgcheck2h1 * 2 + game_state.upgcheck2h2 * 18)
            game_state.printmoney2 += 1
            printmoneytkinter.set(game_state.printmoney2)
            game_state.printprice = int(375 * (math.pow(1.25, game_state.printmoney2)))
            printpricetkinter.set("Money Printer (Costs: $%s)" % game_state.printprice)
            continue
        else:
            game_state.autoclick += (1 + game_state.upgcheck1h1 * 2 + game_state.upgcheck1h2 * 18)
            game_state.autoclick2 += 1
            autoclicktkinter.set(game_state.autoclick2)
            game_state.autoprice = int(20 * (math.pow(1.15, game_state.autoclick2)))
            autopricetkinter.set("Auto-Clicker (Costs: $%s)" % game_state.autoprice)
            continue


# AUTO CLICKER
def boostauto1h1():
    global game_state
    log('ba1h1  invoked')
    if game_state.money < 5000 or game_state.autoclick2 == 0:
        global boostafford1h1
        boostbutton1h1.destroy()
        master.bell()
        boostafford1h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=2 - game_state.clickupgcheck1, column=3, sticky=E)
        master.after(500, norequirements1h1)
    else:
        game_state.money -= 5000
        game_state.autoclick = float(game_state.autoclick * 15) / 10
        game_state.upgcheck1h1 += 1
        game_state.mps += float(game_state.autoclick2) * 1.5
        mpstkinter.set("MPS: %s" % game_state.mps)
        boostbutton1h1.destroy()
        boostbutton2h1.grid(row=3 - (game_state.upgcheck1h1 + game_state.clickupgcheck1), column=3, sticky=E)
        clickbooster2.grid(row=4 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1),
                           column=3, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1 +
                                     game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                            column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirements1h1():
    global boostafford1h1, boostbutton1h1
    log('nq1h1  invoked')
    boostafford1h1.destroy()
    boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
    boostbutton1h1.grid(row=2 - game_state.clickupgcheck1, column=3, sticky=E)


def boostauto1h2():
    global game_state
    log('ba1h2  invoked')
    if game_state.money < 555555 or game_state.upgcheck1h1 == 0:
        global boostafford1h2
        boostbutton1h2.destroy()
        master.bell()
        boostafford1h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h2.grid(row=5 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1 +
                                     game_state.clickupgcheck2), column=3, sticky=E)
        master.after(500, norequirements1h2)
    else:
        game_state.money -= 555555
        game_state.autoclick = float(game_state.autoclick * 50) / 10
        game_state.upgcheck1h2 += 1
        game_state.mps += float(game_state.autoclick2) * 6
        mpstkinter.set("MPS: %s" % game_state.mps)
        boostbutton1h2.destroy()
        boostbutton3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.upgcheck4 + game_state.clickupgcheck1 +
                                     game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirements1h2():
    log('nq1h2 invoked')
    global boostbutton1h2, boostafford1h2
    boostafford1h2.destroy()
    boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35,
                            command=boostauto1h2)
    boostbutton1h2.grid(row=5 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1 +
                                 game_state.clickupgcheck2), column=3, sticky=E)


def deduction1():
    log('deduction1 invoked')
    global game_state
    if game_state.money < int(game_state.autoprice):
        global incafford1
        incbutton1.destroy()
        master.bell()
        incafford1 = Label(master, text="%s" % cannotafford, width=33)
        incafford1.grid(row=1, column=0, sticky=W)
        master.after(500, cannotafford1)

    else:
        game_state.money -= game_state.autoprice
        game_state.autoclick += (1 + game_state.upgcheck1h1 * 2 + game_state.upgcheck1h2 * 18) * game_state.multiplier
        game_state.autoclick2 += game_state.multiplier
        game_state.mps += (1 + game_state.upgcheck1h1 * 2 + game_state.upgcheck1h2 * 18) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        autompstkinter.set("Auto-Clickers MPS: " + str(game_state.autoclick))
        autoclicktkinter.set(game_state.autoclick2)
        game_state.autoprice = int(20 * (math.pow(1.15, game_state.autoclick2)))
        autopricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.autoclick, 1.01)
    if (game_state.autoclick == 1 and game_state.bankheist == 0 and game_state.sharecrash == 0 and
        game_state.counterfeit == 0 and game_state.printmoney == 0):
        automoney()


def cannotafford1():
    log('ca1  invoked')
    global incafford1, incbutton1
    incafford1.destroy()
    incbutton1 = Button(master, textvariable=autopricetkinter, width=33, command=deduction1)
    incbutton1.grid(row=1, column=0, sticky=W)


# MONEY PRINTER
def boostauto2h1():
    global game_state
    log('ba2h1 invoked')
    if game_state.money < 42000 or game_state.printmoney2 == 0:
        global boostafford2h1
        boostbutton2h1.destroy()
        master.bell()
        boostafford2h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=3 - (game_state.upgcheck1h1 + game_state.clickupgcheck1), column=3, sticky=E)
        master.after(500, norequirements2h1)
    else:
        game_state.money -= 42000
        game_state.printmoney = float(game_state.printmoney * 15) / 10
        game_state.upgcheck2h1 += 1
        game_state.mps += float(game_state.printmoney2) * 1.5
        mpstkinter.set("MPS: %s" % game_state.mps)
        boostbutton2h1.destroy()
        clickbooster2.grid(row=4 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1),
                           column=3, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1 +
                                     game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                            column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirements2h1():
    global boostbutton2h1, game_state
    log('nq2h1 invoked')
    boostafford2h1.destroy()
    boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                            command=boostauto2h1)
    boostbutton2h1.grid(row=3 - (game_state.upgcheck1h1 + game_state.clickupgcheck1), column=3, sticky=E)


def boostauto2h2():
    global game_state
    log('ba2h2 invoked')
    if game_state.money < 7777777 or game_state.upgcheck2h1 == 0:
        global boostafford2h2
        boostbutton2h2.destroy()
        master.bell()
        boostafford2h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                            column=3, sticky=E)
        master.after(500, norequirements2h2)
    else:
        game_state.money -= 7777777
        game_state.printmoney = int(float(game_state.printmoney * 50) / 10)
        game_state.upgcheck2h2 += 1
        game_state.mps += float(game_state.printmoney2) * 6
        mpstkinter.set("MPS: %s" % game_state.mps)
        boostbutton2h2.destroy()
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirements2h2():
    global boostbutton2h2, game_state
    log('nq2h2 invoked')
    boostafford2h2.destroy()
    boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
    boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                 game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                        column=3, sticky=E)


def deduction2():
    global game_state
    log('deduction2  invoked')

    if game_state.money < game_state.printprice:
        global incafford2
        incbutton2.destroy()
        master.bell()
        incafford2 = Label(master, text="%s" % cannotafford, width=33)
        incafford2.grid(row=3, column=0, sticky=W)
        master.after(500, cannotafford2)
    else:
        game_state.money -= game_state.printprice
        game_state.printmoney += (1 + game_state.upgcheck2h1 * 2 + game_state.upgcheck2h2 * 18) * game_state.multiplier
        game_state.printmoney2 += game_state.multiplier
        game_state.mps += 15 * (1 + game_state.upgcheck2h1 * 2 + game_state.upgcheck2h2 * 18) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        printmpstkinter.set("Money Printers MPS: " + str(15 * game_state.printmoney))
        printmoneytkinter.set(game_state.printmoney2)
        game_state.printprice = 375 * math.pow(1.25, game_state.printmoney2)
        printpricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.printmoney, 1.01)
        if (game_state.printmoney == 1 and game_state.bankheist == 0 and game_state.sharecrash == 0 and
            game_state.counterfeit == 0 and game_state.autoclick == 0):
            automoney()


def cannotafford2():
    global incafford2, incbutton2
    log('ca2 invoked')
    incafford2.destroy()
    incbutton2 = Button(master, textvariable=printpricetkinter, width=33, command=deduction2)
    incbutton2.grid(row=3, column=0, sticky=W)


# COUNTERFEIT COMPANY
def boostauto3():
    global game_state
    log('ba3 invoked')
    if game_state.money < 2133748 or game_state.counterfeit2 == 0:
        global boostafford3
        boostbutton3.destroy()
        master.bell()
        boostafford3 = Label(master, text="%s" % norequirements, width=35)
        boostafford3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
        master.after(500, norequirements3)
    else:
        game_state.money -= 2133748
        game_state.counterfeit = int(float(game_state.counterfeit * 15) / 10)
        game_state.mps += float(game_state.counterfeit2) * 1.5
        mpstkinter.set("MPS: %s" % game_state.mps)
        game_state.upgcheck3 += 1
        boostbutton3.destroy()
        boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                            column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirements3():
    global boostbutton3
    log('nq3 invoked')
    boostafford3.destroy()
    boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                          command=boostauto3)
    boostbutton3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                               game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def deduction3():
    global game_state
    log('deduction3 invoked')
    if game_state.money < game_state.counterprice:
        global incafford3
        incbutton3.destroy()
        master.bell()
        incafford3 = Label(master, text="%s" % cannotafford, width=33)
        incafford3.grid(row=5, column=0, sticky=W)
        master.after(500, cannotafford3)
    else:
        game_state.money -= game_state.counterprice
        game_state.counterfeit += (1 + game_state.upgcheck3 * 2) * game_state.multiplier
        game_state.counterfeit2 += game_state.multiplier
        game_state.mps += 221 * (1 + game_state.upgcheck3 * 2) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        countermpstkinter.set("Counterfeit Companies MPS: " + str(221 * game_state.counterfeit))
        counterfeittkinter.set(game_state.counterfeit2)
        game_state.counterprice = 9001 * math.pow(1.3, game_state.counterfeit2)
        counterpricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.counterfeit, 1.01)
        if (game_state.counterfeit == 1 and game_state.bankheist and game_state.sharecrash == 0 and
            game_state.printmoney == 0 and game_state.autoclick == 0):
            automoney()


def cannotafford3():
    global incafford3, incbutton3
    log('ca3 invoked')
    incafford3.destroy()
    incbutton3 = Button(master, textvariable=counterpricetkinter, width=33, command=deduction3)
    incbutton3.grid(row=5, column=0, sticky=W)


# SHAREMARKET CRASH
def boostauto4():
    global game_state
    log('ba4 invoked')
    if game_state.money < 12345678 or game_state.sharecrash2 == 0:
        global boostafford4
        boostbutton4.destroy()
        master.bell()
        boostafford4 = Label(master, text="%s" % norequirements, width=35)
        boostafford4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        master.after(500, norequirements4)
    else:
        game_state.money -= 12345678
        game_state.sharecrash = int(float(game_state.sharecrash * 15) / 10)
        game_state.mps += float(game_state.sharecrash2) * 1.5
        mpstkinter.set("MPS: %s" % game_state.mps)
        game_state.upgcheck4 += 1
        boostbutton4.destroy()
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirements4():
    global boostbutton4, game_state
    log('nq4 invoked')
    boostafford4.destroy()
    boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                          command=boostauto4)
    boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                               game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                               game_state.clickupgcheck2), column=3, sticky=E)


def deduction4():
    global game_state
    log('deduction4 invoked')
    if game_state.money < game_state.shareprice:
        global incafford4
        incbutton4.destroy()
        master.bell()
        incafford4 = Label(master, text="%s" % cannotafford, width=33)
        incafford4.grid(row=7, column=0, sticky=W)
        master.after(500, cannotafford4)
    else:
        game_state.money -= game_state.shareprice
        game_state.sharecrash += (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        game_state.sharecrash2 += game_state.multiplier
        game_state.mps += 969 * (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        sharempstkinter.set("Sharemarket Crashes MPS: " + str(969 * game_state.sharecrash))
        sharecrashtkinter.set(game_state.sharecrash2)
        game_state.shareprice = 42000 * math.pow(1.4, game_state.sharecrash2)
        sharepricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.sharecrash, 1.01)
        if (game_state.sharecrash == 1 and game_state.bankheist == 1 and
            game_state.counterfeit == 0 and game_state.printmoney == 0 and game_state.autoclick == 0):
            automoney()


def cannotafford4():
    global incafford4, incbutton4
    log('ca4 invoked')
    incafford4.destroy()
    incbutton4 = Button(master, textvariable=sharempstkinter, width=33, command=deduction4)
    incbutton4.grid(row=7, column=0, sticky=W)


# BANK HEIST
def boostauto5():
    global game_state
    log('ba5 invoked')
    if game_state.money < 12345678 or game_state.bankheist2 == 0:
        global boostafford5
        boostbutton5.destroy()
        master.bell()
        boostafford5 = Label(master, text="%s" % norequirements, width=35)
        boostafford5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
        master.after(500, norequirements5)
    else:
        game_state.money -= 12345678
        game_state.bankheist = int(float(game_state.bankheist * 15) / 10)
        game_state.mps = float(game_state.bankheist2) * 1.5
        mpstkinter.set("MPS: %s" % game_state.mps)
        game_state.upgcheck5 += 1
        boostbutton5.destroy()


def norequirements5():
    global boostbutton5, game_state
    log('nq5 invoked')
    boostafford5.destroy()
    boostbutton5 = Button(master, text="Bank Blueprints ($91215000)", width=35, command=boostauto5)
    boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                               game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                               game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def deduction5():
    global game_state
    log('deduction5 invoked')
    if game_state.money < game_state.bankprice:
        global incafford5
        incbutton5.destroy()
        master.bell()
        incafford5 = Label(master, text="%s" % cannotafford, width=33)
        incafford5.grid(row=9, column=0, sticky=W)
        master.after(500, cannotafford5)
    else:
        game_state.money -= game_state.bankprice
        game_state.bankheist += (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        game_state.bankheist2 += game_state.multiplier
        game_state.mps += 1844 * (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        bankmpstkinter.set("Bank Heists MPS: " + str(1844 * game_state.bankheist))
        bankheisttkinter.set(game_state.bankheist2)
        game_state.bankprice = int(42000 * math.pow(1.1, game_state.bankheist2))
        bankpricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.bankheist, 1.01)
        if (game_state.bankheist == 1 and game_state.sharecrash == 0 and game_state.counterfeit == 0 and
            game_state.printmoney == 0 and game_state.autoclick == 0):
            automoney()


def cannotafford5():
    global incafford5, incbutton5
    log('ca5 invoked')
    incafford5.destroy()
    incbutton5 = Button(master, textvariable=bankpricetkinter, width=33, command=deduction4)
    incbutton5.grid(row=9, column=0, sticky=W)


# CLICKS
def collectmoney():
    global main_laid_out, game_state
    log('collectmoney invoked')

    game_state.money += game_state.inc

    moneytkinter.set("Balance: $" + format_price(game_state.money))

    game_state.animate += 1
    animationthingy()
    game_state.totalclicks += 1
    main_laid_out = False


def format_price(pricevar):
    def add_decimal(price, d):
        price = str(price / 10 ** d)
        return price[:-1]  #+ '.' + price[-1]

    if pricevar < 10 ** 6:
        return '%s' % round(pricevar, 1)
    elif pricevar < 10 ** 9:
        return '%sm' % add_decimal(pricevar, 5)
    elif pricevar < 10 ** 12:
        return '%sb' % add_decimal(pricevar, 8)
    elif pricevar < 10 ** 15:
        return '%st' % add_decimal(pricevar, 11)
    elif pricevar < 10 ** 18:
        return '%sq' % add_decimal(pricevar, 14)
    else:
        return '%sQ' % add_decimal(pricevar, 17)


def autopricechoice():
    autopricetkinter.set("Auto-Clicker (Costs: $%s)" % format_price(game_state.autoprice))


def printpricechoice():
    printpricetkinter.set("Money Printer (Costs: $%s)" % format_price(game_state.printprice))


def counterpricechoice():
    counterpricetkinter.set("Counterfeit Company (Costs: $%s)" % format_price(game_state.counterprice))


def sharepricechoice():
    sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % format_price(game_state.shareprice))


def bankpricechoice():
    bankpricetkinter.set("Bank Heist (Costs: $%s)" % format_price(game_state.bankprice))


def clickboost1():
    global game_state
    log('cb1 invoked')
    if game_state.money < 2100:
        global clickafford1
        clickbooster1.destroy()
        master.bell()
        clickafford1 = Label(master, text="%s" % norequirements, width=35)
        clickafford1.grid(row=1, column=3, sticky=E)
        master.after(500, norequirementsc1)
    else:
        game_state.money -= 2100
        game_state.inc += 2
        inctkinter.set("+%s money!" % game_state.inc)
        game_state.clickupgcheck1 += 1
        clickbooster1.destroy()
        boostbutton1h1.grid(row=2 - game_state.clickupgcheck1, column=3, sticky=E)
        boostbutton2h1.grid(row=3 - (game_state.upgcheck1h1 + game_state.clickupgcheck1), column=3, sticky=E)
        clickbooster2.grid(row=4 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1),
                           column=3, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1 +
                                     game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                            column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirementsc1():
    global clickbooster1
    log('nq1 invoked')
    clickafford1.destroy()
    clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
    clickbooster1.grid(row=1, column=3, sticky=E)


def clickboost2():
    global game_state
    log('cb2 invoked')
    if game_state.money < 200000 or not game_state.clickupgcheck1:
        global clickafford2
        clickbooster2.destroy()
        master.bell()
        clickafford2 = Label(master, text="%s" % norequirements, width=35)
        clickafford2.grid(row=4 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1),
                          column=3, sticky=E)
        master.after(500, norequirementsc2)
    else:
        game_state.money -= 200000
        game_state.inc += game_state.mps / 10
        inctkinter.set("+%s money!" % game_state.inc)
        game_state.clickupgcheck2 += 1
        clickbooster2.destroy()
        boostbutton1h2.grid(row=5 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1 +
                                     game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                            column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)


def norequirementsc2():
    global clickbooster2, game_state
    log('nqc2 invoked')
    clickafford2.destroy()
    clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35, command=clickboost2)
    clickbooster2.grid(row=4 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1), column=3,
                       sticky=E)


def automoneychoice():
    global game_state

    moneytkinter.set("Balance: $" + format_price(game_state.money))
    automoney()


def automoney():
    if game_state.check == 10:
        auto_money_helper()
        game_state.timeplay += 1

    bugfixer()
    game_state.money += float(game_state.mps) / 10.0
    game_state.check += 1

    master.after(100, automoneychoice)


def auto_money_helper():
    global goldbutton, game_state

    # GOLD UPGRADE
    random1 = randint(1, 300)
    game_state.check = 1
    if random1 == 1 and not game_state.goldcheck:
        goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
        goldbutton.image = gold
        goldbutton.place(x=(int(randint(0, 450))), y=(int(randint(0, 200))))
        game_state.goldcheck = True

    # ACHIEVEMENT UPDATES
    if game_state.statscheck:
        set_stats(game_state, totalclicksvar, timevar, totalspentvar)


# RESETTING GAME
def resetgame():
    log('resetgame invoked')
    toplevel = Toplevel()
    msg = Label(toplevel, text="Are you sure you want to reset?")
    msg.grid(row=0, column=0, columnspan=2)

    yesbutton = Button(toplevel, text="Yes", command=lambda: save_and_load.encode_and_save(username, data=None))
    yesbutton.grid(row=1, column=0)
    nobutton = Button(toplevel, text="No", command=toplevel.destroy)
    nobutton.grid(row=1, column=1)


# STATS STUFF
def showstats():
    global totalclickslabel, totalclicksvar, timelabel, timevar, totalspentlabel, totalspentvar, hidestatsbutton, \
        game_state

    statsbutton.destroy()
    resetbutton.grid(row=13, column=0, sticky=W)
    savebutton.grid(row=13, column=3, sticky=E)
    reportbutton.grid(row=14, column=2)
    logoutbutton.grid(row=15, column=2)
    game_state.statscheck = True

    totalclicksvar = StringVar()
    totalclickslabel = Label(master, textvariable=totalclicksvar)
    totalclickslabel.grid(row=12, column=0, sticky=W)

    timevar = StringVar()
    timelabel = Label(master, textvariable=timevar)
    timelabel.grid(row=12, column=3, sticky=E)

    totalspentvar = StringVar()
    totalspentlabel = Label(master, textvariable=totalspentvar)
    totalspentlabel.grid(row=11, column=3, sticky=E)

    set_stats(game_state, totalclicksvar, timevar, totalspentvar)

    hidestatsbutton = Button(master, text="Hide Stats", width=10, command=hidestats)
    hidestatsbutton.grid(row=11, column=0, sticky=W)


def hidestats():
    global statsbutton, game_state
    game_state.statscheck = False
    totalclickslabel.destroy()
    timelabel.destroy()
    totalspentlabel.destroy()
    hidestatsbutton.destroy()
    statsbutton = Button(master, text="Stats", width=10, command=showstats)
    statsbutton.grid(row=12, column=0, sticky=W)
    resetbutton.grid(row=13, column=0, sticky=W)
    savebutton.grid(row=13, column=3, sticky=E)
    if game_state.upgbuttoncheck:
        exitupgrades.grid(row=11, column=3, sticky=E)


# UPGRADES WINDOW
def showupgrades():
    global game_state

    game_state.upgbuttoncheck = True

    global clickbooster1, boostbutton1h1, boostbutton2h1, clickbooster2, boostbutton1h2, boostbutton3, \
        boostbutton2h2, boostbutton4, boostbutton5, exitupgrades
    upgrades.destroy()
    if game_state.clickupgcheck1 == 0:
        clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
        clickbooster1.grid(row=1, column=3, sticky=E)
    if game_state.upgcheck1h1 == 0:
        boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
        boostbutton1h1.grid(row=2 - game_state.clickupgcheck1, column=3, sticky=E)
    if game_state.upgcheck2h1 == 0:
        boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                                command=boostauto2h1)
        boostbutton2h1.grid(row=3 - (game_state.upgcheck1h1 + game_state.clickupgcheck1), column=3, sticky=E)
    if game_state.clickupgcheck2 == 0:
        clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35, command=clickboost2)
        clickbooster2.grid(row=4 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1),
                           column=3, sticky=E)
    if game_state.upgcheck1h2 == 0:
        boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35, command=boostauto1h2)
        boostbutton1h2.grid(row=5 - (game_state.upgcheck1h1 + game_state.upgcheck2h1 + game_state.clickupgcheck1 +
                                     game_state.clickupgcheck2), column=3, sticky=E)
    if game_state.upgcheck3 == 0:
        boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                              command=boostauto3)
        boostbutton3.grid(row=6 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
    if game_state.upgcheck2h2 == 0:
        boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
        boostbutton2h2.grid(row=7 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                     game_state.upgcheck3 + game_state.clickupgcheck1 + game_state.clickupgcheck2),
                            column=3, sticky=E)
    if game_state.upgcheck4 == 0:
        boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                              command=boostauto4)
        boostbutton4.grid(row=8 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.clickupgcheck1 +
                                   game_state.clickupgcheck2), column=3, sticky=E)
    if game_state.upgcheck5 == 0:
        boostbutton5 = Button(master, text="Bank Blueprints (Costs: $91215000)", width=35, command=boostauto5)
        boostbutton5.grid(row=9 - (game_state.upgcheck1h1 + game_state.upgcheck1h2 + game_state.upgcheck2h1 +
                                   game_state.upgcheck2h2 + game_state.upgcheck3 + game_state.upgcheck4 +
                                   game_state.clickupgcheck1 + game_state.clickupgcheck2), column=3, sticky=E)
    exitupgrades = Button(master, text="Hide Upgrades", command=hideupgrades)
    if game_state.statscheck:
        global hidestatsbutton
        exitupgrades.grid(row=11, column=3, sticky=E)
        hidestatsbutton.grid(row=12, column=0, sticky=W)
        totalspentlabel.grid(row=12, column=3, sticky=E)
        totalclickslabel.grid(row=13, column=0, sticky=W)
        timelabel.grid(row=13, column=3, sticky=E)
        resetbutton.grid(row=14, column=0, sticky=W)
        savebutton.grid(row=14, column=3, sticky=E)
        reportbutton.grid(row=15, column=2)
        logoutbutton.grid(row=16, column=2)
    else:
        exitupgrades.grid(row=11, column=3, sticky=E)
        statsbutton.grid(row=12, column=0, sticky=W)
        resetbutton.grid(row=13, column=0, sticky=W)
        savebutton.grid(row=13, column=3, sticky=E)
        reportbutton.grid(row=14, column=2)
        logoutbutton.grid(row=15, column=2)


def hideupgrades():
    global exitupgrades, game_state

    game_state.upgbuttoncheck = False

    if game_state.clickupgcheck1 == 0:
        clickbooster1.destroy()
    if game_state.upgcheck1h1 == 0:
        boostbutton1h1.destroy()
    if game_state.upgcheck2h1 == 0:
        boostbutton2h1.destroy()
    if game_state.clickupgcheck2 == 0:
        clickbooster2.destroy()
    if game_state.upgcheck1h2 == 0:
        boostbutton1h2.destroy()
    if game_state.upgcheck3 == 0:
        boostbutton3.destroy()
    if game_state.upgcheck2h2 == 0:
        boostbutton2h2.destroy()
    if game_state.upgcheck4 == 0:
        boostbutton4.destroy()
    if game_state.upgcheck5 == 0:
        boostbutton5.destroy()
    global upgrades
    upgrades = Button(master, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=1, column=3, rowspan=8, sticky=E)
    exitupgrades.destroy()
    if game_state.statscheck:
        hidestatsbutton.grid(row=12, column=0, sticky=W)
        resetbutton.grid(row=13, column=0, sticky=W)
        savebutton.grid(row=13, column=3, sticky=E)
        reportbutton.grid(row=14, column=2)
        logoutbutton.grid(row=15, column=2)
    else:
        statsbutton.grid(row=11, column=0, sticky=W)
        resetbutton.grid(row=12, column=0, sticky=W)
        savebutton.grid(row=12, column=3, sticky=E)
        reportbutton.grid(row=14, column=2)
        logoutbutton.grid(row=15, column=2)


# ANIMATION
def animationthingy():
    global game_state

    game_state.animate = game_state.animate % 3

    if game_state.animate == 0:
        animation1 = Label(master, image=Animation1)
        animation1.place(x=253, y=0)
        animation1.image = Animation1
    elif game_state.animate == 1:
        animation2 = Label(master, image=Animation2)
        animation2.place(x=253, y=0)
        animation2.image = Animation2
    elif game_state.animate == 2:
        animation3 = Label(master, image=Animation3)
        animation3.place(x=253, y=0)
        animation3.image = Animation3
    clickcolour()


# PSYCHEDELIC COLOURS
def clickcolour():
    global game_state
    game_state.clickcolourcheck += 1
    if game_state.clickcolourcheck == 0:
        clickbutton.configure(bg="red")
    elif game_state.clickcolourcheck == 1:
        clickbutton.configure(bg="orange")
    elif game_state.clickcolourcheck == 2:
        clickbutton.configure(bg="yellow")
    elif game_state.clickcolourcheck == 3:
        clickbutton.configure(bg="green")
    elif game_state.clickcolourcheck == 4:
        clickbutton.configure(bg="blue")
    elif game_state.clickcolourcheck == 5:
        clickbutton.configure(bg="purple")
    elif game_state.clickcolourcheck == 6:
        clickbutton.configure(bg="violet")
    else:
        game_state.clickcolourcheck -= 7


# GOLD BUTTON
def goldupgrade():
    global goldbutton

    goldbutton.destroy()
    game_state.goldcheck = False
    goldupgcheck = randint(1, 77)
    if goldupgcheck == int(1):
        game_state.mps *= 77
        mpstkinter.set("MPS: %s" % game_state.mps)
        toplevel = Toplevel()
        goldtime = Message(toplevel,
                           text="Gold Upgrade Activated (multiply current MPS by 77 for 7.7 seconds!)")
        goldtime.pack()
        master.after(7700, goldmpsstop)
    else:
        game_state.money += int(game_state.mps * 50)
        toplevel = Toplevel()
        goldtime2 = Message(toplevel, text="Gold Upgrade Activated (get money equal to *50 MPS!)")
        goldtime2.pack()


def goldmpsstop():
    game_state.mps *= (1 / 77.0)
    mpstkinter.set("MPS: %s" % game_state.mps)


# MULTIPLIER STUFF
def multiplierchange():
    global multipliercheck
    if multipliercheck == 0:
        multipliercheck += 1
        multiplier.set("x1")
        game_state.multiplierset("1")
        updatevars()
    elif multipliercheck == 1:
        multipliercheck += 1
        multiplier.set("x10")
        game_state.multiplierset("10")
        updatevars()
    elif multipliercheck == 2:
        multipliercheck += 1
        multiplier.set("x100")
        game_state.multiplierset("100")
        updatevars()
    elif multipliercheck >= 3:
        multipliercheck -= 3
        multiplierchange()


def updatevars():
    autoclicktkinter.set(game_state.autoclick2)
    autopricetkinter.set("Auto-Clicker (Costs: $%s)" % str(format_price(game_state.autoprice)))
    autompstkinter.set("Auto-Clickers MPS: " + str(game_state.autoclick))
    printmoneytkinter.set(game_state.printmoney2)
    printpricetkinter.set("Money Printer (Costs: $%s)" % str(format_price(game_state.printprice)))
    printmpstkinter.set("Money Printers MPS: " + str(game_state.printmoney * 15))
    counterfeittkinter.set(game_state.counterfeit2)
    counterpricetkinter.set("Counterfeit Company (Costs: $%s)" % str(format_price(game_state.counterprice)))
    countermpstkinter.set("Counterfeit Companies MPS: " + str(game_state.counterfeit * 221))
    sharecrashtkinter.set(game_state.sharecrash2)
    sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % str(format_price(game_state.shareprice)))
    sharempstkinter.set("Sharemarket Crashes MPS: " + str(game_state.sharecrash * 969))
    bankheisttkinter.set(game_state.bankheist2)
    bankpricetkinter.set("Bank Heist (Costs: $%s)" % str(format_price(game_state.bankprice)))
    bankmpstkinter.set("Bank Heists MPS: " + str(game_state.bankheist * 2015))


def main():
    # BUTTONS, LABELS AND ENTRIES
    global incbutton1, incbutton2, incbutton3, incbutton4, incbutton5, upgrades, resetbutton, savebutton, clickbutton, \
        statsbutton, reportbutton, logoutbutton, moneylabel, lottobutton
    background = Label(master, image=img1)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    background.image = img1

    upgrades = Button(master, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=1, column=3, rowspan=8, sticky=E)

    moneylabel = Label(master, textvariable=moneytkinter)
    moneylabel.grid(row=0, column=0, sticky=W)

    mpslabel = Label(master, textvariable=mpstkinter)
    mpslabel.grid(row=0, column=3, sticky=E)

    multiplierbutton = Button(master, textvariable=multiplier, command=multiplierchange)
    multiplierbutton.grid(row=2, column=2)

    clickbutton = Button(master, textvariable=inctkinter, height=6, width=18, command=collectmoney, bg="red")
    clickbutton.grid(row=3, column=2, rowspan=4)

    incbutton1 = Button(master, textvariable=autopricetkinter, width=33, command=deduction1)
    incbutton1.grid(row=1, column=0, sticky=W)

    checklabel1 = Label(master, textvariable=autoclicktkinter, width=2)
    checklabel1.grid(row=1, column=1, sticky=W)

    mpscheck1 = Label(master, textvariable=autompstkinter, width=35)
    mpscheck1.grid(row=2, column=0, sticky=W, columnspan=2)

    incbutton2 = Button(master, textvariable=printpricetkinter, width=33, command=deduction2)
    incbutton2.grid(row=3, column=0, sticky=W)

    checklabel2 = Label(master, textvariable=printmoneytkinter, width=2)
    checklabel2.grid(row=3, column=1, sticky=W)

    mpscheck2 = Label(master, textvariable=printmpstkinter, width=35)
    mpscheck2.grid(row=4, column=0, sticky=W, columnspan=2)

    incbutton3 = Button(master, textvariable=counterpricetkinter, width=33, command=deduction3)
    incbutton3.grid(row=5, column=0, sticky=W)

    checklabel3 = Label(master, textvariable=counterfeittkinter, width=2)
    checklabel3.grid(row=5, column=1, sticky=W)

    mpscheck3 = Label(master, textvariable=countermpstkinter, width=35)
    mpscheck3.grid(row=6, column=0, sticky=W, columnspan=2)

    incbutton4 = Button(master, textvariable=sharepricetkinter, width=33, command=deduction4)
    incbutton4.grid(row=7, column=0, sticky=W)

    checklabel4 = Label(master, textvariable=sharecrashtkinter, width=2)
    checklabel4.grid(row=7, column=1, sticky=W)

    mpscheck4 = Label(master, textvariable=sharempstkinter, width=35)
    mpscheck4.grid(row=8, column=0, sticky=W, columnspan=2)

    incbutton5 = Button(master, textvariable=bankpricetkinter, width=33, command=deduction5)
    incbutton5.grid(row=9, column=0, sticky=W)

    checklabel5 = Label(master, textvariable=bankheisttkinter, width=2)
    checklabel5.grid(row=9, column=1, sticky=W)

    mpscheck5 = Label(master, textvariable=bankmpstkinter, width=35)
    mpscheck5.grid(row=10, column=0, sticky=W, columnspan=2)

    lottobutton = Button(master, textvariable=lottoprice, width=35, command=lotto)
    lottobutton.grid(row=11, column=0, sticky=W)

    statsbutton = Button(master, text="Stats", width=10, command=showstats)
    statsbutton.grid(row=12, column=0, sticky=W)

    resetbutton = Button(master, text="Reset Game", width=10, command=resetgame)
    resetbutton.grid(row=13, column=0, sticky=W)

    savebutton = Button(master, text="Save Game", width=10, command=savegame)
    savebutton.grid(row=13, column=3, sticky=E)

    reportbutton = Button(master, text='Report Issue to Github', width=20, command=report)
    reportbutton.grid(row=14, column=2)

    logoutbutton = Button(master, text='Log Out', width=20, command=logout)
    logoutbutton.grid(row=15, column=2)


def lotto():
    global game_state, lottobutton, cannotafford
    if game_state.money < int(game_state.lottoprice):
        lottobutton.destroy()
        master.bell()
        lottoafford = Label(master, text="%s" % cannotafford, width=35)
        lottoafford.grid(row=8, column=0, sticky=W)

        def update_lotto_afford(price):
            lottoafford.destroy()
            lottobutton = Button(master, width=35, text="Lotto ($%s)" % (price))
            lottobutton.grid(row=11, column=0, sticky=W)

        master.after(500, lambda: update_lotto_afford(game_state.lottoprice))
    else:
        global lottoprice
        lp = game_state.lottoprice
        money = game_state.money - lp
        game_state.lottoprice *= uniform(1.1, 5.1)
        prob = random()
        if prob < 0.5:
            money += (lp / 2.0)
        elif prob < 0.7:
            money += (lp / 1.5)
        elif prob < 0.8:
            money += lp
        elif prob < 0.8625:
            money += lp * 1.5
        elif prob < 0.8825:
            money += lp * 2.5
        elif prob < 0.895:
            money += lp * 4
        elif prob < 0.896:
            money += lp * 10
        elif prob < 0.8965:
            money += lp * 40
        elif prob < 0.8967:
            money += lp * 250
        elif prob < 0.896875:
            money += lp * 1000
        elif prob < 0.897:
            money += lp * 20000
        else:
            money /= 2.0
        lottoprice.set('Lotto ($' + str(round(lp, 1)) + ')')
        game_state.money = money


# LOG OUT
def logout():
    global username, g2
    del username
    del g2

def initialize_vars():
    args = ['incbutton1', 'incbutton2', 'incbutton3', 'incbutton4', 'incbutton5', 'upgrades', 'resetbutton', 'savebutton', 'clickbutton', \
            'statsbutton', 'reportbutton', 'logoutbutton', 'moneylabel', 'lottobutton', 'save_needed', 'moneytkinter', 'mpstkinter', 'inctkinter', \
            'multiplier', 'autopricetkinter', 'autoclicktkinter', 'autompstkinter', 'printpricetkinter', 'printmoneytkinter', 'printmpstkinter', \
            'counterpricetkinter', 'counterfeittkinter', 'countermpstkinter', 'sharepricetkinter', 'sharecrashtkinter', 'sharempstkinter', \
            'bankheisttkinter', 'bankpricetkinter', 'bankmpstkinter', 'multipliercheck', 'main_laid_out', 'data_loaded', 'game_state', 'lottoprice'
]
    for i in args:
        globals()[i] = None

def main_tick():
    global save_needed, moneytkinter, mpstkinter, inctkinter, multiplier, autopricetkinter, autoclicktkinter, \
        autompstkinter, printpricetkinter, printmoneytkinter, printmpstkinter, counterpricetkinter, \
        counterfeittkinter, countermpstkinter, sharepricetkinter, sharecrashtkinter, sharempstkinter, \
        bankheisttkinter, bankpricetkinter, bankmpstkinter, multipliercheck, main_laid_out, data_loaded, \
        game_state, lottoprice
    # while True:
    if signincheck == signinvalue:
        if save_needed:
            savegame()
            save_needed = False
        elif not data_loaded:
            try:
                multipliercheck = 0
                moneytkinter = StringVar()
                moneytkinter.set("Balance: $0")

                autoclicktkinter = IntVar()
                autoclicktkinter.set(g2[1])
                autopricetkinter = StringVar()
                autopricetkinter.set("Auto-Clicker (Costs: $%s)" % str(game_state.autoprice))
                autompstkinter = StringVar()
                autompstkinter.set("Auto-Clickers MPS: " + str(game_state.autoclick))
                printmoneytkinter = IntVar()
                printmoneytkinter.set(g2[3])
                printpricetkinter = StringVar()
                printpricetkinter.set("Money Printer (Costs: $%s)" % str(game_state.printprice))
                printmpstkinter = StringVar()
                printmpstkinter.set("Money Printers MPS: " + str(game_state.printmoney * 15))
                counterfeittkinter = IntVar()
                counterfeittkinter.set(g2[5])
                counterpricetkinter = StringVar()
                counterpricetkinter.set("Counterfeit Company (Costs: $%s)" % str(game_state.counterprice))
                countermpstkinter = StringVar()
                countermpstkinter.set("Counterfeit Companies MPS: " + str(game_state.counterfeit * 221))
                sharecrashtkinter = IntVar()
                sharecrashtkinter.set(g2[7])
                sharepricetkinter = StringVar()
                sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % str(game_state.shareprice))
                sharempstkinter = StringVar()
                sharempstkinter.set("Sharemarket Crashes MPS: " + str(game_state.sharecrash * 969))
                bankheisttkinter = IntVar()
                bankheisttkinter.set(g2[9])
                bankpricetkinter = StringVar()
                bankpricetkinter.set("Bank Heist (Costs: $%s)" % str(game_state.bankprice))
                bankmpstkinter = StringVar()
                bankmpstkinter.set("Bank Heists MPS: " + str(game_state.bankheist * 2015))
                mpstkinter = StringVar()
                mpstkinter.set("MPS: %s" % str(game_state.mps))
                inctkinter = StringVar()
                inctkinter.set("+%s money!" % game_state.inc)
                multiplier = StringVar()
                multiplier.set("x1")
                lottoprice = StringVar()
                lottoprice.set("Lotto ($%s)" % str(game_state.lottoprice))
                if g2[21] == 1:
                    clickbooster1.destroy()
                if g2[9] == 1:
                    boostbutton1h1.destroy()
                if g2[13] == 1:
                    boostbutton2h1.destroy()
                if g2[23] == 1:
                    clickbooster2.destroy()
                if g2[11] == 1:
                    boostbutton1h2.destroy()
                if g2[17] == 1:
                    boostbutton3.destroy()
                if g2[15] == 1:
                    boostbutton2h2.destroy()
                if g2[19] == 1:
                    boostbutton4.destroy()
                if g2[25] == 1:
                    boostbutton5.destroy()
                if game_state and game_state.mps >= 1:
                    automoneychoice()

                if not main_laid_out:
                    main()
                    main_laid_out = True
                # break

                data_loaded = True

            except NameError:
                signin()

    master.after(1000, main_tick)

initialize_vars()
master.after(0, main_tick)
master.mainloop()