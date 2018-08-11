from pyramid_object import PyramidObject

class MazeIO(object):
	
	def save_maze(self, pyramid, fname):
		try:
			filu = open(fname, "w")
		except IOError:
			print "Something went wrong when opening file stream! No save made."
			filu.close()
			return False
		
		array = pyramid.get_array()
		
		for z in range(pyramid.get_height()):
			laini = ""
			laini = "Level number:" + str(z) + "\n"
			filu.write(laini)
			
			for y in range(pyramid.get_size_y()):
				laini = ""
				for x in range(pyramid.get_size_x()):
					laini = laini + array[z][y][x]
				
				laini = laini + "\n"
				filu.write(laini)
		
			laini = "==========\n"
			filu.write(laini)
		
		filu.close()
		return True
				
		
	def load_maze(self, fname):
		try:
			filu = open(fname, "r")
		except IOError:
			print "Something went wrong when opening file stream! No load made."
			filu.close()
			return None
		
		array = []
		array_lvl = []
		
		for rivi in filu:
			rivi = rivi.rstrip('\n')
			if "Level number:" in rivi:
				array_lvl = []
			elif rivi == "==========":
				array.append(array_lvl)
			else:
				array_lvl.append(rivi)
		
		'''
		THIS PART IS DANGEROUS.
		Please write some safeguards.
		'''
		height = len(array)
		size_y = len(array[0])
		size_x = len(array[0][0])
			
		pyramid = PyramidObject(size_x, size_y, height, array)
		
		filu.close()
		return pyramid
