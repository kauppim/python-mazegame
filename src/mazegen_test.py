from maze_generator import MazeGenerator
from pyramid_object import PyramidObject
from player_object import PlayerObject

def main():
	
	pelaaja = PlayerObject("Seppo")
	generator = MazeGenerator()
	pyramidi = generator.generate_maze(pelaaja)
	
	labyrintti = pyramidi.get_array()
	
	for level in range(3):
		for row in range(50):
			rivi = ""
			for col in range(50):
				rivi += labyrintti[level][row][col]
			print rivi
	print pyramidi.get_player()


main()
