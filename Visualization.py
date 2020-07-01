import pygame, random
from Control import Control
screen = pygame.display.set_mode((Control.width, Control.height))
pygame.init()
from Node import Node


class Visualization:
	def __init__(self,ggrid,sstart,eend):
		self.grid = ggrid
		self.start = sstart
		self.end = eend

	def mousePress(self,x):
		t = x[0]
		w = x[1]
		g1 = t // (Control.width // Control.cols)
		g2 = w // (Control.height // Control.row)
		acess = self.grid[g1][g2] = Node(g1, g2)
		if acess != self.start and acess != self.end:
			if acess.obs == False:
				acess.obs = True
				acess.show((220, 220, 220), 0)

	def initial(self):
	
		loop = True

		while loop:
			ev = pygame.event.get()

			for event in ev:
				
				if event.type == pygame.QUIT:
					pygame.quit()
				if pygame.mouse.get_pressed()[0]:
					try:
						pos = pygame.mouse.get_pos()
						self.mousePress(pos)
					except AttributeError:
						pass
				elif event.type == pygame.KEYDOWN:
					try:
						return True
					except AttributeError:
						pass
					loop = False
					break
