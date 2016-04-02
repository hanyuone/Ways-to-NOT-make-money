from Tkinter import *
from random import *
from tkMessageBox import showerror
import math
import save_and_load
import game_model

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


def savegame():
    global game_state
    data = ["auto", game_state.get_autoclick2(), "print", game_state.get_printmoney2(),
            "counter", game_state.get_counterfeit2(), "shares", game_state.get_sharecrash2(),
            "bank", game_state.get_bankheist2(), "upg1h1", game_state.get_upgcheck1h1(),
            "upg1h2", game_state.get_upgcheck1h2(), "upg2h1", game_state.get_upgcheck2h1(),
            "upg2h2", game_state.get_upgcheck2h2(), "upg3", game_state.get_upgcheck3(),
            "upg4", game_state.get_upgcheck4(), "upg5", game_state.get_upgcheck5(),
            "cupg1", game_state.get_clickupgcheck1(), "cupg2", game_state.get_clickupgcheck2(),
            "money", float(str(game_state.get_money())[-8:]), "time", game_state.get_timeplay(),
            "clicks", game_state.get_total_clicks(), "lotto", game_state.get_lotto()]

    save_and_load.encode_and_save(username, data)

    toplevel = Toplevel()
    msg = Message(toplevel, text="Game saved!")
    msg.pack()

def auto_updater(g2, un):
    # AUTO-UPDATE
    # lt 0.6.3 -> 0.6.3b3
    try:
        g2[39]
    except IndexError:
        g = open('savefile_' + un + '.txt', "w")
        gtemp = ["time", int(0), "clicks", int(0)]
        g2.extend(gtemp)
        g.write(str("_".join(str(y) for y in g2)).encode("hex"))
        g.close()

    # lt 0.6.3b3 -> 0.6.4a1
    try:
        g2[41]
    except IndexError:
        g = open('savefile_' + un + '.txt', "w")
        gtemp = ["lotto", 100]
        g2.extend(gtemp)
        g.write(str("_".join(str(y) for y in g2)).encode("hex"))
        g.close()

    return g2

def signin():
    global signincheck, game_state
    signincheck += 1

    def verifysignin():
        global username, game_state, save_needed
        username = unentry.get()
        if save_and_load.save_file_exists(username):
            global g2, signinvalue
            try:
                g2 = save_and_load.read_game_data(username)
                print 'g2', g2
                g2 = save_and_load.auto_updater(g2, username)
                print 'update', g2
            except IOError as ioe:
                print ioe
            save_and_load.encode_and_save(username, g2)
            game_state = game_model.GameState(g2)
            print 'game_state', game_state
            for i in [l, unentry, b1, b2]:
                i.destroy()

            signinvalue += 1
            save_needed = True
        else:
            showerror(title='Error!', message='Wrong Username.')

    def createaccount():
        global g2, signinvalue, username, game_state, save_needed
        print("Yes")
        username = unentry.get()
        save_and_load.encode_and_save(username, data=None)
        try:
            g2 = save_and_load.read_game_data(username)
            game_state = game_model.GameState(g2)
            print 'game_state', game_state
        except IOError as ioe:
            print ioe
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
    clicksvar.set("Total clicks: %s" % state.get_total_clicks())
    timepassedvar.set("Total time: %s" % state.get_timeplay())
    spentvar.set("Total money spent: %s" % state.get_totalspent())


def report():
    webbrowser.open("https://github.com/DerpfacePython/Ways-to-NOT-make-money/issues/new", new=0, autoraise=True)

# BUG FIXER
def bugfixer():
    global game_state
    while game_state.get_mps() > (game_state.get_autoclick() + game_state.get_printmoney() * 15 +
                                  game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969 +
                                  game_state.get_bankheist() * 2015):
        if game_state.get_mps() - 2015 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 +
                                           game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969 +
                                           game_state.get_bankheist() * 2015):
            game_state.inc_bankheist(1 + game_state.get_upgcheck5() * 2)
            game_state.inc_bankheist2()
            bankheisttkinter.set(game_state.get_bankheist2())
            game_state.set_bankprice(int(42000 * (math.pow(1.1, game_state.get_bankheist2()))))
            bankpricetkinter.set("Bank Heist (Costs: $%s)" % game_state.get_bankprice())
            continue

        elif game_state.get_mps() - 969 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 +
                                            game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969 +
                                            game_state.get_bankheist() * 2015):
            game_state.inc_sharecrash(1 + game_state.get_upgcheck4() * 2)
            game_state.inc_sharecrash2()
            sharecrashtkinter.set(game_state.get_sharecrash2())
            game_state.set_shareprice(int(42000 * (math.pow(1.4, game_state.get_sharecrash2()))))
            sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % game_state.get_shareprice())
            continue
        elif game_state.get_mps() - 321 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 +
                                            game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969 +
                                            game_state.get_bankheist() * 2015):
            game_state.inc_counterfeit(1 + game_state.get_upgcheck3() * 2)
            game_state.inc_counterfeit2()
            counterfeittkinter.set(game_state.get_counterfeit2())
            game_state.set_counterfeitprice(int(9001 * (math.pow(1.3, game_state.get_counterfeit2()))))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % game_state.get_counterfeitprice())
            continue
        elif game_state.get_mps() - 15 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 +
                                           game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969 +
                                           game_state.get_bankheist() * 2015):
            game_state.inc_printmoney(1 + game_state.get_upgcheck2h1() * 2 + game_state.get_upgcheck2h2() * 18)
            game_state.inc_printmoney2()
            printmoneytkinter.set(game_state.get_printmoney2())
            game_state.set_printprice(int(375 * (math.pow(1.25, game_state.get_printmoney2()))))
            printpricetkinter.set("Money Printer (Costs: $%s)" % game_state.get_printprice())
            continue
        else:
            game_state.inc_autoclick(1 + game_state.get_upgcheck1h1() * 2 + game_state.get_upgcheck1h2() * 18)
            game_state.inc_autoclick2()
            autoclicktkinter.set(game_state.get_autoclick2())
            game_state.set_autoprice(int(20 * (math.pow(1.15, game_state.get_autoclick2()))))
            autopricetkinter.set("Auto-Clicker (Costs: $%s)" % game_state.get_autoprice())
            continue


# AUTO CLICKER
def boostauto1h1():
    global game_state
    if game_state.get_money() < 5000 or game_state.get_autoclick2() == 0:
        global boostafford1h1
        boostbutton1h1.destroy()
        master.bell()
        boostafford1h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=int(2 - game_state.get_clickupgcheck1()), column=3, sticky=E)
        master.after(500, norequirements1h1)
    else:
        game_state.inc_money(-5000)
        game_state.set_autoclick(int(game_state.get_autoclick() * 3) / 2)
        game_state.inc_upgcheck1h1()
        game_state.inc_mps(game_state.get_autoclick2() * 1.5)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton1h1.destroy()
        boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=3,
                            sticky=E)
        clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                    game_state.get_clickupgcheck1()), column=3, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=3, sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()))
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirements1h1():
    global boostafford1h1, boostbutton1h1
    boostafford1h1.destroy()
    boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
    boostbutton1h1.grid(row=int(2 - game_state.get_clickupgcheck1()), column=3, sticky=E)


def boostauto1h2():
    global game_state
    if game_state.get_money() < 555555 or game_state.get_upgcheck1h1() == 0:
        global boostafford1h2
        boostbutton1h2.destroy()
        master.bell()
        boostafford1h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=3,
                            sticky=E)
        master.after(500, norequirements1h2)
    else:
        game_state.inc_money(-555555)
        game_state.set_autoclick(int(game_state.get_autoclick() * 50) / 10)
        game_state.inc_upgcheck1h2()
        game_state.inc_mps(game_state.get_autoclick2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton1h2.destroy()
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()),
                          column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_upgcheck4() + game_state.get_clickupgcheck1() +
                                     game_state.get_clickupgcheck2()),
                            column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()),
                          column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirements1h2():
    global boostbutton1h2, boostafford1h2
    boostafford1h2.destroy()
    boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35,
                            command=boostauto1h2)
    boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                 game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                        column=3, sticky=E)


def deduction1():
    global game_state
    if game_state.get_money() < int(game_state.get_autoprice()):
        global incafford1
        incbutton1.destroy()
        master.bell()
        incafford1 = Label(master, text="%s" % cannotafford, width=33)
        incafford1.grid(row=1, column=0, sticky=W)
        master.after(500, cannotafford1)

    else:
        game_state.inc_money(-int(game_state.get_autoprice()))
        game_state.inc_autoclick((1 + game_state.get_upgcheck1h1() * 2 + game_state.get_upgcheck1h2() * 18) *
                                 game_state.get_multiplier())
        game_state.inc_autoclick2(game_state.get_multiplier())
        game_state.inc_mps((1 + game_state.get_upgcheck1h1() * 2 + game_state.get_upgcheck1h2() * 18) *
                           game_state.get_multiplier())
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        autompstkinter.set("Auto-Clickers MPS: " + str(game_state.get_autoclick()))
        autoclicktkinter.set(game_state.get_autoclick2())
        game_state.set_autoprice(int(20 * (math.pow(1.15, game_state.get_autoclick2()))))
        autopricechoice()
    game_state.set_inc(int(game_state.get_inc() + math.pow(game_state.get_clickupgcheck2() *
                                                           (game_state.get_autoclick() + game_state.get_printmoney() +
                                                            game_state.get_counterfeit() + game_state.get_sharecrash()),
                                                           1.01)))
    if (game_state.get_autoclick() == 1 and game_state.get_bankheist() == 0 and game_state.get_sharecrash() == 0 and
        game_state.get_counterfeit() == 0 and game_state.get_printmoney() == 0):
        automoney()


def cannotafford1():
    global incafford1, incbutton1
    incafford1.destroy()
    incbutton1 = Button(master, textvariable=autopricetkinter, width=33, command=deduction1)
    incbutton1.grid(row=1, column=0, sticky=W)


# MONEY PRINTER
def boostauto2h1():
    global game_state
    if game_state.get_money() < 42000 or game_state.get_printmoney2() == 0:
        global boostafford2h1
        boostbutton2h1.destroy()
        master.bell()
        boostafford2h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=3,
                            sticky=E)
        master.after(500, norequirements2h1)
    else:
        game_state.inc_money(-42000)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 15) / 10))
        game_state.inc_upgcheck2h1()
        game_state.inc_mps(game_state.get_printmoney2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton2h1.destroy()
        clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                    game_state.get_clickupgcheck1()), column=3, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                            sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_upgcheck4() + game_state.get_clickupgcheck1() +
                                     game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirements2h1():
    global boostbutton2h1, game_state
    boostafford2h1.destroy()
    boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                            command=boostauto2h1)
    boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()),
                        column=3, sticky=E)


def boostauto2h2():
    global game_state
    if game_state.get_money() < 7777777 or game_state.get_upgcheck2h1() == 0:
        global boostafford2h2
        boostbutton2h2.destroy()
        master.bell()
        boostafford2h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_upgcheck4() + game_state.get_clickupgcheck1() +
                                     game_state.get_clickupgcheck2()), column=3, sticky=E)
        master.after(500, norequirements2h2)
    else:
        game_state.inc_money(-7777777)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 50) / 10))
        game_state.inc_upgcheck2h2()
        game_state.inc_mps(game_state.get_printmoney2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton2h2.destroy()
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirements2h2():
    global boostbutton2h2, game_state
    boostafford2h2.destroy()
    boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
    boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                 game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                 game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                        column=3, sticky=E)


def deduction2():
    global game_state

    if game_state.get_money() < game_state.get_printprice():
        global incafford2
        incbutton2.destroy()
        master.bell()
        incafford2 = Label(master, text="%s" % cannotafford, width=33)
        incafford2.grid(row=3, column=0, sticky=W)
        master.after(500, cannotafford2)
    else:
        game_state.inc_money(-game_state.get_printprice())
        game_state.inc_printmoney((1 + game_state.get_upgcheck2h1() * 2 + game_state.get_upgcheck2h2() * 18) *
                                  game_state.get_multiplier())
        game_state.inc_printmoney2(game_state.get_multiplier)
        game_state.inc_mps(15 * (1 + game_state.get_upgcheck2h1() * 2 + game_state.get_upgcheck2h2() * 18) *
                           game_state.get_multiplier())
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        printmpstkinter.set("Money Printers MPS: " + str(15 * game_state.get_printmoney()))
        printmoneytkinter.set(game_state.get_printmoney2())
        game_state.set_printprice(int(375 * (math.pow(1.25, game_state.get_printmoney2()))))
        printpricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(game_state.get_clickupgcheck2() *
                                                                   (game_state.get_autoclick() +
                                                                    game_state.get_printmoney() +
                                                                    game_state.get_counterfeit() +
                                                                    game_state.get_sharecrash())), 1.01)))
        if (game_state.get_printmoney() == 1 and game_state.get_bankheist() == 0 and
            game_state.get_sharecrash() == 0 and game_state.get_counterfeit() == 0 and game_state.get_autoclick() == 0):
            automoney()


def cannotafford2():
    global incafford2, incbutton2
    incafford2.destroy()
    incbutton2 = Button(master, textvariable=printpricetkinter, width=33, command=deduction2)
    incbutton2.grid(row=3, column=0, sticky=W)


# COUNTERFEIT COMPANY
def boostauto3():
    global game_state
    if game_state.get_money() < 2133748 or game_state.get_counterfeit2() == 0:
        global boostafford3
        boostbutton3.destroy()
        master.bell()
        boostafford3 = Label(master, text="%s" % norequirements, width=35)
        boostafford3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()),
                          column=3, sticky=E)
        master.after(500, norequirements3)
    else:
        game_state.inc_money(-2133748)
        game_state.set_counterfeit(int(game_state.get_counterfeit() * 15) / 10)
        game_state.inc_mps(game_state.get_counterfeit2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        game_state.inc_upgcheck3()
        boostbutton3.destroy()
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_upgcheck4() + game_state.get_clickupgcheck1() +
                                     game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirements3():
    global boostbutton3
    boostafford3.destroy()
    boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                          command=boostauto3)
    boostbutton3.grid(
            row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() +
                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
            column=3, sticky=E)


def deduction3():
    global game_state
    if game_state.get_money() < game_state.get_counterfeitprice():
        global incafford3
        incbutton3.destroy()
        master.bell()
        incafford3 = Label(master, text="%s" % cannotafford, width=33)
        incafford3.grid(row=5, column=0, sticky=W)
        master.after(500, cannotafford3)
    else:
        game_state.inc_money(-game_state.get_counterfeitprice())
        game_state.inc_counterfeit((1 + game_state.get_upgcheck3() * 2) * game_state.get_multiplier())
        game_state.inc_counterfeit2(game_state.get_multiplier())
        game_state.inc_mps(221 * (1 + game_state.get_upgcheck3() * 2) * game_state.get_multiplier())
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        counterfeitmpstkinter.set("Counterfeit Companies MPS: " + str(221 * game_state.get_counterfeit()))
        counterfeittkinter.set(game_state.get_counterfeit2())
        game_state.set_counterfeitprice(int(9001 * (math.pow(1.3, game_state.get_counterfeit2()))))
        counterfeitpricechoice()
        game_state.set_inc(int(game_state.get_inc() +
                               math.pow(game_state.get_clickupgcheck2() *
                                        (game_state.get_autoclick() + game_state.get_printmoney() +
                                         game_state.get_counterfeit() + game_state.get_sharecrash()),
                                        1.01)))
        if (game_state.get_counterfeit() == 1 and game_state.get_sharecrash() == 0 and
            game_state.get_printmoney() == 0 and game_state.get_autoclick() == 0):
            automoney()


def cannotafford3():
    global incafford3, incbutton3
    incafford3.destroy()
    incbutton3 = Button(master, textvariable=counterfeitpricetkinter, width=33, command=deduction3)
    incbutton3.grid(row=5, column=0, sticky=W)


# SHAREMARKET CRASH
def boostauto4():
    global game_state
    if game_state.get_money() < 12345678 or game_state.get_sharecrash2() == 0:
        global boostafford4
        boostbutton4.destroy()
        master.bell()
        boostafford4 = Label(master, text="%s" % norequirements, width=35)
        boostafford4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()),
                          column=3, sticky=E)
        master.after(500, norequirements4)
    else:
        game_state.inc_money(-12345678)
        game_state.set_sharecrash(int(game_state.get_sharecrash() * 15) / 10)
        game_state.inc_mps(game_state.get_sharecrash2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        game_state.inc_upgcheck4()
        boostbutton4.destroy()
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirements4():
    global boostbutton4, game_state
    boostafford4.destroy()
    boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                          command=boostauto4)
    boostbutton4.grid(
            row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() +
                     game_state.get_upgcheck2h2() + game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                     game_state.get_clickupgcheck2()),
            column=3, sticky=E)


def deduction4():
    global game_state
    if game_state.get_money() < game_state.get_shareprice():
        global incafford4
        incbutton4.destroy()
        master.bell()
        incafford4 = Label(master, text="%s" % cannotafford, width=33)
        incafford4.grid(row=7, column=0, sticky=W)
        master.after(500, cannotafford4)
    else:
        game_state.inc_money(-game_state.get_shareprice())
        game_state.inc_sharecrash((1 + game_state.get_upgcheck4() * 2) * game_state.get_multiplier())
        game_state.inc_sharecrash2(game_state.get_multiplier())
        game_state.inc_mps(969 * (1 + game_state.get_upgcheck4() * 2) * game_state.get_multiplier())
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        sharempstkinter.set("Sharemarket Crashes MPS: " + str(969 * game_state.get_sharecrash()))
        sharecrashtkinter.set(game_state.get_sharecrash2())
        game_state.set_shareprice(int(42000 * (math.pow(1.4, game_state.get_sharecrash2()))))
        sharepricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(game_state.get_clickupgcheck2() *
                                                                   (game_state.get_autoclick() +
                                                                    game_state.get_printmoney() +
                                                                    game_state.get_counterfeit() +
                                                                    game_state.get_sharecrash())), 1.01)))
        if (game_state.get_sharecrash() == 1 and game_state.get_bankheist() == 1 and
            game_state.get_counterfeit() == 0 and game_state.get_printmoney() == 0 and game_state.get_autoclick() == 0):
            automoney()


def cannotafford4():
    global incafford4, incbutton4
    incafford4.destroy()
    incbutton4 = Button(master, textvariable=bankpricetkinter, width=33, command=deduction4)
    incbutton4.grid(row=7, column=0, sticky=W)


# BANK HEIST
def boostauto5():
    global game_state
    if game_state.get_money() < 12345678 or game_state.get_bankheist2() == 0:
        global boostafford5
        boostbutton5.destroy()
        master.bell()
        boostafford5 = Label(master, text="%s" % norequirements, width=35)
        boostafford5.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()),
                          column=3, sticky=E)
        master.after(500, norequirements5)
    else:
        game_state.inc_money(-12345678)
        game_state.set_bankheist(int(game_state.get_bankheist() * 15) / 10)
        game_state.inc_mps(game_state.get_bankheist2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        game_state.inc_upgcheck5()
        boostbutton5.destroy()


def norequirements5():
    global boostbutton5, game_state
    boostafford5.destroy()
    boostbutton5 = Button(master, text="Bank Blueprints ($91215000)", width=35, command=boostauto5)
    boostbutton5.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                               game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                               game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                               game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3, sticky=E)


def deduction5():
    global game_state
    if game_state.get_money() < game_state.get_bankprice():
        global incafford5
        incbutton5.destroy()
        master.bell()
        incafford5 = Label(master, text="%s" % cannotafford, width=33)
        incafford5.grid(row=9, column=0, sticky=W)
        master.after(500, cannotafford5)
    else:
        game_state.inc_money(-game_state.get_bankprice())
        game_state.inc_bankheist((1 + game_state.get_upgcheck4() * 2) * game_state.get_multiplier())
        game_state.inc_bankheist2(game_state.get_multiplier())
        game_state.inc_mps(1844 * (1 + game_state.get_upgcheck4() * 2) * game_state.get_multiplier())
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        bankmpstkinter.set("Bank Heists MPS: " + str(1844 * game_state.get_bankheist()))
        bankheisttkinter.set(game_state.get_bankheist2())
        game_state.set_bankprice(int(42000 * (math.pow(1.1, game_state.get_bankheist2()))))
        bankpricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(game_state.get_clickupgcheck2() *
                                                                   (game_state.get_autoclick() +
                                                                    game_state.get_printmoney() +
                                                                    game_state.get_counterfeit() +
                                                                    game_state.get_bankheist())), 1.01)))
        if (game_state.get_bankheist() == 1 and game_state.get_sharecrash() == 0 and
            game_state.get_counterfeit() == 0 and game_state.get_printmoney() == 0 and game_state.get_autoclick() == 0):
            automoney()


def cannotafford5():
    global incafford5, incbutton5
    incafford5.destroy()
    incbutton5 = Button(master, textvariable=bankpricetkinter, width=33, command=deduction4)
    incbutton5.grid(row=9, column=0, sticky=W)


# CLICKS
def collectmoney():
    global main_laid_out, game_state

    game_state.inc_money(game_state.get_inc())

    moneytkinter.set("Balance: $" + format_price(game_state.get_money()))

    game_state.inc_animate()
    animationthingy()
    game_state.inc_total_clicks()
    main_laid_out = False


def format_price(pricevar):

    def add_decimal(price, d):
        price = str(price / 10 ** d)
        return price[:-1] + '.' + price[-1]

    if pricevar < 10 ** 6:
        return '%s' % pricevar
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
    autopricetkinter.set("Auto-Clicker (Costs: $%s)" % format_price(game_state.get_autoprice()))


def printpricechoice():
    printpricetkinter.set("Money Printer (Costs: $%s)" % format_price(game_state.get_printprice()))


def counterfeitpricechoice():
    counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % format_price(game_state.get_counterfeitprice()))


def sharepricechoice():
    sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % format_price(game_state.get_shareprice()))


def bankpricechoice():
    bankpricetkinter.set("Bank Heist (Costs: $%s)" % format_price(game_state.get_bankprice()))


def clickboost1():
    global game_state
    if game_state.get_money() < 2100:
        global clickafford1
        clickbooster1.destroy()
        master.bell()
        clickafford1 = Label(master, text="%s" % norequirements, width=35)
        clickafford1.grid(row=1, column=3, sticky=E)
        master.after(500, norequirementsc1)
    else:
        game_state.inc_money(-2100)
        game_state.set_inc(game_state.get_inc() + 2)
        inctkinter.set("+%s money!" % game_state.get_inc())
        game_state.inc_clickupgcheck1()
        clickbooster1.destroy()
        boostbutton1h1.grid(row=2 - game_state.get_clickupgcheck1(), column=3, sticky=E)
        boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=3,
                            sticky=E)
        clickbooster2.grid(
                row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()),
                column=3, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=3,
                            sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirementsc1():
    global clickbooster1
    clickafford1.destroy()
    clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
    clickbooster1.grid(row=1, column=3, sticky=E)


def clickboost2():
    global game_state
    if game_state.get_money() < 200000 or game_state.get_clickupgcheck1() == 0:
        global clickafford2
        clickbooster2.destroy()
        master.bell()
        clickafford2 = Label(master, text="%s" % norequirements, width=35)
        clickafford2.grid(
                row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()),
                column=3, sticky=E)
        master.after(500, norequirementsc2)
    else:
        game_state.inc_money(-200000)
        game_state.set_inc(game_state.get_inc() + game_state.get_mps() / 10)
        inctkinter.set("+%s money!" % game_state.get_inc())
        game_state.inc_clickupgcheck2()
        clickbooster2.destroy()
        boostbutton1h2.grid(row=max(0, 5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2())),
                            column=3, sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostafford2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_upgcheck4() + game_state.get_clickupgcheck1() +
                                     game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)


def norequirementsc2():
    global clickbooster2, game_state
    clickafford2.destroy()
    clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35,
                           command=clickboost2)
    clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                game_state.get_clickupgcheck1()), column=3, sticky=E)


def automoneychoice():
    global game_state

    moneytkinter.set("Balance: $" + format_price(game_state.get_money()))
    automoney()


def automoney():
    if game_state.check == 10:
        auto_money_helper()
        game_state.inc_timeplay()

    bugfixer()
    game_state.money += float(game_state.mps) / 10.0
    game_state.check += 1

    master.after(100, automoneychoice)


def auto_money_helper():
    global goldbutton, timevar, game_state

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
    if game_state.get_upgbuttoncheck():
        exitupgrades.grid(row=11, column=3, sticky=E)

# UPGRADES WINDOW
def showupgrades():
    global game_state

    game_state.set_upgbuttoncheck(True)

    global clickbooster1, boostbutton1h1, boostbutton2h1, clickbooster2, boostbutton1h2, boostbutton3, \
        boostbutton2h2, boostbutton4, boostbutton5, exitupgrades
    upgrades.destroy()
    if game_state.get_clickupgcheck1() == 0:
        clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
        clickbooster1.grid(row=1, column=3, sticky=E)
    if game_state.get_upgcheck1h1() == 0:
        boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
        boostbutton1h1.grid(row=2 - game_state.get_clickupgcheck1(), column=3, sticky=E)
    if game_state.get_upgcheck2h1() == 0:
        boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                                command=boostauto2h1)
        boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=3,
                            sticky=E)
    if game_state.get_clickupgcheck2() == 0:
        clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35,
                               command=clickboost2)
        clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                    game_state.get_clickupgcheck1()), column=3, sticky=E)
    if game_state.get_upgcheck1h2() == 0:
        boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35,
                                command=boostauto1h2)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                            sticky=E)
    if game_state.get_upgcheck3() == 0:
        boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                              command=boostauto3)
        boostbutton3.grid(
                row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() +
                         game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3, sticky=E)
    if game_state.get_upgcheck2h2() == 0:
        boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                     game_state.get_upgcheck2h1() + game_state.get_upgcheck3() +
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                            sticky=E)
    if game_state.get_upgcheck4() == 0:
        boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                              command=boostauto4)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_clickupgcheck1() +
                                   game_state.get_clickupgcheck2()), column=3, sticky=E)
    if game_state.get_upgcheck5() == 0:
        boostbutton5 = Button(master, text="Bank Blueprints (Costs: $91215000)", width=35, command=boostauto5)
        boostbutton5.grid(row=9 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() +
                                   game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                                   game_state.get_upgcheck3() + game_state.get_upgcheck4() +
                                   game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), column=3,
                          sticky=E)
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

    game_state.set_upgbuttoncheck(False)

    if game_state.get_clickupgcheck1() == 0:
        clickbooster1.destroy()
    if game_state.get_upgcheck1h1() == 0:
        boostbutton1h1.destroy()
    if game_state.get_upgcheck2h1() == 0:
        boostbutton2h1.destroy()
    if game_state.get_clickupgcheck2() == 0:
        clickbooster2.destroy()
    if game_state.get_upgcheck1h2() == 0:
        boostbutton1h2.destroy()
    if game_state.get_upgcheck3() == 0:
        boostbutton3.destroy()
    if game_state.get_upgcheck2h2() == 0:
        boostbutton2h2.destroy()
    if game_state.get_upgcheck4() == 0:
        boostbutton4.destroy()
    if game_state.get_upgcheck5() == 0:
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
    elif not game_state.statscheck:
        statsbutton.grid(row=11, column=0, sticky=W)
        resetbutton.grid(row=12, column=0, sticky=W)
        savebutton.grid(row=12, column=3, sticky=E)
        reportbutton.grid(row=14, column=2)
        logoutbutton.grid(row=15, column=2)


# ANIMATION
def animationthingy():
    global game_state

    a = game_state.get_animate()
    if a == 0:
        animation1 = Label(master, image=Animation1)
        animation1.place(x=253, y=0)
        animation1.image = Animation1
    elif a == 1:
        animation2 = Label(master, image=Animation2)
        animation2.place(x=253, y=0)
        animation2.image = Animation2
    elif a == 2:
        animation3 = Label(master, image=Animation3)
        animation3.place(x=253, y=0)
        animation3.image = Animation3
    clickcolour()


# PSYCHEDELIC COLOURS
def clickcolour():
    global game_state
    clickcolourcheck = game_state.inc_clickcolourcheck()
    if clickcolourcheck == 0:
        clickbutton.configure(bg="red")
    elif clickcolourcheck == 1:
        clickbutton.configure(bg="orange")
    elif clickcolourcheck == 2:
        clickbutton.configure(bg="yellow")
    elif clickcolourcheck == 3:
        clickbutton.configure(bg="green")
    elif clickcolourcheck == 4:
        clickbutton.configure(bg="blue")
    elif clickcolourcheck == 5:
        clickbutton.configure(bg="purple")
    elif clickcolourcheck == 6:
        clickbutton.configure(bg="violet")


# GOLD BUTTON
def goldupgrade():
    global goldbutton

    goldbutton.destroy()
    game_state.goldcheck = False
    goldupgcheck = randint(1, 77)
    if goldupgcheck == int(1):
        game_state.scale_mps(77)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        toplevel = Toplevel()
        goldtime = Message(toplevel,
                           text="Gold Upgrade Activated (multiply current MPS by 77 for 7.7 seconds!)")
        goldtime.pack()
        master.after(7700, goldmpsstop)
    else:
        game_state.inc_money(int(game_state.get_mps() * 50))
        toplevel = Toplevel()
        goldtime2 = Message(toplevel, text="Gold Upgrade Activated (get money equal to *50 MPS!)")
        goldtime2.pack()


def goldmpsstop():
    game_state.scale_mps(1 / 77.0)
    mpstkinter.set("MPS: %s" % game_state.get_mps())


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
    autoclicktkinter.set(game_state.get_autoclick2())
    autopricetkinter.set("Auto-Clicker (Costs: $%s)" % str(format_price(game_state.get_autoprice())))
    autompstkinter.set("Auto-Clickers MPS: " + str(game_state.get_autoclick()))
    printmoneytkinter.set(game_state.get_printmoney2())
    printpricetkinter.set("Money Printer (Costs: $%s)" % str(format_price(game_state.get_printprice())))
    printmpstkinter.set("Money Printers MPS: " + str(game_state.get_printmoney() * 15))
    counterfeittkinter.set(game_state.get_counterfeit2())
    counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % str(format_price(game_state.get_counterfeitprice())
                                                                         ))
    counterfeitmpstkinter.set("Counterfeit Companies MPS: " + str(game_state.get_counterfeit() * 221))
    sharecrashtkinter.set(game_state.get_sharecrash2())
    sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % str(format_price(game_state.get_shareprice())))
    sharempstkinter.set("Sharemarket Crashes MPS: " + str(game_state.get_sharecrash() * 969))
    bankheisttkinter.set(game_state.get_bankheist2())
    bankpricetkinter.set("Bank Heist (Costs: $%s)" % str(format_price(game_state.get_bankprice())))
    bankmpstkinter.set("Bank Heists MPS: " + str(game_state.get_bankheist() * 2015))

def main():
    # BUTTONS, LABELS AND ENTRIES
    global incbutton1, incbutton2, incbutton3, incbutton4, incbutton5, upgrades, resetbutton, savebutton, clickbutton, \
        statsbutton, reportbutton, logoutbutton, moneylabel, lottoprice, lottobutton
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

    incbutton3 = Button(master, textvariable=counterfeitpricetkinter, width=33, command=deduction3)
    incbutton3.grid(row=5, column=0, sticky=W)

    checklabel3 = Label(master, textvariable=counterfeittkinter, width=2)
    checklabel3.grid(row=5, column=1, sticky=W)

    mpscheck3 = Label(master, textvariable=counterfeitmpstkinter, width=35)
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

    lottobutton = Button(master, text="Lotto ($%s) " % (lottoprice), width=35, command=lotto)
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
    if game_state.get_money() < int(game_state.get_lotto()):
        lottobutton.destroy()
        master.bell()
        lottoafford = Label(master, text="%s" % cannotafford, width=35)
        lottoafford.grid(row=8, column=0, sticky=W)
        master.after(500, lambda: eval('''lottoafford.destroy()
lottobutton = Button(master, width=35, text="Lotto ($%s) " % (lottoprice)')
lottobutton.grid(row=11, column=0, sticky=W)'''))
    else:
        money = game_state.get_money()
        money -= game_state.get_lotto()
        game_state.lottoprice *= uniform(1.1, 5.1)
        prob = random()
        if prob < (1/3.0): # 1/3 probability
            money += 50.0
        elif prob < (1/3.0 + 1/5.0): # 1/5 prob
            money += 120.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0): # 1/7 prob
            money += 200.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0): # 1/9 prob
            money += 260.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0 + 1/11.0): # 1/11 prob
            money += 500.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0 + 1/11.0 + 1/13.0): # 1/13 prob
            money += 600.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0 + 1/11.0 + 1/13.0 + 1/1013.0): # 1/1013 prob
            money += 50000.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0 + 1/11.0 + 1/13.0 + 1/1013.0 + 1/2013.0): # 1/2013 prob
            money += 250000.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0 + 1/11.0 + 1/13.0 + 1/1013.0 + 1/2013.0 + 1/3013.0): # 1/3013 prob
            money += 153250000.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0 + 1/11.0 + 1/13.0 + 1/1013.0 + 1/2013.0 + 1/3013.0 + 1/13013.0): # 1/13013 prob
            money += 23153250000.0
        elif prob < (1/3.0 + 1/5.0 + 1/7.0 + 1/9.0 + 1/11.0 + 1/13.0 + 1/1013.0 + 1/2013.0 + 1/3013.0 + 1/13013.0 + 1/23013.0): # 1/23013 prob
            money += 423153250000.0
        else:
            money /= 2.0 # hee hee hee...
        lottobutton['text'] = ('Lotto ($'+str(round(game_state.get_lotto(), 1))+')')
        game_state.set_money(money)

# LOG OUT
def logout():
    global username, g2
    del username
    del g2


def main_tick():
    global save_needed, moneytkinter, mpstkinter, inctkinter, multiplier, autopricetkinter, autoclicktkinter, \
           autompstkinter, printpricetkinter, printmoneytkinter, printmpstkinter, counterfeitpricetkinter, \
           counterfeittkinter, counterfeitmpstkinter, sharepricetkinter, sharecrashtkinter, sharempstkinter, \
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
                autopricetkinter.set("Auto-Clicker (Costs: $%s)" % str(game_state.get_autoprice()))
                autompstkinter = StringVar()
                autompstkinter.set("Auto-Clickers MPS: " + str(game_state.get_autoclick()))
                printmoneytkinter = IntVar()
                printmoneytkinter.set(g2[3])
                printpricetkinter = StringVar()
                printpricetkinter.set("Money Printer (Costs: $%s)" % str(game_state.get_printprice()))
                printmpstkinter = StringVar()
                printmpstkinter.set("Money Printers MPS: " + str(game_state.get_printmoney() * 15))
                counterfeittkinter = IntVar()
                counterfeittkinter.set(g2[5])
                counterfeitpricetkinter = StringVar()
                counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % str(game_state.get_counterfeitprice()))
                counterfeitmpstkinter = StringVar()
                counterfeitmpstkinter.set("Counterfeit Companies MPS: " + str(game_state.get_counterfeit() * 221))
                sharecrashtkinter = IntVar()
                sharecrashtkinter.set(g2[7])
                sharepricetkinter = StringVar()
                sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % str(game_state.get_shareprice()))
                sharempstkinter = StringVar()
                sharempstkinter.set("Sharemarket Crashes MPS: " + str(game_state.get_sharecrash() * 969))
                bankheisttkinter = IntVar()
                bankheisttkinter.set(g2[9])
                bankpricetkinter = StringVar()
                bankpricetkinter.set("Bank Heist (Costs: $%s)" % str(game_state.get_bankprice()))
                bankmpstkinter = StringVar()
                bankmpstkinter.set("Bank Heists MPS: " + str(game_state.get_bankheist() * 2015))
                mpstkinter = StringVar()
                mpstkinter.set("MPS: %s" % str(game_state.get_mps()))
                inctkinter = StringVar()
                inctkinter.set("+%s money!" % game_state.get_inc())
                multiplier = StringVar()
                multiplier.set("x1")
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
                if game_state and game_state.mps >= 1:
                    automoneychoice()
                lottoprice = int(game_state.get_lotto())

                if not main_laid_out:
                    main()
                    main_laid_out = True
                # break

                data_loaded = True

            except NameError:
                signin()

    master.after(1000, main_tick)


master.after(0, main_tick)
master.mainloop()

