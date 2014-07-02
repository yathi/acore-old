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
from random import random, randint

counter = 0
line = []
stateOfNPCCounter = 0
nameList = ["Smith", "Johnson", "William", "Mary", "David", "Jennifer", "Chris", "Lisa", "Edward", "Laura", "Sergio", "Sarah", "Emilie", "Matthew", "Kevin", "Liam",
"Ahmed", "Merriam"]

# meera = human('Meera')

# print calculateThreat(meera)	#We have to add the resources to the treatened resource and give it a ranking for it to calculate the threat


def makeNPC():
	global counter
	name = nameList[randint(0, (len(nameList))-1)]
	npc = human(name)
	npc.resourceVector[2] += counter*0.3
	counter += 1
	return npc

def displayLine():
	for girl in line:
		print "\nName: " , girl.name
		print "Emotion: " , girl.emotion
		print "Desired Action: " , girl.bestAction()
		print "Protest Cost: " , girl.protestCost()
		print "Wait Cost: " , girl.waitCost()
		print "Pass Cost: " , girl.passCost()
		#print "Resources: " , girl.resourceVector

def intervalCounter():
	print "Testing"
	time.sleep(3)

def stepCounter():
	global stateOfNPCCounter
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
			print "Desired Action: " , girl.bestAction()
			print "Protest Cost: " , girl.protestCost()
			print "Wait Cost: " , girl.waitCost()
			print "Pass Cost: " , girl.passCost()
			#print "Resources: " , girl.resourceVector
	elif response == 3:
		stateOfNPCCounter += 1
		#print "\n\nThe counter is :", str(stateOfNPCCounter%3) , "And the counter is " , str(stateOfNPCCounter) ,  "\n"
		if (stateOfNPCCounter%3)!=0:
			for indx, girl in enumerate(line):
				print "\nName: " , girl.name, " " , str(indx)
				print "Emotion: " , girl.returnEmotion()
				print "Desired Action: " , girl.bestAction()
				print "Protest Cost: " , girl.protestCost()
				print "Wait Cost: " , girl.waitCost()
				print "Pass Cost: " , girl.passCost()
				print "Resources: " , girl.resourceVector
				if girl.bestAction() == "Pass":
					line[indx-1].beingPassed = True
				if girl.bestAction() == "Protest":
					print "\nIndex is ", str(indx), "And the len is : ", str(len(line)), "\n"
					if indx < len(line):
						line[indx+1].beingProtested == True
		elif (stateOfNPCCounter%3)==0:
			for girl in line:
				girl.finalAction()
			displayLine()
				
while True:
	# intervalCounter()
	stepCounter()

