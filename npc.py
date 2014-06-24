"""

Author: Yathi

Description:
	The Base NPC class from which both Humans and Critters are derived
	We could have other kinds of NPCs also derived from this base class!

Changelog:
May 27th: Created the file.
"""

from random import random


class NPC(object):
	"""docstring for NPC"""
	def __init__(self, name):
		super(NPC, self).__init__()
		self.name = name
		self.A = [] #The actions
		self.resourceName = ["Health", "Reputation", "Proximity"]
		self.resourceVector = [1, 1, 1]
		self.resourceWeights = [random(), random(), random()]
		self.emotion = "Neutral"
		self.desAction = "Wait"
		self.sayHello()
	#TestMethod
	def sayHello(self):
		print "\n" , self.name, "welcomes you!"

	def returnEmotion(self):
		return self.emotion

	def returnAction(self):
		return self.desAction


class human(NPC):
	"""docstring for human"""
	def __init__(self, name):
		super(human, self).__init__(name)