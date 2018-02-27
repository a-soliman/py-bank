
class Account:
	def __init__( self, name, balance, min_balance ):
		self.name = name
		self.balance = balance
		self.min_balance = min_balance

	def deposite( self, amount ):
		self.balance += amount

	def withdraw( self, amount):
		if self.balance - amount >= min_balance:
			self.balance -= amount
		else:
			print('Not enough money in your account.')

		return
	def statment( self ):
		print('Account Statment {}.'.format(self.balance)) 
