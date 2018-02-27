
class Account:
	def __init__( self, name, balance, min_balance ):
		self.name = name
		self.balance = balance
		self.min_balance = min_balance

	def deposite( self, amount ):
		self.balance += amount

	def withdraw( self, amount):
		if self.balance - amount >= self.min_balance:
			self.balance -= amount
		else:
			print('Not enough money in your account.')

		return
	def statment( self ):
		print('Account Statment ${}.'.format(self.balance)) 

class Checking(Account):
	def __init__( self, name, balance ):
		super().__init__(name, balance, min_balance = -1000)

x = Checking('Ahmed', 500)
x.deposite(400)
x.statment()

x.withdraw(400)
x.statment()

x.withdraw(800)
x.statment()

x.withdraw(701)
x.statment()