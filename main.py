#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from quickstart import main

b_pref, l_pref = main(3)

for keys, values in b_pref.items():
	print('%s %s' % (keys, values)) # has a 'u' which is weird but stack overflow says it's unicode and it's all chill


class Person(object):

	def __init__(self, name):
		self.name = name
		self.matched = False

	def __str__(self):

		return "name: " + self.name + ", matched: " + str(self.matched) + ", medium: " + self.medium

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

A = Big('A')
print(A)
print(A.preferences)