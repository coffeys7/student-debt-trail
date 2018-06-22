class Information():
	grades = 4.0
	mental_health = 100
	health = 100
	moneys = 5,000

	def __init__(self, name):
        self.name = name

	def downGrade(decrement) :
		grades = 4.0 - decrement
		#calculate actual GPA and stuff here

	def downHealth(decrement_h,decrement_mh) :
		health = health - decrement_h

	def downCash(decrement) :
		moneys = moneys - decrement

class Loan():
    def __init__(self, principal, i_rate):
        self.principal = principal
        self.i_rate = i_rate
        self.year = 0
        self.payments = 0.0

    def set_year(self, year):
        self.year = year

    def advance_year(self):
        self.year += 1

    def total(self):
        return self.principal + self.interest() - self.payments

    def interest(self):
        return self.principal * (self.i_rate * self.year)

    def make_payment(self, payment_amt):
        self.payments += payment_amt

# simple class wrapper for array of string selection options
class Options():
    def __init__(self, options, prompt='Select an option:'):
        self.options = options
        self.prompt = prompt

    def print(self):
        for i in range(len(self.options)):
            print('[' + str(i+1) + ']: ' + str(self.options[i]))

    def select(self):
        self.print()
        index = input(self.prompt + ' ')
        return self.options[int(index) - 1]
