"""

Author: Yathi

Description:
	The main file to run ACORE. The code runs only in python2x for now because pygraphviz is not supported in python 3
	Keep running emote and cope till resource in not threatened. 


Changelog:
May 27th: Created the file fresh seperate from Mirage. ACORE is going to be my research project and Mirage will be my main project. 

"""

from emotion import *
from npc import human
import time

meera = human('Meera')

print calculateThreat(meera)	#We have to add the resources to the treatened resource and give it a ranking for it to calculate the threat

def intervalCounter():
	print "Testing"
	time.sleep(3)

while True:
	intervalCounter()