class MoneyFmt:
    def __init__(self, money):
        self.money = money

    def update(self, new_money):
        self.money = new_money

    def __repr__(self):
        return str(self.money)

    def __str__(self):
        return '${:,.2f}'.format(self.money)


cash = MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
print(repr(cash))