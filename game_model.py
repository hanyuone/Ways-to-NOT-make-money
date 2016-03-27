import math


class GameState:
    def __init__(self, data=None):
        self.data = [] if data is None else data

        self.check = 0
        self.upgbuttoncheck = False
        self.goldcheck = False
        self.statscheck = False

        self.animate = 0
        self.clickcolourcheck = 1

        self.upgcheck1h1 = int(self.data[11])
        self.upgcheck1h2 = int(self.data[13])
        self.upgcheck2h1 = int(self.data[15])
        self.upgcheck2h2 = int(self.data[17])
        self.upgcheck3 = int(self.data[19])
        self.upgcheck4 = int(self.data[21])
        self.upgcheck5 = int(self.data[23])
        self.clickupgcheck1 = int(self.data[25])
        self.clickupgcheck2 = int(self.data[27])

        self.timeplay = int(self.data[41])
        self.totalclicks = int(self.data[43])

        self.money = float(self.data[29])

        self.autoclick2 = int(self.data[1])
        self.autoclick = self.autoclick2 * 18 * self.upgcheck1h2 + self.autoclick2 * 2 * self.upgcheck1h1 + \
                         self.autoclick2
        self.autoprice = int(20 * math.pow(1.15, self.autoclick2))

        self.printmoney2 = int(self.data[3])
        self.printmoney = self.printmoney2* 18 * self.upgcheck2h2 + self.printmoney2 * 2 * self.upgcheck2h1 + \
                          self.printmoney2
        self.printprice = int(375 * math.pow(1.25, self.printmoney2))

        self.counterfeit2 = int(self.data[5])
        self.counterfeit = self.counterfeit2 * 2 * self.upgcheck3 + self.counterfeit2
        self.counterfeitprice = int(9001 * math.pow(1.3, self.counterfeit2))

        self.sharecrash2 = int(self.data[7])
        self.sharecrash = self.sharecrash2 * 2 * self.upgcheck4 + self.sharecrash2
        self.shareprice = int(42000 * math.pow(1.4, self.sharecrash2))

        self.bankheist2 = int(self.data[7])
        self.bankheist = self.bankheist2 * 2 * self.upgcheck4 + self.bankheist2
        self.bankprice = int(175000 * math.pow(1.1, self.bankheist2))

        self.lottoprice = int(self.data[45])

        self.mps = self.autoclick2 + 15 * self.printmoney2 + 321 * self.counterfeit2 + 969 * self.sharecrash2
        self.inc = 1 + self.clickupgcheck1 * 2 + self.clickupgcheck2 * self.mps / 10

        self.multiplier = 1

    def multiplierset(self, n):
        if n == "1":
            self.autoprice = int(20 * math.pow(1.15, self.autoclick2))
            self.printprice = int(375 * math.pow(1.25, self.printmoney2))
            self.counterfeitprice = int(9001 * math.pow(1.3, self.counterfeit2))
            self.shareprice = int(42000 * math.pow(1.4, self.sharecrash2))
            self.bankprice = int(175000 * math.pow(1.1, self.bankheist2))
            self.multiplier = 1
        elif n == "10":
            for a in range(1, 10):
                self.autoprice += int(20 * math.pow(1.15, (self.autoclick2 + a)))
                self.printprice += int(375 * math.pow(1.25, (self.printmoney2 + a)))
                self.counterfeitprice += int(9001 * math.pow(1.3, (self.counterfeit2 + a)))
                self.shareprice += int(42000 * math.pow(1.4, (self.sharecrash2 + a)))
                self.bankprice += int(175000 * math.pow(1.1, (self.bankheist2 + a)))
                self.multiplier = 10
        elif n == "100":
            for a in range(1, 100):
                self.autoprice += int(20 * math.pow(1.15, (self.autoclick2 + a)))
                self.printprice += int(375 * math.pow(1.25, (self.printmoney2 + a)))
                self.counterfeitprice += int(9001 * math.pow(1.3, (self.counterfeit2 + a)))
                self.shareprice += int(42000 * math.pow(1.4, (self.sharecrash2 + a)))
                self.bankprice += int(175000 * math.pow(1.1, (self.bankheist2 + a)))
                self.multiplier = 10

    def set(self, name, value):
        i = self.data.index(name)
        self.data[i + 1] = value

    def get_autoclick(self):
        return self.autoclick

    def set_autoclick(self, amount):
        self.autoclick = amount

    def inc_autoclick(self, amount):
        self.autoclick += amount

    def get_autoclick2(self):
        return self.autoclick2

    def inc_autoclick2(self, amount=1):
        self.autoclick2 += amount

    def get_autoprice(self):
        return self.autoprice

    def set_autoprice(self, amount):
        self.autoprice = amount

    def get_printmoney(self):
        return self.printmoney

    def set_printmoney(self, amount):
        self.printmoney = amount

    def inc_printmoney(self, amount):
        self.printmoney += amount

    def get_printmoney2(self):
        return self.printmoney2

    def set_printmoney2(self, amount):
        self.printmoney2 = amount

    def inc_printmoney2(self, amount=1):
        self.printmoney2 += amount

    def get_printprice(self):
        return self.printprice

    def set_printprice(self, amount):
        self.printprice = amount

    def get_counterfeit(self):
        return self.counterfeit

    def set_counterfeit(self, amount):
        self.counterfeit = amount

    def inc_counterfeit(self, amount):
        self.counterfeit += amount

    def get_counterfeit2(self):
        return self.counterfeit2

    def set_counterfeit2(self, amount):
        self.counterfeit2 = amount

    def inc_counterfeit2(self, amount=1):
        self.counterfeit2 += amount

    def get_counterfeitprice(self):
        return self.counterfeitprice

    def set_counterfeitprice(self, amount):
        self.counterfeitprice = amount

    def get_sharecrash(self):
        return self.sharecrash

    def set_sharecrash(self, amount):
        self.sharecrash = amount

    def inc_sharecrash(self, amount):
        self.sharecrash += amount

    def get_sharecrash2(self):
        return self.sharecrash2

    def set_sharecrash2(self, amount):
        self.sharecrash2 = amount

    def inc_sharecrash2(self, amount=1):
        self.sharecrash2 += amount

    def get_shareprice(self):
        return self.shareprice

    def set_shareprice(self, amount):
        self.shareprice = amount
        
    def get_bankheist(self):
        return self.bankheist

    def set_bankheist(self, amount):
        self.bankheist = amount

    def inc_bankheist(self, amount):
        self.bankheist += amount

    def get_bankheist2(self):
        return self.bankheist2

    def set_bankheist2(self, amount):
        self.bankheist2 = amount

    def inc_bankheist2(self, amount=1):
        self.bankheist2 += amount

    def get_bankprice(self):
        return self.bankprice

    def set_bankprice(self, amount):
        self.bankprice = amount

    def get_mps(self):
        return self.mps

    def set_mps(self, amount):
        self.mps = amount

    def inc_mps(self, amount=1):
        self.mps += amount

    def scale_mps(self, amount):
        self.mps = int(self.mps * amount)

    def get_inc(self):
        return self.inc

    def set_inc(self, amount):
        self.inc = amount

    def get_multiplier(self):
        return self.multiplier

    def get_total_clicks(self):
        return self.totalclicks

    def inc_total_clicks(self):
        self.totalclicks += 1

    def get_timeplay(self):
        return self.timeplay

    def inc_timeplay(self):
        self.timeplay += 1

    def get_totalspent(self):
        x = 0
        for a in range(0, self.get_autoclick2()):
            x += int(20 * math.pow(1.15, self.autoclick2))
        for b in range(0, self.get_printmoney2()):
            x += int(375 * math.pow(1.25, self.printmoney2))
        for c in range(0, self.get_counterfeit2()):
            x += int(9001 * math.pow(1.3, self.counterfeit2))
        for d in range(0, self.get_sharecrash2()):
            x += int(42000 * math.pow(1.4, self.sharecrash2))
        for e in range(0, self.get_bankheist2()):
            x += int(175000 * math.pow(1.1, self.bankheist2))
        x += self.get_total_clicks()
        return x

    def get_money(self):
        return self.money

    def set_money(self, amount):
        self.money = amount

    def inc_money(self, amount=1):
        self.money += amount

    def get_animate(self):
        return self.animate

    def inc_animate(self):
        self.animate = (self.animate + 1) % 3

    def inc_clickcolourcheck(self):
        c = self.clickcolourcheck
        self.clickcolourcheck = (self.clickcolourcheck + 1) % 7
        return c

    def get_upgcheck1h1(self):
        return self.upgcheck1h1

    def inc_upgcheck1h1(self, amount=1):
        self.upgcheck1h1 += amount

    def get_upgcheck1h2(self):
        return self.upgcheck1h2

    def inc_upgcheck1h2(self, amount=1):
        self.upgcheck1h2 += amount

    def get_upgcheck2h1(self):
        return self.upgcheck2h1

    def inc_upgcheck2h1(self, amount=1):
        self.upgcheck2h1 += amount

    def get_upgcheck2h2(self):
        return self.upgcheck2h2

    def inc_upgcheck2h2(self, amount=1):
        self.upgcheck2h2 += amount

    def get_upgcheck3(self):
        return self.upgcheck3

    def inc_upgcheck3(self, amount=1):
        self.upgcheck3 += amount

    def get_upgcheck4(self):
        return self.upgcheck4

    def inc_upgcheck4(self, amount=1):
        self.upgcheck4 += amount

    def get_upgcheck5(self):
        return self.upgcheck5

    def inc_upgcheck5(self, amount=1):
        self.upgcheck5 += amount

    def get_clickupgcheck1(self):
        return self.clickupgcheck1

    def inc_clickupgcheck1(self, amount=1):
        self.clickupgcheck1 += amount

    def get_clickupgcheck2(self):
        return self.clickupgcheck2

    def inc_clickupgcheck2(self, amount=1):
        self.clickupgcheck2 += amount

    def get_upgbuttoncheck(self):
        return self.upgbuttoncheck

    def set_upgbuttoncheck(self, u):
        self.upgbuttoncheck = u

    def get_lotto(self):
        return self.lottoprice

    def set_lotto(self, amount):
        self.lottoprice = amount
