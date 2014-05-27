"""

Author: Yathi

Description:
	The main file to run ACORE. The code runs only in python2x for now because pygraphviz is not supported in python 3
	Keep running emote and cope till resource in not threatened. 


Changelog:
May 27th: Created the file fresh seperate from Mirage. ACORE is going to be my research project and Mirage will be my main project. 

"""

class npc(object):
	"""docstring for npc"""
	def __init__(self, name):
		super(npc, self).__init__()
		self.name = name
		self.A = [] #The actions
		self.T = [] #The threatened resources
		self.P = [] #The possessed resources
		self.D = [] #The desired resources
		self.V = [] #The ordered list of valued resources. 
		self.sayHello()
	#TestMethod
	def sayHello(self):
		print "\n" , self.name, "welcomes you!"

class human(npc):
	"""docstring for human"""
	def __init__(self, name):
		super(human, self).__init__(name)		

