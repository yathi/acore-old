"""

Author: Yathi

Description:
	The Base NPC class from which both Humans and Critters are derived
	We could have other kinds of NPCs also derived from this base class!

Changelog:
May 27th: Created the file.
June 23rd: Changed the resource sturcture to the vector model.
"""

from random import random


class NPC(object):
	"""docstring for NPC"""
	def __init__(self, name):
		super(NPC, self).__init__()
		self.name = name
		self.A = [] #The actions
		self.resourceName = ["Health", "Reputation", "Proximity"]
		self.resourceVector = [1, 1, 0.3]
		self.resourceWeights = [random(), random(), random()]
		self.beingPassed = False
		self.emotion = "Neutral"
		self.nextAction = "Wait"
		self.sayHello()
	#TestMethod
	def sayHello(self):
		print "\n" , self.name, "welcomes you!"

	def returnEmotion(self):
		if self.nextAction == "Pass":
			#For Reputation
			Joy = 0
			Hope = 0
			Fear = 0
			Sorrow = 0
			expectation_repu = 0.95
			expectation_proxi = 0.95
			desire_repu = (0.5 - self.resourceVector[1])*self.resourceWeights[1]
			desire_proxi = (0.3)*self.resourceWeights[2]

			if (desire_repu > 0) and (expectation_repu == 1):   #These for loops have to be rewritten properly to make them resource independent
				Joy += desire_repu								#For that reed to define a proper nextResource vector for each action and state
			elif (desire_repu > 0) and (expectation_repu < 1):
				Hope += desire_repu * expectation_repu
			elif (desire_repu < 0) and (expectation_repu == 1):
				Fear += desire_repu
			elif (desire_repu < 0) and (expectation_repu < 1):
				Sorrow += desire_repu * expectation_repu

			if (desire_proxi > 0) and (expectation_repu == 1):
				Joy += desire_proxi
			elif (desire_proxi > 0) and (expectation_repu < 1):
				Hope += desire_proxi * expectation_repu
			elif (desire_proxi < 0) and (expectation_repu == 1):
				Fear += desire_proxi
			elif (desire_proxi < 0) and (expectation_repu < 1):
				Sorrow += desire_proxi * expectation_repu

			Emotion_P = "Joy: " , Joy, " Hope: " , Hope, " Fear: " , Fear , " Sorrow: " , Sorrow

			self.emotion = Emotion_P

		elif self.nextAction == "Wait" and self.beingPassed:
			Joy = 0
			Hope = 0
			Fear = 0
			Sorrow = 0
			expectation_repu = 0.95
			expectation_proxi = 0.95
			desire_proxi = (-0.3)*self.resourceWeights[2]

			if (desire_proxi > 0) and (expectation_repu == 1):
				Joy += desire_proxi
			elif (desire_proxi > 0) and (expectation_repu < 1):
				Hope += desire_proxi * expectation_repu
			elif (desire_proxi < 0) and (expectation_repu == 1):
				Fear += desire_proxi
			elif (desire_proxi < 0) and (expectation_repu < 1):
				Sorrow += desire_proxi * expectation_repu

			Emotion_P = "Joy: " , Joy, " Hope: " , Hope, " Fear: " , Fear , " Sorrow: " , Sorrow

			self.emotion = Emotion_P


		return self.emotion

	def passCost(self):
		return ((1-self.resourceVector[0])*self.resourceWeights[0] + 
			(0.5 - self.resourceVector[1])*self.resourceWeights[1] + 
			(0.3)*self.resourceWeights[2])

	def waitCost(self):
		if self.beingPassed:
			return (-0.3)*self.resourceWeights[2]
		else:
			return 0

	def protestCost(self):
		return ((1-self.resourceVector[0])*self.resourceWeights[0] + 
			(0.85 - self.resourceVector[1])*self.resourceWeights[1])

	def bestAction(self):
		if self.beingPassed:
			if self.protestCost() > self.waitCost():
				self.nextAction = "Protest"
		else:
			if self.passCost() > self.waitCost():
				self.nextAction = "Pass"
		return self.nextAction


class human(NPC):
	"""docstring for human"""
	def __init__(self, name):
		super(human, self).__init__(name)