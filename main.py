#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from person import *
#from sheets import getData
#from sheets import writeResults

big_list = []
little_list = []
rank = 3

def main(spreadsheet_id):
	createLists(spreadsheet_id)
	if big_list and little_list:
		pearings()
	else:
		print("Pairings list incomplete")
	#writeResults()

def rankNum():
	return rank

def createLists(spreadsheet_id):
	b_pref, l_pref = acquireData(spreadsheet_id)
	for key in b_pref.keys():
		big = Big(key)
		big_list.append(big)
	for key in l_pref.keys():
		little = Little(key)
		little_list.append(little)

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
	for i in range(rank):
		for little in little_list:
			if (len(little.preferences) > 0) and (not little.matched):
				big = little.preferences[0]
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

def returnPearings():
	f = open("static/results", "w")
	unmatchedLittles = []
	unmatchedBigs = []
	for little in little_list:
		if little.matched:
			f.write(little.name + " with " + little.preferences[0] + "\n")
		else:
			unmatchedLittles.append(str(little.name))
	for big in big_list:
		if not big.matched:
			unmatchedBigs.append(str(big.name))
	f.write("Unmatched littles: " + " ".join(unmatchedLittles) + "\n")
	f.write("Unmatched bigs: " + " ".join(unmatchedBigs) + "\n")
	f.close()

if __name__ == "__main__":
	main(spreadsheet_id)

