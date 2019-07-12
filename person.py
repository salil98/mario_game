from controllers import *

class Person(object):
	''' Definition For Person '''

	def __init__(self, length, width, person_type):

		''' Initializing Person '''
		self.length = length
		self.width = width
		self.person_type = person_type
		self.x = None
		self.y = None
		self.matrix = []

	def setNewPosition(self,board_object, x, y):
		''' Set position of person for the first time '''
		if check4clash(board_object, self, x, y,1) == 0:
			overlayMatrix(board_object, self, x, y)
			self.setPosition(x, y)
	

	def setPosition(self,x,y):
		# set position of person once it is established
		self.x = x
		self.y = y
	

	def returnMatrix(self):
		''' return matrix of object'''
		return self.matrix



	def moveLeft(self,board_object):
		# make person move left.
		if check4clash(board_object, self, self.x, self.y-1,1) == 0:	
			overlayMatrix(board_object,self,self.x, self.y-1)
			self.setPosition(self.x, self.y-1)


	def moveRight(self,board_object):
		# make person move right.
		if check4clash(board_object, self, self.x, self.y+1,1) == 0:
			overlayMatrix(board_object,self,self.x, self.y+1)
			self.setPosition(self.x, self.y+1)



	def moveUp(self,board_object):
		# make person move up.
		if check4clash(board_object, self, self.x-1, self.y,1) == 0:
			overlayMatrix(board_object,self,self.x-1,self.y)
			self.setPosition(self.x-1, self.y)
	


	def moveDown(self,board_object):
		# make person move down.
		if check4clash(board_object, self, self.x+1, self.y,1) == 0:
			overlayMatrix(board_object,self,self.x+1, self.y)
			self.setPosition(self.x+1, self.y)

		
