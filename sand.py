from graphics import *
import time
import random

'''
Hello! This is a simple sand simulation made by Jacob Smith. There is only one
particle type for now, being a generic falling sand. This was a way for me to learn
how to use the graphics.py library, and to work more with cellular automota.
This is the project that got me more into instant visual feedback, and inspired me
to make my p5 js web projects later. Enjoy!
'''

#Settings
fps = 30
#Square window size in pixels
windowSize = 500
#Number of cells for each dimension of the window
cellNum = 50

#Cells contain an rgb color, and a flag of if it has been modified on a given frame
cells = [[[(255,255,255), 0]]*cellNum for i in range(cellNum)]
#Stores the drawn rectangles, minimizes new rect calls
rects = [[0]*cellNum for i in range(cellNum)]

#On click, add a sand particle to the right spot
def addCells():
    mouse = window.checkMouse()
    if mouse != None:
        x = int(mouse.getX() // (windowSize / cellNum))
        y = int(mouse.getY() // (windowSize / cellNum))
        #Color varies and is stored per cell
        color = [random.randint(245,255), random.randint(235,249), random.randint(180,203)]
        cells[x][y] = [(color[0], color[1], color[2]), 1]
        rects[x][y].setFill(color_rgb(color[0], color[1], color[2]))


def updateCells():
    #Iterating through cells from bottom right to top left
    for i in range(len(cells)-1, -1, -1):
        for j in range(len(cells[i])-1, -1, -1):
            #If a cell is sand and has not been modified on this frame:
            if cells[i][j][0] != (255,255,255) and cells[i][j][1] == 0:
                if j != (len(cells[i])-1):
                    #If can fall
                    if cells[i][j+1][0] == (255,255,255):
                        cells[i][j+1] = [cells[i][j][0], 0]
                        rects[i][j+1].setFill(color_rgb(cells[i][j][0][0], cells[i][j][0][1], cells[i][j][0][2]))
                        cells[i][j] = [(255,255,255), 0]
                        rects[i][j].setFill(color_rgb(255,255,255))
                        continue
                    #If can fall left
                    if i != 0:
                        if cells[i-1][j+1][0] == (255,255,255):
                            cells[i-1][j+1] = [cells[i][j][0], 1]
                            rects[i-1][j+1].setFill(color_rgb(cells[i][j][0][0], cells[i][j][0][1], cells[i][j][0][2]))
                            cells[i][j] = [(255,255,255), 0]
                            rects[i][j].setFill(color_rgb(255,255,255))
                            continue
                    if i != cellNum-1:
                        if cells[i+1][j+1][0] == (255,255,255):
                            cells[i+1][j+1] = [cells[i][j][0], 1]
                            rects[i+1][j+1].setFill(color_rgb(cells[i][j][0][0], cells[i][j][0][1], cells[i][j][0][2]))
                            cells[i][j] = [(255,255,255), 0]
                            rects[i][j].setFill(color_rgb(255,255,255))
                            continue
    #reset all 'update' flags
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j][1] = 0
    return

#Almighty update call
def update():
    updateCells()
    addCells()
    return

#Main func, inits cells, rects, and window
def main():
    global window
    window = GraphWin("Sand", windowSize, windowSize)
    window.setBackground(color_rgb(0,0,0))
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            p1 = Point((windowSize/cellNum) * i, (windowSize/cellNum) * j)
            p2 = Point((windowSize/cellNum) * (i+1), (windowSize/cellNum) * (j+1))
            rects[i][j] = Rectangle(p1,p2) 
            rects[i][j].setFill(color_rgb(255,255,255))
            rects[i][j].setOutline(color_rgb(255,255,255))
            rects[i][j].setWidth(0)
            rects[i][j].draw(window) 
    #Forever run at set fps
    while(1):
        update()
        time.sleep(1 / fps)
main()