
from Node import Node
import pygame
from Visualization import Visualization
from Control import Control
from collections import deque 
 
class Algorithm_A:
    def __init__(self,ggrid,sstart,eend):
        self.grid = ggrid
        self.start = sstart
        self.end = eend

    def BFS(self): 
          
        start = self.start
        start.obs = True
        end = self.end
          
        q = deque() 
          
        s = start
        q.append(s)
          
        while q: 
      
            curr = q.popleft()
            pt = curr.position
            if pt == end.position:
                current = curr
                while current is not None:
                    # error loop forever 
                    current.show(Control.red,0)
                    current = current.parent
                    if current == start: #kept to stop loop forever
                        pygame.time.delay(Control.delay)
                        pygame.quit()

              
            curr.addNeighbors(self.grid)
            children = curr.neighbors
            for child in children:
                if child.obs == False:
                    child.obs = True
                    q.append(child) 
                if child.parent == None:
                    child.parent = curr
                    curr.show(Control.blue, 1)
                child.show(Control.green, 0)

          
        return -1

def bfs(a,b):
    
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

    start = grid[a[0]][a[1]]
    end = grid[b[0]][b[1]]
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)
    algo  = Algorithm_A(grid, start, end)
    x = Visualization(grid, start, end)

    if x.initial():
        algo.BFS()

