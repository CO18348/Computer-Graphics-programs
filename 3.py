from graphics import *
def main():
    win = GraphWin("Experiment 3", 1100, 600)

    x0=100
    y0=200
    x1=500
    y1=300
    
    dx = (x1 - x0)
    dy = (y1 - y0)
    if dx>=dy :
        steps = dx
    else :
        steps = dy
    
    dx = dx/steps
    dy = dy/steps
    x = x0
    y = y0
    i = 1
    
    while i<= steps :
        b=Point(x,y)
        b.draw(win)
        x += dx
        y += dy
        i=i+1

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
