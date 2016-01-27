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


# STATS STUFF
def statsexpand():
    global totalclickslabel, totalclicksvar, timevar, timelabel, hidestatsbutton, game_state

    statsbutton.destroy()
    resetbutton.grid(row=11, column=0, sticky=W)
    savebutton.grid(row=11, column=2, sticky=E)
    reportbutton.grid(row=12, column=1)
    game_state.statscheck = True

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
    global statsbutton, game_state
    game_state.statscheck = False
    totalclickslabel.destroy()
    timelabel.destroy()
    hidestatsbutton.destroy()
    resetbutton.grid(row=10, column=0, sticky=W)
    savebutton.grid(row=10, column=2, sticky=E)
    statsbutton = Button(master, text="Stats", width=10, command=statsexpand)
    statsbutton.grid(row=9, column=0, sticky=W)
    if game_state.get_upgbuttoncheck():
        exitupgrades.grid(row=9, column=2, sticky=E)


# AUTO CLICKER
def boostauto1h1():
    global game_state
    if game_state.get_money() < 5000 or game_state.get_autoclick2() == 0:
        global boostafford1h1
        boostbutton1h1.destroy()
        master.bell()
        boostafford1h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h1.grid(row=int(2 - game_state.get_clickupgcheck1()), column=2, sticky=E)
        master.after(500, norequirements1h1)
    else:
        game_state.inc_money(-5000)
        game_state.set_autoclick(int(game_state.get_autoclick() * 15) / 10)
        game_state.inc_upgcheck1h1()
        game_state.inc_mps(game_state.get_autoclick2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton1h1.destroy()
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


def norequirements1h1():
    global boostafford1h1, boostbutton1h1
    boostafford1h1.destroy()
    boostbutton1h1 = Button(master, text="Stronger Mouses (Costs: $5000)", width=35, command=boostauto1h1)
    boostbutton1h1.grid(row=int(2 - game_state.get_clickupgcheck1()), column=2, sticky=E)


def boostauto1h2():
    global game_state
    if game_state.get_money() < 555555 or game_state.get_upgcheck1h1() == 0:
        global boostafford1h2
        boostbutton1h2.destroy()
        master.bell()
        boostafford1h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                                    game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                column=2,
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
                          column=2, sticky=E)


def norequirements1h2():
    global boostbutton1h2, boostafford1h2
    boostafford1h2.destroy()
    boostbutton1h2 = Button(master, text="Experienced Clickers (Costs: $555555)", width=35,
                            command=boostauto1h2)
    boostbutton1h2.grid(row=5 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + 
                                 game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
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
    incbutton1 = Button(master, textvariable=autopricetkinter, width=35, command=deduction1)
    incbutton1.grid(row=1, column=0, sticky=W)


# MONEY PRINTER
def boostauto2h1():
    global game_state
    if game_state.get_money() < 42000 or game_state.get_printmoney2() == 0:
        global boostafford2h1
        boostbutton2h1.destroy()
        master.bell()
        boostafford2h1 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), column=2, sticky=E)
        master.after(500, norequirements2h1)
    else:
        game_state.inc_money(-42000)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 15) / 10))
        game_state.inc_upgcheck2h1()
        game_state.inc_mps(game_state.get_printmoney2() * 2)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton2h1.destroy()
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


def norequirements2h1():
    global boostbutton2h1, game_state
    boostafford2h1.destroy()
    boostbutton2h1 = Button(master, text="Unofficial Printer License (Costs: $42000)", width=35,
                            command=boostauto2h1)
    boostbutton2h1.grid(row=3 - (game_state.get_upgcheck1h1() + game_state.get_clickupgcheck1()), 
                        column=2, sticky=E)


def boostauto2h2():
    global game_state
    if game_state.get_money() < 7777777 or game_state.get_upgcheck2h1() == 0:
        global boostafford2h2
        boostbutton2h2.destroy()
        master.bell()
        boostafford2h2 = Label(master, text="%s" % norequirements, width=35)
        boostafford2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_upgcheck3() + game_state.get_upgcheck4() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2,
                            sticky=E)
        master.after(500, norequirements2h2)
    else:
        game_state.inc_money(-7777777)
        game_state.set_printmoney(int(float(game_state.get_printmoney() * 50) / 10))
        game_state.inc_upgcheck2h2()
        game_state.inc_mps(game_state.get_printmoney2() * 18)
        mpstkinter.set("MPS: %s" % game_state.get_mps())
        boostbutton2h2.destroy()
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                            game_state.get_upgcheck2h2() + game_state.get_upgcheck3() + 
                            game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)


def norequirements2h2():
    global boostbutton2h2, game_state
    boostafford2h2.destroy()
    boostbutton2h2 = Button(master, text="Printing Press (Costs: $7777777)", width=35, command=boostauto2h2)
    boostbutton2h2.grid(row=7 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                        game_state.get_upgcheck2h1() + game_state.get_upgcheck3() + 
                        game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                        column=2, sticky=E)


def deduction2():
    global game_state

    if game_state.get_money() < game_state.get_printprice():
        global incafford2
        incbutton2.destroy()
        master.bell()
        incafford2 = Label(master, text="%s" % cannotafford, width=35)
        incafford2.grid(row=3, column=0, sticky=W)
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
    incbutton2 = Button(master, textvariable=printpricetkinter, width=35, command=deduction2)
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
                            game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()),
                            column=2, sticky=E)
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
                            game_state.get_upgcheck4() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)
        boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + 
                            game_state.get_upgcheck2h1() + game_state.get_upgcheck2h2() +
                            game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                            column=2, sticky=E)


def norequirements3():
    global boostbutton3
    boostafford3.destroy()
    boostbutton3 = Button(master, text="Skilled Fake Money Making (Costs: $2133748)", width=35,
                          command=boostauto3)
    boostbutton3.grid(row=6 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                        game_state.get_clickupgcheck1() + game_state.get_clickupgcheck2()), 
                        column=2, sticky=E)


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
    incbutton3 = Button(master, textvariable=counterfeitpricetkinter, width=35, command=deduction3)
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
                            column=2, sticky=E)
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
    boostbutton4 = Button(master, text="Sharemarket Catastrophe (Costs: $12345678)", width=35,
                          command=boostauto4)
    boostbutton4.grid(row=8 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck1h2() + game_state.get_upgcheck2h1() + 
                        game_state.get_upgcheck2h2() + game_state.get_upgcheck3() + game_state.get_clickupgcheck1() + 
                        game_state.get_clickupgcheck2()), 
                        column=2, sticky=E)


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
    incbutton4 = Button(master, textvariable=sharepricetkinter, width=35, command=deduction4)
    incbutton4.grid(row=7, column=0, sticky=W)


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
        clickafford1 = Label(master, text="%s" % norequirements, width=35)
        clickafford1.grid(row=1, column=2, sticky=E)
        master.after(500, norequirementsc1)
    else:
        game_state.inc_money(-2100)
        game_state.set_inc(game_state.get_inc() + 2)
        inctkinter.set("+%s money!" % game_state.get_inc())
        game_state.inc_clickupgcheck1()
        clickbooster1.destroy()
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


def norequirementsc1():
    global clickbooster1
    clickafford1.destroy()
    clickbooster1 = Button(master, text="Reinforced Button (Costs: $2100)", width=35, command=clickboost1)
    clickbooster1.grid(row=1, column=2, sticky=E)


def clickboost2():
    global game_state
    if game_state.get_money() < 200000 or game_state.get_clickupgcheck1() == 0:
        global clickafford2
        clickbooster2.destroy()
        clickafford2 = Label(master, text="%s" % norequirements, width=35)
        clickafford2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                            column=2, sticky=E)
        master.after(500, norequirementsc2)
    else:
        game_state.inc_money(-200000)
        game_state.set_inc(game_state.get_inc() + game_state.get_mps() / 10)
        inctkinter.set("+%s money!" % game_state.get_inc())
        game_state.inc_clickupgcheck2()
        clickbooster2.destroy()
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


def norequirementsc2():
    global clickbooster2, game_state
    clickafford2.destroy()
    clickbooster2 = Button(master, text="Stainless Steel Button (Costs: $200000)", width=35,
                           command=clickboost2)
    clickbooster2.grid(row=4 - (game_state.get_upgcheck1h1() + game_state.get_upgcheck2h1() + game_state.get_clickupgcheck1()), 
                        column=2, sticky=E)


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
        boostbutton2h2, boostbutton4, exitupgrades
    upgrades.destroy()
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
    exitupgrades = Button(master, text="Hide Upgrades", command=hideupgrades)
    if game_state.statscheck:
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
    global upgrades
    upgrades = Button(master, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=1, column=2, rowspan=8, sticky=E)
    exitupgrades.destroy()
    if game_state.statscheck:
        hidestatsbutton.grid(row=9, column=0, sticky=W)
        resetbutton.grid(row=11, column=0, sticky=W)
        savebutton.grid(row=11, column=2, sticky=E)
    elif not game_state.statscheck:
        statsbutton.grid(row=9, column=0, sticky=W)
        resetbutton.grid(row=10, column=0, sticky=W)
        savebutton.grid(row=10, column=2, sticky=E)


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
    global save_needed, moneytkinter, mpstkinter, inctkinter, autopricetkinter, autoclicktkinter, \
           printpricetkinter, printmoneytkinter, counterfeitpricetkinter, \
           counterfeittkinter, sharepricetkinter, \
           sharecrashtkinter, main_laid_out, data_loaded, game_state
    # while True:
    if signincheck == signinvalue:
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

