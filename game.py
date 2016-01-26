from Tkinter import *
from random import *
from tkMessageBox import showerror
from github import Github
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
# signedin = False
save_needed = False
money = 0
moneymillion = 0.0
main_laid_out = False
data_loaded = False
username = ''

game_state = None


def savegame():
    data = ["auto", int(autoclick2), "print", int(printmoney2), "counter", int(counterfeit2), "shares", int(sharecrash2),
         "upg1h1", int(upgcheck1h1), "upg1h2", int(upgcheck1h2), "upg2h1", int(upgcheck2h1), "upg2h2", int(upgcheck2h2),
         "upg3", int(upgcheck3), "upg4", int(upgcheck4), "cupg1", int(clickupgcheck1), "cupg2", int(clickupgcheck2),
         "quintillion", int(moneyquintillion), "quadrillion", int(str(moneyquadrillion)[-5:-2]), "trillion",
         int(str(moneytrillion)[-5:-2]), "billion", int(str(moneybillion)[-5:-2]), "million",
         int(str(moneymillion)[-5:-2]), "money", float(str(money)[-8:]), "time", int(timeplay), "clicks",
         int(totalclicks)]

    save_and_load.encode_and_save(username, data)

    toplevel = Toplevel()
    msg = Message(toplevel, text="Game saved!")
    msg.pack()


def signin():
    global signincheck, game_state
    signincheck += 1

    def verifysignin():
        global g, username, game_state
        username = unentry.get()
        if save_and_load.save_file_exists(username):
            global g2, signinvalue
            try:
                g2 = save_and_load.read_game_data(username)
                print 'g2', g2
            except IOError as ioe:
                print ioe

            g2.extend(["time", 0, "clicks", 0])
            save_and_load.encode_and_save(username, g2)
            game_state = game_model.GameState(g2)
            print 'game_state', game_state

            for i in [l, unentry, b1, b2]:
                i.destroy()

            signinvalue += 1
            # signedin = True
            save_needed = True
        else:
            showerror(title='Error!', message='Wrong Username.')

    def createaccount():
        global g, g2, signinvalue, username, game_state
        print("Yes")
        username = unentry.get()
        save_and_load.encode_and_save(username)

        try:
            g2 = save_and_load.read_game_data(username)
            game_state = game_model.GameState(g2)
            print 'game_state', game_state
        except IOError as ioe:
            print ioe

        signinvalue += 1
        # signedin = True
        save_needed = True

    l = Label(master, text='Please enter your username.')
    l.grid(row=1, column=1)
    unentry = Entry(master, show='')
    unentry.grid(row=2, column=1)
    b1 = Button(master, text='Log in', command=verifysignin)
    b1.grid(row=3, column=1)
    b2 = Button(master, text='Create account under username', command=createaccount)
    b2.grid(row=4, column=1)


def set_stats(state, clicksvar, timevar):
    clicksvar.set("Total clicks: %s" % state.get_total_clicks())
    timevar.set("Total time: %s" % state.get_timeplay())


def report():
    gl = globals()
    gl['t'] = Toplevel()  # global use
    Label(master=gl['t'],
          text="Make sure you are a collaborator of Ways to not make money, and you don't have a fork", bg='yellow') \
        .grid(row=1, column=1)
    Label(master=gl['t'],
          text='Please sign in to your Github account below. (Username first entry, passcode second)').grid(row=2,
                                                                                                            column=1)
    gl['une'] = Entry(master=gl['t'])
    gl['une'].grid(row=3, column=1)
    gl['pce'] = Entry(master=gl['t'], show="*")
    gl['pce'].grid(row=4, column=1)
    globals().update(gl)
    Button(master=gl['t'], text='Verify', command=_verify_report).grid(row=5, column=1)


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
            wtnmm
        except:
            showerror('Not a collaborator')
        else:
            gl['t'].destroy()
            gl['wtnmm'] = wtnmm
            verified = True
    globals().update(gl)
    if verified:
        _create_report()


def _create_report():
    gl = globals()
    gl['t'] = Toplevel()
    t = gl['t']
    Label(t, text='Issue Title: ').grid(row=0, column=0)
    gl['e'] = Entry(t)
    gl['e'].grid(row=0, column=1)
    Label(t, text='Issue Body: ').grid(row=1, column=0, columnspan=2)
    gl['tx'] = Text(t, width=35, height=10)
    gl['tx'].grid(row=2, column=0, columnspan=2)
    globals().update(gl)
    Button(t, text='Create Github Issue', command=_send_report).grid(row=3, column=0, rowspan=2)


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
    global game_state
    while game_state.get_mps() > (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                 game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
        if game_state.get_mps() - 969 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                         game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
            game_state.inc_sharecrash(1 + upgcheck4 * 2)
            game_state.inc_sharecrash2()
            sharecrashtkinter.set("Sharemarket Crashes Amount: %s" % game_state.get_sharecrash2())
            game_state.set_shareprice(int(42000 * (math.pow(1.2, game_state.get_sharecrash2()))))
            sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % game_state.get_shareprice())
            continue
        elif game_state.get_mps() - 321 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                           game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
            game_state.inc_counterfeit(1 + upgcheck3 * 2)
            game_state.inc_counterfeit2()
            counterfeittkinter.set("Counterfeit Companies Amount: %s" % game_state.get_counterfeit2())
            game_state.set_counterfeit_price(int(9001 * (math.pow(1.2, game_state.get_counterfeit2()))))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % game_state.get_counterfeit_price())
            continue
        elif game_state.get_mps() - 15 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                          game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
            global printprice
            game_state.inc_printmoney(1 + upgcheck2h1 * 2 + upgcheck2h2 * 18)
            game_state.inc_printmoney2()
            printmoneytkinter.set("Money Printers Amount: %s" % game_state.get_printmoney2())
            printprice = int(375 * (math.pow(1.2, game_state.get_printmoney2())))
            printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
            continue
        else:
            game_state.inc_autoclick(1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
            game_state.inc_autoclick2()
            autoclicktkinter.set("Money Printers Amount: %s" % game_state.get_autoclick2())
            game_state.set_autoprice(int(20 * (math.pow(1.2, game_state.get_autoclick2()))))
            autopricetkinter.set("Money Printer (Costs: $%s)" % game_state.get_autoprice())
            continue


def automoneychoice():
    global game_state

    if len(str(game_state.get_money())) <= 8:
        moneytkinter.set("Balance: $%s" % game_state.get_money())
        master.after(100, automoney)
    elif len(str(game_state.get_money())) <= 11:
        moneytkinter.set("Balance: $" + str(moneymillion) + "m")
        master.after(100, automoney2)
    elif len(str(game_state.get_money())) <= 14:
        moneytkinter.set("Balance: $" + str(moneybillion) + "b")
        master.after(100, automoney3)
    elif len(str(game_state.get_money())) <= 17:
        moneytkinter.set("Balance: $" + str(moneytrillion) + "t")
        master.after(100, automoney4)
    elif len(str(game_state.get_money())) <= 20:
        moneytkinter.set("Balance: $" + str(moneyquadrillion) + "q")
        master.after(100, automoney5)
    else:
        moneytkinter.set("Balance: $" + str(moneyquintillion) + "Q")
        master.after(100, automoney6)


# STATS STUFF
def statsexpand():
    global totalclickslabel, totalclicksvar, timevar, timelabel, statscheck, hidestatsbutton, game_state

    statsbutton.destroy()
    resetbutton.grid(row=11, column=0, sticky=W)
    savebutton.grid(row=11, column=2, sticky=E)
    reportbutton.grid(row=12, column=1)
    statscheck = True

    totalclicksvar = StringVar()
    totalclickslabel = Label(master, textvariable=totalclicksvar)
    totalclickslabel.grid(row=10, column=0, sticky=W)

    timevar = StringVar()
    timelabel = Label(master, textvariable=timevar)
    timelabel.grid(row=10, column=2, sticky=E)

    set_stats(game_state, totalclicksvar, timevar)

    hidestatsbutton = Button(master, text="Hide Stats", width=10, command=hidestats)
    hidestatsbutton.grid(row=9, column=0, sticky=W)


def hidestats():
    global statsbutton, statscheck, upgbuttoncheck
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
    global upgcheck1h1, game_state
    if game_state.get_money() < 5000 or game_state.get_autoclick2() == 0:
        global boostafford1h1
        boostbutton1h1.destroy()
        master.bell()
        boostafford1h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=int(2 - int(clickupgcheck1)), column=2, sticky=E)
        master.after(500, norequirements1h1)
    else:
        game_state.inc_money(-5000)
        game_state.set_autoclick(int(game_state.get_autoclick() * 15) / 10)
        upgcheck1h1 += 1
        game_state.inc_mps(game_state.get_autoclick2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton1h1.destroy()
        boostbutton2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
                row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        boostbutton3.grid(row=int(
                6 - (
                    int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(
                            clickupgcheck2))),
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
    global upgcheck1h2, game_state
    if game_state.get_money() < 555555 or upgcheck1h1 == 0:
        global boostafford1h2
        boostbutton1h2.destroy()
        master.bell()
        boostafford1h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h2.grid(
                row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        master.after(500, norequirements1h2)
    else:
        game_state.inc_money(-555555)
        game_state.set_autoclick(int(game_state.get_autoclick() * 50) / 10)
        upgcheck1h2 += 1
        game_state.inc_mps(game_state.get_autoclick2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton1h2.destroy()
        boostbutton3.grid(row=int(
                6 - (
                    int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(
                            clickupgcheck2))),
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
    global game_state
    if game_state.get_money() < int(game_state.get_autoprice()):
        global incafford1

        print "can't afford, autoprice:", game_state.get_money(), game_state.get_autoprice()

        incbutton1.destroy()
        master.bell()
        incafford1 = Label(master, text="%s" % cannotafford, width=35)
        incafford1.grid(row=1, column=0, sticky=W)
        master.after(500, cannotafford1)

    else:
        game_state.inc_money(-int(game_state.get_autoprice()))
        game_state.inc_autoclick(1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
        game_state.inc_autoclick2()
        game_state.inc_mps(1 + upgcheck1h1 * 2 + upgcheck1h2 * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        autoclicktkinter.set("Auto-Clickers Amount: %s" % game_state.get_autoclick2())
        game_state.set_autoprice(int(20 * (math.pow(1.2, game_state.get_autoclick2()))))

        print "can afford, autoprice:", game_state.get_money(), game_state.get_autoprice(), game_state.get_autoclick2()

        autopricechoice()
    game_state.set_inc(int(game_state.get_inc() + math.pow(int(clickupgcheck2 * (game_state.get_autoclick() + game_state.get_printmoney() + 
                             game_state.get_counterfeit() + game_state.get_sharecrash())), 1.01)))
    if (game_state.get_autoclick() == 1 and game_state.get_sharecrash() == 0 and 
        game_state.get_counterfeit() == 0 and game_state.get_printmoney() == 0):
        automoney()


def autopricechoice():
    global autopricetkinter, main_laid_out, game_state
    print 'autopricechoice', game_state.get_autoprice()

    main_laid_out = False

    if len(str(game_state.get_autoprice())) <= 8:
        autopricetkinter.set("Auto-Clicker (Costs: $%s)" % game_state.get_autoprice())
    else:
        autopricemillion = round((float(str(game_state.get_autoprice())[:-7]) / 10), 1)
        if len(str(game_state.get_autoprice())) <= 11:
            autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricemillion) + "m)")
        else:
            autopricebillion = round((float(str(autopricemillion)[:-4]) / 10), 1)
            if len(str(game_state.get_autoprice())) <= 14:
                autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricebillion) + "b)")
            else:
                autopricetrillion = round((float(str(autopricebillion)[:-4]) / 10), 1)
                if len(str(game_state.get_autoprice())) <= 17:
                    autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricetrillion) + "t)")
                else:
                    autopricequadrillion = round((float(str(autopricetrillion)[:-4]) / 10), 1)
                    if len(str(game_state.get_autoprice())) <= 20:
                        autopricetkinter.set("Auto-Clicker (Costs: $" + str(autopricequadrillion) + "q)")
                    else:
                        autopricequintillion = round((float(str(autopricequadrillion)[:-4]) / 10), 1)
                        autopricetkinter.set("Auto-Clicker (Costs : $" + str(autopricequintillion) + "Q)")


def cannotafford1():
    global incafford1, incbutton1
    incafford1.destroy()
    incbutton1 = Button(master, textvariable=autopricetkinter, width=35, command=deduction1)
    incbutton1.grid(row=1, column=0, sticky=W)


# MONEY PRINTER
def boostauto2h1():
    global upgcheck2h1
    if game_state.get_money() < 42000 or game_state.get_printmoney2() == 0:
        global boostafford2h1
        boostbutton2h1.destroy()
        master.bell()
        boostafford2h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        master.after(500, norequirements2h1)
    else:
        game_state.inc_money(-42000)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 15) / 10))
        upgcheck2h1 += 1
        game_state.inc_mps(game_state.get_printmoney2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton2h1.destroy()
        clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
                row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        boostbutton3.grid(row=int(
                6 - (
                    int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(
                            clickupgcheck2))),
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
    global upgcheck2h2
    if game_state.get_money() < 7777777 or upgcheck2h1 == 0:
        global boostafford2h2
        boostbutton2h2.destroy()
        master.bell()
        boostafford2h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=2,
                            sticky=E)
        master.after(500, norequirements2h2)
    else:
        game_state.inc_money(-7777777)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 50) / 10))
        upgcheck2h2 += 1
        game_state.inc_mps(game_state.get_printmoney2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
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
    global printprice, game_state
    if game_state.get_money() < int(printprice):
        global incafford2
        incbutton2.destroy()
        master.bell()
        incafford2 = Label(master, text="%s" % cannotafford, width=35)
        incafford2.grid(row=3, column=0, sticky=W)
        master.after(500, cannotafford2)
    else:
        game_state.inc_money(-int(printprice))
        game_state.inc_printmoney(1 + upgcheck2h1 * 2 + upgcheck2h2 * 18)
        game_state.inc_printmoney2()
        game_state.inc_mps(15 * (1 + upgcheck2h1 * 2 + upgcheck2h2 * 18))
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        printmoneytkinter.set("Money Printers Amount: %s" % game_state.get_printmoney2())
        printprice = int(375 * (math.pow(1.2, game_state.get_printmoney2())))
        printpricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(clickupgcheck2 * (game_state.get_autoclick() + game_state.get_printmoney() + 
                                 game_state.get_counterfeit() + game_state.get_sharecrash())), 1.01)))
        if (game_state.get_printmoney() == 1 and game_state.get_sharecrash() == 0 and 
            game_state.get_counterfeit() == 0 and game_state.get_autoclick() == 0):
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
    incbutton2 = Button(master, textvariable=printpricetkinter, width=35, command=deduction2)
    incbutton2.grid(row=3, column=0, sticky=W)


# COUNTERFEIT COMPANY
def boostauto3():
    global upgcheck3, game_state
    if game_state.get_money() < 2133748 or game_state.get_counterfeit2() == 0:
        global boostafford3
        boostbutton3.destroy()
        master.bell()
        boostafford3 = Label(master, text="%s" % norequirements, width=35)
        boostafford3.grid(row=int(
                6 - (
                    int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(
                            clickupgcheck2))),
                column=2, sticky=E)
        master.after(500, norequirements3)
    else:
        game_state.inct_money(-2133748)
        game_state.set_counterfeit(int(game_state.get_counterfeit() * 15) / 10)
        game_state.inc_mps(game_state.get_counterfeit2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
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
    global game_state
    if game_state.get_money() < game_state.get_counterfeit_price():
        global incafford3
        incbutton3.destroy()
        master.bell()
        incafford3 = Label(master, text="%s" % cannotafford, width=35)
        incafford3.grid(row=5, column=0, sticky=W)
        master.after(500, cannotafford3)
    else:
        game_state.inc_money(-game_state.get_counterfeit_price())
        game_state.inc_counterfeit(1 + upgcheck3 * 2)
        game_state.inc_counterfeit2()
        game_state.inc_mps(321 * (1 + upgcheck3 * 2))
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        counterfeittkinter.set("Counterfeit Companies Amount: %s" % game_state.get_counterfeit2())
        game_state.set_counterfeit_price(int(9001 * (math.pow(1.2, game_state.get_counterfeit2()))))
        counterfeitpricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(clickupgcheck2 * (game_state.get_autoclick() + game_state.get_printmoney() + 
                                 game_state.get_counterfeit() + game_state.get_sharecrash())), 1.01)))
        if (game_state.get_counterfeit() == 1 and game_state.get_sharecrash() == 0 and 
            game_state.get_printmoney() == 0 and game_state.get_autoclick() == 0):
            automoney()


def counterfeitpricechoice():
    if len(str(game_state.get_counterfeit_price())) <= 8:
        counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % game_state.get_counterfeit_price())
    else:
        counterfeitpricemillion = round((float(str(game_state.get_counterfeit_price())[:-7]) / 10), 1)
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
    incbutton3 = Button(master, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
    incbutton3.grid(row=5, column=0, sticky=W)


# SHAREMARKET CRASH
def boostauto4():
    global upgcheck4
    if game_state.get_money() < 12345678 or game_state.get_sharecrash2() == 0:
        global boostafford4
        boostbutton4.destroy()
        master.bell()
        boostafford4 = Label(master, text="%s" % norequirements, width=35)
        boostafford4.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=2, sticky=E)
        master.after(500, norequirements4)
    else:
        game_state.inc_money(-12345678)
        game_state.set_sharecrash(int(sharecrash * 15) / 10)
        game_state.inc_mps(game_state.get_sharecrash2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
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
    global game_state
    if game_state.get_money() < game_state.get_shareprice():
        global incafford4
        incbutton4.destroy()
        master.bell()
        incafford4 = Label(master, text="%s" % cannotafford, width=35)
        incafford4.grid(row=7, column=0, sticky=W)
        master.after(500, cannotafford4)
    else:
        game_state.inc_money(-game_state.get_shareprice())
        game_state.inc_sharecrash(1 + upgcheck4 * 2)
        game_state.inc_sharecrash2()
        game_state.inc_mps(969 * (1 + upgcheck4 * 2))
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        sharecrashtkinter.set("Sharemarket Crashes Amount: %s" % game_state.get_sharecrash2())
        game_state.set_shareprice(int(42000 * (math.pow(1.2, game_state.get_sharecrash2()))))
        sharepricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(clickupgcheck2 * (game_state.get_autoclick() + game_state.get_printmoney() + 
                        game_state.get_counterfeit() + game_state.get_sharecrash())), 1.01)))
        if (game_state.get_sharecrash() == 1 and game_state.get_counterfeit() == 0 and 
            game_state.get_printmoney() == 0 and game_state.get_autoclick() == 0):
            automoney()


def sharepricechoice():
    global game_state

    if len(str(game_state.get_shareprice())) <= 8:
        sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % game_state.get_shareprice())
    else:
        sharepricemillion = round((float(str(game_state.get_shareprice())[:-7]) / 10), 1)
        if len(str(game_state.get_shareprice())) <= 11:
            sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricemillion) + "m)")
        else:
            sharepricebillion = round((float(str(sharepricemillion)[:-4]) / 10), 1)
            if len(str(game_state.get_shareprice())) <= 14:
                sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricebillion) + "b)")
            else:
                sharepricetrillion = round((float(str(sharepricebillion)[:-4]) / 10), 1)
                if len(str(game_state.get_shareprice())) <= 17:
                    sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricetrillion) + "t)")
                else:
                    sharepricequadrillion = round((float(str(sharepricetrillion)[:-4]) / 10), 1)
                    if len(str(game_state.get_shareprice())) <= 20:
                        sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(sharepricequadrillion) + "q)")
                    else:
                        sharepricequintillion = round((float(str(sharepricequadrillion)[:-4]) / 10), 1)
                        sharepricetkinter.set("Sharemarket Crash (Costs : $" + str(sharepricequintillion) + "Q)")


def cannotafford4():
    global incafford4, incbutton4
    incafford4.destroy()
    incbutton4 = Button(master, textvariable=sharepricetkinter, width=35, command=deduction4)
    incbutton4.grid(row=7, column=0, sticky=W)


# CLICKS
def collectmoney():
    global animate, totalclicks, main_laid_out, game_state
    game_state.inc_money(game_state.get_inc())
    print 'collectmoney', game_state.get_money(), game_state.get_inc(), moneymillion
    if moneymillion == 0.0:
        moneytkinter.set("Balance: $%s" % game_state.get_money())
    else:
        moneytkinter.set("Balance: $" + str(moneymillion) + "m")
    animate += 1
    if animate > 3:
        animate = 1
    animationthingy()
    game_state.inc_total_clicks()
    main_laid_out = False


def clickboost1():
    global clickupgcheck1
    if game_state.get_money() < 2100:
        global clickafford1
        clickbooster1.destroy()
        clickafford1 = Label(master, text="%s" % norequirements, width=35)
        clickafford1.grid(row=1, column=2, sticky=E)
        master.after(500, norequirementsc1)
    else:
        game_state.inc_money(-2100)
        game_state.set_inc(game_state.get_inc() + 2)
        inctkinter.set("+%s money!" % game_state.get_inc())
        clickupgcheck1 += 1
        clickbooster1.destroy()
        boostbutton1h1.grid(row=int(2 - int(clickupgcheck1)), column=2, sticky=E)
        boostbutton2h1.grid(row=int(3 - (int(upgcheck1h1) + int(clickupgcheck1))), column=2, sticky=E)
        clickbooster2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2, sticky=E)
        boostbutton1h2.grid(
                row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        boostbutton3.grid(row=int(
                6 - (
                    int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(
                            clickupgcheck2))),
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
    global clickupgcheck2
    if game_state.get_money() < 200000 or clickupgcheck1 == int(0):
        global clickafford2
        clickbooster2.destroy()
        clickafford2 = Label(master, text="%s" % norequirements, width=35)
        clickafford2.grid(row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=2,
                          sticky=E)
        master.after(500, norequirementsc2)
    else:
        game_state.inc_money(-200000)
        game_state.set_inc(game_state.get_inc() + game_state.get_mps() / 10)
        inctkinter.set("+%s money!" % game_state.get_inc())
        clickupgcheck2 += 1
        clickbooster2.destroy()
        boostbutton1h2.grid(
                row=int(5 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        boostbutton3.grid(row=int(
                6 - (
                    int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) + int(
                            clickupgcheck2))),
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
    global check, goldbutton, goldcheck, game_state
    game_state.set_money(round(game_state.get_money(), 1))
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
            set_stats(game_state, totalclicksvar, timevar)
        bugfixer()
        game_state.inc_timeplay()
    game_state.inc_money(game_state.get_mps() / 10.0)
    check += 1
    automoneychoice()


# AUTOMATIC MONEY (MILLIONS)
def automoney2():
    global check, goldbutton, goldcheck, timeplay, moneymillion, templist1, game_state
    if len(str(game_state.get_money())) >= 8:
        moneymillion = round((float(str(game_state.get_money())[:-7]) / 10), 1)
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
                set_stats(game_state, totalclicksvar, timevar)

            timeplay += 1
            game_state.inc_timeplay()
            templist1.append(moneymillion)
            if len(templist1) > 2:
                templist1.reverse()
                templist1.pop()
                templist1.reverse()
            if float(templist1[1]) != float(templist1[0]):
                moneymillion += float(templist1[1] - templist1[0]) / 10
        bugfixer()
        game_state.inc_money(game_state.get_mps())
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (BILLIONS)
def automoney3():
    global check, goldbutton, goldcheck, moneybillion, moneymillion, templist2, game_state
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
                set_stats(game_state, totalclicksvar, timevar)

            game_state.inc_timeplay()
            templist2.append(moneybillion)
            if len(templist2) > 2:
                templist2.reverse()
                templist2.pop()
                templist2.reverse()
            if float(templist2[1]) != float(templist2[0]):
                moneybillion += float(templist2[1] - templist2[0]) / 10
        bugfixer()
        moneymillion = float(math.floor((moneymillion + float(game_state.get_mps()) / 10 ** 6) * 10))
        game_state.inc_money(game_state.get_mps())
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (TRILLIONS)
def automoney4():
    global check, goldbutton, goldcheck, moneytrillion, moneybillion, moneymillion, templist3, game_state
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
                set_stats(game_state, totalclicksvar, timevar)

            game_state.inc_timeplay()
            templist3.append(moneytrillion)
            if len(templist3) > 2:
                templist3.reverse()
                templist3.pop()
                templist3.reverse()
            if float(templist3[1]) != float(templist3[0]):
                moneytrillion += float(templist3[1] - templist3[0]) / 10
        bugfixer()
        moneybillion = float(math.floor((moneybillion + float(game_state.get_mps()) / 10 ** 9) * 10))
        moneymillion = float(math.floor((moneymillion + float(game_state.get_mps()) / 10 ** 6) * 10))
        game_state.inc_money(game_state.get_mps())
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (QUADRILLIONS)
def automoney5():
    global check, goldbutton, goldcheck, moneyquadrillion, moneytrillion, moneybillion, moneymillion, templist4, game_state
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
                set_stats(game_state, totalclicksvar, timevar)

            game_state.inc_timeplay()
            templist4.append(moneyquadrillion)
            if len(templist4) > 2:
                templist4.reverse()
                templist4.pop()
                templist4.reverse()
            if float(templist4[1]) != float(templist4[0]):
                moneyquadrillion += float(templist4[1] - templist4[0]) / 10
        bugfixer()
        moneytrillion = float(math.floor((moneytrillion + float(game_state.get_mps()) / 10 ** 12) * 10))
        moneybillion = float(math.floor((moneybillion + float(game_state.get_mps()) / 10 ** 9) * 10))
        moneymillion = float(math.floor((moneymillion + float(game_state.get_mps()) / 10 ** 6) * 10))
        game_state.inc_money(game_state.get_mps())
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# AUTOMATIC MONEY (QUINTILLIONS)
def automoney6():
    global check, goldbutton, goldcheck, moneyquintillion, moneyquadrillion, moneytrillion, moneybillion, moneymillion, templist5, game_state
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
                set_stats(game_state, totalclicksvar, timevar)

            game_state.inc_timeplay()
            templist5.append(moneyquintillion)
            if len(templist5) > 2:
                templist5.reverse()
                templist5.pop()
                templist5.reverse()
            if float(templist5[1]) != float(templist5[0]):
                moneyquintillion += float(templist5[1] - templist5[0]) / 10
        bugfixer()
        moneyquadrillion = float(math.floor(moneyquadrillion + float(game_state.get_mps()) / 10 ** 15) * 10)
        moneytrillion = float(math.floor((moneytrillion + float(game_state.get_mps()) / 10 ** 12) * 10))
        moneybillion = float(math.floor((moneybillion + float(game_state.get_mps()) / 10 ** 9) * 10))
        moneymillion = float(math.floor((moneymillion + float(game_state.get_mps()) / 10 ** 6) * 10))
        game_state.inc_money(game_state.get_mps())
        check += 1
        automoneychoice()
    else:
        automoneychoice()


# RESETTING GAME
def resetgame():
    toplevel = Toplevel()
    msg = Label(toplevel, text="Are you sure you want to reset?")
    msg.grid(row=0, column=0, columnspan=2)

    yesbutton = Button(toplevel, text="Yes", command=lambda: save_and_load.encode_and_save(username))
    yesbutton.grid(row=1, column=0)
    nobutton = Button(toplevel, text="No", command=toplevel.destroy)
    nobutton.grid(row=1, column=1)


# UPGRADES WINDOW
def showupgrades():
    global upgbuttoncheck, statscheck
    upgbuttoncheck = True
    global clickbooster1, boostbutton1h1, boostbutton2h1, clickbooster2, boostbutton1h2, boostbutton3, \
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
    global upgrades
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
    global goldbutton, mpstkinter, goldcheck
    goldbutton.destroy()
    goldcheck = int(0)
    goldupgcheck = randint(1, 77)
    if goldupgcheck == int(1):
        game_state.scale_mps(77)
        mpstkinter = ("MPS: %s" % game_state.get_mps())
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
    global mps, mpstkinter
    game_state.scale_mps(1 / 77.0)
    mpstkinter = ("MPS: %s" % game_state.get_mps())


def main():
    # BUTTONS, LABELS AND ENTRIES
    global incbutton1, incbutton2, incbutton3, incbutton4, upgrades, resetbutton, savebutton, clickbutton, statsbutton,\
           reportbutton, moneylabel

    print 'main() laying things out'

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

    statsbutton = Button(master, text="Stats", width=10, command=statsexpand)
    statsbutton.grid(row=9, column=0, sticky=W)

    resetbutton = Button(master, text="Reset Game", width=10, command=resetgame)
    resetbutton.grid(row=10, column=0, sticky=W)

    savebutton = Button(master, text="Save Game", width=10, command=savegame)
    savebutton.grid(row=10, column=2, sticky=E)

    reportbutton = Button(master, text='Report Issue to Github', width=20, command=report)
    reportbutton.grid(row=11, column=1)
    
    logoutButton = Button(master, text='Log Out', width=20, command=logout)
    logoutButton.grid(row=12, column=1)


# LOG OUT
def logout():
    global username, g2
    del username
    del g2


def main_tick():
    global animate, autoclick, autoclick2, clickcolourcheck, totalclicks, upgbuttoncheck, \
           upgcheck1h1, upgcheck1h2, upgcheck2h1, upgcheck2h2, upgcheck3, upgcheck4, clickupgcheck1, clickupgcheck2, \
           mps, printmoney, printmoney2, counterfeit, counterfeit2, sharecrash, sharecrash2, \
           save_needed, moneytkinter, mpstkinter, inctkinter, autopricetkinter, autoclicktkinter, \
           printprice, printpricetkinter, printmoneytkinter, counterfeitpricetkinter, \
           counterfeittkinter, shareprice, sharepricetkinter, \
           sharecrashtkinter, check, main_laid_out, statscheck, timeplay, goldcheck, \
           money, moneymillion, moneybillion, moneytrillion, moneyquadrillion, moneyquintillion, data_loaded
    # while True:
    if signincheck == signinvalue:
        if save_needed:
            print 'main_tick() saving'
            savegame()
            save_needed = False
        elif not data_loaded:
            print 'main_tick() NOT saving'
            try:
                check = False
                upgbuttoncheck = False
                goldcheck = False
                statscheck = False
                animate = 0
                totalclicks = int(g2[39])
                timeplay = int(g2[37])
                click = 0
                clickcolourcheck = 1
                upgcheck1h1 = int(g2[9])
                upgcheck1h2 = int(g2[11])
                upgcheck2h1 = int(g2[13])
                upgcheck2h2 = int(g2[15])
                upgcheck3 = int(g2[17])
                upgcheck4 = int(g2[19])
                clickupgcheck1 = int(g2[21])
                clickupgcheck2 = int(g2[23])
                money = float(str(g2[25] + g2[27] + g2[29] + g2[31] + g2[33] + g2[35]))
                if len(str(money)) < 8:
                    moneycheck = "0"
                else:
                    moneycheck = str(money)[:1]
                moneymillion = round(float(str(g2[25] + g2[27] + g2[29] + g2[31] + g2[33]) + "." + moneycheck), 1)
                if len(str(moneymillion)) < 5:
                    moneymillioncheck = "0"
                else:
                    moneymillioncheck = str(moneymillion)[:1]
                moneybillion = round(float(str(g2[25] + g2[27] + g2[29] + g2[31]) + "." + moneymillioncheck), 1)
                if len(str(moneybillion)) < 5:
                    moneybillioncheck = "0"
                else:
                    moneybillioncheck = str(moneybillion)[:1]
                moneytrillion = round(float(str(g2[25] + g2[27] + g2[29]) + "." + moneybillioncheck), 1)
                if len(str(moneytrillion)) < 5:
                    moneytrillioncheck = "0"
                else:
                    moneytrillioncheck = str(moneytrillion)[:1]
                moneyquadrillion = round(float(str(g2[25] + g2[27]) + "." + moneytrillioncheck), 1)
                if len(str(moneyquadrillion)) < 5:
                    moneyquadrillioncheck = "0"
                else:
                    moneyquadrillioncheck = str(moneyquadrillion)[:1]
                moneyquintillion = round(float(str(g2[25]) + "." + moneyquadrillioncheck), 1)

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

                autoclick = int((g2[1] * 18 * int(g2[11])) + (g2[1] * 2 * int(g2[9])) + g2[1])
                autoclick2 = int(g2[1])
                autoclicktkinter = StringVar()
                autoclicktkinter.set("Auto-Clickers Amount: " + str(g2[1]))
                autoprice = int(20 * (math.pow(1.2, int(g2[1]))))
                autopricetkinter = StringVar()
                autopricetkinter.set("Auto-Clicker (Costs: $" + str(autoprice) + ")")
                printmoney = int((g2[3] * 2 * int(g2[13])) + g2[3])
                printmoney2 = int(g2[3])
                printmoneytkinter = StringVar()
                printmoneytkinter.set("Money Printers Amount: " + str(g2[3]))
                printprice = int(375 * (math.pow(1.2, int(g2[3]))))
                printpricetkinter = StringVar()
                printpricetkinter.set("Money Printer (Costs: $" + str(printprice) + ")")
                counterfeit = int((g2[5] * 2 * int(g2[17])) + g2[5])
                counterfeit2 = int(g2[5])
                counterfeittkinter = StringVar()
                counterfeittkinter.set("Counterfeit Companies Amount: " + str(g2[5]))
                counterfeitprice = int(9001 * (math.pow(1.2, int(g2[5]))))
                counterfeitpricetkinter = StringVar()
                counterfeitpricetkinter.set("Counterfeit Company (Costs: $" + str(counterfeitprice) + ")")
                sharecrash = int((g2[7] * 2 * int(g2[19])) + g2[7])
                sharecrash2 = int(g2[7])
                sharecrashtkinter = StringVar()
                sharecrashtkinter.set("Sharemarket Crashes Amount: " + str(sharecrash2))
                shareprice = int(42000 * (math.pow(1.2, int(g2[7]))))
                sharepricetkinter = StringVar()
                sharepricetkinter.set("Sharemarket Crash (Costs: $" + str(shareprice) + ")")
                mps = int(g2[1]) + 15 * int(g2[3]) + 321 * int(g2[5]) + 969 * int(g2[7])
                mpstkinter = StringVar()
                mpstkinter.set("MPS: " + str(mps))
                inc = int(1 + (int(g2[21]) * 2) + int(g2[23]) * (mps / 10))
                inctkinter = StringVar()
                inctkinter.set("+%s money!" % game_state.get_inc())
                templist1 = [moneymillion] * 2
                templist2 = [moneybillion] * 2
                templist3 = [moneytrillion] * 2
                templist4 = [moneyquadrillion] * 2
                templist5 = [moneyquintillion] * 2
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
                if mps >= 1:
                    automoneychoice()

                print 'main_tick(), main_laid_out', main_laid_out
                if not main_laid_out:
                    main()
                    main_laid_out = True
                # break

                data_loaded = True

            except NameError as ne:
                print ne
                signin()

    master.after(1000, main_tick)


master.after(0, main_tick)
master.mainloop()

