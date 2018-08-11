'''
Player Object
'''
from pyramid_object import PyramidObject
'''
Let's define some directions
'''
NORTH	= (  0, -1,  0)
SOUTH	= (  0,  1,  0)
EAST	= (  1,  0,  0)
WEST	= ( -1,  0,  0)
UP		= (  0,  0,  1)
DOWN	= (  0,  0, -1)

class PlayerObject(object):
	def __init__(self, name = "Seppo", pyramid = "None"):
		self.name = name
		self.pyramid = pyramid
		
		self.pos_x = 0
		self.pos_y = 0
		self.pos_z = 0
		
		self.undo_stack = []
		self.redo_stack = []
		
	def set_pyramid(self, pyramid):
		self.pyramid = pyramid
	
	def set_position(self, xpos, ypos, zpos):
		self.pos_x = xpos
		self.pos_y = ypos
		self.pos_z = zpos
	
	def get_position(self):
		return self.pos_x, self.pos_y, self.pos_z
	
	def get_directions(self):
		return [NORTH, SOUTH, EAST, WEST, UP, DOWN]
		
	def get_opposite_direction(self, direction):
		directions = self.get_directions()
		pos = directions.index(direction)
		
		if (pos % 2 == 0):
			return directions[pos+1]
		else:
			return directions[pos-1]
	
	def get_pyramid(self):
		return self.pyramid
		
	def get_steps(self):
		return len(self.undo_stack)
		
	def is_at_goal(self):
		if self.pos_x == (self.pyramid.get_size_x() - 1):
			return True
		
		return False
	
	'''
	Undo/Redo
	'''
	def undo_move(self):
		if len(self.undo_stack) > 0:
			action = self.undo_stack.pop()
			action = self.get_opposite_direction(action)
			self.move_player(action)
			self.redo_stack.append(action)
		
	
	def redo_move(self):
		if len(self.redo_stack) > 0:
			action = self.redo_stack.pop()
			action = self.get_opposite_direction(action)
			self.move_player(action)
			self.undo_stack.append(action)
	
	
	'''
	PlayerObject handles the moving of the player.
	Parameters:
	direction: which way player wants to move
	
	Returns:
	True, if succesful
	False, if no success
	'''
	def move_player(self, direction):
		new_x = self.pos_x + direction[0]
		new_y = self.pos_y + direction[1]
		new_z = self.pos_z + direction[2]
		
		if direction == UP and self.pyramid.is_ascent(self.pos_x, self.pos_y, self.pos_z):
			self.set_position(new_x, new_y, new_z)
			return True
		elif direction == DOWN and self.pyramid.is_descent(self.pos_x, self.pos_y, self.pos_z):
			self.set_position(new_x, new_y, new_z)
			return True
		elif direction not in [UP, DOWN] and not self.pyramid.is_wall(new_x, new_y, new_z):
			self.set_position(new_x, new_y, new_z)
			return True
		else:
			return False
	
	def move_player_undo(self, direction):
		if self.move_player(direction):
			self.undo_stack.append(direction)
			self.redo_stack = []
	
	def __str__(self):
		return self.name
