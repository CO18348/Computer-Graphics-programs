from graphics import *
def main():
    win = GraphWin("Experiment 6", 1100, 600)

    xc=100
    yc=100
    r=80


    x=0
    y=r
    d=3 - 2*r

    while y >= x :
        x=x+1
        if d > 0 :
            y=y-1
            d=d + 4*(x-y) + 10
        else :
            d = d + 4*x +6
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
