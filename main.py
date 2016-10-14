#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from quickstart import main
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
		if little.getName == name:
			return little
	return NULL

def getBig(name):
	for big in big_list:
		if big.getName == name:
			return big
	return NULL


def pearings():
	for big in big_list:
		if (len(big.getPreferences()) > 0):
			big.getPreferences()[0]
	return 0

