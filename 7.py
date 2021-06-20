from graphics import *
def main():
    win = GraphWin("Experiment 7", 1100, 600)

    xc=300
    yc=300
    r=100


    x=0
    y=r
    p = 1 - r
    
    
    while x<y :
        if p<0 :
            x=x+1
            p = p + 2*x +1
        else :
            x=x+1
            y=y-1
            p=p + 2*(x-y) + 1
        b=Point(xc+x,yc+y)
        b.draw(win)
        b=Point(xc-x,yc+y)
        b.draw(win)
        b=Point(xc+x,yc-y)
        b.draw(win)
        b=Point(xc-x,yc-y)
        b.draw(win)
        b=Point(xc+y,yc+x)
        b.draw(win)
        b=Point(xc-y,yc+x)
        b.draw(win)
        b=Point(xc+y,yc-x)
        b.draw(win)
        b=Point(xc-y,yc-x)
        b.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
