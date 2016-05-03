from tkinter import *
from random import *
from tkinter.messagebox import showerror
import math
import save_and_load
import frames
import game_model
import webbrowser
import sys

master = Tk()
master.title("Ways To NOT Earn Money")

img1 = PhotoImage(file="img1.gif")
gold = PhotoImage(file="gold.gif")
Animation1 = PhotoImage(file="Animation1.gif")
Animation2 = PhotoImage(file="Animation2.gif")
Animation3 = PhotoImage(file="Animation3.gif")
norequirements = "You do not meet the requirements."
cannotafford = "You cannot afford this."
username = ''

game_state = None

def log(*args):
    if 'debug' in sys.argv:
        print(*args)

def savegame():
    global game_state
    data = ["auto", game_state.autoclick2, "print", game_state.printmoney2, "counter", game_state.counterfeit2,
            "shares", game_state.sharecrash2, "bank", game_state.bankheist2, "upg1h1", game_state.upgcheck1h1,
            "upg1h2", game_state.upgcheck1h2, "upg2h1", game_state.upgcheck2h1, "upg2h2", game_state.upgcheck2h2,
            "upg3", game_state.upgcheck3, "upg4", game_state.upgcheck4, "upg5", game_state.upgcheck5,
            "cupg1", game_state.clickupgcheck1, "cupg2", game_state.clickupgcheck2, "money",
            float(str(game_state.money)[-8:]), "time", game_state.timeplay, "clicks",
            game_state.totalclicks, "lotto", game_state.lottoprice]
    log('savegame invoked', data)

    log('savegame function')
    save_and_load.encode_and_save(username, data)

    toplevel = Toplevel()
    msg = Message(toplevel, text="Game saved!")
    msg.pack()


def signin():

    log('signin invoked')

    def verifysignin(login_frame, username):
        global game_state
        if save_and_load.save_file_exists(username):
            global g2

            login_frame.destroy()

            try:
                g2 = save_and_load.read_game_data(username)
                log('g2', g2)
            except IOError as ioe:
                log(ioe)

            log('verifysignin function')
            save_and_load.encode_and_save(username, g2)

            game_state = game_model.GameState(g2)
            log('game_state', str(game_state))

            main()

        else:
            showerror(title='Error!', message='Wrong Username.')

    def createaccount(login_frame, username):
        global game_state

        login_frame.destroy()

        save_and_load.encode_and_save(username, data=None)

        try:
            g2 = save_and_load.read_game_data(username)
            game_state = game_model.GameState(g2)
            log('game_state', str(game_state))
            main()
        except IOError as ioe:
            log(ioe)

    lf = frames.LoginFrame(master, verifysignin, createaccount)
    master.after(100, lambda: lf.lift())


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
            game_state.bankprice = int(42000 * (math.pow(1.1, game_state.bankheist2)))
            bankpricechoice()

        elif game_state.mps - 969 >= (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                                      game_state.sharecrash * 969 + game_state.bankheist * 2015):
            game_state.sharecrash += 1 + game_state.upgcheck4 * 2
            game_state.sharecrash2 += 1
            game_state.shareprice = int(42000 * (math.pow(1.4, game_state.sharecrash2)))
            sharepricechoice()

        elif game_state.mps - 321 >= (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                                      game_state.sharecrash * 969 + game_state.bankheist * 2015):
            game_state.counterfeit += 1 + game_state.upgcheck3 * 2
            game_state.counterfeit2 += 1
            game_state.counterprice = int(9001 * (math.pow(1.3, game_state.counterfeit2)))
            counterpricechoice()

        elif game_state.mps - 15 >= (game_state.autoclick + game_state.printmoney * 15 + game_state.counterfeit * 321 +
                                     game_state.sharecrash * 969 + game_state.bankheist * 2015):
            game_state.printmoney += (1 + game_state.upgcheck2h1 * 2 + game_state.upgcheck2h2 * 18)
            game_state.printmoney2 += 1
            counterpricechoice()
            game_state.printprice = int(375 * (math.pow(1.25, game_state.printmoney2)))
            printpricechoice()

        else:
            game_state.autoclick += (1 + game_state.upgcheck1h1 * 2 + game_state.upgcheck1h2 * 18)
            game_state.autoclick2 += 1
            game_state.autoprice = int(20 * (math.pow(1.15, game_state.autoclick2)))
            autopricechoice()


def deduction1():
    log('deduction1 invoked')
    global game_state
    if game_state.money < int(game_state.autoprice):
        master.bell()
        status_var.set(cannotafford)

    else:
        game_state.money -= game_state.autoprice
        game_state.autoclick += (1 + game_state.upgcheck1h1 * 2 + game_state.upgcheck1h2 * 18) * game_state.multiplier
        game_state.autoclick2 += game_state.multiplier
        game_state.mps += (1 + game_state.upgcheck1h1 * 2 + game_state.upgcheck1h2 * 18) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        status_var.set('Auto-Clicker purchased')
        game_state.autoprice = int(20 * (math.pow(1.15, game_state.autoclick2)))
        autopricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.autoclick, 1.01)
    if (game_state.autoclick == 1 and game_state.bankheist == 0 and game_state.sharecrash == 0 and
        game_state.counterfeit == 0 and game_state.printmoney == 0):
        automoney()


def deduction2():
    global game_state
    log('deduction2  invoked')

    if game_state.money < game_state.printprice:
        master.bell()
        status_var.set(cannotafford)
    else:
        game_state.money -= game_state.printprice
        game_state.printmoney += (1 + game_state.upgcheck2h1 * 2 + game_state.upgcheck2h2 * 18) * game_state.multiplier
        game_state.printmoney2 += game_state.multiplier
        game_state.mps += 15 * (1 + game_state.upgcheck2h1 * 2 + game_state.upgcheck2h2 * 18) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        counterpricechoice()
        status_var.set('Money Printer purchased')
        game_state.printprice = 375 * math.pow(1.25, game_state.printmoney2)
        printpricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.printmoney, 1.01)
        if (game_state.printmoney == 1 and game_state.bankheist == 0 and game_state.sharecrash == 0 and
            game_state.counterfeit == 0 and game_state.autoclick == 0):
            automoney()


def deduction3():
    global game_state
    log('deduction3 invoked')
    if game_state.money < game_state.counterprice:
        master.bell()
        status_var.set(cannotafford)
    else:
        game_state.money -= game_state.counterprice
        game_state.counterfeit += (1 + game_state.upgcheck3 * 2) * game_state.multiplier
        game_state.counterfeit2 += game_state.multiplier
        game_state.mps += 221 * (1 + game_state.upgcheck3 * 2) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        status_var.set('Counterfeit Company purchased')
        game_state.counterprice = 9001 * math.pow(1.3, game_state.counterfeit2)
        counterpricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.counterfeit, 1.01)
        if (game_state.counterfeit == 1 and game_state.bankheist and game_state.sharecrash == 0 and
            game_state.printmoney == 0 and game_state.autoclick == 0):
            automoney()


def deduction4():
    global game_state
    log('deduction4 invoked')
    if game_state.money < game_state.shareprice:
        master.bell()
        status_var.set(cannotafford)
    else:
        game_state.money -= game_state.shareprice
        game_state.sharecrash += (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        game_state.sharecrash2 += game_state.multiplier
        game_state.mps += 969 * (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        status_var.set('Sharemarket Crash purchased')
        game_state.shareprice = 42000 * math.pow(1.4, game_state.sharecrash2)
        sharepricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.sharecrash, 1.01)
        if (game_state.sharecrash == 1 and game_state.bankheist == 1 and
            game_state.counterfeit == 0 and game_state.printmoney == 0 and game_state.autoclick == 0):
            automoney()


def deduction5():
    global game_state
    log('deduction5 invoked')
    if game_state.money < game_state.bankprice:
        master.bell()
        status_var.set(cannotafford)
    else:
        game_state.money -= game_state.bankprice
        game_state.bankheist += (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        game_state.bankheist2 += game_state.multiplier
        game_state.mps += 1844 * (1 + game_state.upgcheck4 * 2) * game_state.multiplier
        mpstkinter.set("MPS: %s" % game_state.mps)
        status_var.set('Bank Heist purchased')
        bankpricechoice()
        game_state.bankprice = int(42000 * math.pow(1.1, game_state.bankheist2))
        bankpricechoice()
        game_state.inc += math.pow(game_state.clickupgcheck2 * game_state.bankheist, 1.01)
        if (game_state.bankheist == 1 and game_state.sharecrash == 0 and game_state.counterfeit == 0 and
            game_state.printmoney == 0 and game_state.autoclick == 0):
            automoney()


def normal_upgrade(button_frame, tup):
    global game_state
    log('normal_upgrade called', tup)

    (button_label, alt_func, cost, state_dict_key_check, state_dict_key_mod, done_attr, incr_ratio, mps_incr_ratio) = tup

    if alt_func:
        alt_func(button_frame, button_label)

    else:
        if game_state.money < cost or getattr(game_state, state_dict_key_check) == 0:
            master.bell()
            status_var.set(norequirements)
        else:
            game_state.money -= cost
            setattr(game_state, state_dict_key_mod, int(getattr(game_state, state_dict_key_mod) * incr_ratio))
            game_state.mps = getattr(game_state, state_dict_key_check) * mps_incr_ratio
            mpstkinter.set("MPS: %s" % game_state.mps)
            setattr(game_state, done_attr, getattr(game_state, done_attr) + 1)
            button_frame.hide(button_label)

# Reinforced Button
def clickboost1(button_frame, button_name):
    global game_state
    log('cb1 invoked')
    if game_state.money < 2100:
        log('actual money', game_state.money)
        master.bell()
        status_var.set(norequirements)
    else:
        game_state.money -= 2100
        game_state.inc += 2
        inctkinter.set("+%s money!" % game_state.inc)
        game_state.clickupgcheck1 += 1
        button_frame.hide(button_name)

# Stainless Steel Button
def clickboost2(button_frame, button_name):
    global game_state
    log('cb2 invoked')
    if game_state.money < 200000 or not game_state.clickupgcheck1:
        master.bell()
        status_var.set(norequirements)
    else:
        game_state.money -= 200000
        game_state.inc += game_state.mps / 10
        inctkinter.set("+%s money!" % game_state.inc)
        game_state.clickupgcheck2 += 1
        button_frame.hide(button_name)

button_names_and_actions = [
    ('Reinforced Button (Costs: $2100)', clickboost1, 2100, None, None, None, None, None),
    ('Stronger Mouses (Costs: $5000)', None, 5000, 'autoclick2', 'autoclick', 'upgcheck1h1', 1.5, 1.5),
    ('Unofficial Printer License (Costs: $42000)', None, 42000, 'printmoney2', 'printmoney', 'upgcheck2h1', 1.5, 1.5),
    ('Stainless Steel Button (Costs: $200000)', clickboost2, 200000, None, None, None, None, None),
    ('Experienced Clickers (Costs: $555555)', None, 555555, 'autoclick2', 'autoclick', 'upgcheck1h2', 5.0, 6.0),
    ('Skilled Fake Money Making (Costs: $2133748)', None, 2133748, 'counterfeit2', 'counterfeit', 'upgcheck3', 1.5, 1.5),
    ('Printing Press (Costs: $7777777)', None, 7777777, 'printmoney2', 'printmoney', 'upgcheck2h2', 5.0, 6.0),
    ('Sharemarket Catastrophe (Costs: $12345678)', None, 12345678, 'sharecrash2', 'sharecrash', 'upgcheck4', 1.5, 1.5),
    ('Bank Blueprints (Costs: $91215000)', None, 91215000, 'bankheist2', 'bankheist', 'upgcheck5', 1.5, 1.5)
]

# CLICKS
def collectmoney():
    global game_state, moneytkinter

    game_state.money += game_state.inc

    moneytkinter.set("Balance: $" + format_price(game_state.money))

    next_animation_state()
    game_state.totalclicks += 1


def format_price(price):

    def add_decimal(p, d):
        return '%.3f' % (p / 10 ** d)

    if price < 10 ** 6:
        return '%.3f' % (price)
    elif price < 10 ** 9:
        return add_decimal(price, 6) + 'm'
    elif price < 10 ** 12:
        return add_decimal(price, 9) + 'b'
    elif price < 10 ** 15:
        return add_decimal(price, 12) + 't'
    elif price < 10 ** 18:
        return add_decimal(price, 15) + 'q'
    else:
        return add_decimal(price, 18) + 'Q'


def autopricechoice():
    incbutton1.update('Auto-Clicker (%s)' % format_price(game_state.autoprice), '%.2f $/s, %d owned' % (game_state.autoclick * 221, game_state.autoclick2))

def printpricechoice():
    incbutton2.update('Money Printer (%s)' % format_price(game_state.printprice), '%.2f $/s, %d owned' % (game_state.printmoney * 221, game_state.printmoney2))

def counterpricechoice():
    incbutton3.update('Counterfeit Company (%s)' % format_price(game_state.counterprice), '%.2f $/s, %d owned' % (game_state.counterfeit * 221, game_state.counterfeit2))

def sharepricechoice():
    incbutton4.update('Sharemarket Crash (%s)' % format_price(game_state.shareprice), '%.2f $/s, %d owned' % (game_state.sharecrash * 221, game_state.sharecrash2))

def bankpricechoice():
    incbutton5.update('Bank Heist (%s)' % format_price(game_state.bankprice), '%.2f $/s, %d owned' % (game_state.bankheist * 221, game_state.bankheist2))


def automoney():
    global goldbutton, game_state, totalclicksvar, moneytkinter

    # GOLD UPGRADE
    random1 = randint(1, 3000)
    if random1 == 1 and not game_state.goldcheck:
        goldbutton = Button(master, image=gold, width=70, height=50, text="", command=goldupgrade)
        goldbutton.image = gold
        goldbutton.place(x=int(randint(0, 450)), y=int(randint(0, 200)))
        game_state.goldcheck = True

    # ACHIEVEMENT UPDATES
    totalclicksvar.set("Total clicks: %s" % game_state.totalclicks)

    game_state.timeplay += 1
    timevar.set("Total time: %s" % game_state.timeplay)

    totalspentvar.set("Total money spent: %s" % game_state.get_totalspent())
    moneytkinter.set("Balance: $" + format_price(game_state.money))

    bugfixer()
    game_state.money += game_state.mps / 10.0

    master.after(100, automoney)


# GOLD BUTTON
def goldupgrade():
    global goldbutton

    goldbutton.destroy()
    game_state.goldcheck = False
    if randint(1, 77) == 1:
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


# UPGRADES WINDOW
def showupgrades():
    global game_state, bf, button_names_and_actions, exitupgrades

    upgrades.grid_forget() # destroy()

    bf = frames.ButtonFrame(master, button_names_and_actions, normal_upgrade)
    bf.grid(row=1, column=2, rowspan=8)

    log('hiding upgrade buttons')

    if game_state.clickupgcheck1 != 0:
        bf.hide(button_names_and_actions[0][0])

    if game_state.upgcheck1h1 != 0:
        bf.hide(button_names_and_actions[1][0])

    if game_state.upgcheck2h1 != 0:
        bf.hide(button_names_and_actions[2][0])

    if game_state.clickupgcheck2 != 0:
        bf.hide(button_names_and_actions[3][0])

    if game_state.upgcheck1h2 != 0:
        bf.hide(button_names_and_actions[4][0])

    if game_state.upgcheck3 != 0:
        bf.hide(button_names_and_actions[5][0])

    if game_state.upgcheck2h2 != 0:
        bf.hide(button_names_and_actions[6][0])

    if game_state.upgcheck4 != 0:
        bf.hide(button_names_and_actions[7][0])

    if game_state.upgcheck5 != 0:
        bf.hide(button_names_and_actions[8][0])


    exitupgrades = Button(master, text="Hide Upgrades", command=hideupgrades)
    exitupgrades.grid(row=9, column=2, sticky=E)


def hideupgrades():
    global exitupgrades, game_state, upgrades, bf

    upgrades.grid(row=1, column=2, rowspan=9, sticky=N+E+W+S)
    bf.grid_forget()
    exitupgrades.grid_forget() # destroy()


# ANIMATION
def next_animation_state():
    global game_state

    game_state.animate = (game_state.animate + 1) % 3
    images = [Animation1, Animation2, Animation3]
    animation1 = Label(master, image=images[game_state.animate])
    animation1.place(x=253, y=0)

    clickcolour()


# PSYCHEDELIC COLOURS
def clickcolour():
    global game_state

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet']
    game_state.clickcolourcheck = (game_state.clickcolourcheck + 1) % len(colors)
    clickbutton.configure(bg=colors[game_state.clickcolourcheck])


# MULTIPLIER STUFF
def multiplierchange():
    global multipliercheck

    multiplier_strings = ['x1', 'x10', 'x100']
    multipliercheck = (multipliercheck + 1) % 3
    multiplier.set(multiplier_strings[multipliercheck])
    updatevars()


def updatevars():
    autopricechoice()
    printpricechoice()
    counterpricechoice()
    sharepricechoice()
    bankpricechoice()


def main():
    # BUTTONS, LABELS AND ENTRIES
    global incbutton1, incbutton2, incbutton3, incbutton4, incbutton5, upgrades, clickbutton, \
        moneylabel, lottobutton, status_label, status_var, multipliercheck, multiplier, \
        moneytkinter, mpstkinter, totalclicksvar, timevar, totalspentvar

    background = Label(master, image=img1)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    background.image = img1

    upgrades = Button(master, text="Upgrades", height=12, width=15, command=showupgrades)
    upgrades.grid(row=1, column=2, rowspan=9, sticky=N+E+W+S)

    moneytkinter = StringVar()
    moneytkinter.set("Balance: $" + format_price(game_state.money))

    moneylabel = Label(master, textvariable=moneytkinter)
    moneylabel.grid(row=0, column=0, sticky=W)

    mpstkinter = StringVar()
    mpstkinter.set("MPS: %s" % str(game_state.mps))

    mpslabel = Label(master, textvariable=mpstkinter)
    mpslabel.grid(row=0, column=2, sticky=E)

    multipliercheck = 0
    multiplier = StringVar()
    multiplier.set("x1")

    multiplierbutton = Button(master, textvariable=multiplier, command=multiplierchange)
    multiplierbutton.grid(row=2, column=1)

    inctkinter = StringVar()
    inctkinter.set("+%s money!" % game_state.inc)

    clickbutton = Button(master, textvariable=inctkinter, height=6, width=18, command=collectmoney, bg="red")
    clickbutton.grid(row=3, column=1, rowspan=4)

    incbutton1 = frames.ItemFrame(master, 
        'Auto-Clicker (%s)' % format_price(game_state.autoprice), '%.2f $/s, %d owned' % (game_state.autoclick * 221, game_state.autoclick2), 
        deduction1)
    incbutton1.grid(row=1, column=0) # , sticky=W)

    incbutton2 = frames.ItemFrame(master, 
        'Money Printer (%s)' % format_price(game_state.printprice), '%.2f $/s, %d owned' % (game_state.printmoney * 221, game_state.printmoney2), 
        deduction2)
    incbutton2.grid(row=2, column=0) # , sticky=W)

    incbutton3 = frames.ItemFrame(master, 
        'Counterfeit Company (%s)' % format_price(game_state.counterprice), '%.2f $/s, %d owned' % (game_state.counterfeit * 221, game_state.counterfeit2), 
        deduction3)
    incbutton3.grid(row=3, column=0) # , sticky=W)

    incbutton4 = frames.ItemFrame(master, 
        'Sharemarket Crash (%s)' % format_price(game_state.shareprice), '%.2f $/s, %d owned' % (game_state.sharecrash * 221, game_state.sharecrash2), 
        deduction4)
    incbutton4.grid(row=4, column=0) # , sticky=W)

    incbutton5 = frames.ItemFrame(master, 
        'Bank Heist (%s)' % format_price(game_state.bankprice), '%.2f $/s, %d owned' % (game_state.bankheist * 221, game_state.bankheist2), 
        deduction5)
    incbutton5.grid(row=5, column=0) # , sticky=W)

    lottoprice = StringVar()
    lottoprice.set("Lotto ($%s)" % str(game_state.lottoprice))

    lottobutton = Button(master, textvariable=lottoprice, width=35, command=lotto)
    lottobutton.grid(row=6, column=0, sticky=W)

    # start at row 10 here to leave enough space for expanded upgrade frame

    resetbutton = Button(master, text="Reset Game", width=10, command=resetgame)
    resetbutton.grid(row=10, column=0, sticky=W)

    savebutton = Button(master, text="Save Game", width=10, command=savegame)
    savebutton.grid(row=10, column=2, sticky=E)

    reportbutton = Button(master, text='Report Issue to Github', width=20, command=report)
    reportbutton.grid(row=11, column=1)

    totalclicksvar = StringVar()
    totalclickslabel = Label(master, textvariable=totalclicksvar)
    totalclickslabel.grid(row=12, column=0, sticky=N+E+W+S)

    timevar = StringVar()
    timelabel = Label(master, textvariable=timevar)
    timelabel.grid(row=12, column=1, sticky=N+E+W+S)

    totalspentvar = StringVar()
    totalspentlabel = Label(master, textvariable=totalspentvar)
    totalspentlabel.grid(row=12, column=2, sticky=N+E+W+S)

    status_var = StringVar()
    status_label = Label(master, textvariable=status_var)
    status_label.grid(row=13, column=0, columnspan=4, sticky=W)

    automoney() # start updating counts


def lotto():
    global game_state, lottobutton, cannotafford
    if game_state.money < int(game_state.lottoprice):
        lottobutton.destroy()
        master.bell()
        status_var.set(cannotafford)

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


def initialize_vars():
    args = ['incbutton1', 'incbutton2', 'incbutton3', 'incbutton4', 'incbutton5', 'upgrades', 'clickbutton', \
            'moneylabel', 'lottobutton', 'game_state']
    for i in args:
        globals()[i] = None


initialize_vars()
master.after(10, signin)
master.mainloop()
