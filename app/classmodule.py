class Loan():
    def __init__(self, principal, i_rate):
        self.principal = principal
        self.i_rate = i_rate
        self.year = 0
        self.payments = 0.0

    def set_year(year):
        self.year = year

    def advance_year():
        self.year += 1

    def total():
        return self.principal + self.interest() - self.payments

    def interest():
        return self.principal * (1 + (self.i_rate * self.year))

    def make_payment(payment_amt):
        self.payments += payment_amt
