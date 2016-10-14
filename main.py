#Pairing system based off rankings that implements the Stable Marriage Algorithm
#Authors: Angelina Wang and Nicole Peternel
from quickstart import main

b_pref, l_pref = main(3)

for keys, values in b_pref.items():
	print('%s %s' % (keys, values)) # has a 'u' which is weird but stack overflow says it's unicode and it's all chill

