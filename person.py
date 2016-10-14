from sheets import main

b_pref, l_pref = main(3)

class Person(object):

	def __init__(self, name):
		self.name = name
		self.matched = False

	def __str__(self):

		return "name: " + self.name + ", matched: " + str(self.matched) + ", medium: " + self.medium

	def getMatched(self):
		return self.matched

	def getPreferences(self):
		return self.preferences

	def getName(self):
		return self.name

	def alterPreferencces(self):
		self.preferences = self.preferences[1:]

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

