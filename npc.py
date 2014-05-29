"""

Author: Yathi

Description:
	The Base NPC class from which both Humans and Critters are derived
	We could have other kinds of NPCs also derived from this base class!

Changelog:
May 27th: Created the file.
"""

class NPC(object):
	"""docstring for NPC"""
	def __init__(self, name):
		super(NPC, self).__init__()
		self.name = name
		self.A = [] #The actions
		self.T = [] #The threatened resources
		self.P = [] #The possessed resources
		self.D = [] #The desired resources. Not sure if we need a seperate desired resources list. 
		self.V = [] #The ordered list of valued resources. 
		self.sayHello()
	#TestMethod
	def sayHello(self):
		print "\n" , self.name, "welcomes you!"
	#Define the important resources
	def defineImportantResource(self, resourceList):
		self.V.append(resourceList)

	#Method to calculate the rank
	def rank(self, resource):
		return len(self.V) - self.V.index(resource)


class human(NPC):
	"""docstring for human"""
	def __init__(self, name):
		super(human, self).__init__(name)