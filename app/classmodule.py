import random

class Information():
    total_loans = []
    schools_list = [("Albion",27000), ("Andrews",17160), ("Kettering", 19385), ("Rochester", 10320)]
    
    def add_loan(self, in_loan):
        total_loans.append(in_loan)
        return;

    def __init__(self, name):
        self.name = name
        self.school = random.choice(self.schools_list)
        self.grades = 4.0
        self.mental_health = 100
        self.health = 100 
        self.money = 5,000
		
	    
    def downGrade(self,amount) :
        self.grades += amount
        #FIXME: calculate actual GPA and stuff here
	
    def downHealth(self,amount_h,amount_mh) :
        self.health += amount_h
        self.mental_health += amount_mh
    
    def changeCash(self,amount) :
        self.money += amount

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


