'''
Pyramid Object
'''

class PyramidObject(object):

	def __init__(self, size_x = 64, size_y = 48, height = 3, array = None):
		self.height = height
		self.size_x = size_x
		self.size_y = size_y
		
		if array == None:
			self.array = [None] * height
			for h in range(height):
				self.array[h] = [None] * self.size_y
				for y in range(self.size_y):
					self.array[h][y] = [None] * self.size_x
					for x in range(self.size_x):
						self.array[h][y][x] = '#'	# # is the character for a wall in my maze
		else:
			self.array = array
	
	def get_size_x(self):
		return self.size_x
		
	def get_size_y(self):
		return self.size_y
	
	def get_height(self):
		return self.height
		
	def get_array(self):
		return self.array
	
	def is_wall(self, x_pos, y_pos, z_pos):
		if ( 0 <= x_pos < self.size_x ) and ( 0 <= y_pos < self.size_y ) and ( 0 <= z_pos < self.height ):
			if self.array[z_pos][y_pos][x_pos] in [' ', 'A', 'D']:
				return False
		
		return True
	
	def is_ascent(self, x_pos, y_pos, z_pos):
		if ( 0 <= x_pos < self.size_x ) and ( 0 <= y_pos < self.size_y ) and ( 0 <= z_pos < self.height ) and self.array[z_pos][y_pos][x_pos] == 'A':
			return True
		else:
			return False
	
	def is_descent(self, x_pos, y_pos, z_pos):
		if ( 0 <= x_pos < self.size_x ) and ( 0 <= y_pos < self.size_y ) and ( 0 <= z_pos < self.height ) and self.array[z_pos][y_pos][x_pos] == 'D':
			return True
		else:
			return False
	
	def set_passage(self, x_pos, y_pos, z_pos):
		if ( 0 <= x_pos < self.size_x ) and ( 0 <= y_pos < self.size_y ) and ( 0 <= z_pos < self.height ) and self.is_wall(x_pos, y_pos, z_pos):
			self.array[z_pos][y_pos][x_pos] = ' '
			return True
		else:
			return False
	
	def set_passage_pro(self, x_pos, y_pos, z_pos):
		if ( 1 <= x_pos < self.size_x ) and ( 0 <= y_pos < self.size_y ) and ( 0 <= z_pos < self.height) and not self.is_wall(x_pos - 1, y_pos, z_pos):
			self.array[z_pos][y_pos][x_pos] = ' '
			return True
		else:
			return False
	
	def set_ascent(self, x_pos, y_pos, z_pos):
		if ( 0 <= x_pos < self.size_x ) and ( 0 <= y_pos < self.size_y ) and ( 0 <= (z_pos + 1) < self.height ):
			self.array[z_pos][y_pos][x_pos] = 'A'
			self.array[z_pos + 1][y_pos][x_pos] = 'D'
			return True
		else:
			return False
		
	def set_descent(self, x_pos, y_pos, z_pos):
		if ( 0 <= x_pos < self.size_x ) and ( 0 <= y_pos < self.size_y ) and ( 0 <= (z_pos - 1) < self.height ):
			self.array[z_pos][y_pos][x_pos] = 'D'
			self.array[z_pos - 1][y_pos][x_pos] = 'A'
			return True
		else:
			return False
		
	#def copy(self):
		
