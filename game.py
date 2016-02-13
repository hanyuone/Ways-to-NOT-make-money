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
main_laid_out = False
data_loaded = False
username = ''

game_state = None


def savegame():
    global game_state
    data = ["auto", game_state.get_autoclick2(), "print", game_state.get_printmoney2(), 
            "counter", game_state.get_counterfeit2(), 
            "shares", game_state.get_sharecrash2(),
            "upg1h1", game_state.get_upgcheck1h1(), "upg1h2", game_state.get_upgcheck1h2(), 
            "upg2h1", game_state.get_upgcheck2h1(), 
            "upg2h2", game_state.get_upgcheck2h2(),
            "upg3", game_state.get_upgcheck3(), "upg4", game_state.get_upgcheck4(), 
            "cupg1", game_state.get_clickupgcheck1(), 
            "cupg2", game_state.get_clickupgcheck2(),
            "money", float(str(game_state.get_money())[-8:]), 
            "time", game_state.get_timeplay(), 
            "clicks", game_state.get_total_clicks()]

    save_and_load.encode_and_save(username, data)

    toplevel = Toplevel()
    msg = Message(toplevel, text="Game saved!")
    msg.pack()


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
    global signincheck, game_state
    signincheck += 1

    def verifysignin():
        global g, username, game_state
        username = unentry.get()
        if save_and_load.save_file_exists(username):
            global g2, signinvalue
<<<<<<< HEAD
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
=======
            try:
                g2 = save_and_load.read_game_data(username)
                print 'g2', g2
            except IOError as ioe:
                print ioe

            g2.extend(["time", 0, "clicks", 0])
            save_and_load.encode_and_save(username, g2)
            game_state = game_model.GameState(g2)
            print 'game_state', game_state

>>>>>>> pr/46
            for i in [l, unentry, b1, b2]:
                i.destroy()

            signinvalue += 1
            # signedin = True
            save_needed = True
        else:
            showerror(title='Error!', message='Wrong Username.')

    def createaccount():
<<<<<<< HEAD
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
=======
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

>>>>>>> pr/46
        signinvalue += 1
        # signedin = True
        save_needed = True

    l = Label(master, text='Please enter your username.')
    l.grid(row=0, column=0)
    unentry = Entry(master, show='')
    unentry.grid(row=1, column=0)
    b1 = Button(master, text='Log in', command=verifysignin)
    b1.grid(row=2, column=0)
    b2 = Button(master, text='Create account under username', command=createaccount)
    b2.grid(row=3, column=0)


<<<<<<< HEAD
# REPORT AN ISSUE
=======
def set_stats(state, clicksvar, timevar):
    clicksvar.set("Total clicks: %s" % state.get_total_clicks())
    timevar.set("Total time: %s" % state.get_timeplay())


>>>>>>> pr/46
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
    global game_state
    while game_state.get_mps() > (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                 game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
        if game_state.get_mps() - 969 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                         game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
            game_state.inc_sharecrash(1 + game_state.get_upgcheck4() * 2)
            game_state.inc_sharecrash2()
            sharecrashtkinter.set("Sharemarket Crashes Amount: %s" % game_state.get_sharecrash2())
            game_state.set_shareprice(int(42000 * (math.pow(1.2, game_state.get_sharecrash2()))))
            sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % game_state.get_shareprice())
            continue
        elif game_state.get_mps() - 321 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                           game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
            game_state.inc_counterfeit(1 + game_state.get_upgcheck3() * 2)
            game_state.inc_counterfeit2()
            counterfeittkinter.set("Counterfeit Companies Amount: %s" % game_state.get_counterfeit2())
            game_state.set_counterfeit_price(int(9001 * (math.pow(1.2, game_state.get_counterfeit2()))))
            counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % game_state.get_counterfeit_price())
            continue
        elif game_state.get_mps() - 15 >= (game_state.get_autoclick() + game_state.get_printmoney() * 15 + 
                          game_state.get_counterfeit() * 321 + game_state.get_sharecrash() * 969):
            game_state.inc_printmoney(1 + game_state.get_upgcheck2h1() * 2 + game_state.get_upgcheck2h2() * 18)
            game_state.inc_printmoney2()
            printmoneytkinter.set("Money Printers Amount: %s" % game_state.get_printmoney2())
            game_state.set_printprice(int(375 * (math.pow(1.2, game_state.get_printmoney2()))))
            printpricetkinter.set("Money Printer (Costs: $%s)" % game_state.get_printprice())
            continue
        else:
            game_state.inc_autoclick(1 + game_state.get_upgcheck1h1() * 2 + game_state.get_upgcheck1h2() * 18)
            game_state.inc_autoclick2()
            autoclicktkinter.set("Money Printers Amount: %s" % game_state.get_autoclick2())
            game_state.set_autoprice(int(20 * (math.pow(1.2, game_state.get_autoclick2()))))
            autopricetkinter.set("Money Printer (Costs: $%s)" % game_state.get_autoprice())
            continue


<<<<<<< HEAD
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


=======
>>>>>>> pr/46
# STATS STUFF
def statsexpand():
    global totalclickslabel, totalclicksvar, timevar, timelabel, hidestatsbutton, game_state

    statsbutton.destroy()
<<<<<<< HEAD
    resetbutton.grid(row=4, column=0, sticky=W)
    savebutton.grid(row=4, column=2, sticky=E)
    reportbutton.grid(row=5, column=1)
    statscheck = True
=======
    resetbutton.grid(row=11, column=0, sticky=W)
    savebutton.grid(row=11, column=2, sticky=E)
    reportbutton.grid(row=12, column=1)
    game_state.statscheck = True

>>>>>>> pr/46
    totalclicksvar = StringVar()
    totalclickslabel = Label(master, textvariable=totalclicksvar)
<<<<<<< HEAD
    totalclickslabel.grid(row=3, column=1, sticky=W)
=======
    totalclickslabel.grid(row=10, column=0, sticky=W)

>>>>>>> pr/46
    timevar = StringVar()
    timelabel = Label(master, textvariable=timevar)
<<<<<<< HEAD
    timelabel.grid(row=3, column=2, sticky=E)
=======
    timelabel.grid(row=10, column=2, sticky=E)

    set_stats(game_state, totalclicksvar, timevar)

>>>>>>> pr/46
    hidestatsbutton = Button(master, text="Hide Stats", width=10, command=hidestats)
    hidestatsbutton.grid(row=2, column=0, sticky=W)


def hidestats():
    global statsbutton, game_state
    game_state.statscheck = False
    totalclickslabel.destroy()
    timelabel.destroy()
    hidestatsbutton.destroy()
    resetbutton.grid(row=3, column=0, sticky=W)
    savebutton.grid(row=3, column=2, sticky=E)
    reportbutton.grid(row=4, column=1)
    statsbutton = Button(master, text="Stats", width=10, command=statsexpand)
<<<<<<< HEAD
    statsbutton.grid(row=2, column=0, sticky=W)
    if upgbuttoncheck:
        exitupgrades.grid(row=2, column=2, sticky=E)
    elif not upgbuttoncheck:
        pass
=======
    statsbutton.grid(row=9, column=0, sticky=W)
    if game_state.get_upgbuttoncheck():
        exitupgrades.grid(row=9, column=2, sticky=E)
>>>>>>> pr/46


# AUTO CLICKER
def boostauto1h1():
    global game_state
    if game_state.get_money() < 5000 or game_state.get_autoclick2() == 0:
        global boostafford1h1
        boostbutton1h1.destroy()
        master.bell()
<<<<<<< HEAD
        boostafford1h1 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=int(1 - int(clickupgcheck1)), column=0, sticky=E)
=======
        boostafford1h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=int(2 - game_state.get_clickupgcheck1()), column=2, sticky=E)
>>>>>>> pr/46
        master.after(500, norequirements1h1)
    else:
        game_state.inc_money(-5000)
        game_state.set_autoclick(int(game_state.get_autoclick() * 15) / 10)
        game_state.inc_upgcheck1h1()
        game_state.inc_mps(game_state.get_autoclick2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton1h1.destroy()
<<<<<<< HEAD
        boostbutton2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=0, sticky=E)
        clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=0, sticky=E)
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2,
                sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=0, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)
=======
        boostbutton2h1.grid(row=max(0, 3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1())), column=2, sticky=E)
        clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                            column=2, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=2,
                            sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=2, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + 
                            game_state.get_clickupgcheck2()))
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_upgcheck2h2() + game_state.get_upgcheck3() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
>>>>>>> pr/46


def norequirements1h1():
    global boostafford1h1, boostbutton1h1
    boostafford1h1.destroy()
<<<<<<< HEAD
    boostbutton1h1 = Button(frame2, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
    boostbutton1h1.grid(row=int(1 - int(clickupgcheck1)), column=0, sticky=E)
=======
    boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
    boostbutton1h1.grid(row=int(2 - game_state.get_clickupgcheck1()), column=2, sticky=E)
>>>>>>> pr/46


def boostauto1h2():
    global game_state
    if game_state.get_money() < 555555 or game_state.get_upgcheck1h1() == 0:
        global boostafford1h2
        boostbutton1h2.destroy()
        master.bell()
<<<<<<< HEAD
        boostafford1h2 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=0,
=======
        boostafford1h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                                    game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                column=2,
>>>>>>> pr/46
                sticky=E)
        master.after(500, norequirements1h2)
    else:
        game_state.inc_money(-555555)
        game_state.set_autoclick(int(game_state.get_autoclick() * 50) / 10)
        game_state.inc_upgcheck1h2()
        game_state.inc_mps(game_state.get_autoclick2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton1h2.destroy()
<<<<<<< HEAD
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=0, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                    int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostbutton5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                  int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
=======
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() +
                            game_state.get_clickupgcheck2()),
                          column=2, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                                game_state.get_upgcheck2h1() + game_state.get_upgcheck3() + 
                                game_state.get_upgcheck4() + game_state.get_clickupgcheck1() + 
                                game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() + 
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + 
                            game_state.get_clickupgcheck2()), 
>>>>>>> pr/46
                          column=2, sticky=E)


def norequirements1h2():
    global boostbutton1h2, boostafford1h2
    boostafford1h2.destroy()
    boostbutton1h2 = Button(frame2, text="Experienced Clickers (Costs: $555555)", width=35,
                            command=boostauto1h2)
<<<<<<< HEAD
    boostbutton1h2.grid(
            row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
            column=0, sticky=E)
=======
    boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                                 game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                        column=2, sticky=E)
>>>>>>> pr/46


def deduction1():
    global game_state
    if game_state.get_money() < int(game_state.get_autoprice()):
        global incafford1

        print "can't afford, autoprice:", game_state.get_money(), game_state.get_autoprice()

        incbutton1.destroy()
        master.bell()
        incafford1 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford1.grid(row=0, column=1, sticky=W)
        master.after(500, cannotafford1)

    else:
        game_state.inc_money(-int(game_state.get_autoprice()))
        game_state.inc_autoclick(1 + game_state.get_upgcheck1h1() * 2 + game_state.get_upgcheck1h2() * 18)
        game_state.inc_autoclick2()
        game_state.inc_mps(1 + game_state.get_upgcheck1h1() * 2 + game_state.get_upgcheck1h2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        autoclicktkinter.set("Auto-Clickers Amount: %s" % game_state.get_autoclick2())
        game_state.set_autoprice(int(20 * (math.pow(1.2, game_state.get_autoclick2()))))

        print "can afford, autoprice:", game_state.get_money(), game_state.get_autoprice(), game_state.get_autoclick2()

        autopricechoice()
    game_state.set_inc(int(game_state.get_inc() + math.pow(game_state.get_clickupgcheck2() * 
        (game_state.get_autoclick() + game_state.get_printmoney() + 
                             game_state.get_counterfeit() + game_state.get_sharecrash()), 1.01)))
    if (game_state.get_autoclick() == 1 and game_state.get_sharecrash() == 0 and 
        game_state.get_counterfeit() == 0 and game_state.get_printmoney() == 0):
        automoney()


def cannotafford1():
    global incafford1, incbutton1
    incafford1.destroy()
    incbutton1 = Button(frame1, textvariable=autopricetkinter, width=35, command=deduction1)
    incbutton1.grid(row=0, column=1, sticky=W)


# MONEY PRINTER
def boostauto2h1():
    global game_state
    if game_state.get_money() < 42000 or game_state.get_printmoney2() == 0:
        global boostafford2h1
        boostbutton2h1.destroy()
        master.bell()
<<<<<<< HEAD
        boostafford2h1 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=0, sticky=E)
=======
        boostafford2h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=2, sticky=E)
>>>>>>> pr/46
        master.after(500, norequirements2h1)
    else:
        game_state.inc_money(-42000)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 15) / 10))
        game_state.inc_upgcheck2h1()
        game_state.inc_mps(game_state.get_printmoney2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton2h1.destroy()
<<<<<<< HEAD
        clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=0, sticky=E)
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2, sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=0, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=0,
                            sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=2, sticky=E)
=======
        clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                           column=2, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                                     game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=2,
                            sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                                  game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                          column=2, 
                          sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                                game_state.get_upgcheck2h1() + game_state.get_upgcheck3() + 
                                game_state.get_upgcheck4() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                                column=2, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                                game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() + game_state.get_upgcheck3() + 
                                game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                                column=2, sticky=E)
>>>>>>> pr/46


def norequirements2h1():
    global boostbutton2h1, game_state
    boostafford2h1.destroy()
    boostbutton2h1 = Button(frame2, text="Unofficial Printer License (Costs: $42000)", width=35,
                            command=boostauto2h1)
<<<<<<< HEAD
    boostbutton2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=0, sticky=E)
=======
    boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), 
                        column=2, sticky=E)
>>>>>>> pr/46


def boostauto2h2():
    global game_state
    if game_state.get_money() < 7777777 or game_state.get_upgcheck2h1() == 0:
        global boostafford2h2
        boostbutton2h2.destroy()
        master.bell()
<<<<<<< HEAD
        boostafford2h2 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
=======
        boostafford2h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_upgcheck3() + game_state.get_upgcheck4() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2,
                            sticky=E)
>>>>>>> pr/46
        master.after(500, norequirements2h2)
    else:
        game_state.inc_money(-7777777)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 50) / 10))
        game_state.inc_upgcheck2h2()
        game_state.inc_mps(game_state.get_printmoney2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton2h2.destroy()
<<<<<<< HEAD
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=0, sticky=E)
=======
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_upgcheck2h2() + game_state.get_upgcheck3() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
>>>>>>> pr/46


def norequirements2h2():
    global boostbutton2h2, game_state
    boostafford2h2.destroy()
<<<<<<< HEAD
    boostbutton2h2 = Button(frame2, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
    boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                     int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
=======
    boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
    boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                        game_state.get_upgcheck2h1() + game_state.get_upgcheck3() + 
                        game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                        column=2, sticky=E)
>>>>>>> pr/46


def deduction2():
    global game_state

    if game_state.get_money() < game_state.get_printprice():
        global incafford2
        incbutton2.destroy()
        master.bell()
        incafford2 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford2.grid(row=2, column=1, sticky=W)
        master.after(500, cannotafford2)
    else:
        game_state.inc_money(-game_state.get_printprice())
        game_state.inc_printmoney(1 + game_state.get_upgcheck2h1() * 2 + game_state.get_upgcheck2h2() * 18)
        game_state.inc_printmoney2()
        game_state.inc_mps(15 * (1 + game_state.get_upgcheck2h1() * 2 + game_state.get_upgcheck2h2() * 18))
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        printmoneytkinter.set("Money Printers Amount: %s" % game_state.get_printmoney2())
        game_state.set_printprice(int(375 * (math.pow(1.2, game_state.get_printmoney2()))))
        printpricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(game_state.get_clickupgcheck2() * 
                                (game_state.get_autoclick() + game_state.get_printmoney() + 
                                 game_state.get_counterfeit() + game_state.get_sharecrash())), 1.01)))
        if (game_state.get_printmoney() == 1 and game_state.get_sharecrash() == 0 and 
            game_state.get_counterfeit() == 0 and game_state.get_autoclick() == 0):
            automoney()


def format_price(price):

    def add_decimal(price, d):
        price = str(price / 10 ** d)
        return price[:-1] + '.' + price[-1]

    if price < 10 ** 8:
        return '%s' % price
    elif price < 10 ** 11:
        return '%sm' % add_decimal(price, 5)
    elif price < 10 ** 14:
        return '%sb' % add_decimal(price, 8)
    elif price < 10 ** 17:
        return '%st' % add_decimal(price, 11)
    elif price < 10 ** 20:
        return '%sq' % add_decimal(price, 14)
    else:
        return '%sQ' % add_decimal(price, 19)


def autopricechoice():
    autopricetkinter.set("Auto-Clicker (Costs: $%s)" % format_price(game_state.get_autoprice()))


def printpricechoice():
    printpricetkinter.set("Money Printer (Costs: $%s)" % format_price(game_state.get_printprice()))


def counterfeitpricechoice():
    counterfeitpricetkinter.set("Counterfeit Company (Costs: $%s)" % format_price(game_state.get_counterfeit_price()))


def sharepricechoice():
    sharepricetkinter.set("Sharemarket Crash (Costs: $%s)" % format_price(game_state.get_shareprice()))


def cannotafford2():
    global incafford2, incbutton2
    incafford2.destroy()
    incbutton2 = Button(frame1, textvariable=printpricetkinter, width=35, command=deduction2)
    incbutton2.grid(row=2, column=1, sticky=W)


# COUNTERFEIT COMPANY
def boostauto3():
    global game_state
    if game_state.get_money() < 2133748 or game_state.get_counterfeit2() == 0:
        global boostafford3
        boostbutton3.destroy()
        master.bell()
<<<<<<< HEAD
        boostafford3 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=0, sticky=E)
=======
        boostafford3 = Label(master, text="%s" % norequirements, width=35)
        boostafford3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=2, sticky=E)
>>>>>>> pr/46
        master.after(500, norequirements3)
    else:
        game_state.inc_money(-2133748)
        game_state.set_counterfeit(int(game_state.get_counterfeit() * 15) / 10)
        game_state.inc_mps(game_state.get_counterfeit2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        game_state.inc_upgcheck3()
        boostbutton3.destroy()
<<<<<<< HEAD
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=0, sticky=E)
=======
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck3() + 
                            game_state.get_upgcheck4() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
>>>>>>> pr/46


def norequirements3():
    global boostbutton3
    boostafford3.destroy()
    boostbutton3 = Button(frame2, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                          command=boostauto3)
<<<<<<< HEAD
    boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                   int(clickupgcheck2))), column=0, sticky=E)
=======
    boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                        game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                        column=2, sticky=E)
>>>>>>> pr/46


def deduction3():
    global game_state
    if game_state.get_money() < game_state.get_counterfeit_price():
        global incafford3
        incbutton3.destroy()
        master.bell()
        incafford3 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford3.grid(row=4, column=1, sticky=W)
        master.after(500, cannotafford3)
    else:
        game_state.inc_money(-game_state.get_counterfeit_price())
        game_state.inc_counterfeit(1 + game_state.get_upgcheck3() * 2)
        game_state.inc_counterfeit2()
        game_state.inc_mps(321 * (1 + game_state.get_upgcheck3() * 2))
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        counterfeittkinter.set("Counterfeit Companies Amount: %s" % game_state.get_counterfeit2())
        game_state.set_counterfeit_price(int(9001 * (math.pow(1.2, game_state.get_counterfeit2()))))
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
    incbutton3 = Button(frame1, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
    incbutton3.grid(row=4, column=1, sticky=W)


# SHAREMARKET CRASH
def boostauto4():
    global game_state
    if game_state.get_money() < 12345678 or game_state.get_sharecrash2() == 0:
        global boostafford4
        boostbutton4.destroy()
        master.bell()
<<<<<<< HEAD
        boostafford4 = Label(frame2, text="%s" % norequirements, width=35)
        boostafford4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
=======
        boostafford4 = Label(master, text="%s" % norequirements, width=35)
        boostafford4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() + 
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + 
                            game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
>>>>>>> pr/46
        master.after(500, norequirements4)
    else:
        game_state.inc_money(-12345678)
        game_state.set_sharecrash(int(game_state.get_sharecrash() * 15) / 10)
        game_state.inc_mps(game_state.get_sharecrash2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        game_state.inc_upgcheck4()
        boostbutton4.destroy()


def norequirements4():
    global boostbutton4, game_state
    boostafford4.destroy()
    boostbutton4 = Button(frame2, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                          command=boostauto4)
<<<<<<< HEAD
    boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                   int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
=======
    boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                        game_state.get_upgcheck2h2() + game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + 
                        game_state.get_clickupgcheck2()), 
                        column=2, sticky=E)
>>>>>>> pr/46


def deduction4():
    global game_state
    if game_state.get_money() < game_state.get_shareprice():
        global incafford4
        incbutton4.destroy()
        master.bell()
        incafford4 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford4.grid(row=6, column=1, sticky=W)
        master.after(500, cannotafford4)
    else:
        game_state.inc_money(-game_state.get_shareprice())
        game_state.inc_sharecrash(1 + game_state.get_upgcheck4() * 2)
        game_state.inc_sharecrash2()
        game_state.inc_mps(969 * (1 + game_state.get_upgcheck4() * 2))
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        sharecrashtkinter.set("Sharemarket Crashes Amount: %s" % game_state.get_sharecrash2())
        game_state.set_shareprice(int(42000 * (math.pow(1.2, game_state.get_sharecrash2()))))
        sharepricechoice()
        game_state.set_inc(int(game_state.get_inc() + math.pow(int(game_state.get_clickupgcheck2() * 
                            (game_state.get_autoclick() + game_state.get_printmoney() + 
                            game_state.get_counterfeit() + game_state.get_sharecrash())), 1.01)))
        if (game_state.get_sharecrash() == 1 and game_state.get_counterfeit() == 0 and 
            game_state.get_printmoney() == 0 and game_state.get_autoclick() == 0):
            automoney()


def cannotafford4():
    global incafford4, incbutton4
    incafford4.destroy()
    incbutton4 = Button(frame1, textvariable=sharepricetkinter, width=35, command=deduction4)
    incbutton4.grid(row=6, column=1, sticky=W)


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
                          column=0, sticky=E)
        master.after(500, norequirements5)
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
    boostbutton5 = Button(frame2, text="Bank Blueprints (Costs: $91215000)", width=35,
                          command=boostauto5)
    boostbutton5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                   int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                      column=0, sticky=E)


def deduction5():
    global money, bankheist, bankheist2, bankprice, counterfeit, printmoney, autoclick, mps, inc
    if money < int(bankprice):
        global incafford5
        incbutton5.destroy()
        master.bell()
        incafford5 = Label(frame1, text="%s" % cannotafford, width=35)
        incafford5.grid(row=8, column=1, sticky=W)
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
    incbutton5.grid(row=8, column=1, sticky=W)


# CLICKS
def collectmoney():
    global main_laid_out, game_state

    game_state.inc_money(game_state.get_inc())

    moneytkinter.set("Balance: $" + format_price(game_state.get_money()))

    game_state.inc_animate()
    animationthingy()
    game_state.inc_total_clicks()
    main_laid_out = False


def clickboost1():
    global game_state
    if game_state.get_money() < 2100:
        global clickafford1
        clickbooster1.destroy()
        master.bell()
        clickafford1 = Label(frame2, text="%s" % norequirements, width=35)
        clickafford1.grid(row=0, column=0, sticky=E)
        master.after(500, norequirementsc1)
    else:
        game_state.inc_money(-2100)
        game_state.set_inc(game_state.get_inc() + 2)
        inctkinter.set("+%s money!" % game_state.get_inc())
        game_state.inc_clickupgcheck1()
        clickbooster1.destroy()
<<<<<<< HEAD
        boostbutton1h1.grid(row=int(1 - int(clickupgcheck1)), column=0, sticky=E)
        boostbutton2h1.grid(row=int(2 - (int(upgcheck1h1) + int(clickupgcheck1))), column=0, sticky=E)
        clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=0, sticky=E)
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=2, sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=0, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=0,
                            sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=0, sticky=E)
=======
        boostbutton1h1.grid(row=2 - game_state.get_clickupgcheck1(), column=2, sticky=E)
        boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=2, sticky=E)
        clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                            column=2, sticky=E)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=2,
                            sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=2, sticky=E)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck3() + game_state.get_upgcheck4() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
        boostbutton4.grid(row=8 -(game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() + 
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
>>>>>>> pr/46


def norequirementsc1():
    global clickbooster1
    clickafford1.destroy()
    clickbooster1 = Button(frame2, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
    clickbooster1.grid(row=0, column=0, sticky=E)


def clickboost2():
    global game_state
    if game_state.get_money() < 200000 or game_state.get_clickupgcheck1() == 0:
        global clickafford2
        clickbooster2.destroy()
<<<<<<< HEAD
        master.bell()
        clickafford2 = Label(frame2, text="%s" % norequirements, width=35)
        clickafford2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=0,
                          sticky=E)
=======
        clickafford2 = Label(master, text="%s" % norequirements, width=35)
        clickafford2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                            column=2, sticky=E)
>>>>>>> pr/46
        master.after(500, norequirementsc2)
    else:
        game_state.inc_money(-200000)
        game_state.set_inc(game_state.get_inc() + game_state.get_mps() / 10)
        inctkinter.set("+%s money!" % game_state.get_inc())
        game_state.inc_clickupgcheck2()
        clickbooster2.destroy()
<<<<<<< HEAD
        boostbutton1h2.grid(
                row=int(4 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1) + int(clickupgcheck2))),
                column=0,
                sticky=E)
        boostbutton3.grid(row=int(5 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(clickupgcheck1) +
                                       int(clickupgcheck2))), column=0, sticky=E)
        boostbutton2h2.grid(row=int(6 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck3) +
                                         int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))), column=0,
                            sticky=E)
        boostbutton4.grid(row=int(7 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(clickupgcheck1) + int(clickupgcheck2))), column=0, sticky=E)
        boostafford5.grid(row=int(8 - (int(upgcheck1h1) + int(upgcheck1h2) + int(upgcheck2h1) + int(upgcheck2h2) +
                                       int(upgcheck3) + int(upgcheck4) + int(clickupgcheck1) + int(clickupgcheck2))),
                          column=0, sticky=E)
=======
        boostbutton1h2.grid(row=max(0, 5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2())),
                            column=2,
                            sticky=E)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() + 
                            game_state.get_clickupgcheck2()),
                            column=2, sticky=E)
        boostbutton4.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() + 
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
>>>>>>> pr/46


def norequirementsc2():
    global clickbooster2, game_state
    clickafford2.destroy()
    clickbooster2 = Button(frame2, text="Stainless Steel Button (Costs: $200000)", width=35,
                           command=clickboost2)
<<<<<<< HEAD
    clickbooster2.grid(row=int(3 - (int(upgcheck1h1) + int(upgcheck2h1) + int(clickupgcheck1))), column=0,
                       sticky=E)
=======
    clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                        column=2, sticky=E)
>>>>>>> pr/46


def automoneychoice():
    global game_state

    moneytkinter.set("Balance: $" + format_price(game_state.get_money()))
    automoney()

def automoney():
    if game_state.check == 10:
        auto_money_helper()
        game_state.inc_timeplay()

    bugfixer()
    game_state.inc_money(game_state.get_mps())

<<<<<<< HEAD
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
=======
    game_state.money += game_state.mps / 10.0
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
        set_stats(game_state, totalclicksvar, timevar)
>>>>>>> pr/46


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
    global game_state

    game_state.set_upgbuttoncheck(True)

    global clickbooster1, boostbutton1h1, boostbutton2h1, clickbooster2, boostbutton1h2, boostbutton3, \
        boostbutton2h2, boostbutton4, boostbutton5, exitupgrades, scrollbar2
    upgrades.destroy()
<<<<<<< HEAD
    scrollbar2 = Scrollbar(canvas2, orient="vertical", command=canvas2.yview)
    scrollbar2.grid(row=0, column=1, sticky=N+S)
    canvas2.configure(yscrollcommand=scrollbar2.set, scrollregion=(0, 0, 200, 400))
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
=======
    if game_state.get_clickupgcheck1() == 0:
        clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
        clickbooster1.grid(row=1, column=2, sticky=E)
    if game_state.get_upgcheck1h1() == 0:
        boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
        boostbutton1h1.grid(row=2 - game_state.get_clickupgcheck1(), column=2, sticky=E)
    if game_state.get_upgcheck2h1() == 0:
        boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                                command=boostauto2h1)
        boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=2, sticky=E)
    if game_state.get_clickupgcheck2() == 0:
        clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35,
                               command=clickboost2)
        clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                            column=2, sticky=E)
    if game_state.get_upgcheck1h2() == 0:
        boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35,
                                command=boostauto1h2)
        boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                                game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
    if game_state.get_upgcheck3() == 0:
        boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                              command=boostauto3)
        boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
    if game_state.get_upgcheck2h2() == 0:
        boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
        boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
    if game_state.get_upgcheck4() == 0:
        boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                              command=boostauto4)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() + 
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
>>>>>>> pr/46
    exitupgrades = Button(master, text="Hide Upgrades", command=hideupgrades)
    if game_state.statscheck:
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
    if upgcheck5 == int(0):
        boostbutton5.destroy()
    scrollbar2.destroy()
    global upgrades
    upgrades = Button(frame2, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=0, column=0, rowspan=8, sticky=E)
    exitupgrades.destroy()
<<<<<<< HEAD
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
=======
    if game_state.statscheck:
        hidestatsbutton.grid(row=9, column=0, sticky=W)
        resetbutton.grid(row=11, column=0, sticky=W)
        savebutton.grid(row=11, column=2, sticky=E)
    elif not game_state.statscheck:
        statsbutton.grid(row=9, column=0, sticky=W)
        resetbutton.grid(row=10, column=0, sticky=W)
        savebutton.grid(row=10, column=2, sticky=E)
>>>>>>> pr/46


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
    global goldbutton, mpstkinter

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
    global mpstkinter
    game_state.scale_mps(1 / 77.0)
    mpstkinter.set("MPS: %s" % game_state.get_mps())


def main():
    # BUTTONS, LABELS AND ENTRIES
<<<<<<< HEAD
    global incbutton1, incbutton2, incbutton3, incbutton4, incbutton5, upgrades, resetbutton, savebutton, clickbutton, \
        statsbutton, reportbutton, canvas1, canvas2, frame1, frame2
=======
    global incbutton1, incbutton2, incbutton3, incbutton4, upgrades, resetbutton, savebutton, clickbutton, statsbutton,\
           reportbutton, moneylabel

    print 'main() laying things out'

>>>>>>> pr/46
    background = Label(master, image=img1)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    background.image = img1

    metaframe1 = Frame(master, bg="white")
    metaframe1.grid(row=1, column=0, sticky=N+S+E+W)

    canvas1 = Canvas(metaframe1, height=200, width=200)
    canvas1.grid(row=0, column=0, sticky=N+S+E+W)

    scrollbar1 = Scrollbar(canvas1, orient="vertical", command=canvas1.yview)
    scrollbar1.grid(row=0, column=0, sticky=N+S)
    canvas1.configure(yscrollcommand=scrollbar1.set, scrollregion=(0, 0, 200, 400))

    frame1 = Frame(canvas1, bg="white", height=200)
    frame1.grid(row=0, column=1)

    metaframe2 = Frame(master, bg="white")
    metaframe2.grid(row=1, column=2, sticky=N+S+E+W)

    canvas2 = Canvas(metaframe2, height=200, width=200)
    canvas2.grid(row=0, column=0, sticky=N+S+E+W)

    frame2 = Frame(canvas2, bg="white", height=200)
    frame2.grid(row=0, column=0)

    upgrades = Button(frame2, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=0, column=0, rowspan=2, sticky=E)

    moneylabel = Label(master, textvariable=moneytkinter)
    moneylabel.grid(row=0, column=0, sticky=W)

    mpslabel = Label(master, textvariable=mpstkinter)
    mpslabel.grid(row=0, column=2, sticky=E)

    clickbutton = Button(master, textvariable=inctkinter, height=6, width=18, command=collectmoney, bg="red")
    clickbutton.grid(row=1, column=1)

    incbutton1 = Button(frame1, textvariable=autopricetkinter, width=35, command=deduction1)
    incbutton1.grid(row=0, column=1)

    checklabel1 = Label(frame1, textvariable=autoclicktkinter, width=35)
    checklabel1.grid(row=1, column=1)

    incbutton2 = Button(frame1, textvariable=printpricetkinter, width=35, command=deduction2)
    incbutton2.grid(row=2, column=1)

    checklabel2 = Label(frame1, textvariable=printmoneytkinter, width=35)
    checklabel2.grid(row=3, column=1)

    incbutton3 = Button(frame1, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
    incbutton3.grid(row=4, column=1)

    checklabel3 = Label(frame1, textvariable=counterfeittkinter, width=35)
    checklabel3.grid(row=5, column=1)

    incbutton4 = Button(frame1, textvariable=sharepricetkinter, width=35, command=deduction4)
    incbutton4.grid(row=6, column=1)

    checklabel4 = Label(frame1, textvariable=sharecrashtkinter, width=35)
    checklabel4.grid(row=7, column=1)

    incbutton5 = Button(frame1, textvariable=bankpricetkinter, width=35, command=deduction5)
    incbutton5.grid(row=8, column=1)

    checklabel5 = Label(frame1, textvariable=bankheisttkinter, width=35)
    checklabel5.grid(row=9, column=1)

    statsbutton = Button(master, text="Stats", width=10, command=statsexpand)
    statsbutton.grid(row=2, column=0)

    resetbutton = Button(master, text="Reset Game", width=10, command=resetgame)
    resetbutton.grid(row=3, column=0)

    savebutton = Button(master, text="Save Game", width=10, command=savegame)
    savebutton.grid(row=3, column=2, sticky=E)

    reportbutton = Button(master, text='Report Issue to Github', width=20, command=report)
<<<<<<< HEAD
    reportbutton.grid(row=4, column=1)

=======
    reportbutton.grid(row=11, column=1)
    
    logoutButton = Button(master, text='Log Out', width=20, command=logout)
    logoutButton.grid(row=12, column=1)
>>>>>>> pr/46

# AUTO-SAVE SYSTEM
def auto_save():
    global thread
    thread.join()
    savegame()
    exit()

<<<<<<< HEAD
thread = threading.Thread(target=master.mainloop)
thread.start()
otherThread = threading.Thread(target=auto_save)
otherThread.start()
=======
# LOG OUT
def logout():
    global username, g2
    del username
    del g2
>>>>>>> pr/46


def main_tick():
    global save_needed, moneytkinter, mpstkinter, inctkinter, autopricetkinter, autoclicktkinter, \
           printpricetkinter, printmoneytkinter, counterfeitpricetkinter, \
           counterfeittkinter, sharepricetkinter, \
           sharecrashtkinter, main_laid_out, data_loaded, game_state
    # while True:
    if signincheck == signinvalue:
<<<<<<< HEAD
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
=======
        if save_needed:
            print 'main_tick() saving'
            savegame()
            save_needed = False
        elif not data_loaded:
            print 'main_tick() NOT saving'
            try:
                moneytkinter = StringVar()
                moneytkinter.set("Balance: $0")

                autoclicktkinter = StringVar()
                autoclicktkinter.set("Auto-Clickers Amount: " + str(g2[1]))
                autopricetkinter = StringVar()
                autopricetkinter.set("Auto-Clicker (Costs: $0)")
                printmoneytkinter = StringVar()
                printmoneytkinter.set("Money Printers Amount: " + str(g2[3]))
                printpricetkinter = StringVar()
                printpricetkinter.set("Money Printer (Costs: $0)")
                counterfeittkinter = StringVar()
                counterfeittkinter.set("Counterfeit Companies Amount: " + str(g2[5]))
                counterfeitpricetkinter = StringVar()
                counterfeitpricetkinter.set("Counterfeit Company (Costs: $0)")
                sharecrashtkinter = StringVar()
                sharecrashtkinter.set("Sharemarket Crashes Amount: 0")
                sharepricetkinter = StringVar()
                sharepricetkinter.set("Sharemarket Crash (Costs: $0")
                mpstkinter = StringVar()
                mpstkinter.set("MPS: 0")
                inctkinter = StringVar()
                inctkinter.set("+%s money!" % game_state.get_inc())
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

>>>>>>> pr/46
