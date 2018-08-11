'''
Class defining the object, which generates the 3d-maze
'''

from pyramid_object import PyramidObject
import random

class MazeGenerator(object):
	
	def generate_maze(self, size_x = 64, size_y = 48, height = 3):
		'''
		The function generates a new pyramid with parameter properties and returns it.
		
		Weaknesses: invalid size parameters for the pyramid
		
		Suggestion to correct this: throw an exception error, which the main loop or appropriate
		submethoc has to sort out.
		'''
		new_pyramid = PyramidObject(size_x, size_y, height)
		
		# We need random numbers here
		randoms = random.Random()
		#randoms2 = random.Random()
		
		'''
		Here comes the magic in a form of Sidewinder maze carving algorithm, in 3d
		'''
		
		for z in range(height):
			for y in range(size_y):
				new_pyramid.set_passage(0, y, z) #Just to set the empty areas at the beginning
				
			for x in range(1, size_x, 2):
				run_start = 1
				while run_start < size_y:
					run_end = randoms.randint(run_start, size_y - 1)
					for y in range(run_start, run_end):
						if (run_start <= y < run_end):
							new_pyramid.set_passage(x, y, z)
							
					# Dig out a passage to random direction (east, up, down, when possible)
					
					if (run_end - 1 - run_start) > 0:
						# passage = randoms.randint(run_start, run_end - 1)
						# which_way = randoms.randint(1, 10)
						
						success = False
						while not success:
							passage = randoms.randint(run_start, run_end - 1)
							which_way = randoms.randint(1, 10)
							
							if (z < height - 1) and (which_way % 2) == 0:
								success = new_pyramid.set_ascent(x, passage, z)
							elif x == 1:
								success = new_pyramid.set_passage(x - 1, passage, z)
							else:
								success = new_pyramid.set_passage_pro(x - 1, passage, z)
							
							if not success and x == 1:
								success = True
				
					run_start = run_end + 1			
				
				
		return new_pyramid
		
