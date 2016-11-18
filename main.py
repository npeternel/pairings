#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from sheets import *
from person import *

big_list = []
little_list = []
num_preferences = 3

for key in b_pref.keys():
	big = Big(key)
	big_list.append(big)
	#print('Big ' + big.name + ' added')

for key in l_pref.keys():
	little = Little(key)
	little_list.append(little)
	#print('Little ' + little.name + ' added')

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
			print(little)
			rtn = True
	return rtn


def pearings():
	#while keepGoing():
	for i in range(num_preferences):
		for little in little_list:
			if (len(little.preferences) > 0) and (not little.matched):
				big = getBig(little.preferences[0])
				if big != None:
					big.prospects.append(little)
					big.matched = True
					little.matched = True
					if len(big.prospects) == 2:
						one = big.prospects[0]
						two = big.prospects[1]
						if (one.name not in big.preferences) and (two.name not in big.preferences):
							if one.preferences.index(big.name) > two.preferences.index(big.name):
								big.prospects = [two]
								one.alterPreferences()
							else:
								big.prospects = [one]
								two.alterPreferences()
						elif one.name not in big.preferences:
							big.prospects = [two]
							one.alterPreferences()
						elif two.name not in big.preferences:
							big.prospects = [one]
							two.alterPreferences()
						else:
							if big.preferences.index(one.name) > big.preferences.index(two.name):
								big.prospects = [two]
								one.alterPreferences()
							else:
								big.prospects = [one]
								two.alterPreferences()
	returnPearings()
	return None

def returnPearings():
	unmatchedLittle = []
	unmatchedBig = []
	for little in little_list:
		if little.matched:
			print(little.name + " with " + little.preferences[0])
		else:
			unmatchedLittle.append(str(little.name))
	for big in big_list:
		if not big.matched:
			unmatchedBig.append(str(big.name))
	print("Unmatched littles: ")
	print(unmatchedLittle)
	print("Unmatched bigs: ")
	print(unmatchedBig)

if __name__ == '__main__':
    pearings()

