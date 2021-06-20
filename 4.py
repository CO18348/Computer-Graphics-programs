from graphics import *
def main():
    win = GraphWin("Experiment 4", 1100, 600)

    x0=100
    y0=100
    x1=450
    y1=380


    dx=x1-x0
    dy=y1-y0
    x=x0
    y=y0
    p=2*dy-dx
    while x<x1 :
        if p>=0 :
            b=Point(x,y)
            b.draw(win)
            y=y+1
            p=p+2*dy-2*dx
        else :
            b=Point(x,y)
            b.draw(win)
            p=p+2*dy
        x=x+1


    
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
