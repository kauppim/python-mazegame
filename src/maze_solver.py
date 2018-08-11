'''
Class defining the object, which solves the 3d-maze
'''

from pyramid_object import PyramidObject
import copy

class MazeSolver(object):
	
	'''
	Gets the next wall from the copied array.
	
	WARNING. pos-parameters can be almost whatever, and there's not necessarily any safeguards against
	indexing error. Please consider rewriting this or adding some safeguards.
	'''
	def get_next_wall(self, array, pos_z, pos_x, pos_y):
		for y in range( pos_y - 1, -1, -1 ):
			if array[pos_z][y][pos_x] == '#':
				return y
		return -1
	
	'''
	Tries to solve the maze with dead end filler algorithm.
	'''
	def solve_maze(self, pyramid):
		if pyramid != None and pyramid.get_array() != None:
			
			# Don't know how stylish this is to get a deep copy of my array, but...
			array = copy.deepcopy( pyramid.get_array() )
			
			height = pyramid.get_height()
			size_y = pyramid.get_size_y()
			size_x = pyramid.get_size_x()
			
			for z in range( height ):
				
				'''
				Well, the for-loop for the x coordinate requires a bit of explanation.
				It turned out to be like this because of some structural choices earlier in this project:
				- 
				
				We'll iterate until the 3-element in x-direction (not 0-element), because the 0th column
				is always supposed to be empty tiles, totally giving access to 1st column.
				'''
				for x in range( size_x - 3, 1, -2 ):
					run_start = size_y
					
					while run_start >= 0:
						run_end = self.get_next_wall(array, z, x, run_start)
						
						if (run_start - run_end) > 1:
							passages = 0
							
							for y in range(run_start - 1, run_end, -1):
								if array[z][y][x] in ['A', 'D']:
									passages += 1
							
							for y in range(run_start - 1, run_end, -1):
								if array[z][y][x + 1] == ' ':
									passages += 1
							
							if passages == 0:
								for y in range(run_start - 1, run_end, -1):
									array[z][y][x] = '#'
							
						run_start = run_end
			
			return array			
			
		return None
