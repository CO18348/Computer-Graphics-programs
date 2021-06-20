from graphics import *
def main():
    win = GraphWin("Experiment 5", 1100, 600)

    X1=20
    Y1=20
    X2=80
    Y2=50


    dx=X2-X1
    dy=Y2-Y1
    d = dy - (dx/2)
    x = X1
    y = Y1

    while x < X2 :
        x=x+1
        if d < 0 :
            d = d + dy
        else :
            d += (dy - dx)
            y=y+1
        b=Point(x,y)
        b.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
