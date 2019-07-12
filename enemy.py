''' Enemy Class Definition'''

from controllers import *
import random
from person import *

class Enemy(Person):

	def __init__(self, length, width, person_type):
		
		Person.__init__(self, length, width, person_type)
		self.matrix = [['[','E', 'E',']'], [' ','E', 'E',' ']]
		self.destroyed = 'False'
		self.direction = random.randint(0,1)
		self.cnt=0

		# Movement function of enemies
	def move(self, board_object):

		if self.destroyed =='False':
			if self.cnt < 10:
				if self.direction == 0:
					self.moveLeft(board_object)
					self.cnt += 1
				elif self.direction == 1:
					self.moveRight(board_object)
					self.cnt += 1
			if self.cnt == 10:
				if self.direction == 0:
					self.direction = 1
					self.cnt = 1
					self.moveRight(board_object)
				elif self.direction == 1:
					self.direction = 0
					self.cnt = 1
					self.moveLeft(board_object)
		elif self.destroyed=='True1':
			self.matrix = [[' ',' ',' ',' '],[' ',' ',' ',' ']]
			overlayMatrix(board_object,self,self.x,self.y)

