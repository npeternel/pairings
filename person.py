from sheets import *

a_pref = {}
b_pref = {}

def acquireData(spreadsheet_id):
	global a_pref
	global b_pref
	a_pref, b_pref = getData(spreadsheet_id)
	return (a_pref, b_pref)

class Person(object):

	def __init__(self, name):
		self.name = name
		self.matched = False

	def __str__(self):

		return "name: " + self.name + ", matched: " + str(self.matched) + ", medium: " + self.medium

	def alterPreferences(self):
		self.preferences = self.preferences[1:]
		self.matched = False

class ItemA(Person):

	def __init__(self, name):
		super(ItemA, self).__init__(name)
		self.preferences = a_pref[self.name]
		'''self.prefs = []
		for pref in self.preferences:
			self.prefs.append(getBig(pref))'''
		self.medium = 'A'
		#self.prospects = []

class ItemB(Person):

	def __init__(self, name):
		super(ItemB, self).__init__(name)
		self.preferences = b_pref[self.name]
		self.medium = 'B'
		self.prospects = []

