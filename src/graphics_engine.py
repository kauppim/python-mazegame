import pygame
import os
from pyramid_object import PyramidObject
from player_object import PlayerObject

'''
Define some colors
'''

BLACK	= (	  0,	0,    0)
WHITE	= (	255,  255,	255)
GREEN	= (	  0,  255,	  0)
RED		= (	255,	0,	  0)
BLUE	= (   0,    0,  255)
BROWN	= ( 150,   75,	  0)
SANDY	= ( 244,  164,   96)

class GraphicsEngine(object):
	
	def __init__(self, x_res = 640, y_res = 480, refresh_rate = 20):
		self.size = [x_res, y_res]
		self.refresh_rate = refresh_rate
		
		self.background = None
		self.bg_rect = None
		
		self.font = pygame.font.Font(None, 20)
		
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Muumio")
		
	def set_background(self, path):
		self.background = pygame.image.load(path)
		self.bg_rect = self.background.get_rect()
	
	def draw_grid(self, player):
		
		pyramid = player.get_pyramid()
		position = player.get_position()
		level = position[2]
		
		y_point = 0
		for y in range(pyramid.get_size_y()):
			x_point = 0
			for x in range(pyramid.get_size_x()):
				if position == (x, y, level): # Draw the player
					pygame.draw.rect(self.screen, RED, [x_point, y_point, 10, 10])
				elif pyramid.is_wall(x, y, level):
					pygame.draw.rect(self.screen, BROWN, [x_point, y_point, 10, 10])
				elif pyramid.is_ascent(x, y, level):
					pygame.draw.rect(self.screen, GREEN, [x_point, y_point, 10, 10])
				elif pyramid.is_descent(x, y, level):
					pygame.draw.rect(self.screen, BLUE, [x_point, y_point, 10, 10])
				x_point = x_point + 10
			
			y_point = y_point + 10	
		
	def draw_everything(self, player):
		self.screen.fill(SANDY)
		#self.screen.blit(self.background, self.bg_rect)
		
		self.draw_grid(player)
		
		# Update the step count to the screen
		text = self.font.render("Steps: "+str(player.get_steps()), True, BLACK)
		text_rect = text.get_rect()
		
		self.screen.blit(text, [500,0])
		
		# Update screen
		pygame.display.flip()
		
	def draw_solution(self, array, show_which_level):
		self.screen.fill(SANDY)
		#self.screen.blit(self.background, self.bg_rect)
		
		y_point = 0
		for y in range( len( array[show_which_level] ) ):
			x_point = 0
			for x in range( len( array[show_which_level][y] ) ):
				if array[show_which_level][y][x] == '#':
					pygame.draw.rect(self.screen, BROWN, [x_point, y_point, 10, 10])
				elif array[show_which_level][y][x] == 'A':
					pygame.draw.rect(self.screen, GREEN, [x_point, y_point, 10, 10])
				elif array[show_which_level][y][x] == 'D':
					pygame.draw.rect(self.screen, BLUE, [x_point, y_point, 10, 10])
				x_point = x_point + 10
			
			y_point = y_point + 10
		
		# Update screen
		pygame.display.flip()				
