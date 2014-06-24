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
from random import random

counter = 0
line = []

# meera = human('Meera')

# print calculateThreat(meera)	#We have to add the resources to the treatened resource and give it a ranking for it to calculate the threat


def makeNPC():
	global counter
	name = "Girl" + str(counter)
	npc = human(name)
	if random() > 0.5:
		npc.defineImpResource("rank")
		npc.defineImpResource("reputation")
	else:
		npc.defineImpResource("reputation")
		npc.defineImpResource("rank")
	counter += 1
	return npc

def intervalCounter():
	print "Testing"
	time.sleep(3)

def stepCounter():
	print "\n1. Add a new girl in the line"
	print "2. See line"
	print "3. Next Step"
	response = int(raw_input("What would you like to do?"))


	if response == 1:
		line.append(makeNPC())
	elif response == 2:
		print "\n"
		for girl in line:
			print girl.name
			girl.showImpResource()
	elif response == 3:
		for girl in line:
			print "\nName: " , girl.name
			print "Emotion: " , girl.returnEmotion()
			print "Desired Action: " , girl.returnAction()
			

while True:
	# intervalCounter()
	stepCounter()