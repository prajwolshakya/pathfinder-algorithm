import pygame
from Control import Control
screen = pygame.display.set_mode((Control.width, Control.height))
class Node:
	def __init__(self, x, y,parent=None):
		self.parent = parent
		self.i = x
		self.j = y
		self.f = 0
		self.g = 0
		self.h = 0
		self.position = (self.i,self.j)
		self.neighbors = []
		self.obs = False
	def show(self, color, st):
		pygame.draw.rect(screen, color, (self.i * Control.w, self.j * Control.h, Control.w, Control.h), st)
		pygame.display.update()

	def addNeighbors(self, grid):
		i = self.i
		j = self.j
		if i < Control.cols-1 and grid[self.i + 1][j].obs == False:
			self.neighbors.append(grid[self.i + 1][j])
		if i > 0 and grid[self.i - 1][j].obs == False:
			self.neighbors.append(grid[self.i - 1][j])
		if j < Control.row-1 and grid[self.i][j + 1].obs == False:
			self.neighbors.append(grid[self.i][j + 1])
		if j > 0 and grid[self.i][j - 1].obs == False:
			self.neighbors.append(grid[self.i][j - 1])