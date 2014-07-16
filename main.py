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
nameList = ["Smith", "Johnson", "William", "Mary", "David",
"Jennifer", "Chris", "Lisa", "Edward", "Laura", "Sergio", "Sarah", "Emilie", "Matthew", "Kevin", "Liam",
"Ahmed", "Merriam"]

# meera = human('Meera')

# print calculateThreat(meera)	#We have to add the resources to the treatened resource and give it a ranking for it to calculate the threat
initialized = False
gameStatus = 'initial'

def makeNPC():
    global counter
    name = nameList.pop(randint(0, (len(nameList))-1))
    npc = human(name)
    npc.resourceVector[2] += counter*0.3
    counter += 1
    return npc

def initialize(numInLine):
    global line
    count = 0
    for count in range(numInLine):
        line.append(makeNPC())
        count += 1

def displayLine():
	for person in line:
		print "\nName: " , person.name
		print "Emotion: " , person.getEmotion()
		print "Desired Action: " , person.nextAction
		#print "Protest Cost: " , round(person.protestCost(), 2)
		#print "Wait Cost: " , round(person.waitCost(), 2)
		#print "Pass Cost: " , round(person.passCost(), 2)
		#print "Resources: " , person.resourceVector
		#print "Weight Vector" , [round(Weight, 2) for Weight in person.resourceWeights]
		#print "New Resources: " , person.newResourceVector

def stepCounter():
	global stateOfNPCCounter, gameStatus, initialized
	raw_input("\nNext Step?\n:")


	if initialized:
		if len(line) == 0:
			gameStatus = 'Over'
			print '\n ----------Game Over!------------ \n'
	else:
		initialize(numInLine = 6)  #The parameter tells the number of elements
		initialized = True

	if gameStatus == 'initial':
		print 'The game status is ' , gameStatus
		for indx, person in enumerate(line):
			person.decidePass(indx)

		for indx, person in enumerate(line):
			if person.nextAction == 'Pass':
				person.newResourceVector = [1, 0.5, person.resourceVector[2]+0.3]
				person.computeEmotion(0.95)

		displayLine()
		gameStatus = 'protest?'

	elif gameStatus == 'protest?':
		print 'The game status is ' , gameStatus
		for indx, person in enumerate(line):
			if indx < (len(line)-1):
				person.decideProtest(beingPassed = (line[indx+1].nextAction == "Pass"))

		for indx, person in enumerate(line):
			if indx < (len(line)-1):
				person.sanityCheck(indx, notbeingPassed = (line[indx+1].nextAction != 'Pass'))

		for indx, person in enumerate(line):
			if person.nextAction == 'Protest':
				person.newResourceVector = [1, 0.85, person.resourceVector[2]]
				person.resourceVector[2] =- 0.3
				person.computeEmotion(0.95)


		displayLine()
		gameStatus = 'penultimate'

	elif gameStatus == 'penultimate':
		print 'The game status is ' , gameStatus
		for indx, person in enumerate(line):
			if indx != 0:
				if person.nextAction == 'Pass' and line[indx-1].nextAction == 'Protest':
					if random() < 0.50:
						print 'Being protested'
						person.nextAction = 'Pass_Success'
						person.computeEmotion(1)
						line[indx-1].nextAction = 'Wait'
						line[indx-1].newResourceVector = [line[indx-1].resourceVector[0], line[indx-1].resourceVector[1], line[indx-1].resourceVector[2]-0.3]
						line[indx-1].computeEmotion(1)
						line[indx-1].resourceVector = line[indx-1].newResourceVector
						line[indx], line[indx-1] = line[indx-1], line[indx] #Code to swap the 2 positions
					else:
						person.nextAction = 'Pass_Fail'
						person.newResourceVector = [1, 0.5, person.resourceVector[2]]
						person.computeEmotion(1)
				elif person.nextAction == 'Pass' and line[indx-1].nextAction == 'Wait':
					if random() < 0.95:
						print 'Not being protested'
						person.nextAction = 'Pass_Success'
						person.computeEmotion(1)
						line[indx-1].newResourceVector = [line[indx-1].resourceVector[0], line[indx-1].resourceVector[1], line[indx-1].resourceVector[2]-0.3]
						line[indx-1].computeEmotion(1)
						line[indx-1].resourceVector = line[indx-1].newResourceVector
						line[indx], line[indx-1] = line[indx-1], line[indx] #Code to swap the 2 positions
					else:
						person.nextAction = 'Pass_Fail'
						person.newResourceVector = [1, 0.5, person.resourceVector[2]]
						person.computeEmotion(1)

		displayLine()
		gameStatus = 'final'

	elif gameStatus == 'final':
		print '\nThe game status is ' , gameStatus
		print str(line[0].name) , 'gets the Occulus Rift'
		line.pop(0)
		for person in line:
			person.nextAction = 'Wait'

		displayLine()
		gameStatus = 'initial'

while gameStatus != 'Over':
	stepCounter()

