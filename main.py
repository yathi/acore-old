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
		#print "Emotion: " , [round(emo,2) for emo in person.emotion]
		print "Desired Action: " , person.nextAction
		#print "Protest Cost: " , round(person.protestCost(), 2)
		#print "Wait Cost: " , round(person.waitCost(), 2)
		#print "Pass Cost: " , round(person.passCost(), 2)
		#print "Resources: " , person.resourceVector
		#print "Weight Vector" , [round(Weight, 2) for Weight in person.resourceWeights]
		#print "New Resources: " , person.newResourceVector

def stepCounter():
	global stateOfNPCCounter
	print "\n1. Initialize"
	print "2. See line"
	print "3. Next Step"
	response = int(raw_input("What would you like to do?"))


	if response == 1:
		initialize(numInLine = 6)  #The parameter tells the number of elements
	elif response == 2:
		for indx, person in enumerate(line):
			print "\nName: " , person.name, " " , str(indx)
			print "Emotion: " , person.returnEmotion()
			print "Desired Action: " , person.nextAction
			print "Protest Cost: " , person.protestCost()
			print "Wait Cost: " , person.waitCost()
			print "Pass Cost: " , person.passCost()
			#print "Resources: " , person.resourceVector
	elif response == 3:
		if gameStatus == 'initial':
			for indx, person in enumerate(line):
				print "\nName: " , person.name
				#print "Emotion: " , [round(emo,2) for emo in person.emotion]
				print "Desired Action: " , person.decidePass(indx)
				#print "Protest Cost: " , round(person.protestCost(), 2)
				#print "Wait Cost: " , round(person.waitCost(), 2)
				#print "Pass Cost: " , round(person.passCost(), 2)
				#print "Resources: " , person.resourceVector
				#print "Weight Vector" , [round(Weight, 2) for Weight in person.resourceWeights]
				#print "New Resources: " , person.newResourceVector
				gameStatus = 'protest?'
		elif gameStatus == 'protest?':
			for indx, person in enumerate(line):
				person.decideProtest(beingPassed = (line[indx+1].nextAction == "Pass"))


		elif (stateOfNPCCounter%3)==0:
			for person in line:
			 person.finalAction()
			displayLine()

while True:
	# intervalCounter()
	stepCounter()

