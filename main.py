#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from person import *

big_list = []
little_list = []

A = Big('A')
print(A)
print(A.preferences)

for key in b_pref.keys():
	big = Big(key)
	big_list.append(big)
	print('Big ' + big.name + ' added')

for key in l_pref.keys():
	little = Little(key)
	little_list.append(little)
	print('Little ' + little.name + ' added')


