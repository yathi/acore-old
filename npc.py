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
		return self.emotion

	def passCost(self):
		return ((1-self.resourceVector[0])*self.resourceWeights[0] + 
			(0.5 - self.resourceVector[1])*self.resourceWeights[1] + 
			(0.3)*self.resourceWeights[2])

	def waitCost(self):
		if self.beingPassed:
			return 0.3*self.resourceWeights[2]
		else:
			return 0

	def bestAction(self):
		if self.passCost() > self.waitCost():
			self.nextAction = "Pass"


class human(NPC):
	"""docstring for human"""
	def __init__(self, name):
		super(human, self).__init__(name)