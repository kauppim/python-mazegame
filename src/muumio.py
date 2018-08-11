'''
Muumio - a 3d maze game

author:	Mikael Kauppinen
email:	mikael.kauppinen@iki.fi

Version information:
V0.6.1alpha
2018-08-11
'''

import pygame
import os
import signal
from pyramid_object import PyramidObject
from player_object import PlayerObject
from maze_generator import MazeGenerator
from maze_solver import MazeSolver
from command_engine import CommandEngine
from graphics_engine import GraphicsEngine
from maze_io import MazeIO

def handler(signum, frame):
	print 'Couldn\'t create a maze in 5 seconds! Retry...'
	raise NameError('NoSuccess')
	


def main():
		
	'''
	Load mazes.
	'''
	
	pyramid = None
	
	input_output = MazeIO()
	load_maze = str(raw_input("Do you want to load an existing maze? (Y/N) "))
	
	if load_maze.lower() == "y":
		file_name = str(raw_input("Enter file name: "))
		pyramid = input_output.load_maze(file_name)
	
	else:
		generator = MazeGenerator()
		print "MazeGen initialized..."
		
		'''
		I'm not sure if this works as it's supposed to work.
		
		The purpose of this is to break the execution of the generate_maze,
		when too much time has passed, and no maze will evidently be produced.
		'''
		
		maze_done = False
		while not maze_done:
			#signal.signal(signal.SIGALRM, handler)
			
			#signal.alarm(5)
			
			try:
				pyramid = generator.generate_maze()
				if pyramid:
					maze_done = True
			except NameError:
				maze_done = False
			#signal.alarm(0)
	
	if pyramid != None:
	
		print "Pyramid initialized..."
			
		name = str(raw_input("Give player's name: "))
		
		if len(name) > 0:
			player = PlayerObject(name, pyramid)
		else:
			player = PlayerObject("Mikael", pyramid)
		
		pygame.init()
	
		graffat = GraphicsEngine()
		print "Graphics initialized..."
		
		'''
		Background was downloaded from
		http://pixabay.com/en/pyramids-egypt-sandstorm-103304/
		© 2013 Pixabay - Free Images
		'''
		
		#graffat.set_background(os.path.join('img', 'pyramids-103304_640.jpg'))
		#print "Background loaded..."
		
		interfeissi = CommandEngine()
		
		if_done = False
		clock = pygame.time.Clock()
		
		while if_done == False:
			
			if_done = interfeissi.handle_events(player)		
			
			#update graphics here
			
			graffat.draw_everything(player)
			
			# Limit to 20 frames per second
			clock.tick(20)
			if player.is_at_goal():
				print "Goal reached! Hurrah!"
				if_done = True
		
		print player, 'used', player.get_steps(), 'steps for solving this labyrinth.'
		
		show_solution = str(raw_input("Do you want to see the computer's solution? (Y/N) "))
		
		if show_solution.lower() == 'y':
			solver = MazeSolver()
			solution = solver.solve_maze(pyramid)
			height = len(solution)
			
			show_which_level = 0
			while show_which_level >= 0:
				#update graphics here
				
				graffat.draw_solution(solution, show_which_level)
				
				show_which_level = interfeissi.solution_mode(show_which_level, height)
				
				# Limit to 20 frames per second
				clock.tick(20)
		
		pygame.quit()
		
		'''
		Save mazes.
		'''
		
		save_yn = str(raw_input("Do you want to save this maze? (Y/N) "))
		
		if save_yn.lower() == "y":
			file_name = str(raw_input("Enter file name: "))
			input_output.save_maze(player.get_pyramid(), file_name)
	
	
if __name__ == '__main__':
    main()
