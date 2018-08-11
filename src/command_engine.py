from player_object import PlayerObject
import pygame

WAITING_TIME = 0
NORTH	= ( 0, -1,  0)
EAST	= ( 1,  0,  0)
SOUTH	= ( 0,  1,  0)
WEST	= (-1,  0,  0)
UP		= ( 0,  0,  1)
DOWN	= ( 0,  0, -1)

class CommandEngine(object):

	def handle_events(self, player):
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				return True
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					player.move_player_undo(EAST)
				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					player.move_player_undo(WEST)
				elif event.key == pygame.K_UP or event.key == pygame.K_w:
					player.move_player_undo(NORTH)
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					player.move_player_undo(SOUTH)
				elif event.key == pygame.K_q:
					player.move_player_undo(UP)
				elif event.key == pygame.K_e:
					player.move_player_undo(DOWN)
				elif event.key == pygame.K_x:
					return True
				elif event.key == pygame.K_u:
					player.undo_move()
				elif event.key == pygame.K_i:
					player.redo_move()
				
				pygame.time.set_timer(pygame.KEYDOWN, WAITING_TIME)
				
				
		return False
	
	def solution_mode(self, show_which_level, height):
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				return -1
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					if show_which_level + 1 < height:
						return show_which_level + 1
				elif event.key == pygame.K_e:
					if show_which_level - 1 >= 0:
						return show_which_level - 1
				elif event.key == pygame.K_x:
					return -1
				
				pygame.time.set_timer(pygame.KEYDOWN, WAITING_TIME)
				
				
		return show_which_level
