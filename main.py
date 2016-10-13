#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from quickstart import main

b_pref, l_pref = main()

for keys, values in b_pref.items():
	print(keys, values) # has a 'u' which is weird but stack overflow says it's unicode and it's all chill