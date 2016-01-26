import math

class GameState:

    def __init__(self, data=None):
        self.data = [] if data is None else data

        self.check = False
        self.upgbuttoncheck = False
        self.goldcheck = False
        self.statscheck = False

        self.animate = 0
        self.click = 0
        self.clickcolourcheck = 1

        self.upgcheck1h1 = int(self.data[9])
        self.upgcheck1h2 = int(self.data[11])
        self.upgcheck2h1 = int(self.data[13])
        self.upgcheck2h2 = int(self.data[15])
        self.upgcheck3 = int(self.data[17])
        self.upgcheck4 = int(self.data[19])
        self.clickupgcheck1 = int(self.data[21])
        self.clickupgcheck2 = int(self.data[23])

        self.timeplay = int(self.data[37])
        self.totalclicks = int(self.data[39])

        self.money = float(self.data[25] + self.data[27] + self.data[29] + self.data[31] + self.data[33] + self.data[35])
        if len(str(self.money)) < 8:
            self.moneycheck = "0"
        else:
            self.moneycheck = str(self.money)[:1]

        self.moneymillion = round(float(str(self.data[25] + self.data[27] + self.data[29] + self.data[31] + self.data[33]) + "." + self.moneycheck), 1)
        if len(str(self.moneymillion)) < 5:
            self.moneymillioncheck = "0"
        else:
            self.moneymillioncheck = str(self.moneymillion)[:1]

        self.moneybillion = round(float(str(self.data[25] + self.data[27] + self.data[29] + self.data[31]) + "." + self.moneymillioncheck), 1)
        if len(str(self.moneybillion)) < 5:
            self.moneybillioncheck = "0"
        else:
            self.moneybillioncheck = str(self.moneybillion)[:1]

        self.moneytrillion = round(float(self.data[25] + self.data[27] + self.data[29] + "." + self.moneybillioncheck), 1)
        if len(str(self.moneytrillion)) < 5:
            self.moneytrillioncheck = "0"
        else:
            self.moneytrillioncheck = str(self.moneytrillion)[:1]

        self.moneyquadrillion = round(float(self.data[25] + self.data[27] + "." + self.moneytrillioncheck), 1)
        if len(str(self.moneyquadrillion)) < 5:
            self.moneyquadrillioncheck = "0"
        else:
            self.moneyquadrillioncheck = str(self.moneyquadrillion)[:1]

        self.moneyquintillion = round(float(self.data[25] + "." + self.moneyquadrillioncheck), 1)

        self.autoclick2 = int(self.data[1])
        self.autoclick = self.autoclick2 * 18 * self.upgcheck1h2 + self.autoclick2 * 2 * self.upgcheck1h1 + self.autoclick2
        self.autoprice = int(20 * math.pow(1.2, self.autoclick2))

        self.printmoney2 = int(self.data[3])
        self.printmoney = self.printmoney2 * 2 * self.upgcheck2h1 + self.printmoney2
        self.printprice = int(375 * (math.pow(1.2, self.printmoney2)))

        self.counterfeit2 = int(self.data[5])
        self.counterfeit = self.counterfeit2 * 2 * self.upgcheck3 + self.counterfeit2
        self.counterfeitprice = int(9001 * math.pow(1.2, self.counterfeit2))

        self.sharecrash2 = int(self.data[7])
        self.sharecrash = self.sharecrash2 * 2 * self.upgcheck4 + self.sharecrash2
        self.shareprice = int(42000 * math.pow(1.2, self.sharecrash2))

        self.mps = self.autoclick2 + 15 * self.printmoney2 + 321 * self.counterfeit2 + 969 * self.sharecrash2
        self.inc = 1 + self.clickupgcheck1 * 2 + self.clickupgcheck2 * self.mps / 10
        self.templist1 = [self.moneymillion] * 2
        self.templist2 = [self.moneybillion] * 2
        self.templist3 = [self.moneytrillion] * 2
        self.templist4 = [self.moneyquadrillion] * 2
        self.templist5 = [self.moneyquintillion] * 2

    def set(self, name, value):
        i = self.data.index(name)
        self.data[i+1] = value

    def get_balance(self):
        if self.moneymillion == 0:
            money_string = str(self.money)
        elif self.moneybillion == 0:
            money_string = str(self.moneymillion) + "m"
        elif self.moneytrillion == 0:
            money_string = str(self.moneybillion) + "b"
        elif self.moneyquadrillion == 0:
            money_string = str(self.moneytrillion) + "t"
        elif self.moneyquintillion == 0:
            money_string = str(self.moneyquadrillion) + "q"
        else:
            money_string = str(self.moneyquintillion) + "Q"

        return "Balance: $" + money_string

    def get_autoclick(self):
        return self.autoclick

    def set_autoclick(self, amount):
        self.autoclick = amount

    def inc_autoclick(self, amount=1):
        self.autoclick += amount

    def get_autoclick2(self):
        return self.autoclick2

    def inc_autoclick2(self, amount=1):
        self.autoclick2 += amount

    def get_autoprice(self):
        return self.autoprice

    def set_autoprice(self, amount):
        self.autoprice += amount

    def get_printmoney(self):
        return self.printmoney

    def set_printmoney(self, amount):
        self.printmoney = amount

    def inc_printmoney(self, amount=1):
        self.printmoney += amount

    def get_printmoney2(self):
        return self.printmoney2

    def set_printmoney2(self, amount):
        self.printmoney2 = amount

    def inc_printmoney2(self, amount=1):
        self.printmoney2 += amount

    def get_money_printer_price(self):
        return self.printprice

    def get_counterfeit(self):
        return self.counterfeit

    def set_counterfeit(self, amount):
        self.counterfeit = amount

    def inc_counterfeit(self, amount=1):
        self.counterfeit += amount

    def get_counterfeit2(self):
        return self.counterfeit2

    def set_counterfeit2(self, amount):
        self.counterfeit2 = amount

    def inc_counterfeit2(self, amount=1):
        self.counterfeit2 += amount

    def get_counterfeit_price(self):
        return self.counterfeitprice

    def set_counterfeit_price(self, amount):
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

    def get_total_clicks(self):
        return self.totalclicks

    def inc_total_clicks(self):
        self.totalclicks += 1

    def get_timeplay(self):
        return self.timeplay

    def inc_timeplay(self):
        self.timeplay += 1

    def get_money(self):
        return self.money

    def set_money(self, amount):
        self.money = amount

    def inc_money(self, amount=1):
        self.money += amount

