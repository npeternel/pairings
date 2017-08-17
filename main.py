#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from person import *
#from sheets import getData
#from sheets import writeResults

a_list = []
b_list = []
rank = 3

def main(spreadsheet_id):
	createLists(spreadsheet_id)
	if a_list and b_list:
		pearings()
	else:
		print("Pairings list incomplete")
	#writeResults()

def rankNum():
	return rank

def createLists(spreadsheet_id):
	a_pref, b_pref = acquireData(spreadsheet_id)
	for key in a_pref.keys():
		a = ItemA(key)
		a_list.append(a)
	for key in b_pref.keys():
		b = ItemB(key)
		b_list.append(b)

def getItemA(name):
	for a in a_list:
		if a.name == name:
			return a
	return None

def getItemB(name):
	for b in b_list:
		if b.name == name:
			return b
	return None

def keepGoing():
	rtn = False
	for a in a_list:
		if not a.matched and len(a.preferences) > 0:
			print(a)
			rtn = True
	return rtn


def pearings():
	for i in range(rank):
		for a in a_list:
			if (len(a.preferences) > 0) and (not a.matched):
				#b = a.preferences[0]
				b = getItemB(a.preferences[0])
				if b != None:
					b.prospects.append(a)
					b.matched = True
					a.matched = True
					if len(b.prospects) == 2:
						one = b.prospects[0]
						two = b.prospects[1]
						if (one.name not in b.preferences) and (two.name not in b.preferences):
							if one.preferences.index(b.name) > two.preferences.index(b.name):
								b.prospects = [two]
								one.alterPreferences()
							else:
								b.prospects = [one]
								two.alterPreferences()
						elif one.name not in b.preferences:
							b.prospects = [two]
							one.alterPreferences()
						elif two.name not in b.preferences:
							b.prospects = [one]
							two.alterPreferences()
						else:
							if b.preferences.index(one.name) > b.preferences.index(two.name):
								b.prospects = [two]
								one.alterPreferences()
							else:
								b.prospects = [one]
								two.alterPreferences()
	returnPearings()

def returnPearings():
	f = open("static/results", "w")
	unmatchedAs = []
	unmatchedBs = []
	for a in a_list:
		if a.matched:
			f.write(a.name + " with " + a.preferences[0] + "\n")
		else:
			unmatchedAs.append(str(a.name))
	for b in b_list:
		if not b.matched:
			unmatchedBs.append(str(b.name))
	f.write("Unmatched As: " + " ".join(unmatchedAs) + "\n")
	f.write("Unmatched Bs: " + " ".join(unmatchedBs) + "\n")
	f.close()

if __name__ == "__main__":
	main(spreadsheet_id)

