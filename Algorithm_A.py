from Node import Node
import pygame
from Visualization import Visualization
from Control import Control
class Algorithm_A:
	def __init__(self,ggrid,sstart,eend):
		self.grid = ggrid
		self.start = sstart
		self.end = eend

	def path(self):
		start_node = self.start

		start_node.g = start_node.h = start_node.f = 0
		end_node = self.end
		end_node.g = end_node.h = end_node.f = 0

		open_list = []
		closed_list = []

		open_list.append(start_node)
		loop = 0

		# Loop until you find the end
		while len(open_list) > 0:
			# Get the current node
			current_node = open_list[0]
			current_node.obs = True
			current_node.show(Control.blue, 0)

			current_index = 0
			for index, item in enumerate(open_list):
				if item.f < current_node.f:
					current_node = item
					current_index = index

			open_list.pop(current_index)

			closed_list.append(current_node)

			if current_node == end_node:
				current = current_node
				while current is not None:
					# error loop forever 
					current.show(Control.red,0)
					current = current.parent
					if current == start: #kept to stop loop forever
						pygame.time.delay(Control.delay)
						pygame.quit()

				
			current_node.addNeighbors(self.grid)
			children = current_node.neighbors
			for child in children:
				
				if child not in closed_list:
					temp = current_node.g + 1
					if child in open_list:
						if child.g > temp:
							child.g = temp
					else:
						child.g = temp
						open_list.append(child)
				child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
				child.show(Control.green, 0)
				child.f = child.g + child.h
				if child.parent == None:
					child.parent = current_node		

def a(a,b):
	global grid,start,end
	grid = [0 for i in range(Control.cols)]

	for i in range(Control.cols):
		grid[i] = [0 for i in range(Control.row)]

	for i in range(Control.cols):
		for j in range(Control.row):
			grid[i][j] = Node(i, j)
	
	for i in range(Control.cols):
		for j in range(Control.row):
			grid[i][j].show((255, 255, 255), 1)

	# start = grid[1][5]
	# end = grid[28][29]
	start = grid[a[0]][a[1]]
	end = grid[b[0]][b[1]]
	end.show((255, 8, 127), 0)
	start.show((255, 8, 127), 0)
	algo  = Algorithm_A(grid, start, end)
	x = Visualization(grid, start, end)

	if x.initial():
		algo.path()
	
