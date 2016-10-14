#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from quickstart import main

b_pref, l_pref = main(3)

big_list = []
little_list = []



class Person(object):

	def __init__(self, name):
		self.name = name
		self.matched = False

	def isMatched(self):
		return self.matched

class Big(Person):

	def __init__(self, name):
		super(Big, self).__init__(name)
		self.preferences = b_pref[self.name]
		self.medium = 'big'


class Little(Person):

	def __init__(self, name):
		super(Little, self).__init__(name)
		self.preferences = l_pref[self.name]
		self.medium = 'little'

for key in b_pref.keys():
	big = Big(key)
	big_list.append(big)
	print('Big ' + big.name + ' added')

for key in l_pref.keys():
	little = Little(key)
	little_list.append(little)
	print('Little ' + little.name + ' added')

