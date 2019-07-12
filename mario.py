''' Mario Class Definition '''
from person import *
import os


class Mario(Person):
	def __init__(self, length, width, person_type):
		Person.__init__(self,length,width,person_type)
		self.matrix = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]


	def move(self, ch, board_object):
		''' Function to read the character input and move the mario'''

		# call move up function
		if ch == 'w' or ch == 'W':
			self.moveUp(board_object)

		# call move down function
		elif ch == 's' or ch == 'S':
			self.moveDown(board_object)

		# call move left function
		elif ch == 'a' or ch == 'A':
			self.moveLeft(board_object)

		# call move right function
		elif ch == 'd' or ch == 'D':
			self.moveRight(board_object)
			