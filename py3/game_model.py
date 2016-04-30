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

        self.timeplay = int(self.data[31])
        self.totalclicks = int(self.data[33])

        self.money = float(self.data[29])

        self.autoclick2 = int(self.data[1])
        self.autoclick = self.autoclick2 * 18 * self.upgcheck1h2 + self.autoclick2 * 2 * self.upgcheck1h1 + \
                         self.autoclick2
        self.autoprice = int(20 * math.pow(1.15, self.autoclick2))

        self.printmoney2 = int(self.data[3])
        self.printmoney = self.printmoney2 * 18 * self.upgcheck2h2 + self.printmoney2 * 2 * self.upgcheck2h1 + \
                          self.printmoney2
        self.printprice = int(375 * math.pow(1.25, self.printmoney2))

        self.counterfeit2 = int(self.data[5])
        self.counterfeit = self.counterfeit2 * 2 * self.upgcheck3 + self.counterfeit2
        self.counterprice = int(9001 * math.pow(1.3, self.counterfeit2))

        self.sharecrash2 = int(self.data[7])
        self.sharecrash = self.sharecrash2 * 2 * self.upgcheck4 + self.sharecrash2
        self.shareprice = int(42000 * math.pow(1.4, self.sharecrash2))

        self.bankheist2 = int(self.data[7])
        self.bankheist = self.bankheist2 * 2 * self.upgcheck4 + self.bankheist2
        self.bankprice = int(175000 * math.pow(1.1, self.bankheist2))

        if len(self.data) > 35:
            self.lottoprice = int(self.data[35])
        else:
            self.lottoprice = 0

        self.mps = self.autoclick2 + 15 * self.printmoney2 + 321 * self.counterfeit2 + 969 * self.sharecrash2
        self.inc = 1 + self.clickupgcheck1 * 2 + self.clickupgcheck2 * self.mps / 10

        self.multiplier = 1

    def __str__(self):
        return str(self.__dict__)

    def multiplierset(self, n):
        if n == "1":
            self.autoprice = int(20 * math.pow(1.15, self.autoclick2))
            self.printprice = int(375 * math.pow(1.25, self.printmoney2))
            self.counterprice = int(9001 * math.pow(1.3, self.counterfeit2))
            self.shareprice = int(42000 * math.pow(1.4, self.sharecrash2))
            self.bankprice = int(175000 * math.pow(1.1, self.bankheist2))
            self.multiplier = 1
        elif n == "10":
            for a in range(1, 10):
                self.autoprice += int(20 * math.pow(1.15, (self.autoclick2 + a)))
                self.printprice += int(375 * math.pow(1.25, (self.printmoney2 + a)))
                self.counterprice += int(9001 * math.pow(1.3, (self.counterfeit2 + a)))
                self.shareprice += int(42000 * math.pow(1.4, (self.sharecrash2 + a)))
                self.bankprice += int(175000 * math.pow(1.1, (self.bankheist2 + a)))
                self.multiplier = 10
        elif n == "100":
            for a in range(1, 100):
                self.autoprice += int(20 * math.pow(1.15, (self.autoclick2 + a)))
                self.printprice += int(375 * math.pow(1.25, (self.printmoney2 + a)))
                self.counterprice += int(9001 * math.pow(1.3, (self.counterfeit2 + a)))
                self.shareprice += int(42000 * math.pow(1.4, (self.sharecrash2 + a)))
                self.bankprice += int(175000 * math.pow(1.1, (self.bankheist2 + a)))
                self.multiplier = 10

    def get_totalspent(self):
        x = 0
        for a in range(0, self.autoclick2):
            x += int(20 * math.pow(1.15, self.autoclick2))
        for b in range(0, self.printmoney2):
            x += int(375 * math.pow(1.25, self.printmoney2))
        for c in range(0, self.counterfeit2):
            x += int(9001 * math.pow(1.3, self.counterfeit2))
        for d in range(0, self.sharecrash2):
            x += int(42000 * math.pow(1.4, self.sharecrash2))
        for e in range(0, self.bankheist2):
            x += int(175000 * math.pow(1.1, self.bankheist2))
        x += self.totalclicks
        return x
