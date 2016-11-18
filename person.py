from sheets import main

b_pref, l_pref = main(3)

class Person(object):

	def __init__(self, name):
		self.name = name
		self.matched = False

	def __str__(self):

		return "name: " + self.name + ", matched: " + str(self.matched) + ", medium: " + self.medium

	def alterPreferences(self):
		self.preferences = self.preferences[1:]
		self.matched = False

class Big(Person):

	def __init__(self, name):
		super(Big, self).__init__(name)
		self.preferences = b_pref[self.name]
		'''self.prefs = []
		for pref in self.preferences:
			self.prefs.append(getBig(pref))'''
		self.medium = 'big'
		self.prospects = []

class Little(Person):

	def __init__(self, name):
		super(Little, self).__init__(name)
		self.preferences = l_pref[self.name]
		self.medium = 'little'

