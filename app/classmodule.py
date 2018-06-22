class Stats():  
	def __init__(self, name):
        self.name = name
        self.grades = 4.0
        self.mental_health = 100
        self.health = 100 
        self.money = 5,000
		
	def downGrade(amount,self) :
		self.grades += amount
		#calculate actual GPA and stuff here
	
	def downHealth(amount_h,amount_mh,self) :
		self.health += amount_h
        self.mental_health += amount_mh
	
	def downCash(amount,self) :
		self.money  += amount 


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
    def __init__(self, options):
        self.options = options

    def print(self):
        for i in range(len(self.options)):
            print('[' + str(i+1) + ']: ' + self.options[i])

    def select(self, index):
        return self.options[index + 1]
