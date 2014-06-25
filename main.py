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
	npc.resourceVector[2] += counter*0.3
	counter += 1
	return npc

def intervalCounter():
	print "Testing"
	time.sleep(3)

def stepCounter():
	stateOfNPCCounter = 0
	print "\n1. Add a new girl in the line"
	print "2. See line"
	print "3. Next Step"
	response = int(raw_input("What would you like to do?"))


	if response == 1:
		line.append(makeNPC())
	elif response == 2:
		for indx, girl in enumerate(line):
			print "\nName: " , girl.name, " " , str(indx)
			print "Emotion: " , girl.returnEmotion()
			print "Desired Action: " , girl.nextAction
			print "Resources: " , girl.resourceVector
	elif response == 3:
		stateOfNPCCounter += 1
		if (stateOfNPCCounter%4)==1:
			for girl in line:
				girl.bestAction()

			

while True:
	# intervalCounter()
	stepCounter()