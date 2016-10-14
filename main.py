#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from sheets import main
from person import *

big_list = []
little_list = []

for key in b_pref.keys():
	big = Big(key)
	big_list.append(big)
	print('Big ' + big.name + ' added')

for key in l_pref.keys():
	little = Little(key)
	little_list.append(little)
	print('Little ' + little.name + ' added')

def getLittle(name):
	for little in little_list:
		if little.name == name:
			return little
	return None

def getBig(name):
	for big in big_list:
		if big.name == name:
			return big
	return None

def keepGoing():
	rtn = False
	for little in little_list:
		if not little.matched and len(little.preferences) > 0:
			rtn = True
	return rtn


def pearings():
	while keepGoing():
		for little in little_list:
			if (len(little.preferences) > 0):
				big = getBig(little.preferences[0])
				if big != None and not big.matched:
					big.prospects += little
					big.matched = True
					little.matched = True
					if big.prospects == 2:
						one = big.prospects[0]
						two = big.prospects[1]
						if one not in big.preferences and two not in big.preferences:
							if one.preferences.getIndex(big) > two.preferences.getIndex(big):
								big.prospects = [two]
								one.alterPreferences()
							else:
								big.prospects = [one]
								two.alterPreferences()
						elif one not in big.preferences:
							big.prospects = [two]
							one.alterPreferences()
						elif two not in big.preferences:
							big.prospects = [one]
							two.alterPreferences()
						else:
							if big.preferences.getIndex(one) > big.preferences.getIndex(two):
								big.prospects = [two]
								one.alterPreferences()
							else:
								big.prospects = [one]
								two.alterPreferences()
	return None

def returnPearings():
	for little in little_list:
		if little.matched:
			print(little.name + " with " + little.preferences[0])

